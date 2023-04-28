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
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolButton, QWidget)
import my_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(790, 860)
        MainWindow.setMinimumSize(QSize(790, 860))
        MainWindow.setMaximumSize(QSize(790, 860))
        icon = QIcon()
        icon.addFile(u":/pic/Res/pic/app_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textEdit_show = QTextEdit(self.tab)
        self.textEdit_show.setObjectName(u"textEdit_show")
        self.textEdit_show.setGeometry(QRect(40, 630, 691, 111))
        self.textEdit_show.setReadOnly(True)
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 330, 690, 280))
        self.pushButton_start_data_query = QPushButton(self.groupBox)
        self.pushButton_start_data_query.setObjectName(u"pushButton_start_data_query")
        self.pushButton_start_data_query.setGeometry(QRect(290, 243, 101, 31))
        self.checkBox_is_get_previous_value = QCheckBox(self.groupBox)
        self.checkBox_is_get_previous_value.setObjectName(u"checkBox_is_get_previous_value")
        self.checkBox_is_get_previous_value.setGeometry(QRect(41, 201, 132, 20))
        self.label_series = QLabel(self.groupBox)
        self.label_series.setObjectName(u"label_series")
        self.label_series.setGeometry(QRect(41, 227, 52, 16))
        self.lineEdit_series = QLineEdit(self.groupBox)
        self.lineEdit_series.setObjectName(u"lineEdit_series")
        self.lineEdit_series.setGeometry(QRect(99, 227, 71, 21))
        self.lineEdit_series.setClearButtonEnabled(True)
        self.toolButton_reflash_list = QToolButton(self.groupBox)
        self.toolButton_reflash_list.setObjectName(u"toolButton_reflash_list")
        self.toolButton_reflash_list.setGeometry(QRect(30, 30, 51, 22))
        icon1 = QIcon()
        icon1.addFile(u":/icon/Res/icon/refresh_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_reflash_list.setIcon(icon1)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(32, 50, 621, 151))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_module_name_list = QLabel(self.layoutWidget)
        self.label_module_name_list.setObjectName(u"label_module_name_list")

        self.gridLayout_2.addWidget(self.label_module_name_list, 0, 0, 1, 1)

        self.lineEdit_module_name_list = QLineEdit(self.layoutWidget)
        self.lineEdit_module_name_list.setObjectName(u"lineEdit_module_name_list")
        self.lineEdit_module_name_list.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_module_name_list, 0, 1, 1, 1)

        self.label_data_name_list = QLabel(self.layoutWidget)
        self.label_data_name_list.setObjectName(u"label_data_name_list")

        self.gridLayout_2.addWidget(self.label_data_name_list, 0, 2, 1, 1)

        self.lineEdit_data_name_list = QLineEdit(self.layoutWidget)
        self.lineEdit_data_name_list.setObjectName(u"lineEdit_data_name_list")
        self.lineEdit_data_name_list.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_data_name_list, 0, 3, 1, 1)

        self.listWidget_rule_module_name = QListWidget(self.layoutWidget)
        QListWidgetItem(self.listWidget_rule_module_name)
        self.listWidget_rule_module_name.setObjectName(u"listWidget_rule_module_name")

        self.gridLayout_2.addWidget(self.listWidget_rule_module_name, 1, 1, 1, 1)

        self.listWidget_rule_data_name = QListWidget(self.layoutWidget)
        QListWidgetItem(self.listWidget_rule_data_name)
        self.listWidget_rule_data_name.setObjectName(u"listWidget_rule_data_name")

        self.gridLayout_2.addWidget(self.listWidget_rule_data_name, 1, 3, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(40, 30, 690, 280))
        self.button_save = QPushButton(self.groupBox_2)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(112, 31, 75, 24))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.button_save.setFont(font)
        self.button_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_save.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        icon2 = QIcon()
        icon2.addFile(u":/icon/Res/icon/store_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_save.setIcon(icon2)
        self.pushButton_check = QPushButton(self.groupBox_2)
        self.pushButton_check.setObjectName(u"pushButton_check")
        self.pushButton_check.setGeometry(QRect(580, 31, 75, 24))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton_check.setFont(font1)
        self.pushButton_check.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_check.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/Res/icon/check_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_check.setIcon(icon3)
        self.button_load = QPushButton(self.groupBox_2)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setGeometry(QRect(31, 31, 75, 24))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        self.button_load.setFont(font2)
        self.button_load.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_load.setMouseTracking(False)
        self.button_load.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        icon4 = QIcon()
        icon4.addFile(u":/icon/Res/icon/load_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_load.setIcon(icon4)
        self.pushButton_clear_cfg = QPushButton(self.groupBox_2)
        self.pushButton_clear_cfg.setObjectName(u"pushButton_clear_cfg")
        self.pushButton_clear_cfg.setGeometry(QRect(193, 31, 75, 24))
        self.pushButton_clear_cfg.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icon/Res/icon/delete_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_clear_cfg.setIcon(icon5)
        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(34, 70, 621, 188))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_username = QLabel(self.layoutWidget1)
        self.label_username.setObjectName(u"label_username")

        self.gridLayout.addWidget(self.label_username, 0, 0, 1, 1)

        self.lineEdit_username = QLineEdit(self.layoutWidget1)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        font3 = QFont()
        font3.setPointSize(8)
        self.lineEdit_username.setFont(font3)
        self.lineEdit_username.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_username, 0, 1, 1, 1)

        self.label_password = QLabel(self.layoutWidget1)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 0, 2, 1, 1)

        self.lineEdit_password = QLineEdit(self.layoutWidget1)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setFont(font3)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_password, 0, 3, 1, 1)

        self.checkBox_psw = QCheckBox(self.layoutWidget1)
        self.checkBox_psw.setObjectName(u"checkBox_psw")
        self.checkBox_psw.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_psw, 0, 4, 1, 1)

        self.label_projectname = QLabel(self.layoutWidget1)
        self.label_projectname.setObjectName(u"label_projectname")

        self.gridLayout.addWidget(self.label_projectname, 1, 0, 1, 1)

        self.label_projectname_2 = QLabel(self.layoutWidget1)
        self.label_projectname_2.setObjectName(u"label_projectname_2")

        self.gridLayout.addWidget(self.label_projectname_2, 2, 0, 1, 1)

        self.label_path_mech = QLabel(self.layoutWidget1)
        self.label_path_mech.setObjectName(u"label_path_mech")

        self.gridLayout.addWidget(self.label_path_mech, 3, 0, 1, 1)

        self.toolButton_path_mech = QToolButton(self.layoutWidget1)
        self.toolButton_path_mech.setObjectName(u"toolButton_path_mech")

        self.gridLayout.addWidget(self.toolButton_path_mech, 3, 4, 1, 1)

        self.label_path_geskon = QLabel(self.layoutWidget1)
        self.label_path_geskon.setObjectName(u"label_path_geskon")

        self.gridLayout.addWidget(self.label_path_geskon, 4, 0, 1, 1)

        self.toolButton_path_geskon = QToolButton(self.layoutWidget1)
        self.toolButton_path_geskon.setObjectName(u"toolButton_path_geskon")

        self.gridLayout.addWidget(self.toolButton_path_geskon, 4, 4, 1, 1)

        self.label_path_dcm = QLabel(self.layoutWidget1)
        self.label_path_dcm.setObjectName(u"label_path_dcm")

        self.gridLayout.addWidget(self.label_path_dcm, 5, 0, 1, 1)

        self.toolButton_path_dcm = QToolButton(self.layoutWidget1)
        self.toolButton_path_dcm.setObjectName(u"toolButton_path_dcm")

        self.gridLayout.addWidget(self.toolButton_path_dcm, 5, 4, 1, 1)

        self.label_path_a2l = QLabel(self.layoutWidget1)
        self.label_path_a2l.setObjectName(u"label_path_a2l")

        self.gridLayout.addWidget(self.label_path_a2l, 6, 0, 1, 1)

        self.toolButton_path_a2l = QToolButton(self.layoutWidget1)
        self.toolButton_path_a2l.setObjectName(u"toolButton_path_a2l")

        self.gridLayout.addWidget(self.toolButton_path_a2l, 6, 4, 1, 1)

        self.lineEdit_project_name = QLineEdit(self.layoutWidget1)
        self.lineEdit_project_name.setObjectName(u"lineEdit_project_name")
        self.lineEdit_project_name.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_project_name, 1, 1, 1, 3)

        self.lineEdit_data_suffix = QLineEdit(self.layoutWidget1)
        self.lineEdit_data_suffix.setObjectName(u"lineEdit_data_suffix")
        self.lineEdit_data_suffix.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_data_suffix, 2, 1, 1, 3)

        self.lineEdit_path_mech = QLineEdit(self.layoutWidget1)
        self.lineEdit_path_mech.setObjectName(u"lineEdit_path_mech")
        self.lineEdit_path_mech.setReadOnly(False)
        self.lineEdit_path_mech.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_path_mech, 3, 1, 1, 3)

        self.lineEdit_path_geskon = QLineEdit(self.layoutWidget1)
        self.lineEdit_path_geskon.setObjectName(u"lineEdit_path_geskon")
        self.lineEdit_path_geskon.setReadOnly(False)
        self.lineEdit_path_geskon.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_path_geskon, 4, 1, 1, 3)

        self.lineEdit_path_dcm = QLineEdit(self.layoutWidget1)
        self.lineEdit_path_dcm.setObjectName(u"lineEdit_path_dcm")
        self.lineEdit_path_dcm.setReadOnly(False)
        self.lineEdit_path_dcm.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_path_dcm, 5, 1, 1, 3)

        self.lineEdit_path_a2l = QLineEdit(self.layoutWidget1)
        self.lineEdit_path_a2l.setObjectName(u"lineEdit_path_a2l")
        self.lineEdit_path_a2l.setReadOnly(False)
        self.lineEdit_path_a2l.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_path_a2l, 6, 1, 1, 3)

        self.toolButton_clear_show1 = QToolButton(self.tab)
        self.toolButton_clear_show1.setObjectName(u"toolButton_clear_show1")
        self.toolButton_clear_show1.setGeometry(QRect(710, 740, 21, 22))
        icon6 = QIcon()
        icon6.addFile(u":/icon/Res/icon/eraser_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_clear_show1.setIcon(icon6)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(670, -10, 81, 61))
        self.label.setPixmap(QPixmap(u":/pic/Res/pic/bhss_logo-removebg-preview.png"))
        self.label.setScaledContents(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textEdit_show_2 = QTextEdit(self.tab_2)
        self.textEdit_show_2.setObjectName(u"textEdit_show_2")
        self.textEdit_show_2.setGeometry(QRect(40, 630, 691, 111))
        self.textEdit_show_2.setReadOnly(True)
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(40, 30, 690, 591))
        self.pushButton_start_update_doos = QPushButton(self.groupBox_3)
        self.pushButton_start_update_doos.setObjectName(u"pushButton_start_update_doos")
        self.pushButton_start_update_doos.setGeometry(QRect(290, 543, 101, 31))
        self.tableWidget_update_data = QTableWidget(self.groupBox_3)
        self.tableWidget_update_data.setObjectName(u"tableWidget_update_data")
        self.tableWidget_update_data.setEnabled(True)
        self.tableWidget_update_data.setGeometry(QRect(40, 330, 621, 192))
        self.tableWidget_update_data.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_update_data.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_update_data.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_update_data.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.layoutWidget2 = QWidget(self.groupBox_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(41, 300, 621, 26))
        self.gridLayout_7 = QGridLayout(self.layoutWidget2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.toolButton_update_data_table = QToolButton(self.layoutWidget2)
        self.toolButton_update_data_table.setObjectName(u"toolButton_update_data_table")
        self.toolButton_update_data_table.setIcon(icon1)

        self.gridLayout_7.addWidget(self.toolButton_update_data_table, 0, 0, 1, 1)

        self.label_value_current = QLabel(self.layoutWidget2)
        self.label_value_current.setObjectName(u"label_value_current")

        self.gridLayout_7.addWidget(self.label_value_current, 0, 1, 1, 1)

        self.lineEdit_value_current = QLineEdit(self.layoutWidget2)
        self.lineEdit_value_current.setObjectName(u"lineEdit_value_current")
        self.lineEdit_value_current.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_value_current, 0, 2, 1, 1)

        self.label_value_changed = QLabel(self.layoutWidget2)
        self.label_value_changed.setObjectName(u"label_value_changed")

        self.gridLayout_7.addWidget(self.label_value_changed, 0, 3, 1, 1)

        self.lineEdit_value_changed = QLineEdit(self.layoutWidget2)
        self.lineEdit_value_changed.setObjectName(u"lineEdit_value_changed")
        self.lineEdit_value_changed.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.lineEdit_value_changed, 0, 4, 1, 1)

        self.pushButton_changedata_user = QPushButton(self.layoutWidget2)
        self.pushButton_changedata_user.setObjectName(u"pushButton_changedata_user")
        icon7 = QIcon()
        icon7.addFile(u":/icon/Res/icon/change_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_changedata_user.setIcon(icon7)

        self.gridLayout_7.addWidget(self.pushButton_changedata_user, 0, 5, 1, 1)

        self.pushButton_changedata_delete = QPushButton(self.layoutWidget2)
        self.pushButton_changedata_delete.setObjectName(u"pushButton_changedata_delete")
        self.pushButton_changedata_delete.setIcon(icon5)

        self.gridLayout_7.addWidget(self.pushButton_changedata_delete, 0, 6, 1, 1)

        self.pushButton_export_data = QPushButton(self.layoutWidget2)
        self.pushButton_export_data.setObjectName(u"pushButton_export_data")
        icon8 = QIcon()
        icon8.addFile(u":/icon/Res/icon/export_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_export_data.setIcon(icon8)

        self.gridLayout_7.addWidget(self.pushButton_export_data, 0, 7, 1, 1)

        self.layoutWidget3 = QWidget(self.groupBox_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(45, 32, 611, 248))
        self.gridLayout_3 = QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_series_2 = QLabel(self.layoutWidget3)
        self.label_series_2.setObjectName(u"label_series_2")

        self.gridLayout_3.addWidget(self.label_series_2, 0, 0, 1, 1)

        self.label_module_name_list_2 = QLabel(self.layoutWidget3)
        self.label_module_name_list_2.setObjectName(u"label_module_name_list_2")

        self.gridLayout_3.addWidget(self.label_module_name_list_2, 1, 0, 1, 1)

        self.lineEdit_module_name_list_2 = QLineEdit(self.layoutWidget3)
        self.lineEdit_module_name_list_2.setObjectName(u"lineEdit_module_name_list_2")
        self.lineEdit_module_name_list_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_module_name_list_2, 1, 1, 1, 1)

        self.label_data_name_list_2 = QLabel(self.layoutWidget3)
        self.label_data_name_list_2.setObjectName(u"label_data_name_list_2")

        self.gridLayout_3.addWidget(self.label_data_name_list_2, 1, 3, 1, 1)

        self.lineEdit_data_name_list_2 = QLineEdit(self.layoutWidget3)
        self.lineEdit_data_name_list_2.setObjectName(u"lineEdit_data_name_list_2")
        self.lineEdit_data_name_list_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_data_name_list_2, 1, 4, 1, 1)

        self.listWidget_rule_module_name_2 = QListWidget(self.layoutWidget3)
        QListWidgetItem(self.listWidget_rule_module_name_2)
        self.listWidget_rule_module_name_2.setObjectName(u"listWidget_rule_module_name_2")
        self.listWidget_rule_module_name_2.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout_3.addWidget(self.listWidget_rule_module_name_2, 2, 1, 1, 2)

        self.listWidget_rule_data_name_2 = QListWidget(self.layoutWidget3)
        QListWidgetItem(self.listWidget_rule_data_name_2)
        self.listWidget_rule_data_name_2.setObjectName(u"listWidget_rule_data_name_2")
        self.listWidget_rule_data_name_2.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout_3.addWidget(self.listWidget_rule_data_name_2, 2, 4, 1, 1)

        self.comboBox_series = QComboBox(self.layoutWidget3)
        self.comboBox_series.setObjectName(u"comboBox_series")

        self.gridLayout_3.addWidget(self.comboBox_series, 0, 1, 1, 1)

        self.toolButton_reflash_list_2 = QToolButton(self.layoutWidget3)
        self.toolButton_reflash_list_2.setObjectName(u"toolButton_reflash_list_2")
        self.toolButton_reflash_list_2.setIcon(icon1)

        self.gridLayout_3.addWidget(self.toolButton_reflash_list_2, 0, 3, 1, 1)

        self.checkBox_is_bypass_ispnequal = QCheckBox(self.groupBox_3)
        self.checkBox_is_bypass_ispnequal.setObjectName(u"checkBox_is_bypass_ispnequal")
        self.checkBox_is_bypass_ispnequal.setGeometry(QRect(40, 530, 132, 20))
        self.checkBox_is_bypass_ispnequal.setChecked(False)
        self.toolButton_clear_show2 = QToolButton(self.tab_2)
        self.toolButton_clear_show2.setObjectName(u"toolButton_clear_show2")
        self.toolButton_clear_show2.setGeometry(QRect(710, 740, 21, 22))
        self.toolButton_clear_show2.setIcon(icon6)
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(670, -10, 81, 61))
        self.label_2.setPixmap(QPixmap(u":/pic/Res/pic/bhss_logo-removebg-preview.png"))
        self.label_2.setScaledContents(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(670, -10, 81, 61))
        self.label_3.setPixmap(QPixmap(u":/pic/Res/pic/bhss_logo-removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 10, 151, 141))
        self.label_4.setPixmap(QPixmap(u":/pic/Res/pic/app_logo_big.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 140, 81, 21))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setBold(True)
        self.label_5.setFont(font4)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 750, 431, 16))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(8)
        self.label_8.setFont(font5)
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(240, 730, 266, 18))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.label_6)

        self.tabWidget.addTab(self.widget, "")

        self.gridLayout_5.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 790, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DataQueryX", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Data Query", None))
        self.pushButton_start_data_query.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u67e5\u8be2\u6570\u636e", None))
        self.checkBox_is_get_previous_value.setText(QCoreApplication.translate("MainWindow", u"Check Previous Value", None))
        self.label_series.setText(QCoreApplication.translate("MainWindow", u"Set Series", None))
        self.lineEdit_series.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NS", None))
        self.toolButton_reflash_list.setText(QCoreApplication.translate("MainWindow", u"Reflash", None))
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
        self.pushButton_clear_cfg.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"DoorsUserName", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"* Doors Username", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"DoorsPassword", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"* Doors Password", None))
