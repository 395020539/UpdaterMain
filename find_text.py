#!/usr/bin/python
# -*- coding: utf-8 -*-

from logging_maker import logger
import time
import re


# from get_file_path import get_file_path
# file_a2l, file_geskon, file_dcm, file_data_mytable, file_mech_table = get_file_path()

# file_a2l = get_file_path.file_a2l
# file_dcm = get_file_path.file_dcm
# file_geskon = get_file_path.file_geskon
# file_mech_table = get_file_path.file_mech_table
# file_data_mytable = get_file_path.file_data_mytable


# file_geskon = "DF0D01C0100_RG3_X_SCU3_B3_VAR_01_geskon.kon"
# file_dcm = "diff_dcm_JMC_V363C_short axle_steering feeling tuning_LKA_LDW_based on_C01_20220207.dcm"
# # file_name = file_geskon
# variable_to_find = "vVehSp_SubstituteSpeed_XDU16"

# 备份原函数！！！
# def find_text_intxt(variable_to_find, file_name):
#     find_result_intext = False
#     paragraph_find = ""
#     try:
#         with open(file_name, "r", encoding="ANSI", errors="replace") as text:
#             lines = text.readlines()
#             index = 0
#
#             for index, value in enumerate(lines):
#                 # if variable_to_find in value:
#                 if variable_to_find in value and \
#                         (re.search(r'^FESTWERT\s', value) or
#                          re.search(r'^KENNLINIE\s', value) or
#                          re.search(r'^FESTWERTEBLOCK\s', value) or
#                          re.search(r'^KENNFELD\s', value)):
#                     paragraph = ""
#                     paragraph_f2 = ""
#                     line = text.readline()
#                     nRows = 1
#                     while nRows < 50:
#                         if "END" in lines[index + nRows]:
#                             if nRows == 2:
#                                 paragraph_find = lines[index + nRows - 1]
#                             else:
#                                 paragraph_find = paragraph_f2 + paragraph
#                             break
#                         else:
#                             paragraph1 = lines[index + nRows]
#                             if ("LANGNAME" in paragraph1) or ("FUNKTION" in paragraph1) or \
#                                     ("EINHEIT_X" in paragraph1) or ("EINHEIT_W" in paragraph1):
#                                 paragraph_f2 = paragraph_f2
#                             else:
#                                 paragraph_f2 = paragraph_f2 + paragraph1
#                             nRows += 1
#                     find_result_intext = True
#                     break
#
#                 else:
#                     find_result_intext = False
#                     continue
#             if find_result_intext:
#                 print(f"在{file_name}中查找到变量: {variable_to_find}\n变量位于第: {index + 1} 行")
#                 print(f"变量值为:\n {paragraph_find}")
#
#             else:
#                 print(f"在{file_name}中未查找到变量: {variable_to_find}\n")
#
#     except FileNotFoundError:
#         print(f"No such file or directory")
#     except:
#         print(f"Error")
#     return find_result_intext, paragraph_find


def find_text_intxt(variable_to_find, file_name):
    logger.debug(f'调用函数<find_text_intxt>,{variable_to_find},{file_name}')
    find_result_intext = False
    paragraph_find = ""
    find_result, stx_result, sty_result, wert_result = \
        get_value_list_from_text(file_name, variable_to_find)
    if find_result == True:
        find_result_intext = True
        if len(stx_result) > 1:
            for value in stx_result:
                paragraph_find = paragraph_find + value + " "
            paragraph_find = paragraph_find + "\n"
        if len(sty_result) > 1:
            for value in sty_result:
                paragraph_find = paragraph_find + value + " "
            paragraph_find = paragraph_find + "\n"
        if len(wert_result) > 1:
            for value in wert_result:
                paragraph_find = paragraph_find + value + " "
            paragraph_find = paragraph_find + "\n"
        if not "ST/X" in paragraph_find and not "ST/Y" in paragraph_find:
            paragraph_find = "  WERT  "
            for i in range(1, len(wert_result)):
                paragraph_find = paragraph_find + wert_result[i] + " "
                i += 1
    print(f"[find_result]: \n{find_result}")
    print(f"[paragraph_find]: \n{paragraph_find}")
    logger.info(f"查询结果: \n{find_result}")
    logger.info(f"查询内容: \n{paragraph_find}")
    return find_result_intext, paragraph_find


