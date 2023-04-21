#!/usr/bin/python
# -*- coding: utf-8 -*-

from logging_maker import logger
from find_text import find_text_intxt
from find_mech import fun_find_mech
from specifical_variable_find_get_value import *
from find_mech import fun_find_mech_by_para

# file_a2l = get_file_path.file_a2l
# file_dcm = get_file_path.file_dcm
# file_geskon = get_file_path.file_geskon
# file_mech_table = get_file_path.file_mech_table
# file_data_mytable = get_file_path.file_data_mytable

# from get_file_path import get_file_path
# file_a2l, file_geskon, file_dcm, file_data_mytable, file_mech_table = get_file_path()

# file_mech_table = "MechanicalDataSheet -机械参数表 Voyah_H97C_20220902.xlsm"
# file_geskon = "XP1100D0100_RG3_X_SCU3_B3_VAR_01_geskon.kon"
# file_dcm = "DCM_ALL_XIAO PENG_F30_First Tuning(Normal mode_01+Comfortable_06+Sport_11)_Based on XP1100B0100_20220705.DCM"


# Time_Rampup_Suspension
# tHwlWrapI_RampUpSuspensionTime_XDU16*0.001
def spec_fun_find_variable_0(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 0>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="tHwlWrapI_RampUpSuspensionTime_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="tHwlWrapI_RampUpSuspensionTime_XDU16", file_name=file_dcm)
    if find_result_geskon and find_result_dcm:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]):
            print(float(paragraph_find_geskon[8:]))
            logger.debug(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 0.001), 4)
            print(format(spec_find_value, ".4f"))
            logger.debug(format(spec_find_value, ".4f"))
            format_spec_find_para = format(spec_find_value, ".4f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 0.001), 4)
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 0.001), 4)
            format_spec_find_para_geskon = format(spec_find_value_geskon, ".4f")
            format_spec_find_para_dcm = format(spec_find_value_dcm, ".4f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm:
        spec_find_result = True
        spec_find_value = round((float(paragraph_find_geskon[8:]) * 0.001), 4)
        format_spec_find_para = format(spec_find_value, ".4f")
        spec_find_para = str(format_spec_find_para)+ "\n"
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm:
        spec_find_result = True
        spec_find_value = round((float(paragraph_find_dcm[8:]) * 0.001), 4)
        format_spec_find_para = format(spec_find_value, ".4f")
        spec_find_para = str(format_spec_find_para)+ "\n"
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Position_Deviation_Rack_Safety_CSAP
# wRackPo_RackposToleranceRA_XDU16/（Sheet Steering Ratio $Z$15）
def spec_fun_find_variable_1(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 1>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="wRackPo_RackposToleranceRA_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="wRackPo_RackposToleranceRA_XDU16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "Steering Angle", 34, 1, 2)
    find_result_mech2, mech_value2 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 14, 25, 1)

    if find_result_geskon and find_result_dcm and find_result_mech1 and find_result_mech2:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            logger.debug(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 2)
            spec_find_cal = spec_find_value / mech_value2
            print(format(spec_find_cal, ".3f"))
            logger.debug(format(spec_find_cal, ".3f"))
            format_spec_find_para = format(spec_find_cal, ".3f")
            spec_find_para = str(format_spec_find_para) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 2)
            spec_find_value_geskon_cal = spec_find_value_geskon / mech_value2
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 2)
            spec_find_value_dcm_cal = spec_find_value_dcm / mech_value2
            spec_find_value_mech = round((mech_value1 * 1), 2)
            spec_find_value_mech_cal = spec_find_value_mech / mech_value2
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".3f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".3f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".3f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and find_result_mech1 and find_result_mech2:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 2)
            spec_find_cal = spec_find_value / mech_value2
            print(format(spec_find_cal, ".3f"))
            format_spec_find_para = format(spec_find_cal, ".3f")
            spec_find_para = str(format_spec_find_para) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 2)
            spec_find_value_geskon_cal = spec_find_value_geskon / mech_value2
            spec_find_value_mech = round((mech_value1 * 1), 2)
            spec_find_value_mech_cal = spec_find_value_mech / mech_value2
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".3f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".3f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and find_result_mech1 and find_result_mech2:
        spec_find_result = True
        if float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_dcm[8:]))
            spec_find_value = round((float(paragraph_find_dcm[8:]) * 1), 2)
            spec_find_cal = spec_find_value / mech_value2
            print(format(spec_find_cal, ".3f"))
            format_spec_find_para = format(spec_find_cal, ".3f")
            spec_find_para = str(format_spec_find_para) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 2)
            spec_find_value_dcm_cal = spec_find_value_dcm / mech_value2
            spec_find_value_mech = round((mech_value1 * 1), 2)
            spec_find_value_mech_cal = spec_find_value_mech / mech_value2
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".3f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".3f")
            spec_find_para = "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and not find_result_dcm and find_result_mech1 and find_result_mech2:
        spec_find_result = True
        spec_find_value_mech = round((mech_value1 * 1), 2)
        spec_find_value_mech_cal = spec_find_value_mech / mech_value2
        format_spec_find_para_mech = format(spec_find_value_mech_cal, ".3f")
        spec_find_para = str(format_spec_find_para_mech) + "\n"
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and find_result_dcm and not find_result_mech1 and find_result_mech2:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]):
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 2)
            spec_find_cal = spec_find_value / mech_value2
            print(format(spec_find_cal, ".3f"))
            format_spec_find_para = format(spec_find_cal, ".3f")
            spec_find_para = str(format_spec_find_para) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 2)
            spec_find_value_geskon_cal = spec_find_value_geskon / mech_value2
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 2)
            spec_find_value_dcm_cal = spec_find_value_dcm / mech_value2
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".3f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".3f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and not find_result_mech1 and find_result_mech2:
        spec_find_result = True
        spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 2)
        spec_find_value_geskon_cal = spec_find_value_geskon / mech_value2
        format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".3f")
        spec_find_para = str(format_spec_find_para_geskon) + "\n"
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and not find_result_mech1 and find_result_mech2:
        spec_find_result = True
        spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 2)
        spec_find_value_dcm_cal = spec_find_value_dcm / mech_value2
        format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".3f")
        spec_find_para = str(format_spec_find_para_dcm) + "\n"
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Gradient_Handling_Rotortorque_Safety_BLOCK
# xEndStop_RateLimiterToZeroRate_XDU32*1000
def spec_fun_find_variable_2(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 2>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xEndStop_RateLimiterToZeroRate_XDU32", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xEndStop_RateLimiterToZeroRate_XDU32", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "SW-Endstop", 46, 1, 10)

    if find_result_geskon and find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 10)
            spec_find_cal = spec_find_value * 1000
            print(format(spec_find_cal, ".7f"))
            format_spec_find_para = format(spec_find_cal, ".7f")
            spec_find_para = str(format_spec_find_para) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 10)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1000
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 10)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1000
            spec_find_value_mech = round((mech_value1 * 1), 10)
            spec_find_value_mech_cal = spec_find_value_mech * 1000
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".7f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".7f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".7f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech) + "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 10)
            spec_find_cal = spec_find_value * 1000
            print(format(spec_find_cal, ".7f"))
            format_spec_find_para = format(spec_find_cal, ".7f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 10)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1000
            spec_find_value_mech = round((mech_value1 * 1), 10)
            spec_find_value_mech_cal = spec_find_value_mech * 1000
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".7f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".7f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_dcm[8:]))
            spec_find_value = round((float(paragraph_find_dcm[8:]) * 1), 10)
            spec_find_cal = spec_find_value * 1000
            print(format(spec_find_cal, ".10f"))
            format_spec_find_para = format(spec_find_cal, ".10f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 10)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1000
            spec_find_value_mech = round((mech_value1 * 1), 10)
            spec_find_value_mech_cal = spec_find_value_mech * 1000
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".7f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".7f")
            spec_find_para = "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and not find_result_dcm and find_result_mech1:
        spec_find_result = True
        spec_find_value_mech = round((mech_value1 * 1), 10)
        spec_find_value_mech_cal = spec_find_value_mech * 1000
        format_spec_find_para_mech = format(spec_find_value_mech_cal, ".7f")
        spec_find_para = str(format_spec_find_para_mech)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and find_result_dcm and not find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]):
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 10)
            spec_find_cal = spec_find_value * 1000
            print(format(spec_find_cal, ".7f"))
            format_spec_find_para = format(spec_find_cal, ".7f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 10)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1000
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 10)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1000
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".7f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".7f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and not find_result_mech1:
        spec_find_result = True
        spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 10)
        spec_find_value_geskon_cal = spec_find_value_geskon * 1000
        format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".7f")
        spec_find_para = str(format_spec_find_para_geskon)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and not find_result_mech1:
        spec_find_result = True
        spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 10)
        spec_find_value_dcm_cal = spec_find_value_dcm * 1000
        format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".7f")
        spec_find_para = str(format_spec_find_para_dcm)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Min_Vehicle_speed
