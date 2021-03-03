import os, sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from datetime import datetime


from time import sleep
import random
import spintax
from pymongo import MongoClient

import csv
import logging
import xlrd
import json
import re
import math

logging.basicConfig(filename="logfilename.log", level=logging.INFO)

class Bot:
    def __init__(self):
        self.driver = ""
        self.path_to_chromedriver = "C:/Users/Administrator/Documents/bot/chromedriver.exe"
        self.browser_url = ""
        self.target_url = "https://twitter.com/messages"
        self.home_url = "https://twitter.com/home"
        self.base_url = "https://twitter.com/"
        self.notification_url = "https://twitter.com/notifications"
        self.spintax_url = "https://www.linkcollider.com/page/spintaxtester"
        self.msg1_url = ""
        self.msg2_url = ""
        self.comment_url = ""
        self.cnt = 0
        self.browser_port_list = [9230]
        self.account_username_list = ["@HildaRo49368042"]
        self.account_username = ""
        self.profile_index = 0
        # self.browser_port_list = [9228,9227]
        self.excelPath = "C:\\Users\\Administrator\\Documents\\bot\\files\\data.csv"
        self.publicProfileStep = []
        self.privateProfileStep = []
        self.username = ''
        self.name = ''
        self._id = ''
        self.user_id = ''
        self.url = ''

        self.client = ""
        self.username_db = ""

    def driver_startup(self, port):
        chrome_options = Options()
        self.browser_url = f"127.0.0.1:{port}"
        chrome_options.add_experimental_option("debuggerAddress", self.browser_url)
        self.driver = webdriver.Chrome(self.path_to_chromedriver, options=chrome_options)

    def getDbData(self):
        client = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/test?authSource=admin&replicaSet=atlas-4jftde-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
        mongodb = client["peachly_twitter_tweets_usernames"]
        collection = mongodb["usernames"]
        for x in collection.find({},{"_id":"0", "user_id":"1","username": "1"}):
            print(type(x),x)
        return collection

    def saveData(self, data):
        myclient = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/test?retryWrites=true&w=majority')
        print("69")
        mydb = myclient["peachly_dms_disabled"]
        private = mydb["private"]
        public = mydb["public"]
        print("ok", data)
        res = public.insert_one(data)
        print("doneee", res.inserted_id)

    def saveMsg(self, data):
        myclient = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/peachly_twitter_bots?authSource=admin&replicaSet=atlas-4jftde-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true')
        db = myclient["peachly_twitter_bots"]
        messages = db['messages']
        res = messages.insert_one(data)
        print("msg saved", res.inserted_id)

    def saveNewMsg(self, data):
        myclient = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/peachly_twitter_bots?authSource=admin&replicaSet=atlas-4jftde-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true')
        db = myclient["peachly_twitter_bots"]
        messages = db['new_messages']
        res = messages.insert_one(data)
        print("msg saved", res.inserted_id)

    def saveComment(self, data):
        db = self.client["peachly_twitter_bots"]
        comments = db['comments']
        res = comments.insert_one(data)
        print("comment saved", res.inserted_id)

    def getMsg(self, username, coming_time):
        myclient = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/peachly_twitter_bots?authSource=admin&replicaSet=atlas-4jftde-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true')
        db = myclient["peachly_twitter_bots"]
        messages = db['messages']
        print("here is result")
        for x in messages.find({}):
            print(x)
            if x["username"] == username and x["coming_time"] == coming_time:
                return True
        return False

    def getReplyMsg(self):
        myclient = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/peachly_twitter_bots?authSource=admin&replicaSet=atlas-4jftde-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true')
        db = myclient["peachly_twitter_bots"]
        reply_messages = db['reply_messages']
        return reply_messages

    def updateComment(u_name, reply_content, time):
        db = self.client["peachly_twitter_bots"]
        comments = db['comments']
        result = comments.find({"to_username": u_name, "coming_time": time, "content": reply_content}, {})
        if result.count() == 0:
            #save in the db
            dateTimeObj = datetime.now()
            data = {
                "to_username": u_name,
                "account_username": self.account_username,
                "coming_time": time,
                "save_time": dateTimeObj,
                "bot_number":2,
                "profile": self.profile_index
            }
            self.saveComment(data)
            return True
        else:
            return False

    def updateReport(self, updateField):
        myclient = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/peachly_twitter_bots?authSource=admin&replicaSet=atlas-4jftde-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true')
        db = myclient["peachly_twitter_bots"]
        reply_messages = db['reports']
        print("inside suc dm reporot")
        if reply_messages.count() == 0:
            print("ok")
            data = {
                "bot1_successful_dm": 0,
                "bot1_unsuccessful_dm":0,
                "bot1_spintax1_reply": 0,
                "bot2_successful_dm": 0,
                "bot2_unsuccessful_dm":0,
                "bot2_spintax1_reply": 0,
            }
            reply_messages.insert_one(data)       
        else:
            print("else")
            for x in reply_messages.find({}):
                reply_messages.update_one({"_id": x["_id"]}, {"$inc": {updateField:1}})   

    def checkIfSpintax2Reply(self, username):
        client = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/test?authSource=admin&replicaSet=atlas-4jftde-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
        mongodb = client["peachly_twitter_tweets_usernames"]   
        col = mongodb["public"]
        result = col.find({"username": username}, {"spintax2_reply": "1"})
        if result.count() == 0:
            return False
        else:
            return True


    def manage(self,public_or_private, msg1, msg2, commentURL,userNum):
        print("bot starts")
        self.msg1_url = msg1
        self.msg2_url = msg2
        self.comment_url = commentURL
        # self.publicProfileStep = publicStep
        # self.privateProfileStep = privateStep
        self.client = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/test?authSource=admin&replicaSet=atlas-4jftde-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
        self.username_db = self.client["peachly_twitter_tweets_usernames"]

        self.twitter_bot_db = self.client["peachly_twitter_bots"]
        bot_collection = self.twitter_bot_db["bot_infos"]
        reply_msg_collection = self.twitter_bot_db["reply_messages"]
        comment_collection = self.twitter_bot_db["reply_comments"]
        used_account_col = self.twitter_bot_db['used_usernames']
        report_col = self.twitter_bot_db["reports"]
        collection = self.username_db[public_or_private]
        print(type(collection))
        self.username_collection = collection
        index = 1


        for each_user in used_account_col.find({}):
            self._id = each_user['_id']
            self.username = each_user['username']
            self.url = each_user['url']
            print("each", each_user)
            for each_item in each_user:
                print("1000", each_user[each_item])
                current_time = datetime.now()
                if each_item == "dm" and each_user[each_item] == True:
                    dm_time = each_user["dm_time"]
                    print("dm_time", dm_time)
                    time_diff = current_time - dm_time
                    time_diff_hour = math.floor(time_diff.total_seconds() / 3600)
                    if (time_diff_hour >= 48):
                        print("205")
                        #check the dms once more

                        #update the report
                        bot_num = each_user["bot_number"]
                        updateField = "bot"+str(bot_num)+"_unsuccessful_dm" 
                        for x in report_col.find({}):
                            report_col.update_one({"_id": x["_id"]}, {"$inc": {updateField:1}}) 

                        collection.update_one({"username": each_user['username']}, {"$set": {'dm_expired': True}})
                        used_account_col.update_one({"_id": each_user['_id']}, {"$set": {'dm': False, 'dm_expired': True}})


                        #do comment and update the database

                        # _index = random.randint(0, len(self.browser_port_list)-1)
                        # print("profile browser running", _index)
                        # self.profile_index = _index
                        # self.account_username = self.account_username_list[_index]

                        # sleep(3)
                        # random_profile_port = self.browser_port_list[_index]
                        # print("port number", random_profile_port)
                        # self.driver_startup(random_profile_port)
                        # self.driver.maximize_window()
                        # sleep(random.randint(10,15))

                        # comment_result = self.comment()
                        # if comment_result == False:
                        #     used_account_col.update_one({"_id": each_user['_id']}, {"$set": {'comment': False}})
                        # elif comment_result == True:
                        #     used_account_col.update_one({"_id": each_user['_id']}, {"$set": {'comment': True, 'comment_time': datetime.now()}})

                        # # change dm to true
                        # used_account_col.update_one({"_id": each_user['_id']}, {"$set": {'dm': False}})


                elif each_item == "comment" and each_user[each_item] == True:
                    comment_time = each_user["comment_time"]
                    print("comment_time", comment_time)
                    time_diff = current_time - comment_time
                    time_diff_hour = math.floor(time_diff.total_seconds() / 3600)
                    print(math.floor(time_diff.total_seconds() / 3600))
                    if (time_diff_hour >= 48):
                        print("comment expired")
                        #check the comment reply once more

                        #update the report
                        bot_num = each_user["bot_number"]
                        updateField = "bot"+str(bot_num)+"_unsuccessful_comment" 
                        for x in report_col.find({}):
                            report_col.update_one({"_id": x["_id"]}, {"$inc": {updateField:1}})   
                        print("here")

                        collection.update_one({"username": each_user['username']}, {"$set": {'comment_expired': True}})
                        used_account_col.update_one({"_id": each_user['_id']}, {"$set": {'comment': False, 'comment_expired': True}})

                        # delete
                        # used_account_col.delete_one({"_id": each_user['_id']})

            print("index", index)
            index = index + 1
        return "end"
    

    def follow(self):
        self.driver.get(self.home_url)
        sleep(random.randint(5,7))
        search_input = self.driver.find_element_by_xpath('//form[@aria-label="Search Twitter"]//input')
        search_input.send_keys(self.username)
        sleep(random.randint(3,6))

        first_item = self.driver.find_element_by_xpath('//div[@role="listbox"]//div[@role="option"][2]').click()
        sleep(random.randint(3,5))
        print("following...")
        try:
            follow_btn = self.driver.find_element_by_xpath('//div[@data-testid="placementTracking"]//div[@role="button"]').click()
            sleep(random.randint(3,5))
            #update the status field in the database
            # following_person = AccountInfo.query.filter_by(username=self.username).first()
            # print("dddbbb", following_person, following_person.status)
            # following_person.status = "following"
            # db.session.commit()

            return True

        except:
            sleep(1)
            #update the status field in the database
            # following_person = AccountInfo.query.filter_by(username=self.username).first()
            # print("dddbbb", following_person, following_person.status)
            # following_person.status = "suspended"
            # db.session.commit()
            
            return False


    def likeTweets(self):
        print("like tweets started")
        self.driver.get(self.home_url)
        sleep(random.randint(2,5))
        search_input = self.driver.find_element_by_xpath('//form[@aria-label="Search Twitter"]//input')
        search_input.send_keys(self.username)
        sleep(random.randint(3,5))
        first_item = self.driver.find_element_by_xpath('//div[@role="listbox"]//div[@role="option"][2]').click()
        sleep(random.randint(2,4))
        try:
            like_elements = self.driver.find_elements_by_xpath('//section[@role="region"]/div/div//div//article//div[@data-testid="like"]')
            index = 0
            for each_like in like_elements:
                each_like.click()
                sleep(random.randint(5,7))
                index = index + 1
                if index == 2 :
                    break
        except:
            sleep(2)
            pass
        return True

    def comment(self):
        print("comment started")
        try:
            #get url of the name
            profile_link = self.base_url + self.username
            self.driver.get(profile_link)
            sleep(5)
            print("633")
            comment_elements = self.driver.find_elements_by_xpath('//section[@role="region"]/div/div//div//article//div[@data-testid="reply"]')
            comment_elements[0].click()
            sleep(random.randint(4,6))
            print("65656")
            # pyauto gui
            self.driver.get(self.spintax_url)
            sleep(random.randint(7,10))
            print("6660")

            self.driver.get(self.comment_url)
            print("hereee")
            sleep(10)
            # run pyautogui
            pyautogui_class = PyAutoGuiClass()
            pyautogui_class.pySpintaxComment()
            
            sleep(5)
            sleep(random.randint(4,6))
            print("6666")

            reply_button = self.driver.find_element_by_xpath('//div[@data-testid="tweetButton"]/div')
            reply_button.click()
            sleep(random.randint(3,4))
            self.driver.minimize_window()
            #save in the db
            dateTimeObj = datetime.now()
            data = {
                "to_username": self.username,
                "account_username": self.account_username,
                "coming_time": "",
                "save_time": dateTimeObj,
                "bot_number":2,
                "profile": self.profile_index,
                "new_reply": True
            }
            self.saveComment(data)
            return True
        except:
            print("comment error")
            self.driver.minimize_window()
            sleep(2)
            return False



if __name__ == '__main__':
    bot = Bot()
    bot.manage("public", 'bot1_dm1_link', "bot1_dm2_link","bot1_dm1_link","10")