# 备份原函数！！！
# def fun_find_text(variable_to_find, file_geskon, file_dcm):
#     if variable_to_find:
#         find_result_geskon = False
#         find_result_dcm = False
#         paragraph_find_geskon = ""
#         paragraph_find_dcm = ""
#         paragraph_find = ""
#         find_result = False
#         if file_geskon:
#             find_result_geskon, paragraph_find_geskon = find_text_intxt(variable_to_find, file_geskon)
#             print(f"find_result_geskon: {find_result_geskon}")
#             print(f"paragraph_find_geskon: {paragraph_find_geskon}")
#         else:
#             print(f"No geskon file")
#
#         if file_dcm:
#             find_result_dcm, paragraph_find_dcm = find_text_intxt(variable_to_find, file_dcm)
#             print(f"find_result_dcm: {find_result_dcm}")
#             print(f"paragraph_find_dcm: {paragraph_find_dcm}")
#         else:
#             print(f"No dcm file")
#         if find_result_geskon and find_result_dcm:
#             if simp_str(paragraph_find_dcm) == simp_str(paragraph_find_geskon):
#                 find_result = True
#                 paragraph_find = paragraph_find_geskon
#                 if "\n" in paragraph_find[:(len(paragraph_find) - 2)]:
#                     paragraph_find = paragraph_find
#                 else:
#                     paragraph_find = paragraph_find[7:]
#             else:
#                 paragraph_find = "(geskon)\n" + paragraph_find_geskon + "\n" + "(dcm)\n" + paragraph_find_dcm
#                 find_result = True
#         elif find_result_dcm and not find_result_geskon:
#             find_result = True
#             paragraph_find = paragraph_find_dcm
#             if "\n" in paragraph_find[:(len(paragraph_find) - 2)]:
#                 paragraph_find = paragraph_find
#             else:
#                 paragraph_find = paragraph_find[8:]
#         elif find_result_geskon and not find_result_dcm:
#             find_result = True
#             paragraph_find = paragraph_find_geskon
#             if "\n" in paragraph_find[:(len(paragraph_find) - 2)]:
#                 paragraph_find = paragraph_find
#             else:
#                 paragraph_find = paragraph_find[8:]
#         elif not find_result_dcm and not find_result_geskon:
#             find_result = False
#             paragraph_find = ""
#     else:
#         find_result = False
#         paragraph_find = ""
#     print(f"find_result: {find_result}; paragraph_find:\n{paragraph_find}")
#     return find_result, paragraph_find