# vEndStop_uVehSpeedLearnFinished_XDU16
def spec_fun_find_variable_3(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 3>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="vEndStop_uVehSpeedLearnFinished_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="vEndStop_uVehSpeedLearnFinished_XDU16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "SW-Endstop", 24, 1, 5)

    if find_result_geskon and find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 5)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".7f"))
            format_spec_find_para = format(spec_find_cal, ".7f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 5)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 5)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1
            spec_find_value_mech = round((mech_value1 * 1), 5)
            spec_find_value_mech_cal = spec_find_value_mech * 1
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".5f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".5f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".5f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 5)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".5f"))
            format_spec_find_para = format(spec_find_cal, ".5f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 5)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1
            spec_find_value_mech = round((mech_value1 * 1), 5)
            spec_find_value_mech_cal = spec_find_value_mech * 1
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".5f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".5f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_dcm[8:]))
            spec_find_value = round((float(paragraph_find_dcm[8:]) * 1), 5)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".5f"))
            format_spec_find_para = format(spec_find_cal, ".5f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 5)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1
            spec_find_value_mech = round((mech_value1 * 1), 5)
            spec_find_value_mech_cal = spec_find_value_mech * 1
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".5f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".5f")
            spec_find_para = "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and not find_result_dcm and find_result_mech1:
        spec_find_result = True
        spec_find_value_mech = round((mech_value1 * 1), 5)
        spec_find_value_mech_cal = spec_find_value_mech * 1
        format_spec_find_para_mech = format(spec_find_value_mech_cal, ".5f")
        spec_find_para = str(format_spec_find_para_mech)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and find_result_dcm and not find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]):
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 5)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".5f"))
            format_spec_find_para = format(spec_find_cal, ".5f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 5)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1000
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 5)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".5f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".5f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and not find_result_mech1:
        spec_find_result = True
        spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 5)
        spec_find_value_geskon_cal = spec_find_value_geskon * 1
        format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".5f")
        spec_find_para = str(format_spec_find_para_geskon)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and not find_result_mech1:
        spec_find_result = True
        spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 5)
        spec_find_value_dcm_cal = spec_find_value_dcm * 1
        format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".5f")
        spec_find_para = str(format_spec_find_para_dcm)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# rotor_speed_LSS
