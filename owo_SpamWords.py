from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import atexit
import random
import nltk
import re

ini_button = "marginTop8-24uXGp marginCenterHorz-574Oxy linkButton-2ax8wP button-f2h6uQ lookLink-15mFoz lowSaturationUnderline-Z6CW6z colorLink-1Md3RZ sizeMin-DfpWCE grow-2sR_-F"
#8-13
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

if __name__ == "__main__":
    param = getAccount()

    browser = webdriver.Chrome(param["chrome_path"])
    browser.get(param["urlspam"])
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

    email.send_keys(param["email"]) ### here
    password.send_keys(param["password"]) ### here
    button.click()

    atexit.register(close_driver)

    time.sleep(10)
    
    word_list = nltk.corpus.words.words()
    
    while True:
        input_text = browser.find_element_by_xpath('//div[@role="textbox"]')
        
        loop_delay = 61 # time delay for the loop
        seq_len = random.randint(5, 10)
        print('loop_delay:', loop_delay)
        print('sequence length:', seq_len)
        time.sleep(loop_delay)
        tokens = random.sample(word_list, seq_len)
        
        text = ' '.join(tokens)
        
        input_text.send_keys(text)
        input_text.send_keys(Keys.ENTER)