#!/usr/bin/env python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
import sys
import re

phantomjs_path = r'D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe'

def get_geo(target):
    driver = webdriver.PhantomJS(executable_path=phantomjs_path)
    try:
        driver.get("http://www.gpsspg.com/maps.htm")
        driver.find_element_by_xpath('//input[@id="s_t"]').send_keys(target)
        driver.find_element_by_xpath('//input[@id="s_t"]').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//div[@id="m_r"]')
        driver.set_window_size(1200, 900)

        # map_f_2 = driver.find_element_by_name("map_f_2")

        # while not map_f_2:
        #     map_f_2 = driver.find_element_by_name("map_f_2")
        #     print map_f_2
        #     print "waiting..."

        # driver.get_screenshot_as_file('show.png')


        # not driver.find_elements_by_class_name("BMap_bubble_content") or
        # while not driver.find_elements_by_class_name("BMap_bubble_content") or not driver.find_elements_by_name("map_f_2"):
        #     print 123
        #     pass

        time.sleep(2)

        map_f_2 = driver.find_element_by_name("map_f_2")
        driver.switch_to_frame(map_f_2)

        content = driver.find_element_by_class_name("BMap_bubble_content").text.encode("utf-8")
        mc = re.search("百度地图：(.*)", content)
        print target, mc.group(1)

        driver.quit()

        return True

    except Exception, e:
        print e
        driver.quit()

        return False


stations = [
    u'重庆李子坝地铁站',
    u'重庆光电园地铁站',
    u'重庆大龙山地铁站',
]

for station in stations:
    while not get_geo(station):
        get_geo(station)












# driver.find_element_by_name('email').send_keys('your email')
# driver.find_element_by_xpath('//input[@name="password"]').send_keys('your password')
# #driver.find_element_by_xpath('//input[@name="password"]').send_keys(Keys.RETURN)
# time.sleep(2)
# driver.get_screenshot_as_file('show.png')
# #driver.find_element_by_xpath('//button[@class="sign-button"]').click()
# driver.find_element_by_xpath('//form[@class="zu-side-login-box"]').submit()

# try:
#     dr=WebDriverWait(driver,5)
#     dr.until(lambda the_driver:the_driver.find_element_by_xpath('//a[@class="zu-top-nav-userinfo "]').is_displayed())
# except:
#     print '登录失败'
#     sys.exit(0)
# driver.get_screenshot_as_file('show.png')
# #user=driver.find_element_by_class_name('zu-top-nav-userinfo ')
# #webdriver.ActionChains(driver).move_to_element(user).perform() #移动鼠标到我的用户名
# loadmore=driver.find_element_by_xpath('//a[@id="zh-load-more"]')
# actions = ActionChains(driver)
# actions.move_to_element(loadmore)
# actions.click(loadmore)
# actions.perform()
# time.sleep(2)
# driver.get_screenshot_as_file('show.png')
# print driver.current_url
# print driver.page_source