# nEndStop_oRotSpeedLearnFinished_XDU16
def spec_fun_find_variable_4(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 4>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStop_oRotSpeedLearnFinished_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStop_oRotSpeedLearnFinished_XDU16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "SW-Endstop", 31, 1, 0)

    if find_result_geskon and find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 0)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".0f"))
            format_spec_find_para = format(spec_find_cal, ".0f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 0)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 0)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1
            spec_find_value_mech = round((mech_value1 * 1), 0)
            spec_find_value_mech_cal = spec_find_value_mech * 1
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".0f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".0f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".0f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 0)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".0f"))
            format_spec_find_para = format(spec_find_cal, ".0f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 0)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1
            spec_find_value_mech = round((mech_value1 * 1), 0)
            spec_find_value_mech_cal = spec_find_value_mech * 1
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".0f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".0f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_dcm[8:]))
            spec_find_value = round((float(paragraph_find_dcm[8:]) * 1), 0)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".0f"))
            format_spec_find_para = format(spec_find_cal, ".0f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 0)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1
            spec_find_value_mech = round((mech_value1 * 1), 0)
            spec_find_value_mech_cal = spec_find_value_mech * 1
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".0f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".0f")
            spec_find_para = "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and not find_result_dcm and find_result_mech1:
        spec_find_result = True
        spec_find_value_mech = round((mech_value1 * 1), 0)
        spec_find_value_mech_cal = spec_find_value_mech * 1
        format_spec_find_para_mech = format(spec_find_value_mech_cal, ".0f")
        spec_find_para = str(format_spec_find_para_mech)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and find_result_dcm and not find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]):
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 0)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".0f"))
            format_spec_find_para = format(spec_find_cal, ".0f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 0)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1000
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 0)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".0f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".0f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and not find_result_mech1:
        spec_find_result = True
        spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 0)
        spec_find_value_geskon_cal = spec_find_value_geskon * 1
        format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".0f")
        spec_find_para = str(format_spec_find_para_geskon)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and not find_result_mech1:
        spec_find_result = True
        spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 0)
        spec_find_value_dcm_cal = spec_find_value_dcm * 1
        format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".0f")
        spec_find_para = str(format_spec_find_para_dcm)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Factor_Input_Shaft_Torque_2_Rotor_Torque
