# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:40:33 2017

@author: user
"""
from selenium import webdriver
import time

x = webdriver.Chrome()                                          #set browser chrome
x.get('https://www.facebook.com/login.php')                     #go to login page
x.find_element_by_id('email').send_keys('mhk00123@gmail.com')   #find email input text
time.sleep(3)                                                   #sleep 3 seconds
x.find_element_by_id('pass').send_keys('Ctm62987522')           #find password input text
time.sleep(3)                                                   #sleep 3 seconds
x.find_element_by_id('loginbutton').click()                     #find loginbutton and click 

time.sleep(3)                                                   #sleep 3 seconds
#go to graphic api page
x.get('https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=me%3Ffields%3Did%2Cname&version=v2.10')