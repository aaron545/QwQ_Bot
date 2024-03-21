from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import threading
import time
import atexit
import random
import winsound
import requests
import yaml

def getLoadData():
    try:
        with open('param.yaml', 'r', encoding="utf-8") as yaml_file:
            return yaml.safe_load(yaml_file)
    except:
        open('param.yaml', 'w+', encoding="utf-8")
        default_data = {
            "account": {
                "chrome_path": "./chromedriver.exe",
                "email": "your email",
                "password": "your password",
                "name": "your dc name",
                "name_at": "your dc name_at",
                "url": "the url you will entry",
                "urlcommon": "the url remind you beepboop",
                "urlspam": "To be developed",
                "loop": 2000,
                "token": "line token"
            },
            "mod": [
                {
                "command": "wh",
                "prob": 1
                },
                {
                "command": "wb",
                "prob": 1
                },
                {
                "command": "wdt",
                "prob": 0.5
                },
                {
                "command": "owo",
                "prob": 1
                },
                {
                "command": "ws",
                "prob": 1
                },
                {
                "command": "wcf h",
                "prob": 1
                }
            ]
        }
        saveLoadData(default_data)
        return default_data
    
def saveLoadData(data):
    with open('param.yaml', 'w', encoding="utf-8") as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False, allow_unicode=True)
    print("data saved!")
    return True
def close_driver():
    global browser
    browser.quit()
def BeepBoopName(text, param_account):
    print('param_account["name"] = ', param_account["name"])
    if text.find(param_account["name"]) != -1 or text.find(param_account["name_at"]) != -1: 
        print("beepboop!!!")
        return True
    else : 
        return False
def BeepBoop(text, param_account):
    global beepboop
    if (text.find("Beep Boop. Please DM me") != -1 or 
        text.find("Please complete your captcha") != -1 or
        text.find("are you a real human?") != -1):
        print('find name')
        if BeepBoopName(text, param_account):
            beepboop = True       
def distorted(text):
    pass
def playmusic(song):
    def play(scale):
        duration = 400 
        rest = 100 
        if scale == " ":
            time.sleep((duration+rest)*0.001)
        else:
            winsound.Beep(scale,duration)
            time.sleep(rest*0.001)
    freq = {"C4":262, "D4":294, "E4":330, "F4":349, "G4":392, "A4":440, "B4":494, " ":" "}
    for s in song:
        play(freq[s])
def notify(token, message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {
      'Authorization': 'Bearer ' + token
    }
    data = {
      "message": message,
      "stickerPackageId":8525,
      "stickerId":16581311
    }
    response = requests.post(url, headers=headers, data=data)

def dc_task():
    global beepboop 
    beepboop = False

    songBeepBoop = ["C4","C4","G4","G4","A4","A4","G4"," ", # little star
                "F4","F4","E4","E4","D4","D4","C4"]
    songEnd = ["G4","E4","E4"," ","F4","D4","D4"," ",   # little bee
                "C4","D4","E4","F4","G4","G4","G4"]

    loaded_data = getLoadData()
    param_account = loaded_data['account']
    param_mod = loaded_data['mod']
    
    ini_button = "marginTop8__83d4b marginCenterHorz__4cf72 linkButton_ba7970 button_afdfd9 lookLink__93965 lowSaturationUnderline__95e71 colorLink_b651e5 sizeMin__94642 grow__4c8a4"
    global browser
    version = webdriver.__version__.split('.')
    if int(version[0]) < 4 or (int(version[0]) == 4 and int(version[1]) < 12):
        browser = webdriver.Chrome(param_account["chrome_path"])
    else:
        browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    browser.get(param_account["url"])
    try:
        button = browser.find_element(By.XPATH, f'//button[@class="{ini_button}"]')
        button.click()
    except:
        pass
    time.sleep(3)
    email = browser.find_element(By.XPATH, '//input[@class="inputDefault__80165 input_d266e7 inputField__79601"]')
    password = browser.find_element(By.XPATH, '//input[@type="password"]')
    button = browser.find_element(By.XPATH, "//button[@type='submit']")

    email.send_keys(param_account["email"])
    password.send_keys(param_account["password"])
    time.sleep(1)
    button.click()

    atexit.register(close_driver)

    for i in range(int(param_account["loop"])):
        input_text = browser.find_element(By.XPATH, '//div[@role="textbox"]')
        loop_delay = random.randint(20, 30) # time delay for the loop
        command_prob = random.random() # decide whether execute certain command or not
        print('command_prob:', command_prob)
        print('loop_delay:', loop_delay)
        
        for d in param_mod:
            c = d['command']
            p = d['prob']
            dc_text_area = browser.find_elements(By.XPATH, '//div[contains(@class, "messageContent__21e69")]') # change here
            dc_text_area = dc_text_area[-5:]
            
            for element in dc_text_area:
                try:
                    # # get message serial
                    # id = element.get_attribute("id")
                    # # print(id)
                    # serial = int(id.split('-')[-1])
                    # # find message
                    # text_el = element.find_element(By.XPATH, f'//*[@id="message-content-{serial}"]')
                    print('text = ',element.text)
                    BeepBoop(element.text, param_account)
                except:
                    pass
                    # print(element.get_attribute("outerHTML"))
            print("beepboop = ", beepboop)
            if beepboop:
                break
            if command_prob < p:
                command_delay = random.randint(1, 3) # time delay between each command
                print('execute', c)
                input_text.send_keys(c)
                input_text.send_keys(Keys.ENTER)
                time.sleep(command_delay)
            else:
                print('skip', c)
        if beepboop:
            browser.get(param_account["urlcommon"])
            while True:
                time.sleep(8)
                input_text = browser.find_element(By.XPATH, '//div[@role="textbox"]')
                input_text.send_keys(f'beepboop了 別在打字啦!!!{param_account["name_at"]}')
                input_text.send_keys(Keys.ENTER)
                notify(param_account["token"],"BeepBoop!!!")
                playmusic(songBeepBoop)
            # break
        time.sleep(loop_delay)
    notify(param_account["token"],"finish!!!")
    playmusic(songEnd)