# xsyRatioEfficiency_XDU16
def spec_fun_find_variable_5(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 5>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xsyRatioEfficiency_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xsyRatioEfficiency_XDU16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "MechanicalData", 68, 1, 7)

    if find_result_geskon and find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 7)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".7f"))
            format_spec_find_para = format(spec_find_cal, ".7f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 7)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 7)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1
            spec_find_value_mech = round((mech_value1 * 1), 7)
            spec_find_value_mech_cal = spec_find_value_mech * 1
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".7f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".7f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".7f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == mech_value1:
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 7)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".7f"))
            format_spec_find_para = format(spec_find_cal, ".7f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 7)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1
            spec_find_value_mech = round((mech_value1 * 1), 7)
            spec_find_value_mech_cal = spec_find_value_mech * 1
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".7f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".7f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_dcm[8:]) == mech_value1:
            print(float(paragraph_find_dcm[8:]))
            spec_find_value = round((float(paragraph_find_dcm[8:]) * 1), 7)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".7f"))
            format_spec_find_para = format(spec_find_cal, ".7f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 7)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1
            spec_find_value_mech = round((mech_value1 * 1), 7)
            spec_find_value_mech_cal = spec_find_value_mech * 1
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".7f")
            format_spec_find_para_mech = format(spec_find_value_mech_cal, ".7f")
            spec_find_para = "(dcm)" + str(format_spec_find_para_dcm) + "\n" + \
                             "(mech)" + str(format_spec_find_para_mech)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and not find_result_dcm and find_result_mech1:
        spec_find_result = True
        spec_find_value_mech = round((mech_value1 * 1), 7)
        spec_find_value_mech_cal = spec_find_value_mech * 1
        format_spec_find_para_mech = format(spec_find_value_mech_cal, ".7f")
        spec_find_para = str(format_spec_find_para_mech)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and find_result_dcm and not find_result_mech1:
        spec_find_result = True
        if float(paragraph_find_geskon[8:]) == float(paragraph_find_dcm[8:]):
            print(float(paragraph_find_geskon[8:]))
            spec_find_value = round((float(paragraph_find_geskon[8:]) * 1), 7)
            spec_find_cal = spec_find_value * 1
            print(format(spec_find_cal, ".7f"))
            format_spec_find_para = format(spec_find_cal, ".7f")
            spec_find_para = str(format_spec_find_para)+ "\n"
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
        else:
            spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 7)
            spec_find_value_geskon_cal = spec_find_value_geskon * 1000
            spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 7)
            spec_find_value_dcm_cal = spec_find_value_dcm * 1
            format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".7f")
            format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".7f")
            spec_find_para = "(geskon)" + str(format_spec_find_para_geskon) + "\n" + \
                             "(dcm)" + str(format_spec_find_para_dcm)
            print(f"计算结果:\n{spec_find_para}")
            logger.info(f"计算结果:\n{spec_find_para}")
    elif find_result_geskon and not find_result_dcm and not find_result_mech1:
        spec_find_result = True
        spec_find_value_geskon = round((float(paragraph_find_geskon[8:]) * 1), 7)
        spec_find_value_geskon_cal = spec_find_value_geskon * 1
        format_spec_find_para_geskon = format(spec_find_value_geskon_cal, ".7f")
        spec_find_para = str(format_spec_find_para_geskon)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    elif not find_result_geskon and find_result_dcm and not find_result_mech1:
        spec_find_result = True
        spec_find_value_dcm = round((float(paragraph_find_dcm[8:]) * 1), 7)
        spec_find_value_dcm_cal = spec_find_value_dcm * 1
        format_spec_find_para_dcm = format(spec_find_value_dcm_cal, ".7f")
        spec_find_para = str(format_spec_find_para_dcm)
        print(f"计算结果:\n{spec_find_para}")
        logger.info(f"计算结果:\n{spec_find_para}")
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Speed_Rack_HSD_Start_1
# Speed_Rack_HSD_Start_1 =
# (6 * Smallest y-value of nEndStopHsd_HighSpeedDampingStart_XAS16 * RackToPinionRatioAvg) /360 * 1000 * SteeringGearRatioAvg)
def spec_fun_find_variable_6(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 6>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStopHsd_HighSpeedDampingStart_XAS16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStopHsd_HighSpeedDampingStart_XAS16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 15, 25, 3)
    find_result_mech2, mech_value2 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 8, 25, 3)
    get_value_result, smallest_find_geskon = get_Yvalue_smallest_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, smallest_find_dcm = get_Yvalue_smallest_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": smallest_find_geskon, "dcm": smallest_find_dcm}
    # 定义仅在一处存在的值
    dict_find_result_stable = {"mech1": mech_value1, "mech2": mech_value2}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(dict_find_result_stable) and dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key]) * 6 * dict_find_result_stable["mech1"] / \
                                  (360 * 1000 * dict_find_result_stable["mech2"])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Speed_Rack_HSD_Start_2
# Speed_Rack_HSD_Start_2 =
# (6 * last y-value of nEndStopHsd_HighSpeedDampingStart_XAS16 * RackToPinionRatioAvg) /360 * 1000 * SteeringGearRatioAvg)
def spec_fun_find_variable_7(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 7>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStopHsd_HighSpeedDampingStart_XAS16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStopHsd_HighSpeedDampingStart_XAS16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 15, 25, 3)
    find_result_mech2, mech_value2 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 8, 25, 3)
    get_value_result, last_find_geskon = get_Yvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, last_find_dcm = get_Yvalue_last_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": last_find_geskon, "dcm": last_find_dcm}
    # 定义仅在一处存在的值
    dict_find_result_stable = {"mech1": mech_value1, "mech2": mech_value2}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(dict_find_result_stable) and dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key]) * 6 * dict_find_result_stable["mech1"] / \
                                  (360 * 1000 * dict_find_result_stable["mech2"])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Speed_Rotor_Damping_Activate
