#!/usr/bin/python
# -*- coding: utf-8 -*-

from find_text import *
from specifical_variable_find import *
from configuration_reader import MyPath
import re




def formula_1(variable_name='', factor='1', formula=''):
    variable_name = variable_name
    factor = factor
    formula = formula
    result = ""
    mypath = MyPath()
    find_result, paragraph_find = fun_find_text(variable_name, mypath.file_geskon, mypath.file_dcm)
    if find_result == True:
        result = cal_paragraph(paragraph_find,factor)
    print(result)
    return result



def formula_2(variable_name='', factor='1', formula=''):
    variable_name = variable_name
    factor = factor
    formula = formula
    result = ""
    mypath = MyPath()
    find_result, paragraph_find = spec_fun_find_varaible_mech_and_kon(
        mypath.file_geskon,mypath.file_dcm,mypath.file_mech_table, variable_name)
    if find_result == True:
        result = cal_paragraph(paragraph_find,factor)
    print(f"result = {result}")
    return result




def formula_line(variable_name='', factor='1', formula=''):
    variable_name = variable_name
    factor = factor
    formula = formula
    result = ""
    mypath = MyPath()
    find_result, paragraph_find = spec_fun_find_variable_KLINE(variable_name,formula,mypath.file_geskon,mypath.file_dcm)
    if find_result == True:
        result = cal_paragraph(paragraph_find,factor)
    print(f"result = {result}")
    return result



def formula_a2l(variable_name='', factor='1', formula=''):
    variable_name = variable_name
    factor = factor
    formula = formula
    result = ""
    mypath = MyPath()
    if re.match("(A2L)\[([A-Z]+)\]",formula):
        if re.match("(A2L)\[([A-Z]+)\]",formula).group(2) == "MIN":
            type = "min"
        elif re.match("(A2L)\[([A-Z]+)\]",formula).group(2) == "MAX":
            type = "max"
        factor_a, factor_b = get_factor(factor)
        _, result = find_text_a2l(variable_name, mypath.file_a2l, type, factor_a)
    return result












def get_factor(factor):
    factor_a = 1
    factor_b = 0
    if factor == "1":
        factor_a = 1
    elif factor != "1" and isinstance(factor, str):
        pattern1 = r"a\s*=\s*([-+]?\d*\.?\d*)"
        pattern2 = r"b\s*=\s*([-+]?\d*\.?\d*)"
        match1 = re.search(pattern1, factor)
        match2 = re.search(pattern2, factor)
        if match1:
            factor_a = float(match1.group(1))
        if match2:
            factor_b = float(match2.group(1))
    print(f"factor_a = {factor_a}, factor_b = {factor_b}")
    return factor_a,factor_b


def cal_paragraph(paragraph,factor):
    factor_a, factor_b = get_factor(factor)
    paragraph_find = format_paragraph_find(paragraph)
    print(paragraph_find)
    list_element = paragraph_find.split()
    print(list_element)
    paragraph_cal = ""
    for i in list_element:
        if re.match(('\d+\.?\d+'), i):
            fi = float(i) * factor_a + factor_b
            fs = str(fi)
            paragraph_cal = paragraph_cal + fs + " "
        elif re.match('^\(.+\)$', i):
            paragraph_cal = paragraph_cal + "\n" + i
        elif re.match('^\w+/?\w+$', i):
            paragraph_cal = paragraph_cal + "\n" + i + " "
        else:
            paragraph_cal = paragraph_cal + i + " "
    paragraph_cal = paragraph_cal.lstrip("\n")
    print(f"paragraph_cal = {paragraph_cal}")
    return paragraph_cal





if __name__ == '__main__':
    # formula_1(variable_name='aVehSp_MaxNegGradientVAvg_XAU16',factor='a = 100 b = -100', formula='100')
    # formula_2(variable_name='wRackPo_RackposToleranceRA_XDU16', factor='a = -1;', formula='')
    # formula_line(variable_name='nEndStopHsdCheck_HighSpeedDampingStart_XAS16', factor='a = 100', formula='X[LAST]')
    formula_a2l(variable_name='nrsI_IntRotorSpeed_xds16', factor='a = 100', formula='A2L[MIN]')