def fun_find_text(variable_to_find, file_geskon, file_dcm):
    logger.debug(f'调用函数<fun_find_text>,{variable_to_find},{file_geskon},{file_dcm}')
    find_result = False
    find_result_geskon = False
    find_result_dcm = False
    paragraph_find_geskon = ""
    paragraph_find_dcm = ""
    paragraph_find = ""
    if variable_to_find:
        if file_geskon:
            find_result_geskon, stx_result_geskon, sty_result_geskon, wert_result_geskon = \
                get_value_list_from_text(file_geskon, variable_to_find)
            if find_result_geskon == True:
                if len(stx_result_geskon) > 1:
                    for value in stx_result_geskon:
                        paragraph_find_geskon = paragraph_find_geskon + value + " "
                    paragraph_find_geskon = paragraph_find_geskon + "\n"
                if len(sty_result_geskon) > 1:
                    # paragraph_find_geskon = paragraph_find_geskon + "\n"
                    for value in sty_result_geskon:
                        paragraph_find_geskon = paragraph_find_geskon + value + " "
                    paragraph_find_geskon = paragraph_find_geskon + "\n"
                if len(wert_result_geskon) > 1:
                    # paragraph_find_geskon = paragraph_find_geskon + "\n"
                    for value in wert_result_geskon:
                        paragraph_find_geskon = paragraph_find_geskon + value + " "
                    paragraph_find_geskon = paragraph_find_geskon + "\n"
            print(f"[find_result_geskon]: \n{find_result_geskon}")
            print(f"[paragraph_find_geskon]: \n{paragraph_find_geskon}")
            logger.debug(f"[geskon查询结果]: \n{find_result_geskon}")
            logger.debug(f"[geskon查询内容]: \n{paragraph_find_geskon}")
        else:
            print(f"No geskon file")
            logger.debug(f"No geskon file")
        if file_dcm:
            find_result_dcm, stx_result_dcm, sty_result_dcm, wert_result_dcm = \
                get_value_list_from_text(file_dcm, variable_to_find)
            if find_result_dcm == True:
                if len(stx_result_dcm) > 1:
                    for value in stx_result_dcm:
                        paragraph_find_dcm = paragraph_find_dcm + value + " "
                    paragraph_find_dcm = paragraph_find_dcm + "\n"
                if len(sty_result_dcm) > 1:
                    # paragraph_find_dcm = paragraph_find_dcm + "\n"
                    for value in sty_result_dcm:
                        paragraph_find_dcm = paragraph_find_dcm + value + " "
                    paragraph_find_dcm = paragraph_find_dcm + "\n"
                if len(wert_result_dcm) > 1:
                    # paragraph_find_dcm = paragraph_find_dcm + "\n"
                    for value in wert_result_dcm:
                        paragraph_find_dcm = paragraph_find_dcm + value + " "
                    paragraph_find_dcm = paragraph_find_dcm + "\n"
            print(f"[find_result_dcm]: \n{find_result_dcm}")
            print(f"[paragraph_find_dcm]: \n{paragraph_find_dcm}")
            logger.debug(f"[DCM查询结果]: \n{find_result_dcm}")
            logger.debug(f"[DCM查询内容]: \n{paragraph_find_dcm}")
        else:
            print(f"No dcm file")
            logger.debug(f"No dcm file")
        if find_result_geskon and find_result_dcm:
            find_result = True
            if paragraph_find_dcm == paragraph_find_geskon:
                paragraph_find = paragraph_find_dcm
            else:
                paragraph_find = "(geskon)\n" + paragraph_find_geskon + "\n(dcm)\n" + paragraph_find_dcm
        elif find_result_geskon and not find_result_dcm:
            find_result = True
            paragraph_find = paragraph_find_geskon
        elif not find_result_geskon and find_result_dcm:
            find_result = True
            paragraph_find = paragraph_find_dcm
    print(f"<Function: fun_find_text>\nfind_result = {find_result}\nparagraph_find =\n{paragraph_find}")
    logger.debug(f"<Function: fun_find_text>\n查询结果:{find_result}\n查询内容:\n{paragraph_find}")
    return find_result, paragraph_find


def simp_str(str):
    # 筛选字符串中非空格的内容并输出成新字符串
    str_out = ""
    if str:
        for char in str:
            if char != " ":
                str_out = str_out + char
    print(f"str_out = {str_out}")
    return str_out


# t_start = time.perf_counter()
# find_result, paragraph_find = fun_find_text(variable_to_find, file_geskon, file_dcm)
# print(f"find_result = \n{find_result}\nparagraph_find = \n{paragraph_find}")


# find_text(variable_to_find, file_geskon, file_dcm)
# find_result_intext, paragraph_find = find_text_intxt(variable_to_find, file_name)
# print(f"find_result_intext: {find_result_intext}")
# print(f"paragraph_find: {paragraph_find}")

# find_result, paragraph_find = find_text(variable_to_find, file_geskon, file_dcm)
# print(f"find_result_geskon: {find_result_geskon}")
# print(f"paragraph_find_geskon: \n{paragraph_find_geskon}")
# print(f"find_result_dcm: {find_result_dcm}")
# print(f"paragraph_find_dcm: \n{paragraph_find_dcm}")

# print(f"find_result: \n{find_result}")
# print(f"paragraph_find: \n{paragraph_find}")

