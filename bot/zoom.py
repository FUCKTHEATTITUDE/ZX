import logging
from config import Config
import warnings
import threading
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from bot import updater,driver , restricted
from telegram.ext import run_async
from telegram import ChatAction
import os
import pickle
import time
from os import execl
from sys import executable

userId = Config.USERID
MUTEX = threading.Lock()
proxylist = [
    "192.99.101.142:7497",
    "198.50.198.93:3128",
    "52.188.106.163:3128",
    "20.84.57.125:3128",
    "172.104.13.32:7497",
    "172.104.14.65:7497",
   "165.225.220.241:10605",
    "165.225.208.84:10605",
    "165.225.39.90:10605",
    "165.225.208.243:10012",
    "172.104.20.199:7497",
    "165.225.220.251:80",
    "34.110.251.255:80",
    "159.89.49.172:7497",
    "165.225.208.178:80",
    "205.251.66.56:7497",
    "139.177.203.215:3128",
    "64.235.204.107:3128",
    "165.225.38.68:10605",
    "165.225.56.49:10605",
    "136.226.75.13:10605",
    "136.226.75.35:10605",
    "165.225.56.50:10605",
    "165.225.56.127:10605",
    "208.52.166.96:5555",
    "104.129.194.159:443",
    "104.129.194.161:443",
    "165.225.8.78:10458",
    "5.161.93.53:1080",
    "165.225.8.100:10605",
]

name = [
'David Asir',
'Mohammed UAE',
'Victor Sam',
'SENTHILKUMAR DUBAI',
'Tamilarasan',]
def sync_print(text):
    with MUTEX:
        print(text)
        
def get_driver(proxy):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.74 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-infobars")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--use-fake-device-for-media-stream")
    options.add_argument("--start-maximized")
    if proxy is not None:
        options.add_argument(f"--proxy-server={proxy}")      
def driver_wait(driver, locator, by, secs=1, condition=ec.element_to_be_clickable):
    wait = WebDriverWait(driver=driver, timeout=secs)
    element = wait.until(condition((by, locator)))
    return element

def joinZoom(context, url_meet, passStr):

    def students(context):
        print("Running Student Check")

        driver.find_element_by_xpath('//*[@id="wc-container-left"]/div[4]/div/div/div/div[1]').click()
        number = WebDriverWait(driver, 2400).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wc-footer"]/div/div[2]/button[1]/div/div/span'))).text
        print(number)
        if(int(number) <10):
            context.bot.send_message(chat_id=userId, text="Your Class has ended!")
            driver.quit()
            execl(executable, executable, "chromium.py")
    try:
        sync_print(f"{name} started!")
        driver = get_driver(proxy)
        driver.get(f'https://zoom.us/wc/join/'+meetingcode)
        time.sleep(3)
        inp = driver.find_element(By.ID, 'inputname')
        time.sleep(1)
        inp.send_keys(f"{user}")
        btn2 = driver.find_element(By.ID, 'joinBtn')
        btn2.click()
        time.sleep(2)
        inp2 = driver.find_element(By.ID, 'inputpasscode')
        time.sleep(1)
        inp2.send_keys(passStr)
        btn3 = driver.find_element(By.ID, 'joinBtn')
        time.sleep(1)
        btn3.click()
        sync_print(f"{name} sleep for {wait_time} seconds ...")
        time.sleep(wait_time)
        sync_print(f"{name} ended!")

        try:
            continue:

        except NoSuchElementException:
            print("User is already logged in. Continuing")
        except Exception as e:
            print(e)
            print("Probably, Terms and policies agreement isnt asked for.")
        

        
        driver.save_screenshot("ss.png")
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        mid  = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
        os.remove('ss.png')
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
        context.bot.send_message(chat_id=userId, text="Attending you lecture. You can chill :v")
        logging.info("STAAAAPH!!")


        
except Exception as e:
        driver.save_screenshot("ss.png")
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        mid  = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
        os.remove('ss.png')
        context.bot.send_message(chat_id=userId, text="Got some error, forward this to telegram group along with pic")
        context.bot.send_message(chat_id=userId, text=str(e))

    j = updater.job_queue
    j.run_repeating(students, 20, 1000)

@restricted
@run_async
def zoom(update, context):
    logging.info("DOING")

    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)

    url_meet = update.message.text.split()[1]
    passStr = update.message.text.split()[2]
    joinZoom(context, url_meet, passStr)
