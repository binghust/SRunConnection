import random
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


def login(username, password):
    opts = ChromeOptions()
    opts.add_argument("--headless")
    browser = webdriver.Chrome(options=opts)
    time.sleep(1)

    find_by_id = lambda id_: browser.find_element(By.ID, id_)
    try:
        browser.get('http://portal.zjxu.edu.cn/index_5.html')
        time.sleep(1)
        try:
            if find_by_id("logout"):
                print("Already Online!")
                browser.close()
                time.sleep(random.randint(3, 7))
        except NoSuchElementException as e:
            find_by_id("username").clear()
            find_by_id("password").clear()
            find_by_id("username").send_keys(username)
            find_by_id("password").send_keys(password)
            find_by_id("login-account").click()
            time.sleep(2)
            print("Logged In!")

    except:
        browser.close()
        print("Logged Failed!")


if __name__ == '__main__':
    login('username', 'password')
