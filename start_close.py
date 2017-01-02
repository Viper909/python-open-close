import os
import time
import schedule


def start():#name it what you want but it start the program
    start = os.startfile("")#add path to where the exe of the program is
    print("Starting")



def close():#name what you want basically name of closing the program

    close = os.system('TASKKILL /F /IM ')#add the proccess name you can check the programs name in task manager
    print("closing ")


schedule.every().day.at("0:02").do(start)#time when it starts
schedule.every().day.at("06:58").do(close)#time it closes

while True:
    schedule.run_pending()
    time.sleep(9)
