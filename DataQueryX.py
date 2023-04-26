# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataQueryX.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 929)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textEdit_show = QTextEdit(self.tab)
        self.textEdit_show.setObjectName(u"textEdit_show")
        self.textEdit_show.setGeometry(QRect(40, 630, 691, 111))
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 200, 691, 421))
        self.pushButton_start_data_query = QPushButton(self.groupBox)
        self.pushButton_start_data_query.setObjectName(u"pushButton_start_data_query")
        self.pushButton_start_data_query.setGeometry(QRect(260, 390, 101, 24))
        self.checkBox_is_get_previous_value = QCheckBox(self.groupBox)
        self.checkBox_is_get_previous_value.setObjectName(u"checkBox_is_get_previous_value")
        self.checkBox_is_get_previous_value.setGeometry(QRect(41, 341, 132, 20))
        self.label_series = QLabel(self.groupBox)
        self.label_series.setObjectName(u"label_series")
        self.label_series.setGeometry(QRect(41, 367, 52, 16))
        self.lineEdit_series = QLineEdit(self.groupBox)
        self.lineEdit_series.setObjectName(u"lineEdit_series")
        self.lineEdit_series.setGeometry(QRect(99, 367, 132, 21))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 40, 501, 108))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_path_mech = QLabel(self.layoutWidget)
        self.label_path_mech.setObjectName(u"label_path_mech")

        self.gridLayout.addWidget(self.label_path_mech, 0, 0, 1, 1)

        self.lineEdit_path_mech = QLineEdit(self.layoutWidget)
        self.lineEdit_path_mech.setObjectName(u"lineEdit_path_mech")

        self.gridLayout.addWidget(self.lineEdit_path_mech, 0, 1, 1, 1)

        self.toolButton_path_mech = QToolButton(self.layoutWidget)
        self.toolButton_path_mech.setObjectName(u"toolButton_path_mech")

        self.gridLayout.addWidget(self.toolButton_path_mech, 0, 2, 1, 1)

        self.label_path_geskon = QLabel(self.layoutWidget)
        self.label_path_geskon.setObjectName(u"label_path_geskon")

        self.gridLayout.addWidget(self.label_path_geskon, 1, 0, 1, 1)

        self.lineEdit_path_geskon = QLineEdit(self.layoutWidget)
        self.lineEdit_path_geskon.setObjectName(u"lineEdit_path_geskon")

        self.gridLayout.addWidget(self.lineEdit_path_geskon, 1, 1, 1, 1)

        self.toolButton_path_geskon = QToolButton(self.layoutWidget)
        self.toolButton_path_geskon.setObjectName(u"toolButton_path_geskon")

        self.gridLayout.addWidget(self.toolButton_path_geskon, 1, 2, 1, 1)

        self.label_path_dcm = QLabel(self.layoutWidget)
        self.label_path_dcm.setObjectName(u"label_path_dcm")

        self.gridLayout.addWidget(self.label_path_dcm, 2, 0, 1, 1)

        self.lineEdit_path_dcm = QLineEdit(self.layoutWidget)
        self.lineEdit_path_dcm.setObjectName(u"lineEdit_path_dcm")

        self.gridLayout.addWidget(self.lineEdit_path_dcm, 2, 1, 1, 1)

        self.toolButton_path_dcm = QToolButton(self.layoutWidget)
        self.toolButton_path_dcm.setObjectName(u"toolButton_path_dcm")

        self.gridLayout.addWidget(self.toolButton_path_dcm, 2, 2, 1, 1)

        self.label_path_a2l = QLabel(self.layoutWidget)
        self.label_path_a2l.setObjectName(u"label_path_a2l")

        self.gridLayout.addWidget(self.label_path_a2l, 3, 0, 1, 1)

        self.lineEdit_path_a2l = QLineEdit(self.layoutWidget)
        self.lineEdit_path_a2l.setObjectName(u"lineEdit_path_a2l")

        self.gridLayout.addWidget(self.lineEdit_path_a2l, 3, 1, 1, 1)

        self.toolButton_path_a2l = QToolButton(self.layoutWidget)
        self.toolButton_path_a2l.setObjectName(u"toolButton_path_a2l")

        self.gridLayout.addWidget(self.toolButton_path_a2l, 3, 2, 1, 1)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 180, 611, 141))
        self.gridLayout_4 = QGridLayout(self.layoutWidget1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_module_name_list = QLabel(self.layoutWidget1)
        self.label_module_name_list.setObjectName(u"label_module_name_list")

        self.gridLayout_3.addWidget(self.label_module_name_list, 0, 0, 1, 1)

        self.lineEdit_module_name_list = QLineEdit(self.layoutWidget1)
        self.lineEdit_module_name_list.setObjectName(u"lineEdit_module_name_list")

        self.gridLayout_3.addWidget(self.lineEdit_module_name_list, 0, 1, 1, 1)

        self.label_data_name_list = QLabel(self.layoutWidget1)
        self.label_data_name_list.setObjectName(u"label_data_name_list")

        self.gridLayout_3.addWidget(self.label_data_name_list, 0, 2, 1, 1)

        self.lineEdit_data_name_list = QLineEdit(self.layoutWidget1)
        self.lineEdit_data_name_list.setObjectName(u"lineEdit_data_name_list")

        self.gridLayout_3.addWidget(self.lineEdit_data_name_list, 0, 3, 1, 1)

        self.listWidget_rule_module_name = QListWidget(self.layoutWidget1)
        QListWidgetItem(self.listWidget_rule_module_name)
        self.listWidget_rule_module_name.setObjectName(u"listWidget_rule_module_name")

        self.gridLayout_3.addWidget(self.listWidget_rule_module_name, 1, 1, 1, 1)

        self.listWidget_rule_data_name = QListWidget(self.layoutWidget1)
        QListWidgetItem(self.listWidget_rule_data_name)
        self.listWidget_rule_data_name.setObjectName(u"listWidget_rule_data_name")

        self.gridLayout_3.addWidget(self.listWidget_rule_data_name, 1, 3, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.toolButton_reflash_list = QToolButton(self.layoutWidget1)
        self.toolButton_reflash_list.setObjectName(u"toolButton_reflash_list")

        self.gridLayout_4.addWidget(self.toolButton_reflash_list, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(40, 30, 691, 141))
        self.button_save = QPushButton(self.groupBox_2)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(107, 110, 72, 24))
        self.button_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_save.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        self.pushButton_check = QPushButton(self.groupBox_2)
        self.pushButton_check.setObjectName(u"pushButton_check")
        self.pushButton_check.setGeometry(QRect(460, 110, 71, 24))
        font = QFont()
        font.setBold(True)
        self.pushButton_check.setFont(font)
        self.pushButton_check.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_check.setStyleSheet(u"")
        self.button_load = QPushButton(self.groupBox_2)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setGeometry(QRect(30, 110, 72, 24))
        self.button_load.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_load.setMouseTracking(False)
        self.button_load.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        self.layoutWidget2 = QWidget(self.groupBox_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(32, 30, 505, 76))
        self.gridLayout_2 = QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_projectname = QLabel(self.layoutWidget2)
        self.label_projectname.setObjectName(u"label_projectname")

        self.gridLayout_2.addWidget(self.label_projectname, 0, 0, 1, 1)

        self.label_projectname_2 = QLabel(self.layoutWidget2)
        self.label_projectname_2.setObjectName(u"label_projectname_2")

        self.gridLayout_2.addWidget(self.label_projectname_2, 1, 0, 1, 1)

        self.label_username = QLabel(self.layoutWidget2)
        self.label_username.setObjectName(u"label_username")

        self.gridLayout_2.addWidget(self.label_username, 2, 0, 1, 1)

        self.lineEdit_username = QLineEdit(self.layoutWidget2)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        font1 = QFont()
        font1.setPointSize(8)
        self.lineEdit_username.setFont(font1)

        self.gridLayout_2.addWidget(self.lineEdit_username, 2, 1, 1, 1)

        self.label_password = QLabel(self.layoutWidget2)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout_2.addWidget(self.label_password, 2, 2, 1, 1)

        self.lineEdit_password = QLineEdit(self.layoutWidget2)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setFont(font1)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.lineEdit_password, 2, 3, 1, 1)

        self.checkBox_psw = QCheckBox(self.layoutWidget2)
        self.checkBox_psw.setObjectName(u"checkBox_psw")
        self.checkBox_psw.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_psw, 2, 4, 1, 1)

        self.lineEdit_data_suffix = QLineEdit(self.layoutWidget2)
        self.lineEdit_data_suffix.setObjectName(u"lineEdit_data_suffix")

        self.gridLayout_2.addWidget(self.lineEdit_data_suffix, 1, 1, 1, 3)

        self.lineEdit_project_name = QLineEdit(self.layoutWidget2)
        self.lineEdit_project_name.setObjectName(u"lineEdit_project_name")

        self.gridLayout_2.addWidget(self.lineEdit_project_name, 0, 1, 1, 3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textEdit_show_2 = QTextEdit(self.tab_2)
        self.textEdit_show_2.setObjectName(u"textEdit_show_2")
        self.textEdit_show_2.setGeometry(QRect(30, 640, 691, 111))
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 20, 691, 541))
        self.pushButton_start_update_doos = QPushButton(self.groupBox_3)
        self.pushButton_start_update_doos.setObjectName(u"pushButton_start_update_doos")
        self.pushButton_start_update_doos.setGeometry(QRect(270, 470, 101, 24))
        self.layoutWidget3 = QWidget(self.groupBox_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(42, 30, 621, 241))
        self.gridLayout_6 = QGridLayout(self.layoutWidget3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_data_name_list_2 = QLabel(self.layoutWidget3)
        self.label_data_name_list_2.setObjectName(u"label_data_name_list_2")

        self.gridLayout_6.addWidget(self.label_data_name_list_2, 2, 3, 1, 1)

        self.listWidget_rule_data_name_2 = QListWidget(self.layoutWidget3)
        QListWidgetItem(self.listWidget_rule_data_name_2)
        self.listWidget_rule_data_name_2.setObjectName(u"listWidget_rule_data_name_2")
        self.listWidget_rule_data_name_2.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout_6.addWidget(self.listWidget_rule_data_name_2, 3, 4, 1, 1)

        self.lineEdit_module_name_list_2 = QLineEdit(self.layoutWidget3)
        self.lineEdit_module_name_list_2.setObjectName(u"lineEdit_module_name_list_2")

        self.gridLayout_6.addWidget(self.lineEdit_module_name_list_2, 2, 2, 1, 1)

        self.label_series_2 = QLabel(self.layoutWidget3)
        self.label_series_2.setObjectName(u"label_series_2")

        self.gridLayout_6.addWidget(self.label_series_2, 0, 0, 1, 1)

        self.lineEdit_data_name_list_2 = QLineEdit(self.layoutWidget3)
        self.lineEdit_data_name_list_2.setObjectName(u"lineEdit_data_name_list_2")

        self.gridLayout_6.addWidget(self.lineEdit_data_name_list_2, 2, 4, 1, 1)

        self.listWidget_rule_module_name_2 = QListWidget(self.layoutWidget3)
        QListWidgetItem(self.listWidget_rule_module_name_2)
        self.listWidget_rule_module_name_2.setObjectName(u"listWidget_rule_module_name_2")
        self.listWidget_rule_module_name_2.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout_6.addWidget(self.listWidget_rule_module_name_2, 3, 2, 1, 1)

        self.label_module_name_list_2 = QLabel(self.layoutWidget3)
        self.label_module_name_list_2.setObjectName(u"label_module_name_list_2")

        self.gridLayout_6.addWidget(self.label_module_name_list_2, 2, 0, 1, 1)

        self.comboBox_series = QComboBox(self.layoutWidget3)
        self.comboBox_series.setObjectName(u"comboBox_series")

        self.gridLayout_6.addWidget(self.comboBox_series, 0, 2, 1, 1)

        self.toolButton_reflash_list_2 = QToolButton(self.layoutWidget3)
        self.toolButton_reflash_list_2.setObjectName(u"toolButton_reflash_list_2")

        self.gridLayout_6.addWidget(self.toolButton_reflash_list_2, 0, 4, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 893, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DataQueryX", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Data Query", None))
        self.pushButton_start_data_query.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u67e5\u8be2\u6570\u636e", None))
        self.checkBox_is_get_previous_value.setText(QCoreApplication.translate("MainWindow", u"Check Previous Value", None))
        self.label_series.setText(QCoreApplication.translate("MainWindow", u"Set Series", None))
        self.label_path_mech.setText(QCoreApplication.translate("MainWindow", u"\u673a\u68b0\u53c2\u6570\u8868", None))
        self.toolButton_path_mech.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_path_geskon.setText(QCoreApplication.translate("MainWindow", u"Geskon\u6587\u4ef6", None))
        self.toolButton_path_geskon.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_path_dcm.setText(QCoreApplication.translate("MainWindow", u"DCM\u6587\u4ef6", None))
        self.toolButton_path_dcm.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_path_a2l.setText(QCoreApplication.translate("MainWindow", u"A2L\u6587\u4ef6", None))
        self.toolButton_path_a2l.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_module_name_list.setText(QCoreApplication.translate("MainWindow", u"Module Name", None))
        self.label_data_name_list.setText(QCoreApplication.translate("MainWindow", u"Data Name", None))

        __sortingEnabled = self.listWidget_rule_module_name.isSortingEnabled()
        self.listWidget_rule_module_name.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_rule_module_name.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"... ...", None));
        self.listWidget_rule_module_name.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.listWidget_rule_data_name.isSortingEnabled()
        self.listWidget_rule_data_name.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget_rule_data_name.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"... ...", None));
        self.listWidget_rule_data_name.setSortingEnabled(__sortingEnabled1)

        self.toolButton_reflash_list.setText(QCoreApplication.translate("MainWindow", u"Reflash", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
#if QT_CONFIG(tooltip)
        self.button_save.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u4fdd\u5b58\u914d\u7f6e\u6587\u4ef6</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.pushButton_check.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u68c0\u67e5\u914d\u7f6e\u6587\u4ef6</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_check.setText(QCoreApplication.translate("MainWindow", u"Check", None))
#if QT_CONFIG(tooltip)
        self.button_load.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u52a0\u8f7d\u914d\u7f6e\u6587\u4ef6</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_projectname.setText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.label_projectname_2.setText(QCoreApplication.translate("MainWindow", u"Variant Suffix", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"DoorsUserName", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*Doors Username", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"DoorsPassword", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*Doors Password", None))
#if QT_CONFIG(tooltip)
        self.checkBox_psw.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u663e\u793a\u5bc6\u7801</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_psw.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main Data Query", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Update Doors", None))
        self.pushButton_start_update_doos.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u67e5\u8be2\u6570\u636e", None))
        self.label_data_name_list_2.setText(QCoreApplication.translate("MainWindow", u"Data Name", None))

        __sortingEnabled2 = self.listWidget_rule_data_name_2.isSortingEnabled()
        self.listWidget_rule_data_name_2.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_rule_data_name_2.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"... ...", None));
        self.listWidget_rule_data_name_2.setSortingEnabled(__sortingEnabled2)

        self.label_series_2.setText(QCoreApplication.translate("MainWindow", u"Select Series", None))

        __sortingEnabled3 = self.listWidget_rule_module_name_2.isSortingEnabled()
        self.listWidget_rule_module_name_2.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidget_rule_module_name_2.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"... ...", None));
        self.listWidget_rule_module_name_2.setSortingEnabled(__sortingEnabled3)

        self.label_module_name_list_2.setText(QCoreApplication.translate("MainWindow", u"Module Name", None))
        self.toolButton_reflash_list_2.setText(QCoreApplication.translate("MainWindow", u"Reflash", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Main Update Doors", None))
    # retranslateUi

