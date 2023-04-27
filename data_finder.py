#!/usr/bin/python
# -*- coding: utf-8 -*-

from database_hander import MyDataBaseHander
from formula_library import *
from dxl_command_sender import DxlSender, MyDxlCommand


class MyData:
    def __init__(self, data_name, module_name, series="NS", get_previous=False):
        # SWITCH
        self.get_previous = get_previous

        self.data_name = data_name
        self.module_name = module_name

        self.formula_type = ""
        self.variable_name = ""
        self.factor = ""
        self.formula = ""

        self.value_new = ""
        self.value_previous = ""
        self.series = series
        self.is_pn_equal = False
        self.is_gdm_equal = False

        # functions
        # 获取公式
        if self.get_formula():
            # 查询新值
            self.get_new_value()
        if self.get_previous:
            # 查询先前值
            self.get_previous_value()
        # 校验新数据中各来源值是否相等
        self.is_gdm_equal = self.check_data_gdm_equal()
        # 校验新旧值是否相等
        self.is_pn_equal = self.check_data_pn_equal()
        # 存储数据至db
        self.save_data_to_db()

    def get_formula(self):
        dbhander = MyDataBaseHander()
        data_formula = dbhander.select_data_formula(self.data_name, self.module_name)
        if not data_formula:
            return False
        else:
            self.formula_type = data_formula[0]
            self.variable_name = data_formula[1]
            self.factor = data_formula[2]
            self.formula = data_formula[3]
            print(f"formula_type = {self.formula_type}, "
                  f"variable_name = {self.variable_name},"
                  f"factor = {self.factor},"
                  f"formula = {self.formula}")
            return True

    def get_new_value(self):
        finder = MyFinder(formula_type=self.formula_type,
                          variable_name=self.variable_name,
                          factor=self.factor,
                          formula=self.formula)
        self.value_new = finder.value_new
        return

    def save_data_to_db(self):
        dbhander = MyDataBaseHander()
        if self.data_name != "":
            if self.get_previous:
                # 更新 value_previous
                dbhander.update_data_update(self.data_name,
                                            self.module_name,
                                            self.value_previous,
                                            self.value_new,
                                            self.series,
                                            self.is_pn_equal,
                                            self.is_gdm_equal)
            elif not self.get_previous or self.get_previous == "":
                # 不更新 value_previous 和 is_pn_equal
                dbhander.update_new_data_update(self.data_name,
                                                self.module_name,
                                                self.value_new,
                                                self.series,
                                                self.is_gdm_equal)

    def check_data_pn_equal(self):
        """ 校验 value_new 和 value_previous 是否相等"""
        check_result = False
        if self.value_previous != "" and self.value_new != "":
            try:
                if self.value_new.replace("\n", "").replace(" ", "") == \
                        self.value_previous.replace("\n", "").replace(" ", ""):
                    check_result = True
                else:
                    check_result = False
            except Exception as e:
                print(f"An error occurs: {e}")
            if not check_result:
                try:
                    if float(self.value_new) == float(self.value_previous):
                        check_result = True
                    else:
                        check_result = False
                except Exception as e:
                    print(f"An error occurs: {e}")
        elif self.value_previous == "":
            check_result = False
        elif self.value_new == "":
            check_result = False
        return check_result

    def check_data_gdm_equal(self):
        """ 校验 value_new 中dcm、geskon、mech数据是否有不一致"""
        check_result = False
        if not re.match("\(.+\)", self.value_new):
            check_result = True
        print("gdm result: ", check_result)
        return check_result

    def get_previous_value(self):
        """ 从doors中读取先前值 """
        mydxlcmd = MyDxlCommand()
        find_value_dxl_cmd = mydxlcmd.find_value(self.data_name, self.module_name)
        mysender = DxlSender()
        response = mysender.send_dxl_commands(find_value_dxl_cmd)
        if response != "":
            self.value_previous = response
        print("value_previous = ", self.value_previous)
        return


class MyFinder:
    def __init__(self, formula_type='', variable_name='', factor='1', formula=''):
        self.formula_type = formula_type
        self.variable_name = variable_name.replace(" ", "")
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
            print("Go to formula_type A2L")
            self.value_new = formula_a2l(variable_name=self.variable_name, factor=self.factor, formula=self.formula)
        elif self.formula_type == "21":
            print("Go to formula_type 21")
            self.value_new = formula_21(variable_name=self.variable_name, factor=self.factor, formula=self.formula)
        elif self.formula_type == "32":
            print("Go to formula_type 32")
            self.value_new = formula_32(variable_name=self.variable_name, factor=self.factor, formula=self.formula)
        elif self.formula_type == "33":
            print("Go to formula_type 33")
            self.value_new = formula_33(variable_name=self.variable_name, factor=self.factor, formula=self.formula)
        elif self.formula_type == "51":
            print("Go to formula_type 51")
            self.value_new = formula_51()
        elif self.formula_type == "52":
            print("Go to formula_type 52")
            self.value_new = formula_52()
        elif self.formula_type == "53":
            print("Go to formula_type 53")
            self.value_new = formula_53()
        elif self.formula_type == "54":
            print("Go to formula_type 54")
            self.value_new = formula_54()
        elif self.formula_type == "55":
            print("Go to formula_type 55")
            self.value_new = formula_55()
        elif self.formula_type == "56":
            print("Go to formula_type 56")
            self.value_new = formula_56()
        elif self.formula_type == "57":
            print("Go to formula_type 57")
            self.value_new = formula_57()
        elif self.formula_type == "58":
            print("Go to formula_type 58")
            self.value_new = formula_58()
        elif self.formula_type == "59":
            print("Go to formula_type 59")
            self.value_new = formula_59()
        elif self.formula_type == "60":
            print("Go to formula_type 60")
            self.value_new = formula_60()


if __name__ == '__main__':
    dbhander = MyDataBaseHander()
    data_list = dbhander.select_data_list()[:10]
    mydata_list = []
    for tuple in data_list:
        print(tuple[0], tuple[1])
        print("构建mydata")
        mydata = MyData(tuple[0], tuple[1], series="NS", get_previous=False)
        print("构建完成mydata", mydata.data_name, mydata.module_name, mydata.value_new)
        mydata_list.append(mydata)
        # if mydata.formula_type == "21":
        #     print(f"mydata.data_name = {mydata.data_name}")
        #     print(f"mydata.value_new = {mydata.value_new}")

    # print(data_list[0][0], data_list[0][1])
    # mydata = MyData(data_list[0][0], data_list[0][1])
    print("number of mydata is: ", len(mydata_list))
    for mydata in mydata_list:
        print(mydata.data_name, mydata.module_name, mydata.value_new)

    mydata = MyData("Min_Vehicle_speed", "LSS", series="NS", get_previous=True)
