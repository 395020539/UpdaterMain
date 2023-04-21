#!/usr/bin/python
# -*- coding: utf-8 -*-

from logging_maker import logger
import re
from find_text import find_text_intxt
from find_mech import fun_find_mech

# from get_file_path import get_file_path
# file_a2l, file_geskon, file_dcm, file_data_mytable, file_mech_table = get_file_path()

# file_a2l = get_file_path.file_a2l
# file_dcm = get_file_path.file_dcm
# file_geskon = get_file_path.file_geskon
# file_mech_table = get_file_path.file_mech_table
# file_data_mytable = get_file_path.file_data_mytable

# file_mech_table = "MechanicalDataSheet -机械参数表 Voyah_H97C_20220902.xlsm"
# file_geskon = "XP1100D0100_RG3_X_SCU3_B3_VAR_01_geskon.kon"
# file_dcm = "DCM_ALL_XIAO PENG_F30_First Tuning(Normal mode_01+Comfortable_06+Sport_11)_Based on XP1100B0100_20220705.DCM"
#
# find_result_geskon, paragraph_find_geskon = \
#     find_text_intxt(variable_to_find="nEndStopHsd_HighSpeedDampingStart_XAS16", file_name=file_geskon)


# 获取KENNLINIE数据中y-value的最小值
def get_Yvalue_smallest_from_KENNLINIE(paragraph_find):
    logger.debug('调用函数<get_Yvalue_smallest_from_KENNLINIE>')
    get_value_result = False
    get_value = ""
    if "WERT" in paragraph_find:
        # match = re.search(r'WERT\s+([\d\s]+(?:\.\d+)?)', paragraph_find)
        match = re.search(r"WERT\s+([\d\s+.?]+)", paragraph_find)
        if match:
            numbers = match.group(1).split()
            print(f"获取数据: {numbers}")
            # 将字符串列表转换为浮点数列表
            numbers = [float(number) for number in numbers]
            # 找到最小值
            min_number = min(numbers)
            print(f"获取最小值: {min_number}")
            get_value_result = True
            get_value = min_number
        else:
            print("未找到匹配")
    print(f"查询最小值结果: {get_value_result}; 数值: {get_value}")
    logger.info(f"查询最小值结果: {get_value_result}; 数值: {get_value}")
    return get_value_result, get_value


# 获取KENNLINIE数据中y-value的最后一个数据
def get_Yvalue_last_from_KENNLINIE(paragraph_find):
    logger.debug('调用函数<get_Yvalue_last_from_KENNLINIE>')
    get_value_result = False
    get_value = ""
    if "WERT" in paragraph_find:
        match = re.search(r'WERT\s+([\d\s+.?]+)', paragraph_find)
        if match:
            # 将匹配到的数字字符串拆分成列表
            numbers = match.group(1).split()
            print(f"获取数据: {numbers}")
            # 将字符串列表转换为浮点数列表
            numbers = [float(number) for number in numbers]
            # 找到最后一个值
            last_number = numbers[-1]
            print(f"获取末值: {last_number}")
            get_value_result = True
            get_value = last_number
        else:
            print("未找到匹配的数字")
    print(f"查询末值结果: {get_value_result}; 数值: {get_value}")
    logger.info(f"查询末值结果: {get_value_result}; 数值: {get_value}")
    return get_value_result, get_value

# 获取KENNLINIE数据中y-value的第一个数据
def get_Yvalue_first_from_KENNLINIE(paragraph_find):
    logger.debug('调用函数<get_Yvalue_first_from_KENNLINIE>')
    get_value_result = False
    get_value = ""
    if "WERT" in paragraph_find:
        match = re.search(r'WERT\s+([\d\s+.?]+)', paragraph_find)
        if match:
            # 将匹配到的数字字符串拆分成列表
            numbers = match.group(1).split()
            print(f"获取数据: {numbers}")
            # 将字符串列表转换为浮点数列表
            numbers = [float(number) for number in numbers]
            # 找到最后一个值
            last_number = numbers[0]
            print(f"获取首值: {last_number}")
            get_value_result = True
            get_value = last_number
        else:
            print("未找到匹配的数字")
    print(f"查询首值结果: {get_value_result}; 数值: {get_value}")
    logger.info(f"查询首值结果: {get_value_result}; 数值: {get_value}")
    return get_value_result, get_value


