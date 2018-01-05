#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/25

from selenium import webdriver
import time

driver = webdriver.Chrome()

def get_screen():
    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    driver.get_screenshot_as_file("%s.jpg" % nowtime)


def screen(func):
    try:
        def inner():
            func()
            return func
    except BaseException as e:
            get_screen()
            print("异常信息是：%s" % e)

    return inner


def search(driver):
    driver.get("https://www.baidu.com/")
    driver.find_element_by_id("kw").send_keys("python")
    driver.find_element_by_id("su").click()

search(driver)