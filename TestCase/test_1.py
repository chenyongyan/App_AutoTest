# ecoding=utf-8
__author__ = "Jechen"

from appium import webdriver
from Public_method import mean,MySql
import unittest,time,json,re


file = open(r"E:\App_AutoTest\Public_file\date.json", "r", encoding="UTF-8")
dict = json.load(file)

class case(unittest.TestCase):

# 初始化
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = dict['machine']['platformName']
        desired_caps['platformVersion'] = dict['machine']['platformVersion']
        desired_caps['deviceName'] = dict['machine']['deviceName']
        desired_caps['appPackage'] = dict['machine']['appPackage']
        desired_caps['appActivity'] = dict['machine']['appActivity']
        desired_caps['appWaitActivity'] = dict['machine']['appWaitActivity']
        desired_caps['automationName'] = dict['machine']['automationName']
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote(dict['machine']['webdriver'], desired_caps)

# 自动注册登录
    def test1(self):
        # 微信快捷注册登陆
        mean.wechat_login(self)
        self.driver.close()
        # 断言
        page_phoneNumber = mean.get_text(self,dict['element']['首页手机号'])
        sql = 'SELECT phone FROM MEM_UserBase WHERE Phone =' + str(page_phoneNumber)
        text1 = MySql.db_Query_200(self,dict['mysql']['datebase200'],sql)
        text2 = re.findall(r"'(.+?)'",str(text1))
        db_phoneNumber = text2[0]
        try:
            assert page_phoneNumber == db_phoneNumber
            print('微信快捷注册登录入会成功！')
        except:
            print('微信快捷注册登录入会失败！')

        # 清空测试数据
        delete_localhost_sql = "DELETE FROM saas_member_test_20190428.MEM_UserBase WHERE Phone = " + str(page_phoneNumber)
        try:
            MySql.db_NotQuery_200(self,dict['mysql']['datebase200'],delete_localhost_sql)
        except Exception as err:
            print(err)
        delete_ywpt_sql1 = "update dbo.Mall_Leaguer set Phone=null where Phone = " + str(page_phoneNumber)
        delete_ywpt_sql2 = "update dbo.Mall_LeaguerApply set PhoneNumber=null where PhoneNumber = " + str(page_phoneNumber)
        delete_ywpt_sql3 = "DELETE FROM dbo.Ykb_NewMembersGivingLog WHERE Phone = " + str(page_phoneNumber)
        try:
            MySql.db_NotQuery_233(self,dict['mysql']['datebase233'], delete_ywpt_sql1)
            MySql.db_NotQuery_233(self,dict['mysql']['datebase233'], delete_ywpt_sql2)
            MySql.db_NotQuery_233(self,dict['mysql']['datebase233'], delete_ywpt_sql3)

        except Exception as err:
            print(err)

        # 断言数据是否清空
        sql = "select Phone from saas_member_test_20190428.MEM_UserBase WHERE Phone = " + str(page_phoneNumber)
        sql1 = "select Phone from dbo.Mall_Leaguer where Phone = " + str(page_phoneNumber)
        sql2 = "select Phone from dbo.Ykb_NewMembersGivingLog where Phone = " + str(page_phoneNumber)
        sql3 = "select PhoneNumber from dbo.Mall_LeaguerApply where PhoneNumber = " + str(page_phoneNumber)
        locdb = MySql.db_Query_200(self,dict['mysql']['datebase200'],sql)
        ywpt1 = MySql.db_Query_233(self,dict['mysql']['datebase233'],sql1)
        ywpt2 = MySql.db_Query_233(self, dict['mysql']['datebase233'], sql2)
        ywpt3 = MySql.db_Query_233(self, dict['mysql']['datebase233'], sql3)

        try:
            assert locdb == () and ywpt1 == [] and ywpt2 == [] and ywpt3 == []
            print('用户数据清除成功！')
        except Exception as er:
            print(er)



    def test2(self):
        # 手机号注册登录
        mean.phone_login(self)
        self.driver.close()
        # 断言
        page_phoneNumber = self.driver.find_element_by_xpath('//*[@class="android.view.View" and @index="2"]').text
        sql = 'SELECT phone FROM MEM_UserBase WHERE Phone =' + str(page_phoneNumber)
        text1 = MySql.db_Query_200(self,dict['mysql']['datebase200'],sql)
        text2 = re.findall(r"'(.+?)'", str(text1))
        db_phoneNumber = text2[0]
        try:
            assert page_phoneNumber == db_phoneNumber
            print('微信快捷注册登录入会成功！')
        except:
            print('微信快捷注册登录入会失败！')

        # 清空测试数据
        delete_localhost_sql = "DELETE FROM saas_member_test_20190428.MEM_UserBase WHERE Phone = " + str(
            page_phoneNumber)
        try:
            MySql.db_NotQuery_200(self, dict['mysql']['datebase200'], delete_localhost_sql)
        except Exception as err:
            print(err)
        delete_ywpt_sql1 = "update dbo.Mall_Leaguer set Phone=null where Phone = " + str(page_phoneNumber)
        delete_ywpt_sql2 = "update dbo.Mall_LeaguerApply set PhoneNumber=null where PhoneNumber = " + str(
            page_phoneNumber)
        delete_ywpt_sql3 = "DELETE FROM dbo.Ykb_NewMembersGivingLog WHERE Phone = " + str(page_phoneNumber)
        try:
            MySql.db_NotQuery_233(self, dict['mysql']['datebase233'], delete_ywpt_sql1)
            MySql.db_NotQuery_233(self, dict['mysql']['datebase233'], delete_ywpt_sql2)
            MySql.db_NotQuery_233(self, dict['mysql']['datebase233'], delete_ywpt_sql3)

        except Exception as err:
            print(err)

        # 断言数据是否清空
        sql = "select Phone from saas_member_test_20190428.MEM_UserBase WHERE Phone = " + str(page_phoneNumber)
        sql1 = "select Phone from dbo.Mall_Leaguer where Phone = " + str(page_phoneNumber)
        sql2 = "select Phone from dbo.Ykb_NewMembersGivingLog where Phone = " + str(page_phoneNumber)
        sql3 = "select PhoneNumber from dbo.Mall_LeaguerApply where PhoneNumber = " + str(page_phoneNumber)
        locdb = MySql.db_Query_200(self, dict['mysql']['datebase200'], sql)
        ywpt1 = MySql.db_Query_233(self, dict['mysql']['datebase233'], sql1)
        ywpt2 = MySql.db_Query_233(self, dict['mysql']['datebase233'], sql2)
        ywpt3 = MySql.db_Query_233(self, dict['mysql']['datebase233'], sql3)

        try:
            assert locdb == () and ywpt1 == [] and ywpt2 == [] and ywpt3 == []
            print('用户数据清除成功！')
        except Exception as er:
            print(er)

