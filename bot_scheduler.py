from pymongo import MongoClient
from time import sleep

from bot.main import Bot

def getBotInfo():
    client = MongoClient('mongodb+srv://wang:lasQ7q350LVsRQWm@cluster0.asfo1.mongodb.net/test?authSource=admin&replicaSet=atlas-4jftde-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
    mongodb = client["peachly_twitter_bots"]
    collection = mongodb["bot_infos"]
    # for x in collection.find():
    #     print(type(x),x)
    return collection

def scheduler():
    print("scheduler is runnuing")
    bot_info = getBotInfo()
    i = 1
    for x in bot_info.find():
        if i >= 2:
            break
        bot = Bot()
        bot.manage("public", x['bot1_dm1_link'], x["bot1_dm2_link"],x["bot1_dm1_link"],x["username_number"])

    # while True:
        # print("ok")
        # bot_info = getBotInfo()
        # i = 1
        # for x in bot_info.find():
        #     if i >= 2:
        #         break
        #     if x['status'] == "start":
        #         #start the bot
        #         bot = Bot()
        #         bot.manage("public", x['bot1_dm1_link'], x["bot1_dm2_link"],x["bot1_dm1_link"],x["username_number"])
        #     else:
        #         # end the bot
        #         print("end")
        #     i = i+1
        # sleep(4)


if __name__ == '__main__':
    scheduler()