from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import atexit
import random
import winsound

beepboop = False

little_star = ["do","do","so","so","la","la","so"," ",
               "fa","fa","mi","mi","re","re","do"]

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
    freq = {"do":262, "re":294, "mi":330, "fa":349, "so":392, "la":440, "si":494, " ":" "}
    for s in song:
        play(freq[s])

if __name__ == "__main__":
    param = getAccount()
    chrome_path = "C:/Users/aaron/Desktop/python/OwO/chromedriver.exe"    
    browser = webdriver.Chrome(chrome_path)
    browser.get(param["url"])

    time.sleep(5)

    #browser.refresh()
    email = browser.find_element_by_xpath('//input[@class="inputDefault-3FGxgL input-2g-os5 inputField-2RZxdl"]')
    password = browser.find_element_by_xpath('//input[@type="password"]')
    button = browser.find_element_by_xpath("//button[@type='submit']")

    email.send_keys(param["email"])
    password.send_keys(param["password"])
    time.sleep(1)
    button.click()

    atexit.register(close_driver)

    time.sleep(10)
    cp = [{'prob':0.00, 'command':'wh'},
          {'prob':1.00, 'command':'wb'},
          {'prob':0.10, 'command':'wlvl'},
          {'prob':0.01, 'command':'wcl'},
          {'prob':0.20, 'command':'whb'},
          {'prob':0.01, 'command':'wq'},
          {'prob':0.10, 'command':'wcash'},
          {'prob':0.10, 'command':'wz'}]
    
    while True:
        input_text = browser.find_element_by_xpath('//div[@role="textbox"]')

        random.shuffle(cp)
        loop_delay = random.randint(20, 30) # time delay for the loop
        command_prob = random.random() # decide whether execute certain command or not
        print('command_prob:', command_prob)
        print('loop_delay:', loop_delay)
        
        for d in cp:
            c = d['command']
            p = d['prob']
            dc_text_area = browser.find_elements_by_xpath('//*[@class="scrollerInner-2PPAp2"]/li[@class="messageListItem-ZZ7v6g"]')

            dc_text_area = dc_text_area[-5:]

            for element in dc_text_area:
                # get message serial
                id = element.get_attribute("id")
                serial = int(id.split('-')[-1])
                # find message
                text_el = element.find_element_by_xpath(f'//*[@id="message-content-{serial}"]')
                BeepBoop(text_el.text)
            if beepboop:
                break
            if command_prob < p:
                command_delay = random.randint(3, 6) # time delay between each command
                print('execute', c)
                input_text.send_keys(c)
                input_text.send_keys(Keys.ENTER)
                time.sleep(command_delay)
            else:
                print('skip', c)
        if beepboop:
            browser.get(param["urlcommon"])
            time.sleep(8)
            input_text = browser.find_element_by_xpath('//div[@role="textbox"]')
            input_text.send_keys(f'beepboop了 別在打字啦!!!{param["name_at"]}')
            input_text.send_keys(Keys.ENTER)
            playmusic(little_star)
            break
        time.sleep(loop_delay)
