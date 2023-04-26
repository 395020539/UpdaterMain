#!/usr/bin/python
# -*- coding: utf-8 -*-

from database_hander import MyDataBaseHander
from dxl_command_creator import MyDxlCommand
from dxl_command_sender import DxlSender


if __name__ == '__main__':
    mydbhander = MyDataBaseHander()

    # 获取更新数据清单
    # update_list[(data name, module_name, data_value)]
    update_list = []
    # series 默认为 "NS"
    update_list_temp= mydbhander.select_data_list_by_series()
    print(update_list_temp)
    print(len(update_list_temp))

    for i in update_list_temp:
        if i[5] == 0:
            update_list.append((i[0],i[1],i[3]))
    print(update_list)
    print(len(update_list))

    # 构建Dxl清单
    mydxlcreator = MyDxlCommand()
    mydxl_list = mydxlcreator.create_update_dxl(update_list)

    message_number = len(mydxl_list)
    response_number = 0
    message_counter = 0
    # 实例化Mysender
    mysender = DxlSender()
    mysender.mydoors.run_doors()

    for cmd in mydxl_list:
        message_counter += 1
        print(f"开始发送第{message_counter}条")
        print(cmd)
        response = mysender.send_dxl_command_single(cmd)
        if response != "":
            response_number += 1
            print(f"第{message_counter}条发送成功")
        else:
            print(f"第{message_counter}条发送失败")
        print(f"发送成功{response_number}条")
    print(f"需发送{message_number}条，发送成功{response_number}条")

    mysender.mydoors.kill_doors()