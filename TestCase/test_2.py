
from Public_method import MySql
import json,unittest,re,time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Public_method import MySql
import traceback

file = open("E:\\App_AutoTest\\Public_file\\date.json", "r", encoding="UTF-8")
dict = json.load(file)


class case(unittest.TestCase):

    # 清空注册用户数据
    def test1(self):
        sql1 = "DELETE FROM saas_member_test_20190428.MEM_UserBase WHERE Phone = '13424474182'"
        sql2 = "update dbo.Mall_Leaguer set Phone=null where Phone='13424474182'"
        sql3 = "update dbo.Mall_LeaguerApply set PhoneNumber=null where PhoneNumber='13424474182'"
        sql4 = "DELETE FROM dbo.Ykb_NewMembersGivingLog WHERE Phone = '13424474182'"

        MySql.db_NotQuery_200(self,'saas_member_test_20190428',sql1)
        MySql.db_NotQuery_233(self,'YCHMALL',sql2)
        MySql.db_NotQuery_233(self,'YCHMALL',sql3)
        MySql.db_NotQuery_233(self,'YCHMALL',sql4)



if __name__=="__main__":
    unittest.main()