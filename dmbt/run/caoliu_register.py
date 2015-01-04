#!/usr/bin/env python
# encoding: utf-8

import traceback
from selenium import webdriver


def start():
    s = "/home/daipeng/Desktop/chromedriver"
    chrome = webdriver.Chrome(s)
    chrome.implicitly_wait(10)
    return chrome


def register(chrome, nickname):
    # goto register page
    start_url = 'http://www.ct66y.com/u/?id=乌龟hk'
    chrome.get(start_url)
    register = chrome.find_element_by_xpath('//*[@id="header"]/div[1]/a[2]')
    register.click()

    # register form
    name = chrome.find_element_by_xpath('//*[@id="regname"]')
    name.send_keys(nickname)
    pwd = chrome.find_element_by_xpath('//*[@id="regpwd"]')
    pwd.send_keys('123456')
    pwd2 = chrome.find_element_by_xpath('//*[@id="regpwdrepeat"]')
    pwd2.send_keys('123456')
    mail = chrome.find_element_by_xpath('//*[@id="regemail"]')
    mail.send_keys('892312006@qq.com')
    submit = chrome.find_element_by_xpath('//*[@id="main"]/form/div[2]/input')
    submit.click()

    # logout
    out = chrome.find_element_by_xpath('//*[@id="header"]/div[1]/a')
    out.click()


def main():
    chrome = start()

    for i in range(6, 56):
        nickname = u"乌龟hk%s" % i
        try:
            register(chrome, nickname)
        except Exception as e:
            print e.message
            traceback.print_exc()
    print "register finish"
    chrome.quit()


if __name__ == "__main__":
    main()
