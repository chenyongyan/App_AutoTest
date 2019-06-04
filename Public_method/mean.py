# user/python
# encoding:utf-8

from appium import webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time,json,re
from Public_method import MySql
from appium.webdriver.common.touch_action import TouchAction


file = open(r"E:\App_AutoTest\Public_file\date.json", "r", encoding="UTF-8")
dict = json.load(file)


# 登录盈客宝
def wechat_login(self):
    # 微信快捷注册登陆
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)
    self.driver.find_element_by_xpath(dict['login']['盈客宝小程序']).click()
    time.sleep(1)
    self.driver.find_element_by_xpath(dict['login']['请先绑定会员卡或注册会员']).click()
    time.sleep(1)
    self.driver.find_element_by_xpath(dict['login']['微信用户快捷登录']).click()
    time.sleep(1)
    self.driver.find_element_by_xpath(dict['login']['确认授权']).click()
    time.sleep(1)

def phone_login(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)
    self.driver.find_element_by_xpath(dict['login']['盈客宝小程序']).click()
    time.sleep(1)
    self.driver.find_element_by_xpath(dict['login']['请先绑定会员卡或注册会员']).click()
    time.sleep(1)
    self.driver.find_element_by_xpath(dict['login']['手机号登录']).click()
    time.sleep(1)
    self.driver.find_element_by_xpath(dict['login']['请输入您的手机号']).sendkeys(dict['login']['手机号'])
    time.sleep(1)
    self.driver.find_element_by_xpath(dict['login']['请输入验证码']).sendkeys(dict['login']['验证码'])
    time.sleep(1)
    self.driver.find_element_by_xpath(dict['login']['手机号登录确定按钮']).click()

# 浏览器打开B端页面进行入会方式的修改
# 自动注册入会
def AutoLogon(self):
    self.driver = webdriver.Chrome()
    url = dict['B端测试环境']['url']
    self.driver.get(url)
    self.driver.implicitly_wait(15)
    self.driver.maximize_window()
    self.driver.find_element_by_css_selector(dict['B端测试环境']['用户名输入框']).send_keys(dict['B端测试环境']['登录用户名'])
    self.driver.find_element_by_css_selector(dict['B端测试环境']['密码输入框']).send_keys(dict['B端测试环境']['登录密码'])
    time.sleep(1)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['登录按钮']).click()
    time.sleep(2)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['线上']).click()
    time.sleep(2)
    self.driver.switch_to_frame(1)
    time.sleep(1)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['线上渠道']).click()
    time.sleep(1)
    self.driver.switch_to_default_content()
    time.sleep(1)
    self.driver.switch_to_frame(2)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['盈客宝管理']).click()
    time.sleep(1)
    self.driver.switch_to_default_content()
    self.driver.switch_to_frame(3)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['会员注册设置']).click()
    time.sleep(1)
    # 选择购买入会套餐
    self.driver.switch_to_frame(1)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['自动注册']).click()
    time.sleep(1)
    # 保存按钮
    self.driver.find_element_by_css_selector(dict['B端测试环境']['入会方式保存按钮']).click()
    time.sleep(1)
    self.driver.close()

    # 断言
    # 入会方式：0自动注册入会；1购买超级套餐入会
    try:
        sql = dict['mysql']['查询会员入会方式']
        result = MySql.db_Query_233(self,dict['mysql']['datebase233'], sql)
        result2 = re.findall(r"[(](.+?)[,]", str(result))
        wayValues = result2[0]
        if wayValues == '0':
            print(r'当前入会方式为：自动注册入会！')
        elif wayValues == '1':
            print(r'当前入会方式为：购买超级套餐入会！')
    except Exception as error:
        print('查询入会方式失败！',error)

#购买超级会员套餐
def BuyMeal(self):
    self.driver = webdriver.Chrome()
    url = dict['B端测试环境']['url']
    self.driver.get(url)
    self.driver.implicitly_wait(15)
    self.driver.maximize_window()
    self.driver.find_element_by_css_selector(dict['B端测试环境']['用户名输入框']).send_keys(dict['B端测试环境']['登录用户名'])
    self.driver.find_element_by_css_selector(dict['B端测试环境']['密码输入框']).send_keys(dict['B端测试环境']['登录密码'])
    time.sleep(1)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['登录按钮']).click()
    time.sleep(2)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['线上']).click()
    time.sleep(2)
    self.driver.switch_to_frame(1)
    time.sleep(1)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['线上渠道']).click()
    time.sleep(1)
    self.driver.switch_to_default_content()
    time.sleep(1)
    self.driver.switch_to_frame(2)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['盈客宝管理']).click()
    time.sleep(1)
    self.driver.switch_to_default_content()
    self.driver.switch_to_frame(3)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['会员注册设置']).click()
    time.sleep(1)
    # 选择购买入会套餐
    self.driver.switch_to_frame(1)
    self.driver.find_element_by_css_selector(dict['B端测试环境']['购买入会套餐']).click()
    time.sleep(1)
    self.driver.find_element_by_xpath(dict['B端测试环境']['超级会员套餐复选框']).click()
    time.sleep(1)
    # 保存按钮
    self.driver.find_element_by_css_selector(dict['B端测试环境']['入会方式保存按钮']).click()
    time.sleep(1)
    self.driver.close()

    # 断言
    # 入会方式：0自动注册入会；1购买超级套餐入会
    try:
        sql = dict['mysql']['查询会员入会方式']
        result = MySql.db_Query_233(self,dict['mysql']['datebase233'], sql)
        result2 = re.findall(r"[(](.+?)[,]", str(result))
        wayValues = result2[0]
        if wayValues == '0':
            print(r'当前入会方式为：自动注册入会！')
        elif wayValues == '1':
            print(r'当前入会方式为：购买超级套餐入会！')
    except Exception:
        print('查询入会方式失败！',Exception)


# 后退
def back(self):
    self.driver.keyevent(4)
# 退出
def over(self):
    element = self.driver.quit()
    return element
# 截图
def get_screen(self, path):
    self.driver.get_screenshot_as_file(path)

# 获取界面大小
def get_size(self):
    size = self.driver.get_window_size()
    return size

# 向上滑动屏幕
def swipe_to_up(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

# 向下滑动屏幕
def swipe_to_down(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)
    time.sleep(1)

# 向左滑动屏幕
def swipe_to_left(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

# 向右滑动屏幕
def swipe_to_right(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

# 长按元素
def long_press(self,type,loc):
    if type == 'id':
        element = self.driver.find_element_by_id(loc)
        TouchAction(self.driver).long_press(element).perform()
    elif type == 'xpath':
        element = self.driver.find_element_by_xpath(loc)
        TouchAction(self.driver).long_press(element).perform()
    elif type == 'class_name':
        element = self.driver.find_element_by_class_name(loc)
        TouchAction(self.driver).long_press(element).perform()
    elif type == 'text':
        element = self.driver.file_detector_context(loc)
        TouchAction(self.driver).long_press(element).perform()

# 点击元素
def click(self,loc):
    self.driver.find_element_by_xpath(loc).click()

# 获取文本
def get_text(self,loc):
    text = self.driver.find_element_by_xpath(loc).text

# 文本框输入
def input(self,loc,value):
    self.driver.find_element_by_xpath(loc).send_keys(value)

