# 盈客宝储值充值
    # 预存款充值
    def test3(self):
        mean.wechat_login(self)
        time.sleep(1)
        mean.swipe_to_down(self)
        # 获取充值前预存款储值
        yck_befor = mean.get_text(self,dict['element']['预存款储值'])
        time.sleep(1)
        mean.click(self,dict['element']['预存款充值按钮'])
        time.sleep(1)
        mean.click(self,dict['element']['商品100预存款'])
        time.sleep(1)
        mean.click(self,dict['element']['支付按钮'])
        time.sleep(1)
        # 微信输入密码弹出安全键盘，界面无输入控件，不知道用send_keys方法是否可行
        mean.input(self,dict['element']['微信密码输入框'],dict['element']['微信支付密码'])
        time.sleep(1)
        mean.click(self,dict['element']['微信支付完成按钮'])
        time.sleep(1)
        mean.click(self,dict['element']['查看订单详情按钮'])
        time.sleep(1)
        orde_text = mean.get_text(self,dict['element']['获取订单状态'])  # 订单状态：已完成
        time.sleep(1)
        mean.back(self)
        time.sleep(1)
        mean.swipe_to_down(self)
        time.sleep(1)
        yck_after = mean.get_text(self,dict['element']['预存款储值'])
        self.driver.close()
        # 断言
        try:
            #这里再加个业务平台数预存款储值据库的校验
            assert yck_befor + int(100) == yck_after
            assert orde_text == '订单状态：已完成'
            print('预存款充值成功！订单状态已完成！')
        except:
            print('预存款充值失败！')


    # 代币预存款充值
    def test4(self):
        # 获取充值前代币的储值
        a = MySql.db_Query_233(self,dict['mysql']['datebase233'],dict['mysql']['查询代币'])
        b = re.findall(r"['](.+?)[.]",str(a))
        db_befor = b[0]
        time.sleep(1)
        # 获取充值前预存款的储值
        mean.wechat_login(self)
        time.sleep(1)
        mean.swipe_to_down(self)
        time.sleep(1)
        yck_befor = mean.get_text(self,dict['element']['预存款储值'])
        time.sleep(1)
        # 登录盈客宝充值代币
        mean.wechat_login(self)
        mean.swipe_to_down(self)
        mean.click(self,dict['element']['代币充值按钮'])
        time.sleep(1)
        # 选择充值套餐
        mean.click(self,dict['element']['商品100代币'])
        time.sleep(1)
        # 选取预存款支付
        mean.click(self,dict['element']['预存款支付'])
        time.sleep(1)
        # 点击支付
        mean.click(self,dict['element']['支付按钮'])
        time.sleep(1)
        # 输入会员密码
        mean.input(self,dict['element']['会员密码输入框'],dict['element']['会员密码'])
        time.sleep(1)
        # 点击【确定】
        mean.click(self,dict['element']['会员密码确定按钮'])
        time.sleep(1)
        # 充值后代币的储值
        c = MySql.db_Query_233(self,'YCHMALL',dict['mysql']['查询代币'])
        d = re.findall(r"['](.+?)[.]",str(c))
        db_after = d[0]
        # 充值后预存款储值
        time.sleep(2)
        mean.click(self,dict['element']['订单完成返回首页按钮'])
        time.sleep(1)
        mean.swipe_to_down(self)
        time.sleep(1)
        yck_after = mean.get_text(self,dict['element']['预存款储值'])
        self.driver.close()
        # 断言
        try:
            assert db_befor + int(100) == db_after
            assert yck_befor - float(0.01) == yck_after
            print('代币充值成功，预存款扣款正确！')
        except:
            print('代币充值失败！')

    # 代币微信充值
    def test5(self):
        # 获取充值前代币的储值
        a = MySql.db_Query_233(self,dict['mysql']['datebase233'], dict['mysql']['查询代币'])
        b = re.findall(r"['](.+?)[.]", str(a))
        db_befor = b[0]
        # 获取充值前预存款的储值
        mean.wechat_login(self)
        time.sleep(1)
        mean.swipe_to_down(self)
        time.sleep(1)
        yck_befor = mean.get_text(self,dict['element']['预存款储值'])
        time.sleep(1)
        # 登录盈客宝充值代币
        mean.click(self,dict['element']['代币充值按钮'])
        time.sleep(1)
        # 选择充值套餐
        mean.click(self,dict['element']['商品100代币'])
        time.sleep(1)
        # 选择微信支付
        mean.click(self,dict['element']['微信支付'])
        time.sleep(1)
        mean.click(self,dict['element']['支付按钮'])
        time.sleep(1)
        mean.input(self,dict['element']['微信支付密码输入框'],dict['element']['微信支付密码'])
        time.sleep(1)
        # 获取充值后预存款储值
        mean.click(self,dict['element']['订单返回按钮'])
        time.sleep(1)
        mean.swipe_to_down(self)
        time.sleep(1)
        yck_after = mean.get_text(self,dict['element']['预存款储值'])
        self.driver.close()
        # 获取充值后的的代币
        c = MySql.db_Query_233(self,dict['mysql']['datebase233'], dict['mysql']['查询代币'])
        d = re.findall(r"['](.+?)[.]", str(c))
        db_after = d[0]
        # 断言
        try:
            assert db_befor + int(100) == db_after
            assert yck_befor - float(0.01) == yck_after
            print('微信充值代币成功！')
        except:
            print('微信充值代币失败！')

    # 金币预存款充值
    def test6(self):
        # 获取当前金币储值
        a = MySql.db_Query_233(self, dict['mysql']['datebase233'], dict['mysql']['查询金币'])
        b = re.findall(r"['](.+?)[.]", str(a))
        jb_befor = b[0]
        # 获取当前预存款储值
        mean.wechat_login(self)
        time.sleep(1)
        mean.swipe_to_down(self)
        time.sleep(1)
        yck_befor = mean.get_text(self,dict['element']['预存款储值'])
        time.sleep(1)
        mean.click(self,dict['element']['金币充值按钮'])
        time.sleep(1)
        mean.click(self,dict['element']['商品100金币'])
        time.sleep(1)
        mean.click(self,dict['element']['预存款支付'])
        time.sleep(1)
        mean.click(self,dict['element']['支付按钮'])
        time.sleep(1)
        mean.input(self,dict['element']['会员密码输入框'],dict['element']['会员密码'])
        time.sleep(1)
        mean.click(self,dict['element']['会员密码确定按钮'])
        time.sleep(1)
        mean.click(self,dict['element']['订单完成返回首页按钮'])
        time.sleep(1)
        mean.swipe_to_down(self)
        time.sleep(1)
        # 获取充值后预存款余额
        yck_after = mean.get_text(self,dict['element']['预存款储值'])
        # 获取充值后金币储值
        c = MySql.db_Query_233(self, dict['mysql']['datebase233'], dict['mysql']['查询金币'])
        d = re.findall(r"['](.+?)[.]", str(c))
        jb_after = d[0]
        self.driver.close()
        # 断言
        try:
            assert yck_after + float(0.01) == yck_befor
            assert jb_befor + int(100) == jb_after
            print('金币充值成功！')
        except Exception as err:
            print('金币充值失败！',err)

    # 金币微信充值
    def test7(self):
        # 获取当前金币储值
        a = MySql.db_Query_233(self, dict['mysql']['datebase233'], dict['mysql']['查询金币'])
        b = re.findall(r"['](.+?)[.]", str(a))
        jb_befor = b[0]
        # 获取当前预存款储值
        mean.wechat_login(self)
        time.sleep(1)
        mean.swipe_to_down(self)
        time.sleep(1)
        mean.click(self, dict['element']['金币充值按钮'])
        time.sleep(1)
        mean.click(self, dict['element']['商品100金币'])
        time.sleep(1)
        mean.click(self, dict['element']['微信支付'])
        time.sleep(1)
        mean.click(self, dict['element']['支付按钮'])
        time.sleep(1)
        mean.input(self, dict['element']['微信支付密码输入框'], dict['element']['微信支付密码'])
        time.sleep(1)
        mean.click(self, dict['element']['订单完成返回首页按钮'])
        time.sleep(1)
        mean.swipe_to_down(self)
        time.sleep(1)
        # 获取充值后金币储值
        c = MySql.db_Query_233(self, dict['mysql']['datebase233'], dict['mysql']['查询金币'])
        d = re.findall(r"['](.+?)[.]", str(c))
        jb_after = d[0]
        self.driver.close()
        # 断言
        try:
            assert jb_befor + int(100) == jb_after
            print('金币充值成功！')
        except Exception as err:
            print('金币充值失败！', err)

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()






















