# Y Axis of nEndStopHsdCheck_HighSpeedDampingStart_XAS16[0]
def spec_fun_find_variable_8(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 8>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStopHsdCheck_HighSpeedDampingStart_XAS16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStopHsdCheck_HighSpeedDampingStart_XAS16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Yvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para

# Torque_HSD_Short_Before_Endstop
# mEndStopHsd_MaxMotorTorque_FirstP_XDU16 or
# Y Axis of mEndStopHsd_MaxMotorTorque_XAS16[0]
def spec_fun_find_variable_9(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 9>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="mEndStopHsd_MaxMotorTorque_FirstP_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="mEndStopHsd_MaxMotorTorque_FirstP_XDU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Yvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_first_from_KENNLINIE(paragraph_find_dcm)

    find_result_geskon2, paragraph_find_geskon2 = \
        find_text_intxt(variable_to_find="mEndStopHsd_MaxMotorTorque_XAS16", file_name=file_geskon)
    find_result_dcm2, paragraph_find_dcm2 = \
        find_text_intxt(variable_to_find="mEndStopHsd_MaxMotorTorque_XAS16", file_name=file_dcm)
    get_value_result2, first_find_geskon2 = get_Yvalue_first_from_KENNLINIE(paragraph_find_geskon2)
    get_value_result2, first_find_dcm2 = get_Yvalue_first_from_KENNLINIE(paragraph_find_dcm2)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon1": first_find_geskon, "dcm1": first_find_dcm,
                                "geskon2": first_find_geskon2, "dcm2": first_find_dcm2}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 6)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Torque_HSD_High_Distance_2_Endstop
# mEndStopHsd_MaxMotorTorque_LastP_XDU16 or
# Y Axis of mEndStopHsd_MaxMotorTorque_XAS16[2]
def spec_fun_find_variable_10(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 10>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="mEndStopHsd_MaxMotorTorque_LastP_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="mEndStopHsd_MaxMotorTorque_LastP_XDU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Yvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_first_from_KENNLINIE(paragraph_find_dcm)

    find_result_geskon2, paragraph_find_geskon2 = \
        find_text_intxt(variable_to_find="mEndStopHsd_MaxMotorTorque_XAS16", file_name=file_geskon)
    find_result_dcm2, paragraph_find_dcm2 = \
        find_text_intxt(variable_to_find="mEndStopHsd_MaxMotorTorque_XAS16", file_name=file_dcm)
    get_value_result2, first_find_geskon2 = get_Yvalue_last_from_KENNLINIE(paragraph_find_geskon2)
    get_value_result2, first_find_dcm2 = get_Yvalue_last_from_KENNLINIE(paragraph_find_dcm2)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon1": first_find_geskon, "dcm1": first_find_dcm,
                                "geskon2": first_find_geskon2, "dcm2": first_find_dcm2}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 6)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para



# Speed_Tie_Rod_Damping_Activate
# 6*x-value of xActDamp_TorqueDepOnRotorSpeed_XAU16[0]*(Sheet Steering Ratio $Z$16) / (​360 * 1000 * Sheet Steering Ratio $Z$9)
def spec_fun_find_variable_11(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 11>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xActDamp_TorqueDepOnRotorSpeed_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xActDamp_TorqueDepOnRotorSpeed_XAU16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 15, 25, 3)
    find_result_mech2, mech_value2 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 8, 25, 3)
    get_value_result, first_find_geskon = get_Xvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义仅在一处存在的值
    dict_find_result_stable = {"mech1": mech_value1, "mech2": mech_value2}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(dict_find_result_stable) and dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key]) * 6 * dict_find_result_stable["mech1"] / \
                                  (360 * 1000 * dict_find_result_stable["mech2"])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para

# Voltage_Power_Supply_Threshold
# x-value nEndStopHsd_UnderVoltageStartOffset_XAU16 [3] or
# uEndStopHsd_ApplyUOffsetTh_XDU16
def spec_fun_find_variable_12(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 12>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStopHsd_UnderVoltageStartOffset_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStopHsd_UnderVoltageStartOffset_XAU16", file_name=file_dcm)
    get_value_result, last_find_geskon = get_Xvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, last_find_dcm = get_Xvalue_last_from_KENNLINIE(paragraph_find_dcm)

    find_result_geskon2, paragraph_find_geskon2 = \
        find_text_intxt(variable_to_find="uEndStopHsd_ApplyUOffsetTh_XDU16", file_name=file_geskon)
    find_result_dcm2, paragraph_find_dcm2 = \
        find_text_intxt(variable_to_find="uEndStopHsd_ApplyUOffsetTh_XDU16", file_name=file_dcm)
    get_value_result2, first_find_geskon2 = get_Yvalue_last_from_KENNLINIE(paragraph_find_geskon2)
    get_value_result2, first_find_dcm2 = get_Yvalue_last_from_KENNLINIE(paragraph_find_dcm2)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon1": last_find_geskon, "dcm1": last_find_dcm,
                                "geskon2": first_find_geskon2, "dcm2": first_find_dcm2}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 6)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para



