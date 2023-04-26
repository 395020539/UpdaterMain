#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import os


class MyConfig:
    def __init__(self):
        mypath = MyPath()
        self.return_code, self.doors_username, self.doors_password, \
            self.doors_project_path, self.data_file, self.data_suffix \
            = self.read_config(mypath.config_path, mypath.app_dir, mypath.data_dir)
        self.doors_exe_path = r'C:\Program Files (x86)\ibm\Rational\DOORS\9.5\bin\doors.exe'
        print(f"doors_exe_path = \n{self.doors_exe_path}")

    def read_config(self, config_path, app_dir, data_path):
        return_code = "0"
        doors_username = ""
        doors_password = ""
        doors_project_path = ""
        data_file = ""
        data_suffix = ""
        try:
            with open(config_path, 'r', encoding='utf - 8') as f:
                json_data = json.load(f)
                # print(f"json_data = \n{json_data}")
                doors_username = json_data['doors_username']
                print(f"doors_username = \n{doors_username}")
                doors_password = json_data['doors_password']
                print(f"doors_password = \n{doors_password}")
                doors_project_path = "/" + json_data['project_name']
                print(f"doors_project_path = \n{doors_project_path}")
                data_suffix = json_data['data_suffix']
                print(f"data_suffix = \n{data_suffix}")
                data_file = json_data['data_file']
                data_file = os.path.join(data_path, data_file)
                print(f"data_file = \n{data_file}")
        except Exception as e:
            print("An error occurred:", e, config_path)
            return_code = "1"
        finally:
            return return_code, doors_username, doors_password, doors_project_path, data_file, data_suffix

    def check_my_config(self):
        error_flag = 0
        error_message = ""
        e = None

        if self.doors_username == "" or self.doors_username == "Default" or not self.doors_username:
            error_flag = 1
            error_message = "无效的用户名"
        elif self.doors_password == "" or self.doors_password == "Default" or not self.doors_password:
            error_flag = 1
            error_message = "无效的密码"
        elif self.doors_project_path == "/" or self.doors_project_path == "Default" or \
                not self.doors_project_path or self.doors_project_path == "":
            error_flag = 1
            error_message = "无效的项目名"

        return error_flag, error_message


class MyPath:
    def __init__(self):
        if getattr(sys, 'frozen', False):
            # 如果是打包后的 exe 文件，获取可执行文件的路径
            self.app_dir = os.path.dirname(sys.executable)
        else:
            # 如果是源代码，获取脚本文件所在的目录
            self.app_dir = os.path.dirname(os.path.abspath(__file__))

        # 指定所有相关路径
        self.config_dir = os.path.join(self.app_dir, 'Config')
        self.data_dir = os.path.join(self.app_dir, 'Data')
        self.log_dir = os.path.join(self.app_dir, 'Log')
        self.temp_dir = os.path.join(self.app_dir, 'Temp')

        self.config_path = os.path.join(self.config_dir, 'config.json')
        self.database_path = os.path.join(self.config_dir, 'SysEngDataDB.db')
        # 初始化相关路径，如路径不存在，创建路径或文件
        self.init_all_path()

        # 指定参数查询所需文件的路径
        self.file_a2l = r"D:\MyPython\UpdaterMain\Temp\GA1103C0300_RG3_X_SCU3_B3_VAR_04.a2l"
        self.file_geskon = r"D:\MyPython\UpdaterMain\Temp\GA1103C0300_RG3_X_SCU3_B3_VAR_04_geskon.kon"
        self.file_dcm = r"D:\MyPython\UpdaterMain\Temp\DCM_ALL_HYCAN_G08_Feeling first tuning_based on_GA1103C0200_20230222.dcm"
        self.file_mech_table = r"D:\MyPython\UpdaterMain\Temp\HYCAN G08 mechanicalDataSheet-20220812.xlsm"

        print(f"app_dir = \n{self.app_dir}")
        print(f"config_dir = \n{self.config_dir}")
        print(f"data_dir = \n{self.data_dir}")
        print(f"log_dir = \n{self.log_dir}")
        print(f"temp_dir = \n{self.temp_dir}")
        print(f"config_path = \n{self.config_path}")
        print(f"database_path = \n{self.database_path}")

    def init_all_path(self):
        if not os.path.exists(self.config_dir):
            os.mkdir(self.config_dir)
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)

        if not os.path.exists(self.config_path):
            default_cfg = {"doors_username": "Default",
                           "doors_password": "Default",
                           "project_name": "Default",
                           "data_suffix": "Default",
                           "data_file": "Default",
                           "file_mech": "Default",
                           "file_geskon": "Default",
                           "file_dcm": "Default",
                           "file_a2l": "Default"}
            json_data = json.dumps(default_cfg, indent=4)
            # Write the JSON string to a file
            with open(self.config_path, 'w') as f:
                f.write(json_data)
        if not os.path.exists(self.database_path):
            print("Database missing")




class MyFilePath:
    def __init__(self):
        mypath = MyPath()
        self.return_code, self.file_mech, self.file_geskon, self.file_dcm, self.file_a2l \
            = self.read_path(mypath.config_path)
    def read_path(self, config_path):
        return_code = "0"

        try:
            with open(config_path, 'r', encoding='utf - 8') as f:
                json_data = json.load(f)
                file_mech = json_data['file_mech']
                print(f"file_mech = \n{file_mech}")
                file_geskon = json_data['file_geskon']
                print(f"file_geskon = \n{file_geskon}")
                file_dcm = "/" + json_data['file_dcm']
                print(f"file_dcm = \n{file_dcm}")
                file_a2l = json_data['file_a2l']
                print(f"file_a2l = \n{file_a2l}")
        except Exception as e:
            print("An error occurred:", e, config_path)
            return_code = "1"
        finally:
            return return_code, file_mech, file_geskon, file_dcm, file_a2l





if __name__ == '__main__':
    mypath = MyPath()

    myconfig = MyConfig()
    # print("doors_username: ", myconfig.doors_username)
    # print("doors_password: ", myconfig.doors_password)
    # print("doors_project_path: ", myconfig.doors_project_path)
    # print("data_file: ", myconfig.data_file)
    # print("doors_exe_path: ", myconfig.doors_exe_path)
    # print("data_suffix: ", myconfig.data_suffix)

    myfilepath = MyFilePath()
    print("file_mech: ", myconfig.file_mech)
    print("file_geskon: ", myconfig.file_geskon)
    print("file_dcm: ", myconfig.file_dcm)
    print("file_a2l: ", myconfig.file_a2l)

