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

beepboop = False

songBeepBoop = ["C4","C4","G4","G4","A4","A4","G4"," ", # little star
               "F4","F4","E4","E4","D4","D4","C4"]
songEnd = ["G4","E4","E4"," ","F4","D4","D4"," ",   # little bee
              "C4","D4","E4","F4","G4","G4","G4"]


def getAccount():
    param = dict()
    with open("account.txt","r", encoding="utf-8") as f:
        for line in f.readlines():
            p = line.split("=")
            param[p[0].strip()] = p[1].strip()
        return param
def close_driver():
    global browser
    browser.quit()
def BeepBoopName(text):
    if text.find(param["name"]) != -1 or text.find(param["name_at"]) != -1: 
        return True
    else : 
        return False

def BeepBoop(text):
    global beepboop
    if text.find("Beep Boop. Please DM me") != -1 or text.find("Please complete your captcha") != -1:
        print('find name')
        if BeepBoopName(text):
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

if __name__ == "__main__":
    param = getAccount()
    
    ini_button = "marginTop40__2b1fe button__47891 button_afdfd9 lookFilled__19298 colorBrand_b2253e sizeLarge__9049d fullWidth__7c3e8 grow__4c8a4"
    browser = webdriver.Chrome(param["chrome_path"])
    browser.get(param["url"])
    
    browser.implicitly_wait(15)
    
    try:
        button = browser.find_element(By.XPATH, f'//button[@class="{ini_button}"]')
        button.click()
    except:
        pass
    time.sleep(3)

    #browser.refresh()
    email = browser.find_element(By.XPATH, '//input[@class="inputDefault__80165 input_d266e7 inputField__79601"]')
    password = browser.find_element(By.XPATH, '//input[@type="password"]')
    button = browser.find_element(By.XPATH, "//button[@type='submit']")

    email.send_keys(param["email"])
    password.send_keys(param["password"])
    time.sleep(1)
    button.click()

    atexit.register(close_driver)

    time.sleep(10)
    cp = [{'prob':1.00, 'command':'wh'},
          {'prob':1.00, 'command':'wb'},
          {'prob':0.50, 'command':'wdt'},
          {'prob':0.00, 'command':'wlvl'},
          {'prob':0.00, 'command':'whb'},
          {'prob':0.00, 'command':'wz'},
          {'prob':1.00, 'command':'owo'},
          {'prob':1.00, 'command':'ws'},
          {'prob':1.00, 'command':'wcf h'}]
    
    for i in range(int(param["loop"])):
        input_text = browser.find_element(By.XPATH, '//div[@role="textbox"]')
        random.shuffle(cp)
        loop_delay = random.randint(20, 30) # time delay for the loop
        command_prob = random.random() # decide whether execute certain command or not
        print('command_prob:', command_prob)
        print('loop_delay:', loop_delay)
        
        for d in cp:
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
                    BeepBoop(element.text)
                except:
                    pass
                    # print(element.get_attribute("outerHTML"))
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
            browser.get(param["urlcommon"])
            while True:
                time.sleep(8)
                input_text = browser.find_element(By.XPATH, '//div[@role="textbox"]')
                input_text.send_keys(f'beepboop了 別在打字啦!!!{param["name_at"]}')
                input_text.send_keys(Keys.ENTER)
                notify(param["token"],"BeepBoop!!!")
                playmusic(songBeepBoop)
            # break
        time.sleep(loop_delay)
    notify(param["token"],"finish!!!")
    playmusic(songEnd)
