from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    if text.find(param["name"]) != -1: 
        return True
    else : 
        return False
def BeepBoop(text):
    global beepboop
    if text.find("Beep Boop. Please DM me") != -1 or text.find("Please complete your captcha") != -1:
        if BeepBoopName(text):
            beepboop = True
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
    
    ini_button = "marginTop8-24uXGp marginCenterHorz-574Oxy linkButton-2ax8wP button-f2h6uQ lookLink-15mFoz lowSaturationUnderline-Z6CW6z colorLink-1Md3RZ sizeMin-DfpWCE grow-2sR_-F"
    browser = webdriver.Chrome(param["chrome_path"])
    browser.get(param["url"])
    
    browser.implicitly_wait(10)
    
    time.sleep(5)
    try:
        button = browser.find_element(By.XPATH, f'//button[@class="{ini_button}"]')
        button.click()
    except:
        pass
    time.sleep(3)

    #browser.refresh()
    email = browser.find_element(By.XPATH, '//input[@class="inputDefault-3FGxgL input-2g-os5 inputField-2RZxdl"]')
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
          {'prob':0.70, 'command':'wdt'},
          {'prob':0.10, 'command':'wlvl'},
          {'prob':0.20, 'command':'whb'},
          {'prob':0.10, 'command':'wz'},
          {'prob':0.00, 'command':'owo'},
          {'prob':0.00, 'command':'wcf h'}]
    
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
            
            try:
                WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@class="scrollerInner-2PPAp2"]/li[@class="messageListItem-ZZ7v6g"]')))
                dc_text_area = browser.find_elements(By.XPATH, '//*[@class="scrollerInner-2PPAp2"]/li[@class="messageListItem-ZZ7v6g"]')
            except:
                print(dc_text_area)
            dc_text_area = dc_text_area[-5:]

            for element in dc_text_area:
                # get message serial
                id = element.get_attribute("id")
                serial = int(id.split('-')[-1])
                # find message
                text_el = element.find_element(By.XPATH, f'//*[@id="message-content-{serial}"]')

                BeepBoop(text_el.text)
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
            time.sleep(8)
            input_text = browser.find_element(By.XPATH, '//div[@role="textbox"]')
            input_text.send_keys(f'beepboop了 別在打字啦!!!{param["name_at"]}')
            input_text.send_keys(Keys.ENTER)
            notify(param["token"],"BeepBoop!!!")
            playmusic(songBeepBoop)
            break
        time.sleep(loop_delay)
    notify(param["token"],"finish!!!")
    playmusic(songEnd)
