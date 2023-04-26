#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QFileDialog, \
    QMessageBox, QMenu, QTextBrowser, QVBoxLayout, QListWidgetItem
from PySide6.QtCore import Qt, QObject, Signal, QThread, Slot, QRect
from PySide6.QtGui import QAction
import json
import time

from DataQueryX import Ui_MainWindow
from configuration_reader import MyPath, MyConfig
from database_hander import MyDataBaseHander
from data_finder import MyData


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.mypath = MyPath()
        self.myconfig = MyConfig()

        self.task = None
        self.setupUi(self)
        self.retranslateUi(self)

        # 创建 QThread 对象
        self.worker = MyTask_QueryData()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()

        # 连接任务的 started 信号到槽函数，禁用按钮
        self.worker.started.connect(self.on_task_started)
        #
        # # 连接任务的 finished 信号到槽函数，恢复按钮
        self.worker.finished.connect(self.on_task_finished)
        self.worker.message.connect(self.on_message_send)

        # Data Query Group
        self.toolButton_path_mech.clicked.connect(self.select_file_mech)
        self.toolButton_path_geskon.clicked.connect(self.select_file_geskon)
        self.toolButton_path_dcm.clicked.connect(self.select_file_dcm)
        self.toolButton_path_a2l.clicked.connect(self.select_file_a2l)
        self.pushButton_start_data_query.clicked.connect(self.confirm_data)
        self.pushButton_start_data_query.clicked.connect(self.worker.query_data)

        # Data Query Group
        self.button_load.clicked.connect(self.load_cfg)
        self.button_save.clicked.connect(self.save_cfg)
        self.pushButton_check.clicked.connect(self.check_config)
        self.checkBox_psw.stateChanged.connect(self.password_display)
        self.toolButton_reflash_list.clicked.connect(self.reflash_data_list)
        self.toolButton_reflash_list_2.clicked.connect(self.reflash_data_list2)

        self.check_data_list_reflash()
        self.check_data_list_reflash_2()

    def select_file_mech(self):
        file_path_mech, _ = QFileDialog.getOpenFileName(self, "选择机械参数表", ".", "表格文件(*.xlsm);;所有文件(*)")
        if file_path_mech:
            self.lineEdit_path_mech.setText(file_path_mech)
            print(file_path_mech)
            try:
                with open(self.mypath.config_path, 'r', encoding='utf - 8') as f:
                    json_data = json.load(f)
                    json_data["file_mech"] = file_path_mech
            except Exception as e:
                print("An error occurred:", e)
            try:
                with open(self.mypath.config_path, 'w') as f:
                    f.write(json.dumps(json_data, indent=4))
            except Exception as e:
                print("An error occurred:", e)

        return file_path_mech

    def select_file_geskon(self):
        file_path_geskon, _ = QFileDialog.getOpenFileName(self, "选择Geskon文件", ".", "geskon文件(*.kon);;所有文件(*)")
        if file_path_geskon:
            self.lineEdit_path_geskon.setText(file_path_geskon)
            print(file_path_geskon)
            try:
                with open(self.mypath.config_path, 'r', encoding='utf - 8') as f:
                    json_data = json.load(f)
                    json_data["file_geskon"] = file_path_geskon
            except Exception as e:
                print("An error occurred:", e)
            try:
                with open(self.mypath.config_path, 'w') as f:
                    f.write(json.dumps(json_data, indent=4))
            except Exception as e:
                print("An error occurred:", e)
        return file_path_geskon

    def select_file_dcm(self):
        file_path_dcm, _ = QFileDialog.getOpenFileName(self, "选择DCM文件", ".", "dcm文件(*.dcm);;所有文件(*)")
        if file_path_dcm:
            self.lineEdit_path_dcm.setText(file_path_dcm)
            print(file_path_dcm)
            try:
                with open(self.mypath.config_path, 'r', encoding='utf - 8') as f:
                    json_data = json.load(f)
                    json_data["file_dcm"] = file_path_dcm
            except Exception as e:
                print("An error occurred:", e)
            try:
                with open(self.mypath.config_path, 'w') as f:
                    f.write(json.dumps(json_data, indent=4))
            except Exception as e:
                print("An error occurred:", e)
        return file_path_dcm

    def select_file_a2l(self):
        file_path_a2l, _ = QFileDialog.getOpenFileName(self, "选择A2L文件", ".", "a2l文件(*.a2l);;所有文件(*)")
        if file_path_a2l:
            self.lineEdit_path_a2l.setText(file_path_a2l)
            print(file_path_a2l)
            try:
                with open(self.mypath.config_path, 'r', encoding='utf - 8') as f:
                    json_data = json.load(f)
                    json_data["file_a2l"] = file_path_a2l
            except Exception as e:
                print("An error occurred:", e)
            try:
                with open(self.mypath.config_path, 'w') as f:
                    f.write(json.dumps(json_data, indent=4))
            except Exception as e:
                print("An error occurred:", e)

        return file_path_a2l

    def load_cfg(self):
        print("load cfg")
        myconfig = MyConfig()
        project_name = myconfig.doors_project_path[1:]
        print(f"project_name is [{project_name}]")
        data_suffix = myconfig.data_suffix
        print(f"data_suffix is [{data_suffix}]")
        doors_username = myconfig.doors_username
        print(f"doors_username is [{doors_username}]")
        doors_password = myconfig.doors_password
        print(f"doors_password is [{doors_password}]")

        self.lineEdit_project_name.setText(project_name)
        self.lineEdit_data_suffix.setText(data_suffix)
        self.lineEdit_username.setText(doors_username)
        self.lineEdit_password.setText(doors_password)

    def save_cfg(self):
        mypath = MyPath()
        print("save cfg")
        project_name = self.lineEdit_project_name.text()
        data_suffix = self.lineEdit_data_suffix.text()
        doors_username = self.lineEdit_username.text()
        doors_password = self.lineEdit_password.text()

        try:
            with open(mypath.config_path, 'r', encoding='utf - 8') as f:
                json_data = json.load(f)
                json_data["project_name"] = project_name
                json_data["data_suffix"] = data_suffix
                json_data["doors_username"] = doors_username
                json_data["doors_password"] = doors_password
        except Exception as e:
            print("An error occurred:", e)
        try:
            with open(mypath.config_path, 'w') as f:
                f.write(json.dumps(json_data, indent=4))
        except Exception as e:
            print("An error occurred:", e)

        QMessageBox.information(self, "提示", "已保存！")

    def password_display(self):
        if self.checkBox_psw.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def check_config(self):
        myconfig = MyConfig()
        error_flag, error_message = myconfig.check_my_config()

        if error_flag == 0:
            QMessageBox.information(self, "提示", "检查通过！")
        else:
            QMessageBox.information(self, "提示", error_message)

    def reflash_data_list(self):
        print("更新列表")
        self.listWidget_rule_module_name.clear()
        self.listWidget_rule_data_name.clear()
        self.lineEdit_module_name_list.setText("--ALL--")
        self.lineEdit_data_name_list.setText("--ALL--")
        module_list = []
        data_list = []
        if self.lineEdit_module_name_list.text() == "" or self.lineEdit_module_name_list.text() == "--ALL--":
            dbhander = MyDataBaseHander()
            db_data_list = dbhander.select_data_list()
            print("data_list = ", db_data_list)

            item = QListWidgetItem("--ALL--")
            # item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Add the checkable flag
            # item.setCheckState(Qt.Unchecked)  # Set the initial check state to unchecked
            self.listWidget_rule_module_name.addItem(item)

            for data in db_data_list:
                print("data:", data)
                if data[1] not in module_list:
                    module_list.append(data[1])
                data_list.append(data[0])
            for i in module_list:
                item = QListWidgetItem(i)
                # item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Add the checkable flag
                # item.setCheckState(Qt.Unchecked)  # Set the initial check state to unchecked
                self.listWidget_rule_module_name.addItem(item)
            # for i in data_list:
            #     self.listWidget_rule_data_name.addItem(i)


    def check_data_list_reflash(self):
        print("check data list reflash")

        def on_item_select_changed_module():
            self.lineEdit_data_name_list.setText("--ALL--")
            selected_item = self.listWidget_rule_module_name.currentItem()
            if selected_item is not None:
                selected_text = selected_item.text()
                print("选择了:", selected_text)
                self.lineEdit_module_name_list.setText(selected_text)
                if selected_text == "--ALL--":
                    self.reflash_data_list()
                else:
                    dbhander = MyDataBaseHander()
                    db_data_list = dbhander.select_data_list_by_module_name(selected_text)
                    data_list = []
                    for data in db_data_list:
                        data_list.append(data[0])
                    self.listWidget_rule_data_name.clear()
                    self.listWidget_rule_data_name.addItems(data_list)

        def on_item_select_changed_data():
            selected_item = self.listWidget_rule_data_name.currentItem()
            if selected_item is not None:
                selected_text = selected_item.text()
                print("选择了:", selected_text)
                self.lineEdit_data_name_list.setText(selected_text)

        self.listWidget_rule_module_name.itemClicked.connect(on_item_select_changed_module)
        self.listWidget_rule_data_name.itemClicked.connect(on_item_select_changed_data)

    def start_data_query(self):
        get_previous = False
        if self.checkBox_is_get_previous_value.isChecked():
            get_previous = True
        if self.lineEdit_series.text() == "":
            series = "NS"
        else:
            series = self.lineEdit_series.text()
        print("get_previous = ", get_previous)
        print("series", series)
        select_module_name = self.lineEdit_module_name_list.text()
        select_data_name = self.lineEdit_data_name_list.text()
        print("select_module_name: ",select_module_name, "select_data_name: ",select_data_name)
        db_data_list = []
        if select_module_name == "--ALL--":
            dbhander_temp = MyDataBaseHander()
            db_data_list = dbhander_temp.select_data_list()
        elif select_module_name != "--ALL--":
            if select_data_name == "--ALL--":
                dbhander_temp = MyDataBaseHander()
                db_data_list = dbhander_temp.select_data_list_by_module_name(select_module_name)
            else:
                db_data_list.append((select_data_name, select_module_name))

        print("db_data_list = ", db_data_list)

        print("start_data_query")

        # 创建 QThread 对象
        self.worker = MyTask_QueryData()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()
        self.textEdit_show.clear()
        for data_tuple in db_data_list:
            # data_tuple = (data_name, module_name)
            print()
            data_name, module_name, value_new, value_previous = self.worker.query_data(data_tuple,series, get_previous)
            print(f"data_name is {data_tuple[0]}, data_module is {data_tuple[1]}")
            self.textEdit_show.append(f"模块名称: {module_name}")
            self.textEdit_show.append(f"数据名称: {data_name}")
            self.textEdit_show.append(f"参数值: {value_new}")
            if value_previous != "":
                self.textEdit_show.append(f"参数值: {value_previous}")


        #
        # # # 连接任务的 started 信号到槽函数，禁用按钮
        # # self.worker.started.connect(self.on_task_started)
        # #
        # # # 连接任务的 finished 信号到槽函数，恢复按钮
        # # self.worker.finished.connect(self.on_task_finished)
        #
        # 任务执行完毕后，清理并退出线程
        self.worker.deleteLater()
        self.thread.quit()
        self.thread.wait()

    def confirm_data(self):
        global db_data_list
        global series
        global get_previous
        get_previous = False
        if self.checkBox_is_get_previous_value.isChecked():
            get_previous = True
        if self.lineEdit_series.text() == "":
            series = "NS"
        else:
            series = self.lineEdit_series.text()
        print("get_previous = ", get_previous)
        print("series", series)
        select_module_name = self.lineEdit_module_name_list.text()
        select_data_name = self.lineEdit_data_name_list.text()
        print("select_module_name: ", select_module_name, "select_data_name: ", select_data_name)
        db_data_list = []
        if select_module_name == "--ALL--":
            dbhander_temp = MyDataBaseHander()
            db_data_list = dbhander_temp.select_data_list()
        elif select_module_name != "--ALL--":
            if select_data_name == "--ALL--":
                dbhander_temp = MyDataBaseHander()
                db_data_list = dbhander_temp.select_data_list_by_module_name(select_module_name)
            else:
                db_data_list.append((select_data_name, select_module_name))

        print("db_data_list = ", db_data_list)

    def on_message_send(self, data_name, module_name, value_new, value_previous):
        print("信号：", data_name, module_name, value_new, value_previous)
        self.textEdit_show.append(f"模块名称: {module_name} ;数据名称: {data_name}")
        self.textEdit_show.append(f"参数值:\n{value_new}")
        if value_previous != "":
            self.textEdit_show.append(f"以往值:\n{value_previous}")

    def on_task_started(self):
        self.textEdit_show.clear()
        self.textEdit_show.append(f"[Info: Start... ...]")

    def on_task_finished(self):
        self.textEdit_show.append(f"[Info: Finish.]")

    def reflash_data_list2(self):
        self.comboBox_series.clear()
        dbhander_temp = MyDataBaseHander()
        result = dbhander_temp.select_update_data_list()
        if result is not None:
            list_series = []
            for i in result:
                if i[4] not in list_series:
                    list_series.append(i[4])
            self.comboBox_series.addItems(list_series)


        print("更新列表")
        self.listWidget_rule_module_name_2.clear()
        self.listWidget_rule_data_name_2.clear()
        # item1 = QListWidgetItem("--ALL--")
        # item1.setFlags(item1.flags() | Qt.ItemIsUserCheckable)  # Add the checkable flag
        # item1.setCheckState(Qt.Unchecked)  # Set the initial check state to unchecked
        # item2 = QListWidgetItem("--ALL--")
        # item2.setFlags(item2.flags() | Qt.ItemIsUserCheckable)  # Add the checkable flag
        # item2.setCheckState(Qt.Unchecked)  # Set the initial check state to unchecked
        # self.listWidget_rule_module_name_2.addItem(item1)
        # self.listWidget_rule_data_name_2.addItem(item2)

        module_list = ["--ALL--"]
        data_list = ["--ALL--"]

        series = self.comboBox_series.currentText()
        print("选择的series是", series)

        dbhander_temp = MyDataBaseHander()
        result =  dbhander_temp.select_data_list_by_series(series)
        if result is not None:
            for i in result:
                if i[1] not in module_list:
                    module_list.append(i[1])
                data_list.append(i[0])

        # for module in module_list:
        #     item_module = QListWidgetItem(module)
        #     item_module.setFlags(item_module.flags() | Qt.ItemIsUserCheckable)  # Add the checkable flag
        #     item_module.setCheckState(Qt.Unchecked)  # Set the initial check state to unchecked
            self.listWidget_rule_module_name_2.addItems(module_list)

        # for data in data_list:
        #     item_data = QListWidgetItem(data)
        #     item_data.setFlags(item_data.flags() | Qt.ItemIsUserCheckable)  # Add the checkable flag
        #     item_data.setCheckState(Qt.Unchecked)  # Set the initial check state to unchecked
            self.listWidget_rule_data_name_2.addItems(data_list)

    def check_data_list_reflash_2(self):
        def on_select_series_changed():
            self.listWidget_rule_module_name_2.clear()
            self.listWidget_rule_data_name_2.clear()
            series = self.comboBox_series.currentText()
            print("选择的series是", series)
            module_list = ["--ALL--"]
            data_list = ["--ALL--"]
            dbhander_temp = MyDataBaseHander()
            result = dbhander_temp.select_data_list_by_series(series)
            if result is not None:
                for i in result:
                    if i[1] not in module_list:
                        module_list.append(i[1])
                    data_list.append(i[0])

            # for module in module_list:
            #     item_module = QListWidgetItem(module)
            #     item_module.setFlags(item_module.flags() | Qt.ItemIsUserCheckable)  # Add the checkable flag
            #     item_module.setCheckState(Qt.Unchecked)  # Set the initial check state to unchecked
                self.listWidget_rule_module_name_2.addItems(module_list)

            # for data in data_list:
            #     item_data = QListWidgetItem(data)
            #     item_data.setFlags(item_data.flags() | Qt.ItemIsUserCheckable)  # Add the checkable flag
            #     item_data.setCheckState(Qt.Unchecked)  # Set the initial check state to unchecked
                self.listWidget_rule_data_name_2.addItems(data_list)

        def on_item_select_changed_module():
            items = self.listWidget_rule_module_name_2.selectedItems()
            for item in items:
                module = item.text()
                print("当前选择的module是",module)
                if module == "--ALL--":
                    print("当前选择的module是: 全部")
                    self.listWidget_rule_data_name_2.clear()
                    self.listWidget_rule_data_name_2.addItem("--ALL--")
                    items = self.listWidget_rule_module_name_2.selectedItems()
                    self.listWidget_rule_module_name_2.selectAll()
                    item.setSelected(True)
                else:
                    current_item = self.listWidget_rule_module_name_2.currentItem()
                    current_module = current_item.text()
                    print(f"当前选择的module是: {current_module}")
                    self.listWidget_rule_data_name_2.clear()
                    dbhander_temp = MyDataBaseHander()
                    data_list = []
                    db_data_list = dbhander_temp.select_data_list_by_module_name(current_module)
                    if db_data_list is not None:
                        for i in db_data_list:
                            data_list.append(i[0])
                    self.listWidget_rule_data_name_2.addItems(data_list)
                    if len(items) > 1:
                        print("选择了多个module")
                        self.listWidget_rule_data_name_2.selectAll()
                        for index in range(self.listWidget_rule_data_name_2.count()):
                            item = self.listWidget_rule_data_name_2.item(index)
                            item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
                            item.setSelected(True)







        self.comboBox_series.currentTextChanged.connect(on_select_series_changed)

        self.listWidget_rule_module_name_2.itemClicked.connect(on_item_select_changed_module)
        # self.listWidget_rule_data_name_2.itemClicked.connect(on_item_select_changed_data)






class MyTask_QueryData(QObject):

    started = Signal()
    finished = Signal()
    message = Signal(str, str, str, str)

    # def query_data(self, data_tuple, series, get_previous):
    def query_data(self):
        global db_data_list
        global series
        global get_previous
        # 发出 started 信号以通知 UI 线程
        self.started.emit()

        t_start = time.perf_counter()
        for data_tuple in db_data_list:
            print(data_tuple[0], data_tuple[1])
            print("构建mydata")
            mydata = MyData(data_tuple[0], data_tuple[1], series, get_previous)
            print("构建完成mydata", mydata.data_name, mydata.module_name, mydata.value_new, mydata.value_previous)
            self.message.emit(mydata.data_name, mydata.module_name, mydata.value_new, mydata.value_previous)

        # print("运行中")
        # time.sleep(5)
        t_end = time.perf_counter()
        t_cost = t_end - t_start
        print(f'运行耗时:{t_cost:.8f}s')
        # print("运行结束")

        # 任务完成后发出 finished 信号
        self.finished.emit()

        return mydata.data_name,mydata.module_name,mydata.value_new,mydata.value_previous



if __name__ == '__main__':
    app = QApplication([])
    app.setStyle("Fusion")
    window = MyWindow()
    window.show()
    app.exec()
