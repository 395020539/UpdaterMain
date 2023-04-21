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


    def select_data_formula(self,data_name,module_name):
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
        # 返回一个元组(formula_type,variable_name, factor, formula)
        return select_result



if __name__ == '__main__':
    mydbhander = MyDataBaseHander()
    select_result = mydbhander.select_data_list()
    print(select_result)
    print(len(select_result))
    select_result = mydbhander.select_data_formula(select_result[0][0],select_result[0][1])
    print(select_result)