# Speed_Tie_Rod_Low
# 6 * nEndStopHsd_MinNeededRotSpdVLow_XDU16 * (Sheet Steering Ratio $Z$16) /360 * 1000 * Sheet Steering Ratio $Z$9)
def spec_fun_find_variable_13(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 13>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStopHsd_MinNeededRotSpdVLow_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStopHsd_MinNeededRotSpdVLow_XDU16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 15, 25, 3)
    find_result_mech2, mech_value2 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 8, 25, 3)
    get_value_result, first_find_geskon = get_Yvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义仅在一处存在的值
    dict_find_result_stable = {"mech1": mech_value1, "mech2": mech_value2}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(dict_find_result_stable) and dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key]) * 6 * dict_find_result_stable["mech1"] / \
                                  (360 * 1000 * dict_find_result_stable["mech2"])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Speed_Tie_Rod_High
# 6 * nEndStopHsd_MinNeededRotSpdVHigh_XDU16 *(Sheet Steering Ratio $Z$16) / 360 * 1000 * Sheet Steering Ratio $Z$9)
def spec_fun_find_variable_14(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 14>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStopHsd_MinNeededRotSpdVHigh_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStopHsd_MinNeededRotSpdVHigh_XDU16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 15, 25, 3)
    find_result_mech2, mech_value2 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 8, 25, 3)
    get_value_result, first_find_geskon = get_Yvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义仅在一处存在的值
    dict_find_result_stable = {"mech1": mech_value1, "mech2": mech_value2}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(dict_find_result_stable) and dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key]) * 6 * dict_find_result_stable["mech1"] / \
                                  (360 * 1000 * dict_find_result_stable["mech2"])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Speed_Tie_Rod_Undervoltage_Offset
# 6 * nEndStopHsd_UndervoltOffset_XDU16 * (Sheet Steering Ratio $Z$16)  / 360 * 1000 * Sheet Steering Ratio $Z$9)
def spec_fun_find_variable_15(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 15>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStopHsd_UndervoltOffset_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStopHsd_UndervoltOffset_XDU16", file_name=file_dcm)
    find_result_mech1, mech_value1 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 15, 25, 3)
    find_result_mech2, mech_value2 = \
        fun_find_mech(file_mech_table, "Steering Ratio", 8, 25, 3)
    get_value_result, first_find_geskon = get_Yvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义仅在一处存在的值
    dict_find_result_stable = {"mech1": mech_value1, "mech2": mech_value2}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(dict_find_result_stable) and dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key]) * 6 * dict_find_result_stable["mech1"] / \
                                  (360 * 1000 * dict_find_result_stable["mech2"])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para

