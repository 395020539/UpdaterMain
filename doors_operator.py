#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os
import time
from win32api import GetShortPathName
from configuration_reader import MyConfig, MyPath

class DoorsOperator:
    def __init__(self):
        myconfig = MyConfig()
        mypath = MyPath()
        self.doors_exe_path = myconfig.doors_exe_path
        self.username = myconfig.doors_username
        self.password = myconfig.doors_password
        self.app_dir = mypath.app_dir

    def run_doors(self):
        # batchserver_dxl_path = app_dir + r"\batchserver.dxl"
        batchserver_dxl_path = self.app_dir + r"\temp_dxl.dxl"
        # Create batch_dxl
        create_batch_dxl(1)
        if os.path.exists(self.doors_exe_path):
            doors_exe_path = GetShortPathName(self.doors_exe_path)
            # print(doors_exe_path)
            doors_cmd_options = r' -user {} -password {} -batch {} -k -W'.format(self.username, self.password,
                                                                              batchserver_dxl_path)
            # print(doors_cmd_options)
            doors_cmd = doors_exe_path + doors_cmd_options
            print(doors_cmd)
            try:
                exe = os.popen(doors_cmd)
                time.sleep(20)
                print("doors exe: ", exe)
            except Exception as e:
                print("An error occurred:", e)
        else:
            doors_exe_path = ""
            print("Doors路径无效")


    def kill_doors(self):
        os.system('taskkill /f /im %s' % 'doors.exe')
        # remove batch_dxl
        create_batch_dxl(2)


def create_batch_dxl(type):
    """ type 1: create; type 2: remove """
    # 获取可执行文件的路径
    if getattr(sys, 'frozen', False):
        # 如果是打包后的 exe 文件，获取可执行文件的路径
        app_dir = os.path.dirname(sys.executable)
    else:
        # 如果是源代码，获取脚本文件所在的目录
        app_dir = os.path.dirname(os.path.abspath(__file__))

    temp_dxl_path = os.path.join(app_dir, 'temp_dxl.dxl')
    print("temp_dxl_path = ", temp_dxl_path)
    if type == 1:
        dxl_content = r"""
// batchserver.dxl
IPC ipc = server 5094
string request
/* add functions for you interface here */
while (true) {
    if (accept(ipc)) {
        if (!recv(ipc, request)) {
            warn "Server has disconnected"
            break
        }
    } else {
        warn "error accepting client connection"
        break
    }

    // print "request: "
    // print request
    // print "\n"
    errors = false
    if (request == "shutdown_") {
        send(ipc, "done_")
        break
    }

    if (request == "errors_")
        break

    if (request == "quit_")
        continue

    ans = eval_ request
    if (ans == "errors in eval_ string") {
        print "errors in request\n"
    }

    send(ipc, ans)
    disconnect(ipc)
}
        """
        try:
            f = open(temp_dxl_path, 'w')
            f.write(dxl_content)
            f.close()
        except Exception as e:
            print("error creating socket: ", e)
    if type == 2:
        print("delete temp_dxl.dxl")
        if os.path.exists(temp_dxl_path):
            os.remove(temp_dxl_path)


if __name__ == '__main__':
    mydoors = DoorsOperator()
    mydoors.run_doors()
    mydoors.kill_doors()