# 获取KENNLINIE数据中x-value的第一个数据
def get_Xvalue_first_from_KENNLINIE(paragraph_find):
    logger.debug('调用函数<get_Xvalue_first_from_KENNLINIE>')
    get_value_result = False
    get_value = ""
    if "WERT" in paragraph_find:
        match = re.search(r'ST/X\s+([-?\d\s+.?]+)', paragraph_find)
        if match:
            # 将匹配到的数字字符串拆分成列表
            numbers = match.group(1).split()
            print(f"获取数据: {numbers}")
            # 将字符串列表转换为浮点数列表
            numbers = [float(number) for number in numbers]
            # 找到最后一个值
            last_number = numbers[0]
            print(f"获取首值: {last_number}")
            get_value_result = True
            get_value = last_number
        else:
            print("未找到匹配的数字")
    print(f"查询首值结果: {get_value_result}; 数值: {get_value}")
    logger.info(f"查询首值结果: {get_value_result}; 数值: {get_value}")
    return get_value_result, get_value


# 获取KENNLINIE数据中x-value的最后一位数据
def get_Xvalue_last_from_KENNLINIE(paragraph_find):
    logger.debug('调用函数<get_Xvalue_last_from_KENNLINIE>')
    get_value_result = False
    get_value = ""
    if "WERT" in paragraph_find:
        match = re.search(r'ST/X\s+([\d\s+.?]+)', paragraph_find)
        if match:
            # 将匹配到的数字字符串拆分成列表
            numbers = match.group(1).split()
            print(f"获取数据: {numbers}")
            # 将字符串列表转换为浮点数列表
            numbers = [float(number) for number in numbers]
            # 找到最后一个值
            last_number = numbers[-1]
            print(f"获取末值: {last_number}")
            get_value_result = True
            get_value = last_number
        else:
            print("未找到匹配的数字")
    print(f"查询末值结果: {get_value_result}; 数值: {get_value}")
    logger.info(f"查询末值结果: {get_value_result}; 数值: {get_value}")
    return get_value_result, get_value


# 获取KENNLINIE数据中y-value为0时的x-value
def get_Xvalue_Y0_from_KENNLINIE(paragraph_find):
    logger.debug('调用函数<get_Xvalue_Y0_from_KENNLINIE>')
    get_value_result = False
    get_value = ""
    if "WERT" in paragraph_find and "ST/X" in paragraph_find:
        matchX = re.search(r"ST/X\s+([-?\d\s+.?]+)", paragraph_find)
        matchY = re.search(r"WERT\s+([-?\d\s+.?]+)", paragraph_find)
        if matchX and matchY:
            numbersX = matchX.group(1).split()
            numbersY = matchY.group(1).split()
            print(f"获取数据: {numbersX}\n{numbersY}")
            # 将字符串列表转换为浮点数列表
            numbersX = [float(numberX) for numberX in numbersX]
            numbersY = [float(numberY) for numberY in numbersY]
            # 找到Y=0时的X值
            i = 0
            for numberY in numbersY:
                if numberY == 0:
                    numberX = numbersX[i]
                    break
                i += 1
            print(f"获取y-value为0时的x-value: {numberX}")
            get_value_result = True
            get_value = numberX
        else:
            print("未找到匹配")
    print(f"查询(y-value为0时的x-value)结果: {get_value_result}; 数值: {get_value}")
    logger.info(f"查询(y-value为0时的x-value)结果: {get_value_result}; 数值: {get_value}")
    return get_value_result, get_value


