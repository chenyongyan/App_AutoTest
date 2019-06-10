# encoding:utf-8

import unittest,time
from ddt import ddt, data, unpack, file_data
import itertools
from selenium import webdriver


@ddt
class case(unittest.TestCase):


    def test1(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.get('http://172.16.0.161:9999/admin')
        self.dr.implicitly_wait(20)

        self.dr.find_element_by_id('txtName').send_keys('admin')
        self.dr.find_element_by_id('txtPwd').send_keys('1')
        self.dr.find_element_by_id('fm-login-submit').click()
        time.sleep(2)
        self.dr.find_element_by_id('mumu_group100001400').click()
        time.sleep(1)
        self.dr.find_element_by_id('left_100001400').click()
        time.sleep(1)
        self.dr.find_element_by_id('left_101016100').click()
        time.sleep(3)
        self.dr.switch_to_frame(1)

        # 会员卡号
        #self.dr.find_element_by_id("txtLeaguerCode").send_keys(phone)
        # 会员姓名
        #self.dr.find_element_by_id("txtLeaguergName").send_keys(name)



        # 账期
        a = ['//*[@id="asd1fgh3jkldll1"]/div/div/ul/li[1]','//*[@id="asd1fgh3jkldll1"]/div/div/ul/li[2]','//*[@id="asd1fgh3jkldll1"]/div/div/ul/li[3]','//*[@id="asd1fgh3jkldll1"]/div/div/ul/li[4]']
        # 类型
        b = ['//*[@id="IsChange"]/div/div/ul/li[2]', '//*[@id="IsChange"]/div/div/ul/li[3]']
        for x in itertools.product(a, b):

            self.dr.find_element_by_xpath('//*[@id="asd1fgh3jkldll1"]/div/div').click()
            time.sleep(1)
            self.dr.find_element_by_xpath(x[0]).click()

            self.dr.find_element_by_xpath('//*[@id="IsChange"]/div/div/button').click()
            time.sleep(1)
            self.dr.find_element_by_xpath(x[1]).click()

            self.dr.find_element_by_xpath('/html/body/div[1]/div[6]/button[1]').click()

    @data('1', '2', '3')
    def test2(self, keys):
        print(keys)

    @data(['value_1','key_1'], ['value_2','key_2'],['value_3','key_3'],['value_4','key_4'])
    @unpack
    def test3(self, values, keys):
        # print(values)
        print(keys)

    @file_data(r'E:\App_AutoTest\Public_file\test.json')
    def test4(self,values):
        print(values)


if __name__ == "__main__":
    unittest.main()
