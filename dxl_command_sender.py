#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import socket
import os
from doors_operator import DoorsOperator
from dxl_command_creator import MyDxlCommand

class DxlSender:
    def __init__(self):
        self.mydoors = DoorsOperator()

    def send_dxl_commands(self,dxl_commands):
        self.mydoors.run_doors()
        start = time.monotonic()
        response_number = 0
        message_counter = 0
        response = ""
        if isinstance(dxl_commands, list):
            message_number = len(dxl_commands)
            for dxl_command in dxl_commands:
                message_counter += 1
                print(f"开始发送第{message_counter}条")
                print("dxl_command = \n", dxl_command)
                response = self.send_socket_message(dxl_command)
                if response != "":
                    response_number += 1
                    print(f"第{message_counter}条发送成功")
                else:
                    print(f"第{message_counter}条发送失败")
                print(f"发送成功{response_number}条")
                time.sleep(0.2)
        else:
            message_number = 1
            response = self.send_socket_message(dxl_commands)
            if response != "":
                response_number += 1
        print(f"需发送{message_number}条，发送成功{response_number}条")
        end = time.monotonic()

        print(f"运行耗时: {(end - start)} s")
        self.mydoors.kill_doors()
        return response

    def send_dxl_command_single(self, dxl_commands):
        # # 开启 doors IPC server
        # self.mydoors.run_doors()
        start = time.monotonic()
        response_number = 0
        response = ""
        message_number = 1
        response = self.send_socket_message(dxl_commands)
        if response != "":
            response_number += 1
        print(f"需发送{message_number}条，发送成功{response_number}条")
        end = time.monotonic()

        print(f"运行耗时: {(end - start)} s")
        # # 关闭 doors 进程
        # self.mydoors.kill_doors()
        return response



    def send_socket_message(self, message):
        # set up the host and port for the server
        HOST = 'localhost'
        PORT = 5094
        # set the timeout value for the socket
        TIMEOUT = 90
        # set the maximum number of retries
        MAX_RETRIES = 10
        # create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # keep track of the number of connection attempts
        num_attempts = 0
        response = ""
        while num_attempts < MAX_RETRIES:
            try:
                # set the timeout for the socket
                client_socket.settimeout(TIMEOUT)
                # connect to the server
                client_socket.connect((HOST, PORT))
                # send a message to the server
                print("Send message to the server")
                client_socket.sendall(message)
                # receive a response from the server
                while True:
                    data = None
                    data = client_socket.recv(1024)
                    response += data.decode("utf-8")
                    # print("data from server:", data)
                    if data != None:
                        break
                # strip any newline characters from the response
                response = response.strip()
                # print the response from the server
                print("Response from server:", response)
                # break out of the loop if the connection was successful
                break

            except socket.timeout:
                print("Connection timed out.")
            except ConnectionRefusedError:
                print("Connection refused. Please check if the server is running.")
            except Exception as e:
                print("An error occurred:", e)

            # increment the number of connection attempts
            num_attempts += 1
            # wait for a few seconds before retrying
            time.sleep(3)

        if num_attempts == MAX_RETRIES:
            print("Failed to connect to the server after", MAX_RETRIES, "attempts.")

        # close the socket
        client_socket.close()
        return response


if __name__ == '__main__':
    mydxl = MyDxlCommand()
    data_name = "Speed_Invalid_Signal"
    module_name = "ASM"
    dxl_command = mydxl.find_value(data_name, module_name)
    mysender = DxlSender()
    response = mysender.send_dxl_command_single(dxl_command)
    print("response = ", response)

    os.system("Pause")
