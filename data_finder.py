#!/usr/bin/python
# -*- coding: utf-8 -*-

from database_hander import MyDataBaseHander
from formula_library import *


class MyData:
    def __init__(self, data_name, module_name):
        self.data_name = data_name
        self.module_name = module_name
        self.formula_type = ""
        self.variable_name = ""
        self.factor = ""
        self.formula = ""

        self.get_formula()
        self.get_new_value()


    def get_formula(self):
        dbhander = MyDataBaseHander()
        data_formula = dbhander.select_data_formula(self.data_name, self.module_name)
        self.formula_type = data_formula[0]
        self.variable_name = data_formula[1]
        self.factor = data_formula[2]
        self.formula = data_formula[3]
        print(f"formula_type = {self.formula_type}, "
              f"variable_name = {self.variable_name},"
              f"factor = {self.factor},"
              f"formula = {self.formula}")

    def get_new_value(self):
        finder = MyFinder(formula_type=self.formula_type,
                          variable_name=self.variable_name,
                          factor=self.factor,
                          formula=self.formula)
        self.value_new = finder.value_new



class MyFinder:
    def __init__(self, formula_type='', variable_name='', factor='1', formula=''):
        self.formula_type = formula_type
        self.variable_name = variable_name.replace(" ","")
        self.factor = factor
        self.formula = formula
        self.value_previous = ""
        self.value_new = ""

        self.find_value()

    def find_value(self):
        if self.formula_type == "":
            print("None formula_type")
        elif self.formula_type == "1":
            print("Go to formula_type 1")
            self.value_new = formula_1(variable_name=self.variable_name, factor=self.factor, formula=self.formula)
        elif self.formula_type == "2":
            print("Go to formula_type 2")
            self.value_new = formula_2(variable_name=self.variable_name, factor=self.factor, formula=self.formula)
        elif self.formula_type == "LINE":
            print("Go to formula_type LINE")
            self.value_new = formula_line(variable_name=self.variable_name, factor=self.factor, formula=self.formula)
        elif self.formula_type == "A2L":
            self.value_new = formula_a2l(variable_name=self.variable_name, factor=self.factor, formula=self.formula)
            print("Go to formula_type A2L")




if __name__ == '__main__':
    dbhander = MyDataBaseHander()
    data_list = dbhander.select_data_list()
    for tuple in data_list:
        print(tuple[0], tuple[1])
        mydata = MyData(tuple[0], tuple[1])
        if mydata.formula_type == "A2L":
            print(f"mydata.data_name = {mydata.data_name}")
            print(f"mydata.value_new = {mydata.value_new}")
    # print(data_list[0][0], data_list[0][1])
    # mydata = MyData(data_list[0][0], data_list[0][1])
