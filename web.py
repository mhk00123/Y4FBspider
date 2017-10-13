# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:33:37 2017

@author: Wei
"""

from selenium import webdriver
import time  

browser = webdriver.Chrome()
browser.get('https://www.facebook.com/login.php')
browser.find_element_by_id('email').send_keys('whatyou564@yahoo.com.tw')
time.sleep(2)
browser.find_element_by_id('pass').send_keys('at18ukoucopan')
time.sleep(2)
browser.find_element_by_id('loginbutton').click()
time.sleep(2)
browser.get('https://developers.facebook.com/tools/explorer/145634995501895?method=GET&path=allenabcde%2Fposts&version=v2.10')
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/a/span[2]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="js_8"]/div/ul/li[7]/a').click()
time.sleep(1)
token = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/label/input').get_attribute('value')
print(token)

browser.close()