# Speed_Vehicle_Thres_DynStMotTrq
# last point of zBci_BaseTorqueCharSelect_XAS16
def spec_fun_find_variable_16(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 16>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="zBci_BaseTorqueCharSelect_XAS16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="zBci_BaseTorqueCharSelect_XAS16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Yvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_last_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para

# Force_Rack_Max_TargetStTrqCurve
# kBci_MaxRackForce_XDU16
# find in geskon/dcm and mech
def spec_fun_find_variable_17(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 17>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="kBci_MaxRackForce_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="kBci_MaxRackForce_XDU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Yvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_last_from_KENNLINIE(paragraph_find_dcm)
    find_result_mech, mech_value = \
        fun_find_mech(file_mech_table, "other tuning", 11, 1, 0)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm, "mech": mech_value}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Ratio_RackForce2MotorTrq
# xsyRackForceToEngTorque_XDU16
# find in geskon/dcm and mech
def spec_fun_find_variable_18(file_a2l,file_geskon,file_dcm,file_mech_table):
    logger.debug('调用函数<algorithm 18>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xsyRackForceToEngTorque_XDU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xsyRackForceToEngTorque_XDU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Yvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_last_from_KENNLINIE(paragraph_find_dcm)
    find_result_mech, mech_value = \
        fun_find_mech(file_mech_table, "MechanicalData", 71, 1, 10)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm, "mech": mech_value}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Distance_Travel_UpdateStatus_EndStopLearning_Rack
# lEndStop_StatusChangeAllowedOffset_XDU16 + mEndStop_SpringTorque_XAS16's start position
def spec_fun_find_variable_19(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 19")
    logger.debug('调用函数<algorithm 19>')
    search_in_sheet_list = ["SW-Endstop"]
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon1, paragraph_find_geskon1 = \
        find_text_intxt(variable_to_find="lEndStop_StatusChangeAllowedOffset_XDU16", file_name=file_geskon)
    find_result_dcm1, paragraph_find_dcm1 = \
        find_text_intxt(variable_to_find="lEndStop_StatusChangeAllowedOffset_XDU16", file_name=file_dcm)
    mech_value1 = fun_find_mech_by_para(file_mech_table,"lEndStop_StatusChangeAllowedOffset_XDU16", search_in_sheet_list)
    get_value_result1, first_find_geskon1 = get_Yvalue_first_from_KENNLINIE(paragraph_find_geskon1)
    get_value_result1, first_find_dcm1 = get_Yvalue_first_from_KENNLINIE(paragraph_find_dcm1)

    find_result_geskon2, paragraph_find_geskon2 = \
        find_text_intxt(variable_to_find="mEndStop_SpringTorque_XAS16", file_name=file_geskon)
    find_result_dcm2, paragraph_find_dcm2 = \
        find_text_intxt(variable_to_find="mEndStop_SpringTorque_XAS16", file_name=file_dcm)
    get_value_result2, first_find_geskon2 = get_Xvalue_first_from_KENNLINIE(paragraph_find_geskon2)
    get_value_result2, first_find_dcm2 = get_Xvalue_first_from_KENNLINIE(paragraph_find_dcm2)

    # 定义可能在多处存在的值
    dict_find_result_uunique1 = {"geskon1": first_find_geskon1, "dcm1": first_find_dcm1, "mech": mech_value1}
    dict_find_result_uunique2 = {"geskon2": first_find_geskon2, "dcm2": first_find_dcm2}
    # # 定义仅在一处存在的值
    # dict_find_result_stable = {"mech1": mech_value1, "mech2": mech_value2}
    # 定义不重复的值
    new_dict_find_result1 = dict_compare(dict_find_result_uunique1)
    new_dict_find_result2 = dict_compare(dict_find_result_uunique2)

    if dict_check_valid(new_dict_find_result1) and dict_check_valid(new_dict_find_result2):
        spec_find_result = True
        list_key1 = list(new_dict_find_result1.keys())
        list_key2 = list(new_dict_find_result2.keys())
        for key1 in list_key1:
            print(f"key: {key1}; value: {new_dict_find_result1[key1]}")
            for key2 in list_key2:
                spec_find_value_cal = float(new_dict_find_result1[key1]) + float(new_dict_find_result2[key2])
                # 调整精度
                spec_find_value_cal = round(spec_find_value_cal, 10)
                if key1 == "value":
                    spec_find_para = str(spec_find_value_cal)
                else:
                    spec_find_para = spec_find_para + f"({key1}AND{key2})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para

# Distance_Travel_FromEndStop_EndStopDampingActive
# xEndStop_Damping_XAS16_0 Y轴为0对应的X
def spec_fun_find_variable_20(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 20")
    logger.debug('调用函数<algorithm 20>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xEndStop_Damping_XAS16_0", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xEndStop_Damping_XAS16_0", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_Y0_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_Y0_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para



# Distance_Travel_FromEndStop_EndStopDampingPeak
# xEndStop_Damping_XAS16_0 Y轴最大对应的X
def spec_fun_find_variable_21(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 21")
    logger.debug('调用函数<algorithm 21>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xEndStop_Damping_XAS16_0", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xEndStop_Damping_XAS16_0", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_Ymax_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_Ymax_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Speed_Border1_ExtraDamping_Motor
# X-Axis of xEndStop_FadeFactorLimitation_XAU16[0]
def spec_fun_find_variable_22(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 22")
    logger.debug('调用函数<algorithm 22>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xEndStop_FadeFactorLimitation_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xEndStop_FadeFactorLimitation_XAU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Speed_Border2_ExtraDamping_Motor
# X-Axis of xEndStop_FadeFactorLimitation_XAU16[1]
def spec_fun_find_variable_23(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 23")
    logger.debug('调用函数<algorithm 23>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xEndStop_FadeFactorLimitation_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xEndStop_FadeFactorLimitation_XAU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_last_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para



# Supply_Voltage_Threshold
# max value of X-Axis of nEndStopHsd_UnderVoltageStartOffset_XAU16
def spec_fun_find_variable_24(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 24")
    logger.debug('调用函数<algorithm 24>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStopHsd_UnderVoltageStartOffset_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStopHsd_UnderVoltageStartOffset_XAU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_max_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_max_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Speed_Rotor_Threshold_Activate_HSD_Forward
# Y Axis of nEndStopHsd_HighSpeedDampingStart_XAS16[0]
def spec_fun_find_variable_25(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 25")
    logger.debug('调用函数<algorithm 25>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="nEndStopHsd_HighSpeedDampingStart_XAS16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="nEndStopHsd_HighSpeedDampingStart_XAS16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Yvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Voltage_Min_Range_Active_Reduction
# x-values xLowVoltAssRed_UnderVoltageReductionLevel_XAU16[0]
def spec_fun_find_variable_26(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 26")
    logger.debug('调用函数<algorithm 26>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageReductionLevel_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageReductionLevel_XAU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para



# Voltage_Min_Range_Active_Reduction
# x-values xLowVoltAssRed_UnderVoltageReductionLevel_XAU16[3]
def spec_fun_find_variable_27(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 27")
    logger.debug('调用函数<algorithm 27>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageReductionLevel_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageReductionLevel_XAU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_last_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Voltage_Min_Range_Active_Limitation
# x-values xLowVoltAssRed_UnderVoltageMotorCharTorqueAxis_XAU16[0]
def spec_fun_find_variable_28(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 28")
    logger.debug('调用函数<algorithm 28>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageMotorCharTorqueAxis_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageMotorCharTorqueAxis_XAU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Voltage_Min_Range_Active_Reduction
# x-values xLowVoltAssRed_UnderVoltageMotorCharTorqueAxis_XAU16[3]
def spec_fun_find_variable_29(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 29")
    logger.debug('调用函数<algorithm 29>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageMotorCharTorqueAxis_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageMotorCharTorqueAxis_XAU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_last_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal) + "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para



# Voltage_Min_Range_Limitation_Gradient
# x-values xLowVoltAssRed_UnderVoltageTorqueReductionGradient_XAU16[0]
def spec_fun_find_variable_30(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 30")
    logger.debug('调用函数<algorithm 30>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageTorqueReductionGradient_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageTorqueReductionGradient_XAU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_first_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_first_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


# Voltage_Min_Range_Limitation_Gradient
# x-values xLowVoltAssRed_UnderVoltageTorqueReductionGradient_XAU16[1]
def spec_fun_find_variable_31(file_a2l,file_geskon,file_dcm,file_mech_table):
    print(f"algorithm 31")
    logger.debug('调用函数<algorithm 31>')
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageTorqueReductionGradient_XAU16", file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find="xLowVoltAssRed_UnderVoltageTorqueReductionGradient_XAU16", file_name=file_dcm)
    get_value_result, first_find_geskon = get_Xvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Xvalue_last_from_KENNLINIE(paragraph_find_dcm)
    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para



# 根据变量名（parameter）从机械参数表/geskon/dcm中查询数据
def spec_fun_find_varaible_mech_and_kon(file_geskon,file_dcm,file_mech_table, search_parameter):
    logger.debug('调用函数<spec_fun_find_varaible_mech_and_kon>')
    search_in_sheet_list = ["MechanicalData", "SW-Endstop", "Steering Angle", "LoadTracking", "other tuning"]
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find= search_parameter, file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find= search_parameter, file_name=file_dcm)
    get_value_result, first_find_geskon = get_Yvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_last_from_KENNLINIE(paragraph_find_dcm)
    mech_value = fun_find_mech_by_para(file_mech_table,search_parameter, search_in_sheet_list)

    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm, "mech": mech_value}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key])
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para




# 根据数据名（data_module）或变量名从机械参数表/geskon/dcm中查询数据,并进行乘法运算factor为乘法系数）
# 如果定义了参数在机械参数表中的坐标，优先以坐标作为输入查询
def spec_fun_find_varaible_mech_and_kon_fur(file_a2l,file_geskon,file_dcm,file_mech_table, search_variable, search_parameter, mech_positon, factor):
    logger.debug('调用函数<spec_fun_find_varaible_mech_and_kon_fur>')
    search_in_sheet_list = ["MechanicalData", "SW-Endstop", "Steering Angle", "LoadTracking", "other tuning"]
    spec_find_result = False
    spec_find_para = ""
    find_result_geskon, paragraph_find_geskon = \
        find_text_intxt(variable_to_find= search_parameter, file_name=file_geskon)
    find_result_dcm, paragraph_find_dcm = \
        find_text_intxt(variable_to_find= search_parameter, file_name=file_dcm)
    get_value_result, first_find_geskon = get_Yvalue_last_from_KENNLINIE(paragraph_find_geskon)
    get_value_result, first_find_dcm = get_Yvalue_last_from_KENNLINIE(paragraph_find_dcm)
    if mech_positon[0] == "":
        mech_value = fun_find_mech_by_para(file_mech_table,search_parameter, search_in_sheet_list)
    else:
        find_result, mech_value = fun_find_mech(file_mech_table, mech_positon[0], mech_positon[1], mech_positon[2], 10)

    # 定义可能在多处存在的值
    dict_find_result_uunique = {"geskon": first_find_geskon, "dcm": first_find_dcm, "mech": mech_value}
    # 定义不重复的值
    new_dict_find_result = dict_compare(dict_find_result_uunique)

    if dict_check_valid(new_dict_find_result):
        spec_find_result = True
        list_key = list(new_dict_find_result.keys())
        for key in list_key:
            print(f"key: {key}; value: {new_dict_find_result[key]}")
            spec_find_value_cal = float(new_dict_find_result[key]) * factor
            # 调整精度
            spec_find_value_cal = round(spec_find_value_cal, 10)
            if key == "value":
                spec_find_para = str(spec_find_value_cal)+ "\n"
            else:
                spec_find_para = spec_find_para + f"({key})\n" + str(spec_find_value_cal) + "\n"
    print(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    logger.info(f"计算结果: {spec_find_result}; 计算值: {spec_find_para}")
    return spec_find_result, spec_find_para