# if find_result_geskon and find_result_dcm:
#     if paragraph_find_geskon == paragraph_find_dcm:
#         print("相同")
#     else:
#         print("不同")
#         # print(f"长度{len()}")

# t_end = time.perf_counter()
# t_cost = t_end - t_start
#
# print(f'运行耗时:{t_cost:.8f}s')


# 查找A2L变量的边界值
# Type = "max"为最大值，Type = "min" 为最小值, factor为乘法系数
def find_text_a2l(variable_to_find, file_name, type, factor):
    print(f"查找A2L，类型为{type}, factor为{factor}")
    logger.info(f"查找A2L参数{variable_to_find}，类型为{type}, factor为{factor}")
    find_result_intext = False
    paragraph_find = ""
    try:
        with open(file_name, "r", encoding="ANSI", errors="replace") as text:
            lines = text.readlines()
            index = 0

            for index, value in enumerate(lines):
                # print(value.replace('\ufffd',"?"))
                # if variable_to_find in value:
                if variable_to_find in value and re.search(r'^\s+/begin\s', value):
                    print(index, value.replace('\ufffd', "?"))
                    nextline = lines[index + 1]
                    print(f"nextline = {nextline}")
                    logger.debug(f"nextline = {nextline}")
                    if re.search(r'^\s+SWORD\s', nextline) or \
                            re.search(r'^\s+UWORD\s', nextline):
                        # numbers = re.findall(r'-?\d+', nextline)
                        numbers = re.findall(r'\s-?\d+', nextline)
                        print(f"找到数据: {numbers}")
                        print(f"边界值：{numbers[2]}, {numbers[3]}")
                        logger.info(f"找到数据: {numbers}")
                        logger.info(f"边界值：{numbers[2]}, {numbers[3]}")
                        find_result_intext = True
                        if type == "max":
                            paragraph_find = numbers[3]
                        else:
                            paragraph_find = numbers[2]
                    break
                else:
                    find_result_intext = False
                    continue
            if find_result_intext:
                paragraph_find = float(paragraph_find) * float(factor)
                paragraph_find = str(paragraph_find) + "\n"
                print(f"在{file_name}中查找到变量: {variable_to_find}\n变量位于第: {index + 1} 行")
                print(f"变量值为:\n {paragraph_find}")
                logger.infoprint(f"在{file_name}中查找到变量: {variable_to_find}\n变量位于第: {index + 1} 行")
                logger.info(f"变量值为:\n {paragraph_find}")

            else:
                print(f"在{file_name}中未查找到变量: {variable_to_find}\n")
                logger.error(f"在{file_name}中未查找到变量: {variable_to_find}\n")

    except FileNotFoundError:
        print(f"No such file or directory")
        logger.critical(f"No such file or directory")
    except Exception as e:
        print(f"Other error occurred: {e}")
        logger.critical(f"Other error occurred: {e}")
    finally:
        return find_result_intext, paragraph_find