#if QT_CONFIG(tooltip)
        self.checkBox_psw.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u663e\u793a\u5bc6\u7801</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_psw.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_projectname.setText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.label_projectname_2.setText(QCoreApplication.translate("MainWindow", u"Variant Suffix", None))
        self.label_path_mech.setText(QCoreApplication.translate("MainWindow", u"\u673a\u68b0\u53c2\u6570\u8868", None))
        self.toolButton_path_mech.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_path_geskon.setText(QCoreApplication.translate("MainWindow", u"Geskon\u6587\u4ef6", None))
        self.toolButton_path_geskon.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_path_dcm.setText(QCoreApplication.translate("MainWindow", u"DCM\u6587\u4ef6", None))
        self.toolButton_path_dcm.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_path_a2l.setText(QCoreApplication.translate("MainWindow", u"A2L\u6587\u4ef6", None))
        self.toolButton_path_a2l.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_project_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"* Input your project name", None))
        self.lineEdit_data_suffix.setText("")
        self.lineEdit_data_suffix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input the suffix for your data module in Doors", None))
        self.lineEdit_path_mech.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select your MechanicalDataSheet", None))
        self.lineEdit_path_geskon.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select your Geskon file", None))
        self.lineEdit_path_dcm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select your DCM file", None))
        self.lineEdit_path_a2l.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select your A2L file", None))
        self.toolButton_clear_show1.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Data Query", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Update Doors", None))
        self.pushButton_start_update_doos.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u66f4\u65b0Doors", None))
        self.toolButton_update_data_table.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_value_current.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_value_changed.setText(QCoreApplication.translate("MainWindow", u"Changed Value", None))
        self.lineEdit_value_changed.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom value", None))
        self.pushButton_changedata_user.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.pushButton_changedata_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_export_data.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_series_2.setText(QCoreApplication.translate("MainWindow", u"Select Series", None))
        self.label_module_name_list_2.setText(QCoreApplication.translate("MainWindow", u"Module Name", None))
        self.label_data_name_list_2.setText(QCoreApplication.translate("MainWindow", u"Data Name", None))

        __sortingEnabled2 = self.listWidget_rule_module_name_2.isSortingEnabled()
        self.listWidget_rule_module_name_2.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_rule_module_name_2.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"... ...", None));
        self.listWidget_rule_module_name_2.setSortingEnabled(__sortingEnabled2)


        __sortingEnabled3 = self.listWidget_rule_data_name_2.isSortingEnabled()
        self.listWidget_rule_data_name_2.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidget_rule_data_name_2.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"... ...", None));
        self.listWidget_rule_data_name_2.setSortingEnabled(__sortingEnabled3)

        self.toolButton_reflash_list_2.setText(QCoreApplication.translate("MainWindow", u"Reflash", None))
        self.checkBox_is_bypass_ispnequal.setText(QCoreApplication.translate("MainWindow", u"Bypass P/N Equal", None))
        self.toolButton_clear_show2.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Update Doors", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2023 BOSCH HUAYU STEERING SYSTEMS CO., LTD. ALL Rights Reserved.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<a href=\"mailto:zhengli.yang@boschhuayu-steering.com\">zhengli.yang@boschhuayu-steering.com</a>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

