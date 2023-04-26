#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import time
from configuration_reader import MyPath


class MyDataBaseHander:
    def __init__(self):
        mypath = MyPath()
        self.db_path = mypath.database_path

    # 连接到数据库
    def connect(self):
        conn = None
        attempts = 0
        while attempts < 3:
            try:
                conn = sqlite3.connect(self.db_path)
                break
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")
                attempts += 1
                time.sleep(1)
        return conn

    # 关闭游标和连接
    def close_connection(self, conn):
        if conn:
            conn.close()

    # 查询路径
    def query_path(self, data_name, module_name):
        """ 从数据库表 data_rules 中获取数据doors路径 """
        conn = self.connect()
        result = ""
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            sql = """select data_path from data_module_info where data_name = '{}' and module_name like '{}'""" \
                .format(data_name, module_name)
            try:
                cursor.execute(sql)
                result = cursor.fetchall()[0][0]
            except Exception as e:
                print(f"Error querying data: {e}")
        else:
            print("Failed to connect to database.")
        self.close_connection(conn)
        return result

    def select_data_list(self):
        """ 从数据库表 data_rules 中获取数据清单 """
        conn = self.connect()
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            sql = """
            SELECT data_name,module_name 
            FROM data_rules 
            WHERE formula_type != '' AND formula_type IS NOT NULL
            """
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
            except Exception as e:
                print(f"Error querying data: {e}")
        else:
            print("Failed to connect to database.")
        self.close_connection(conn)
        select_result = result
        # 返回一个列表，元组(data_name,module_name)作为列表元素
        return select_result

    def select_data_list_by_module_name(self, module_name):
        """ 从数据库表 data_rules 中根据 module_name 获取数据清单 """
        conn = self.connect()
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            sql = """
            SELECT data_name,module_name 
            FROM data_rules 
            WHERE formula_type != '' AND module_name = '{}' AND formula_type IS NOT NULL
            """.format(module_name)
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
            except Exception as e:
                print(f"Error querying data: {e}")
        else:
            print("Failed to connect to database.")
        self.close_connection(conn)
        select_result = result
        # 返回一个列表，元组(data_name,module_name)作为列表元素
        return select_result


    def select_data_formula(self,data_name,module_name):
        """ 从数据库表 data_rules 中获取数据公式 """
        conn = self.connect()
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            sql = """
            SELECT formula_type,variable_name, factor, formula 
            FROM data_rules 
            WHERE data_name = '{}' AND module_name = '{}'
            """ .format(data_name, module_name)
            try:
                cursor.execute(sql)
                result = cursor.fetchone()
            except Exception as e:
                print(f"Error querying data: {e}")
        else:
            print("Failed to connect to database.")
        self.close_connection(conn)
        select_result = result
        print("data_formula is",result)
        # 返回一个元组(formula_type,variable_name, factor, formula)
        return select_result


    def update_data_update(self,data_name,module_name,value_previous,value_new,series,is_pn_equal,is_gdm_equal):
        """ 保存数据至数据库表 data_update """
        conn = self.connect()
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            sql_select = """
            SELECT * FROM data_update 
            WHERE data_name = '{}' AND module_name = '{}' AND series = '{}'
            """ .format(data_name, module_name, series)
            try:
                cursor.execute(sql_select)
                result = cursor.fetchone()
            except Exception as e:
                print(f"Error querying data: {e}")

            if result:
                sql_update = """
            UPDATE data_update
            SET value_previous = '{}', value_new = '{}', is_pn_equal = {}, is_gdm_equal = {} 
            WHERE data_name = '{}' AND module_name = '{}' AND series = '{}'
            """ .format(value_previous,value_new,is_pn_equal,is_gdm_equal,data_name,module_name,series)
            else:
                sql_update = """
            INSERT INTO data_update 
            (data_name,module_name,value_previous,value_new,series,is_pn_equal,is_gdm_equal) 
            VALUES ('{}','{}', '{}', '{}','{}',{},{})
                """.format(data_name, module_name, value_previous, value_new, series, is_pn_equal, is_gdm_equal)
            try:
                cursor.execute(sql_update)
                conn.commit()
            except Exception as e:
                print(f"Error querying data: {e}")
            # commit the changes
        else:
            print("Failed to connect to database.")
        self.close_connection(conn)
        return

    def update_new_data_update(self, data_name, module_name, value_new, series, is_gdm_equal):
        """ 保存数据至数据库表 data_update """
        conn = self.connect()
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            sql_select = """
             SELECT * FROM data_update 
             WHERE data_name = '{}' AND module_name = '{}' AND series = '{}'
             """.format(data_name, module_name, series)
            try:
                cursor.execute(sql_select)
                result = cursor.fetchone()
            except Exception as e:
                print(f"Error querying data: {e}")

            if result:
                sql_update = """
             UPDATE data_update
             SET value_new = '{}', is_gdm_equal = {} 
             WHERE data_name = '{}' AND module_name = '{}' AND series = '{}'
             """.format(value_new, is_gdm_equal, data_name, module_name, series)
            else:
                sql_update = """
             INSERT INTO data_update 
             (data_name,module_name,value_new,series,is_gdm_equal) 
             VALUES ('{}','{}', '{}','{}',{})
                 """.format(data_name, module_name, value_new, series, is_gdm_equal)
            try:
                cursor.execute(sql_update)
                conn.commit()
            except Exception as e:
                print(f"Error querying data: {e}")
            # commit the changes
        else:
            print("Failed to connect to database.")
        self.close_connection(conn)
        return

    def select_data_update(self, data_name, module_name, series=""):
        """ 根据字段 data_name 、module_name 、series 从数据库表 data_update 中获取数据属性 """
        conn = self.connect()
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            if series == "":
                sql = """
                SELECT data_name, module_name, value_previous, value_new, series, is_pn_equal, is_gdm_equal
                FROM data_update 
                WHERE data_name = '{}' AND module_name = '{}' 
                """ .format(data_name, module_name)
            else:
                sql = """
                SELECT data_name, module_name, value_previous, value_new, series, is_pn_equal, is_gdm_equal
                FROM data_update 
                WHERE data_name = '{}' AND module_name = '{}' AND series = '{}' 
                """ .format(data_name, module_name, series)
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
            except Exception as e:
                print(f"Error querying data: {e}")
        else:
            print("Failed to connect to database.")
        self.close_connection(conn)
        select_result = result
        # 返回一个列表，列表元素为元组(data_name, module_name, value_previous, value_new, series, is_pn_equal, is_gdm_equal)
        return select_result


    def select_data_list_by_series(self, series="NS"):
        """ 根据字段 series 从数据库表 data_update 中获取数据清单 """
        result = []
        conn = self.connect()
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            sql = """
            SELECT data_name, module_name, value_previous, value_new, series, is_pn_equal, is_gdm_equal
            FROM data_update 
            WHERE series = '{}' 
            """ .format(series)
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
            except Exception as e:
                print(f"Error querying data: {e}")
        else:
            print("Failed to connect to database.")
        self.close_connection(conn)
        select_result = result
        # 返回一个列表，列表元素为元组(data_name, module_name, value_previous, value_new, series, is_pn_equal, is_gdm_equal)
        return select_result



    def select_update_data_list(self):
        """ 从数据库表 data_update 中获取所有数据清单 """
        conn = self.connect()
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            sql = """
            SELECT data_name,module_name, value_previous, value_new, series, is_pn_equal, is_gdm_equal
            FROM data_update 
            """
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
            except Exception as e:
                print(f"Error querying data: {e}")
        else:
            print("Failed to connect to database.")
        self.close_connection(conn)
        select_result = result
        # 返回一个列表，元组(data_name,module_name, value_previous, value_new, series, is_pn_equal, is_gdm_equal)作为列表元素
        return select_result



if __name__ == '__main__':
    mydbhander = MyDataBaseHander()
    # select_result = mydbhander.select_data_list()
    # print(select_result)
    # print(len(select_result))
    # select_result = mydbhander.select_data_formula(select_result[0][0],select_result[0][1])
    # print(select_result)

    # data_name = "TESTDATANAME1"
    # module_name = "TESTMODULENAME1"
    # value_previous = "value_previous3"
    # value_new = "value_new3"
    # series = "series2"
    # is_pn_equal = True
    # is_gdm_equal = True
    # mydbhander.update_data_update(data_name,module_name,value_previous,value_new,series,is_pn_equal,is_gdm_equal)

    # data_name = "Min_Vehicle_speed"
    # module_name = "LSS"
    # series = ""
    # select_result = mydbhander.select_data_update(data_name, module_name, series)
    # for i in select_result:
    #     print("data_name = ", i[0])
    #     print("module_name = ", i[1])
    #     print("value_previous = ", i[2])
    #     print("value_new = ", i[3])
    #     print("series = ", i[4])
    #     print("is_pn_equal = ", i[5], type(i[5]))
    #     print("is_gdm_equal = ", i[6], type(i[6]))


    update_list = mydbhander.select_data_list_by_series()
    print(update_list)