def get_value_list_from_text(file_name, damos):
    """从txt文件中查找damos，根据ST/X、ST/Y、WERT输入三个list"""
    logger.debug(f'调用函数<get_value_list_from_text>,{file_name},{damos}')
    find_result = False
    stx_result = ["ST/X"]
    sty_result = ["ST/Y"]
    wert_result = ["WERT"]
    stx_line = ""
    sty_line = ""
    wert_line = ""
    try:
        with open(file_name, "r", encoding="ANSI", errors="replace") as text:
            lines = text.readlines()
            index = 0
            for index, line in enumerate(lines):
                if damos in line and \
                        (re.search(r'^FESTWERT\s', line) or
                         re.search(r'^KENNLINIE\s', line) or
                         re.search(r'^FESTWERTEBLOCK\s', line) or
                         re.search(r'^KENNFELD\s', line)):
                    print(f"Damos found at: index = {index}, line = {line}")
                    logger.info(f"Damos found at: index = {index}, line = {line}")
                    # nextline = lines[index+1]
                    # print(nextline)
                    find_result = True
                    break
            if find_result:
                while lines:
                    index += 1
                    nextline = lines[index]
                    print(f"[text]: {nextline}")
                    logger.debug(f"[text]: {nextline}")
                    if re.search(r'\s+ST/X\s', nextline):
                        stx_line = (stx_line + nextline).replace("\n", " ")
                        print(f"STX_line: {stx_line}")
                        logger.debug(f"STX_line: {stx_line}")
                    if re.search(r'\s+ST/Y\s', nextline):
                        sty_line = (sty_line + nextline).replace("\n", " ")
                        print(f"STY_line: {sty_line}")
                        logger.debug(f"STY_line: {sty_line}")
                    if re.search(r'\s+WERT\s', nextline):
                        wert_line = (wert_line + nextline).replace("\n", " ")
                        print(f"WERT_line: {wert_line}")
                        logger.debug(f"WERT_line: {wert_line}")
                    elif re.search(r'^END\s*', nextline):
                        print("text END")
                        logger.debug("text END")
                        # print(stx_line, sty_line, wert_line)
                        break
                stx_numbers = get_value_list(stx_line)
                sty_numbers = get_value_list(sty_line)
                wert_numbers = get_value_list(wert_line)
                print("stx_numbers:", stx_numbers)
                print("sty_numbers:", sty_numbers)
                print("wert_numbers:", wert_numbers)
                logger.debug(f"stx_numbers:{stx_numbers}")
                logger.debug(f"sty_numbers:{sty_numbers}")
                logger.debug(f"wert_numbers:{wert_numbers}")
                stx_result = stx_result + stx_numbers
                sty_result = sty_result + sty_numbers
                wert_result = wert_result + wert_numbers
                print("stx_result:", stx_result)
                print("sty_result:", sty_result)
                print("wert_result:", wert_result)
                logger.debug(f"stx_result:{stx_result}")
                logger.debug(f"sty_result:{sty_result}")
                logger.debug(f"wert_result:{sty_result}")
    except FileNotFoundError:
        print(f"No such file or directory")
        logger.critical(f"No such file or directory")
    except Exception as e:
        print("<Function: get_value_list_from_text>")
        print(f"Other error occurred: {e}")
        logger.critical("<Function: get_value_list_from_text>")
        logger.critical(f"Other error occurred: {e}")
    finally:
        if len(stx_result) == 1 and len(sty_result) == 1 and len(wert_result) == 1:
            find_result = False
        else:
            find_result = True
        stx_result = remove_point(stx_result)
        sty_result = remove_point(sty_result)
        wert_result = remove_point(wert_result)
        print(f"查询结果: {find_result}; 查询参数值: {damos}; 查询文件: {file_name}")
        print(f"结果如下:\nST/X = {stx_result}\nST/Y = {sty_result}\nWERT = {wert_result}")
        logger.info(f"查询结果: {find_result}; 查询参数值: {damos}; 查询文件: {file_name}")
        logger.info(f"结果如下:\nST/X = {stx_result}\nST/Y = {sty_result}\nWERT = {wert_result}")
        return find_result, stx_result, sty_result, wert_result


def get_value_list(value_line):
    """清理文本内容，根据空格分隔，生成list"""
    numbers = []
    match = re.search(r"([\d\s+.?]+)", value_line)
    if match:
        split = re.split(r'\s+', value_line)
        print("split:", split)
        logger.debug(f"split:{split}")
        for i in split:
            # print("i: ", i)
            # print(re.search("[a-zA-Z]", i))
            if not re.search("[a-zA-Z]", i) and not i == "":
                numbers.append(i)
    return numbers


def format_paragraph_find(paragraph_find):
    if type(paragraph_find) == str:
        if "WERT" in paragraph_find and not "ST/X" in paragraph_find and not "ST/Y" in paragraph_find:
            paragraph_find = paragraph_find.replace("WERT", "")
    return paragraph_find


def remove_point(data_list):
    """清理数据后面的点号"""
    if len(data_list) > 0:
        for i in range(1, len(data_list)):
            # print("data_list[i]=", data_list[i])
            if re.search(r'.$\B', data_list[i]):
                data_list[i] = data_list[i][:-1]
    return data_list
