# user/python3
# encoding:utf-8

import pymysql,json,pymssql

file = open("E:\\App_AutoTest\\Public_file\\date.json", "r", encoding="UTF-8")
dict_load = json.load(file)


def db_Query_200(self,database,sql):
    # 链接数据库
    self.db = pymysql.connect(
        host=dict_load['mysql']['host200'],
        user=dict_load['mysql']['username200'],
        password=dict_load['mysql']['password200'],
        database=database
    )
    try:
        self.db
    except:
        print('数据库连接失败！请检查！')
    # 获取数据库列表
    self.cursor = self.db.cursor()
    self.cursor.execute('SHOW DATABASES')
    # 查询
    self.cursor.execute(sql)
    result = self.cursor.fetchall()
    self.db.close()
    return result

def db_Query_233(self,database,sql):
    # 链接数据库
    self.db = pymssql.connect(
        host=dict_load['mysql']['host233'],
        user=dict_load['mysql']['username233'],
        password=dict_load['mysql']['password233'],
        database=database
    )
    self.db.cursor()
    try:
        self.db
    except:
        print('数据库连接失败！请检查！')
    # 获取数据库列表
    self.cursor = self.db.cursor()
    # 查询
    self.cursor.execute(sql)
    result = self.cursor.fetchall()
    self.db.close()
    return result


def db_NotQuery_200(self,database,sql):
    # 链接数据库
    self.db = pymysql.connect(
        host=dict_load['mysql']['host200'],
        user=dict_load['mysql']['username200'],
        password=dict_load['mysql']['password200'],
        database=database
    )
    try:
        self.db

    except:
        print('数据库连接失败！请检查！')
    # 获取数据库列表
    self.cursor = self.db.cursor()
    self.cursor.execute('SHOW DATABASES')
    # 查询
    self.cursor.execute(sql)
    self.db.commit()
    try:
        self.cursor.execute(sql)
    except:

        print('SQL执行失败，请检查！')
    self.db.close()

def db_NotQuery_233(self,database,sql):
    # 链接数据库
    self.db = pymssql.connect(
        host=dict_load['mysql']['host233'],
        user=dict_load['mysql']['username233'],
        password=dict_load['mysql']['password233'],
        database=database
    )
    try:
        self.db

    except:
        print('数据库连接失败！请检查！')
    # 获取数据库列表
    self.cursor = self.db.cursor()
    # 查询
    self.cursor.execute(sql)
    self.db.commit()
    try:
        self.cursor.execute(sql)
    except:

        print('SQL执行失败，请检查！')
    self.db.close()