# 获取KENNLINIE数据中y-value最大值的x-value
def get_Xvalue_Ymax_from_KENNLINIE(paragraph_find):
    logger.debug('调用函数<get_Xvalue_Ymax_from_KENNLINIE>')
    get_value_result = False
    get_value = ""
    if "WERT" in paragraph_find and "ST/X" in paragraph_find:
        matchX = re.search(r"ST/X\s+([-?\d\s+.?]+)", paragraph_find)
        matchY = re.search(r"WERT\s+([-?\d\s+.?]+)", paragraph_find)
        if matchX and matchY:
            numbersX = matchX.group(1).split()
            numbersY = matchY.group(1).split()
            print(f"获取数据: {numbersX}\n{numbersY}")
            # 将字符串列表转换为浮点数列表
            numbersX = [float(numberX) for numberX in numbersX]
            numbersY = [float(numberY) for numberY in numbersY]
            maxnumberY = max(numbersY)
            # 找到Y=最大值时的X值
            i = 0
            for numberY in numbersY:
                if numberY == maxnumberY:
                    numberX = numbersX[i]
                    break
                i += 1
            print(f"获取y-value为0时的x-value: {numberX}")
            get_value_result = True
            get_value = numberX
        else:
            print("未找到匹配")
    print(f"查询(y-value为0时的x-value)结果: {get_value_result}; 数值: {get_value}")
    logger.info(f"查询(y-value为0时的x-value)结果: {get_value_result}; 数值: {get_value}")
    return get_value_result, get_value


# 获取KENNLINIE数据中x-value的最大值
def get_Xvalue_max_from_KENNLINIE(paragraph_find):
    logger.debug('调用函数<get_Xvalue_max_from_KENNLINIE>')
    get_value_result = False
    get_value = ""
    if "WERT" in paragraph_find:
        # match = re.search(r'WERT\s+([\d\s]+(?:\.\d+)?)', paragraph_find)
        match = re.search(r"ST/X\s+([\d\s+.?]+)", paragraph_find)
        if match:
            numbers = match.group(1).split()
            print(f"获取数据: {numbers}")
            # 将字符串列表转换为浮点数列表
            numbers = [float(number) for number in numbers]
            # 找到最小值
            max_number = max(numbers)
            print(f"获取最大值: {max_number}")
            get_value_result = True
            get_value = max_number
        else:
            print("未找到匹配")
    print(f"查询最大值结果: {get_value_result}; 数值: {get_value}")
    logger.info(f"查询最大值结果: {get_value_result}; 数值: {get_value}")
    return get_value_result, get_value





# get_value_result, get_value = get_Yvalue_smallest_from_KENNLINIE(paragraph_find_geskon)
# get_value_result, get_value = get_Yvalue_last_from_KENNLINIE(paragraph_find_geskon)

# 在字典中获取不重复的有效值，并输出新字典
def dict_compare(dict_find_result):
    logger.debug('调用函数<dict_compare>')
    new_dict = {}
    valid_values = [v for v in dict_find_result.values() if not (isinstance(v, str) and v == "") and v is not None]
    print(f"有效值序列:{valid_values}")
    print(f"有效不重复序列:{set(valid_values)}")
    if len(set(valid_values)) == 1:
        # new_dict = {k: v for k, v in dict_find_result.items() if not (isinstance(v, str) and v == "")}
        # print(new_dict)
        spec_find_value = valid_values[0]
        print(f"spec_find_value: {spec_find_value}")
        new_dict = {"value": spec_find_value}
        print(new_dict)
    else:
        new_dict = {k: v for k, v in dict_find_result.items() if not (isinstance(v, str) and v == "")}
        # print(f"new_dict: {new_dict}")
        # print(new_dict.keys())
    print(f"生成新数据组: {new_dict}")
    logger.info(f"生成新数据组: {new_dict}")
    return new_dict

# 检查字典中是否所有值都无效
def dict_check_valid(dict):
    dict_check_valid = False
    valid_values = [v for v in dict.values() if not (isinstance(v, str) and v == "") and v is not None]
    if len(set(valid_values)) > 0:
        dict_check_valid = True
    return dict_check_valid

