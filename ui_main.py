# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.frameHome_content = QFrame(self.page_home)
        self.frameHome_content.setObjectName(u"frameHome_content")
        self.horizontalLayout_13 = QHBoxLayout(self.frameHome_content)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(1, 1, 1, 1)
        self.frame_xevao = QFrame(self.frameHome_content)
        self.frame_xevao.setObjectName(u"frame_xevao")
        self.verticalLayout_14 = QVBoxLayout(self.frame_xevao)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(1, 1, 1, 1)
        self.frame_monitor = QFrame(self.frame_xevao)
        self.frame_monitor.setObjectName(u"frame_monitor")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.frame_monitor.sizePolicy().hasHeightForWidth())
        self.frame_monitor.setSizePolicy(sizePolicy5)
        self.frame_monitor.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_16 = QVBoxLayout(self.frame_monitor)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(1, 1, 1, 1)
        self.monitor = QLabel(self.frame_monitor)
        self.monitor.setObjectName(u"monitor")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.monitor.sizePolicy().hasHeightForWidth())
        self.monitor.setSizePolicy(sizePolicy5)
        self.monitor.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.monitor.setGeometry(0,0,440,440)
        self.verticalLayout_monitor = QVBoxLayout(self.monitor)
        self.verticalLayout_monitor.setObjectName(u"verticalLayout_monitor")
        self.verticalLayout_monitor.setContentsMargins(1, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_monitor)

        self.frame_widgets = QFrame(self.frame_xevao)
        self.frame_widgets.setObjectName(u"frame_widgets")
        self.verticalLayout_17 = QVBoxLayout(self.frame_widgets)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalFrame = QFrame(self.frame_widgets)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(1, 1, 1, 1)
        self.verticalFrame_2 = QFrame(self.horizontalFrame)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalLayout_13 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btnChonAnh = QPushButton(self.verticalFrame_2)
        self.btnChonAnh.setObjectName(u"btnChonAnh")
        self.btnChonAnh.setMinimumSize(QSize(150, 30))
        self.btnChonAnh.setFont(font4)
        self.btnChonAnh.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-image-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnChonAnh.setIcon(icon3)

        self.verticalLayout_13.addWidget(self.btnChonAnh)


        self.horizontalLayout_14.addWidget(self.verticalFrame_2)

        self.verticalFrame = QFrame(self.horizontalFrame)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_22 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.btnXuLy = QPushButton(self.verticalFrame)
        self.btnXuLy.setObjectName(u"btnXuLy")
        self.btnXuLy.setMinimumSize(QSize(150, 30))
        self.btnXuLy.setFont(font4)
        self.btnXuLy.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-ethernet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnXuLy.setIcon(icon4)

        self.verticalLayout_22.addWidget(self.btnXuLy)


        self.horizontalLayout_14.addWidget(self.verticalFrame)


        self.gridLayout_3.addWidget(self.horizontalFrame, 0, 0, 1, 1)

        self.verticalFrame1 = QFrame(self.frame_widgets)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalFrame1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_24 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(1, 1, 1, 1)
        self.txtChuSo = QLineEdit(self.verticalFrame1)
        self.txtChuSo.setObjectName(u"txtChuSo")
        self.txtChuSo.setMinimumSize(QSize(420, 36))
        self.txtChuSo.setMaximumSize(QSize(400, 36))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.txtChuSo.setFont(font5)
        self.txtChuSo.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtChuSo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.txtChuSo, 0, Qt.AlignHCenter)


        self.gridLayout_3.addWidget(self.verticalFrame1, 1, 0, 1, 1)

        self.verticalFrame2 = QFrame(self.frame_widgets)
        self.verticalFrame2.setObjectName(u"verticalFrame2")
        self.verticalFrame2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_20 = QVBoxLayout(self.verticalFrame2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(1, 1, 1, 1)
        self.horizontalFrame1 = QFrame(self.verticalFrame2)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(1, 1, 1, 1)
        self.verticalFrame_21 = QFrame(self.horizontalFrame1)
        self.verticalFrame_21.setObjectName(u"verticalFrame_21")
        self.verticalLayout_23 = QVBoxLayout(self.verticalFrame_21)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.btnTachChu = QPushButton(self.verticalFrame_21)
        self.btnTachChu.setObjectName(u"btnTachChu")
        self.btnTachChu.setMinimumSize(QSize(150, 30))
        self.btnTachChu.setFont(font4)
        self.btnTachChu.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-wrap-text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnTachChu.setIcon(icon5)

        self.verticalLayout_23.addWidget(self.btnTachChu)


        self.horizontalLayout_16.addWidget(self.verticalFrame_21)

        self.verticalFrame3 = QFrame(self.horizontalFrame1)
        self.verticalFrame3.setObjectName(u"verticalFrame3")
        self.verticalLayout_25 = QVBoxLayout(self.verticalFrame3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.btnLuu = QPushButton(self.verticalFrame3)
        self.btnLuu.setObjectName(u"btnLuu")
        self.btnLuu.setMinimumSize(QSize(150, 30))
        self.btnLuu.setFont(font4)
        self.btnLuu.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLuu.setIcon(icon6)

        self.verticalLayout_25.addWidget(self.btnLuu)


        self.horizontalLayout_16.addWidget(self.verticalFrame3)


        self.verticalLayout_20.addWidget(self.horizontalFrame1)


        self.gridLayout_3.addWidget(self.verticalFrame2, 2, 0, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout_3)


        self.verticalLayout_14.addWidget(self.frame_widgets)


        self.horizontalLayout_13.addWidget(self.frame_xevao)

        self.frame_xera = QFrame(self.frameHome_content)
        self.frame_xera.setObjectName(u"frame_xera")
        self.verticalLayout_12 = QVBoxLayout(self.frame_xera)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.frame_monitor_2 = QFrame(self.frame_xera)
        self.frame_monitor_2.setObjectName(u"frame_monitor_2")
        sizePolicy5.setHeightForWidth(self.frame_monitor_2.sizePolicy().hasHeightForWidth())
        self.frame_monitor_2.setSizePolicy(sizePolicy5)
        self.frame_monitor_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_30 = QVBoxLayout(self.frame_monitor_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(1, 1, 1, 1)
        self.monitor2 = QLabel(self.frame_monitor_2)
        self.monitor2.setObjectName(u"monitor2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.monitor2.sizePolicy().hasHeightForWidth())
        self.monitor2.setSizePolicy(sizePolicy5)
        self.monitor2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.monitor2.setGeometry(0, 0, 440, 440)
        self.verticalLayout_monitor2 = QVBoxLayout(self.monitor2)
        self.verticalLayout_monitor2.setObjectName(u"verticalLayout_monitor2")
        self.verticalLayout_monitor2.setContentsMargins(1, 1, 1, 1)

        self.verticalLayout_12.addWidget(self.frame_monitor_2)

        self.frame_widgets_2 = QFrame(self.frame_xera)
        self.frame_widgets_2.setObjectName(u"frame_widgets_2")
        self.verticalLayout_18 = QVBoxLayout(self.frame_widgets_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalFrame_2 = QFrame(self.frame_widgets_2)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(1, 1, 1, 1)
        self.verticalFrame_3 = QFrame(self.horizontalFrame_2)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalLayout_19 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.btnChonAnh_2 = QPushButton(self.verticalFrame_3)
        self.btnChonAnh_2.setObjectName(u"btnChonAnh_2")
        self.btnChonAnh_2.setMinimumSize(QSize(150, 30))
        self.btnChonAnh_2.setFont(font4)
        self.btnChonAnh_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btnChonAnh_2.setIcon(icon3)

        self.verticalLayout_19.addWidget(self.btnChonAnh_2)


        self.horizontalLayout_15.addWidget(self.verticalFrame_3)

        self.verticalFrame_4 = QFrame(self.horizontalFrame_2)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalLayout_26 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.btnXuLy_2 = QPushButton(self.verticalFrame_4)
        self.btnXuLy_2.setObjectName(u"btnXuLy_2")
        self.btnXuLy_2.setMinimumSize(QSize(150, 30))
        self.btnXuLy_2.setFont(font4)
        self.btnXuLy_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btnXuLy_2.setIcon(icon4)

        self.verticalLayout_26.addWidget(self.btnXuLy_2)


        self.horizontalLayout_15.addWidget(self.verticalFrame_4)


        self.gridLayout_4.addWidget(self.horizontalFrame_2, 0, 0, 1, 1)

        self.verticalFrame_5 = QFrame(self.frame_widgets_2)
        self.verticalFrame_5.setObjectName(u"verticalFrame_5")
        self.verticalFrame_5.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_27 = QVBoxLayout(self.verticalFrame_5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(1, 1, 1, 1)
        self.txtChuSo_2 = QLineEdit(self.verticalFrame_5)
        self.txtChuSo_2.setObjectName(u"txtChuSo_2")
        self.txtChuSo_2.setMinimumSize(QSize(420, 36))
        self.txtChuSo_2.setMaximumSize(QSize(400, 36))
        self.txtChuSo_2.setFont(font5)
        self.txtChuSo_2.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtChuSo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.txtChuSo_2, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.verticalFrame_5, 1, 0, 1, 1)

        self.verticalFrame_6 = QFrame(self.frame_widgets_2)
        self.verticalFrame_6.setObjectName(u"verticalFrame_6")
        self.verticalFrame_6.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_21 = QVBoxLayout(self.verticalFrame_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.horizontalFrame_3 = QFrame(self.verticalFrame_6)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.verticalFrame_7 = QFrame(self.horizontalFrame_3)
        self.verticalFrame_7.setObjectName(u"verticalFrame_7")
        self.verticalLayout_28 = QVBoxLayout(self.verticalFrame_7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.btnTachChu_2 = QPushButton(self.verticalFrame_7)
        self.btnTachChu_2.setObjectName(u"btnTachChu_2")
        self.btnTachChu_2.setMinimumSize(QSize(150, 30))
        self.btnTachChu_2.setFont(font4)
        self.btnTachChu_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btnTachChu_2.setIcon(icon5)

        self.verticalLayout_28.addWidget(self.btnTachChu_2)


        self.horizontalLayout_17.addWidget(self.verticalFrame_7)

        self.verticalFrame_8 = QFrame(self.horizontalFrame_3)
        self.verticalFrame_8.setObjectName(u"verticalFrame_8")
        self.verticalLayout_29 = QVBoxLayout(self.verticalFrame_8)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.btnLuu_2 = QPushButton(self.verticalFrame_8)
        self.btnLuu_2.setObjectName(u"btnLuu_2")
        self.btnLuu_2.setMinimumSize(QSize(150, 30))
        self.btnLuu_2.setFont(font4)
        self.btnLuu_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btnLuu_2.setIcon(icon6)

        self.verticalLayout_29.addWidget(self.btnLuu_2)


        self.horizontalLayout_17.addWidget(self.verticalFrame_8)


        self.verticalLayout_21.addWidget(self.horizontalFrame_3)


        self.gridLayout_4.addWidget(self.verticalFrame_6, 2, 0, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_4)


        self.verticalLayout_12.addWidget(self.frame_widgets_2)


        self.horizontalLayout_13.addWidget(self.frame_xera)


        self.verticalLayout_10.addWidget(self.frameHome_content)

        self.stackedWidget.addWidget(self.page_home)
        self.page_find = QWidget()
        self.page_find.setObjectName(u"page_find")
        self.verticalLayout_34 = QVBoxLayout(self.page_find)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(1, 1, 1, 1)
        self.findFrame = QFrame(self.page_find)
        self.findFrame.setObjectName(u"findFrame")
        self.verticalLayout_33 = QVBoxLayout(self.findFrame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(1, 1, 1, 1)
        self.frame_input = QFrame(self.findFrame)
        self.frame_input.setObjectName(u"frame_input")
        self.horizontalLayout_18 = QHBoxLayout(self.frame_input)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(1, 1, 1, 1)
        self.frame_findName = QFrame(self.frame_input)
        self.frame_findName.setObjectName(u"frame_findName")
        self.frame_findName.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_38 = QVBoxLayout(self.frame_findName)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(1, 1, 1, 1)
        self.frame_findNameTitle = QFrame(self.frame_findName)
        self.frame_findNameTitle.setObjectName(u"frame_findNameTitle")
        self.verticalLayout_39 = QVBoxLayout(self.frame_findNameTitle)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.txtfindNameTitle = QLabel(self.frame_findNameTitle)
        self.txtfindNameTitle.setObjectName(u"txtfindNameTitle")
        self.txtfindNameTitle.setFont(font1)
        self.txtfindNameTitle.setStyleSheet(u"")

        self.verticalLayout_39.addWidget(self.txtfindNameTitle)


        self.verticalLayout_38.addWidget(self.frame_findNameTitle)

        self.frame_findNameWidgets = QFrame(self.frame_findName)
        self.frame_findNameWidgets.setObjectName(u"frame_findNameWidgets")
        sizePolicy5.setHeightForWidth(self.frame_findNameWidgets.sizePolicy().hasHeightForWidth())
        self.frame_findNameWidgets.setSizePolicy(sizePolicy5)
        self.verticalLayout_40 = QVBoxLayout(self.frame_findNameWidgets)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(1, 1, 1, 1)
        self.findInputFrame = QFrame(self.frame_findNameWidgets)
        self.findInputFrame.setObjectName(u"findInputFrame")
        sizePolicy5.setHeightForWidth(self.findInputFrame.sizePolicy().hasHeightForWidth())
        self.findInputFrame.setSizePolicy(sizePolicy5)
        self.verticalLayout_41 = QVBoxLayout(self.findInputFrame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(1, 1, 1, 1)
        self.txtfindName = QLineEdit(self.findInputFrame)
        self.txtfindName.setObjectName(u"txtfindName")
        self.txtfindName.setMinimumSize(QSize(434, 80))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(16)
        self.txtfindName.setFont(font6)
        self.txtfindName.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtfindName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.txtfindName, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_40.addWidget(self.findInputFrame)

        self.findButtonFrame = QFrame(self.frame_findNameWidgets)
        self.findButtonFrame.setObjectName(u"findButtonFrame")
        self.horizontalLayout_19 = QHBoxLayout(self.findButtonFrame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(1, 1, 1, 1)
        self.findButtonFrame2 = QFrame(self.findButtonFrame)
        self.findButtonFrame2.setObjectName(u"findButtonFrame2")
        self.verticalLayout_42 = QVBoxLayout(self.findButtonFrame2)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.btnTimKiem = QPushButton(self.findButtonFrame2)
        self.btnTimKiem.setObjectName(u"btnTimKiem")
        self.btnTimKiem.setMinimumSize(QSize(150, 30))
        self.btnTimKiem.setFont(font4)
        self.btnTimKiem.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnTimKiem.setIcon(icon7)

        self.verticalLayout_42.addWidget(self.btnTimKiem)


        self.horizontalLayout_19.addWidget(self.findButtonFrame2)

        self.findButtonFrame1 = QFrame(self.findButtonFrame)
        self.findButtonFrame1.setObjectName(u"findButtonFrame1")
        self.verticalLayout_43 = QVBoxLayout(self.findButtonFrame1)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.btnXoaTrang = QPushButton(self.findButtonFrame1)
        self.btnXoaTrang.setObjectName(u"btnXoaTrang")
        self.btnXoaTrang.setMinimumSize(QSize(150, 30))
        self.btnXoaTrang.setFont(font4)
        self.btnXoaTrang.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnXoaTrang.setIcon(icon8)

        self.verticalLayout_43.addWidget(self.btnXoaTrang)


        self.horizontalLayout_19.addWidget(self.findButtonFrame1)


        self.verticalLayout_40.addWidget(self.findButtonFrame)


        self.verticalLayout_38.addWidget(self.frame_findNameWidgets)


        self.horizontalLayout_18.addWidget(self.frame_findName)

        self.frame_findNum = QFrame(self.frame_input)
        self.frame_findNum.setObjectName(u"frame_findNum")
        self.frame_findNum.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_37 = QVBoxLayout(self.frame_findNum)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(1, 1, 1, 1)
        self.frame_findNumTitle = QFrame(self.frame_findNum)
        self.frame_findNumTitle.setObjectName(u"frame_findNumTitle")
        self.verticalLayout_48 = QVBoxLayout(self.frame_findNumTitle)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(9, 9, 9, 9)
        self.txtfindNumTitle = QLabel(self.frame_findNumTitle)
        self.txtfindNumTitle.setObjectName(u"txtfindNumTitle")
        self.txtfindNumTitle.setFont(font1)
        self.txtfindNumTitle.setStyleSheet(u"")

        self.verticalLayout_48.addWidget(self.txtfindNumTitle)


        self.verticalLayout_37.addWidget(self.frame_findNumTitle)

        self.frame_findNameWidgets_2 = QFrame(self.frame_findNum)
        self.frame_findNameWidgets_2.setObjectName(u"frame_findNameWidgets_2")
        sizePolicy5.setHeightForWidth(self.frame_findNameWidgets_2.sizePolicy().hasHeightForWidth())
        self.frame_findNameWidgets_2.setSizePolicy(sizePolicy5)
        self.verticalLayout_44 = QVBoxLayout(self.frame_findNameWidgets_2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(1, 1, 1, 1)
        self.findInputFrame_2 = QFrame(self.frame_findNameWidgets_2)
        self.findInputFrame_2.setObjectName(u"findInputFrame_2")
        sizePolicy5.setHeightForWidth(self.findInputFrame_2.sizePolicy().hasHeightForWidth())
        self.findInputFrame_2.setSizePolicy(sizePolicy5)
        self.verticalLayout_45 = QVBoxLayout(self.findInputFrame_2)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(1, 1, 1, 1)
        self.txtfindNum = QLineEdit(self.findInputFrame_2)
        self.txtfindNum.setObjectName(u"txtfindNum")
        self.txtfindNum.setMinimumSize(QSize(434, 80))
        self.txtfindNum.setFont(font6)
        self.txtfindNum.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtfindNum.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.txtfindNum, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_44.addWidget(self.findInputFrame_2)

        self.findButtonFrame_2 = QFrame(self.frame_findNameWidgets_2)
        self.findButtonFrame_2.setObjectName(u"findButtonFrame_2")
        self.horizontalLayout_20 = QHBoxLayout(self.findButtonFrame_2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.findButtonFrame2_2 = QFrame(self.findButtonFrame_2)
        self.findButtonFrame2_2.setObjectName(u"findButtonFrame2_2")
        self.verticalLayout_46 = QVBoxLayout(self.findButtonFrame2_2)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(1, 1, 1, 1)
        self.btnTimKiem_2 = QPushButton(self.findButtonFrame2_2)
        self.btnTimKiem_2.setObjectName(u"btnTimKiem_2")
        self.btnTimKiem_2.setMinimumSize(QSize(150, 30))
        self.btnTimKiem_2.setFont(font4)
        self.btnTimKiem_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btnTimKiem_2.setIcon(icon7)

        self.verticalLayout_46.addWidget(self.btnTimKiem_2)


        self.horizontalLayout_20.addWidget(self.findButtonFrame2_2)

        self.findButtonFrame1_2 = QFrame(self.findButtonFrame_2)
        self.findButtonFrame1_2.setObjectName(u"findButtonFrame1_2")
        self.verticalLayout_47 = QVBoxLayout(self.findButtonFrame1_2)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(1, 1, 1, 1)
        self.btnXoaTrang_2 = QPushButton(self.findButtonFrame1_2)
        self.btnXoaTrang_2.setObjectName(u"btnXoaTrang_2")
        self.btnXoaTrang_2.setMinimumSize(QSize(150, 30))
        self.btnXoaTrang_2.setFont(font4)
        self.btnXoaTrang_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btnXoaTrang_2.setIcon(icon8)

        self.verticalLayout_47.addWidget(self.btnXoaTrang_2)


        self.horizontalLayout_20.addWidget(self.findButtonFrame1_2)


        self.verticalLayout_44.addWidget(self.findButtonFrame_2)


        self.verticalLayout_37.addWidget(self.frame_findNameWidgets_2)


        self.horizontalLayout_18.addWidget(self.frame_findNum)


        self.verticalLayout_33.addWidget(self.frame_input)

        self.frame_display = QFrame(self.findFrame)
        self.frame_display.setObjectName(u"frame_display")
        self.frame_display.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_36 = QVBoxLayout(self.frame_display)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_displayTitle = QFrame(self.frame_display)
        self.frame_displayTitle.setObjectName(u"frame_displayTitle")
        self.frame_displayTitle.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_49 = QVBoxLayout(self.frame_displayTitle)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.txtframeDisplayTitle = QLabel(self.frame_displayTitle)
        self.txtframeDisplayTitle.setObjectName(u"txtframeDisplayTitle")
        self.txtframeDisplayTitle.setFont(font1)
        self.txtframeDisplayTitle.setStyleSheet(u"")

        self.verticalLayout_49.addWidget(self.txtframeDisplayTitle)


        self.verticalLayout_36.addWidget(self.frame_displayTitle)

        self.frame_displayWidget = QFrame(self.frame_display)
        self.frame_displayWidget.setObjectName(u"frame_displayWidget")
        sizePolicy5.setHeightForWidth(self.frame_displayWidget.sizePolicy().hasHeightForWidth())
        self.frame_displayWidget.setSizePolicy(sizePolicy5)
        self.frame_displayWidget.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(26, 29, 36);")
        self.horizontalLayout_22 = QHBoxLayout(self.frame_displayWidget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_displayWidgetLeft = QFrame(self.frame_displayWidget)
        self.frame_displayWidgetLeft.setObjectName(u"frame_displayWidgetLeft")
        self.verticalLayout_51 = QVBoxLayout(self.frame_displayWidgetLeft)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(1, 1, 1, 1)
        self.txtQBienSo = QLineEdit(self.frame_displayWidgetLeft)
        self.txtQBienSo.setObjectName(u"txtQBienSo")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.txtQBienSo.sizePolicy().hasHeightForWidth())
        self.txtQBienSo.setSizePolicy(sizePolicy6)
        self.txtQBienSo.setMinimumSize(QSize(130, 35))
        self.txtQBienSo.setMaximumSize(QSize(130, 35))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.txtQBienSo.setFont(font7)
        self.txtQBienSo.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQBienSo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQBienSo.setReadOnly(True)

        self.verticalLayout_51.addWidget(self.txtQBienSo)

        self.txtQThoiGianVao = QLineEdit(self.frame_displayWidgetLeft)
        self.txtQThoiGianVao.setObjectName(u"txtQThoiGianVao")
        sizePolicy6.setHeightForWidth(self.txtQThoiGianVao.sizePolicy().hasHeightForWidth())
        self.txtQThoiGianVao.setSizePolicy(sizePolicy6)
        self.txtQThoiGianVao.setMinimumSize(QSize(130, 35))
        self.txtQThoiGianVao.setMaximumSize(QSize(130, 35))
        self.txtQThoiGianVao.setFont(font7)
        self.txtQThoiGianVao.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQThoiGianVao.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQThoiGianVao.setReadOnly(True)

        self.verticalLayout_51.addWidget(self.txtQThoiGianVao)

        self.txtQThoiGianRa = QLineEdit(self.frame_displayWidgetLeft)
        self.txtQThoiGianRa.setObjectName(u"txtQThoiGianRa")
        sizePolicy6.setHeightForWidth(self.txtQThoiGianRa.sizePolicy().hasHeightForWidth())
        self.txtQThoiGianRa.setSizePolicy(sizePolicy6)
        self.txtQThoiGianRa.setMinimumSize(QSize(130, 35))
        self.txtQThoiGianRa.setMaximumSize(QSize(130, 35))
        self.txtQThoiGianRa.setFont(font7)
        self.txtQThoiGianRa.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQThoiGianRa.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQThoiGianRa.setReadOnly(True)

        self.verticalLayout_51.addWidget(self.txtQThoiGianRa)


        self.horizontalLayout_22.addWidget(self.frame_displayWidgetLeft)

        self.frame_displayWidgetRight = QFrame(self.frame_displayWidget)
        self.frame_displayWidgetRight.setObjectName(u"frame_displayWidgetRight")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_displayWidgetRight.sizePolicy().hasHeightForWidth())
        self.frame_displayWidgetRight.setSizePolicy(sizePolicy7)
        self.verticalLayout_50 = QVBoxLayout(self.frame_displayWidgetRight)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(1, 1, 1, 1)
        self.txtBienSo = QLineEdit(self.frame_displayWidgetRight)
        self.txtBienSo.setObjectName(u"txtBienSo")
        self.txtBienSo.setMinimumSize(QSize(434, 35))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(14)
        self.txtBienSo.setFont(font8)
        self.txtBienSo.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtBienSo.setAlignment(Qt.AlignCenter)
        self.txtBienSo.setReadOnly(True)

        self.verticalLayout_50.addWidget(self.txtBienSo)

        self.txtThoiGianVao = QLineEdit(self.frame_displayWidgetRight)
        self.txtThoiGianVao.setObjectName(u"txtThoiGianVao")
        self.txtThoiGianVao.setMinimumSize(QSize(434, 35))
        self.txtThoiGianVao.setFont(font8)
        self.txtThoiGianVao.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtThoiGianVao.setAlignment(Qt.AlignCenter)
        self.txtThoiGianVao.setReadOnly(True)

        self.verticalLayout_50.addWidget(self.txtThoiGianVao)

        self.txtThoiGianRa = QLineEdit(self.frame_displayWidgetRight)
        self.txtThoiGianRa.setObjectName(u"txtThoiGianRa")
        self.txtThoiGianRa.setMinimumSize(QSize(434, 35))
        self.txtThoiGianRa.setFont(font8)
        self.txtThoiGianRa.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtThoiGianRa.setAlignment(Qt.AlignCenter)
        self.txtThoiGianRa.setReadOnly(True)

        self.verticalLayout_50.addWidget(self.txtThoiGianRa)


        self.horizontalLayout_22.addWidget(self.frame_displayWidgetRight)


        self.verticalLayout_36.addWidget(self.frame_displayWidget)


        self.verticalLayout_33.addWidget(self.frame_display)

        self.frame_history = QFrame(self.findFrame)
        self.frame_history.setObjectName(u"frame_history")
        self.frame_history.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_35 = QVBoxLayout(self.frame_history)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_historyTitle = QFrame(self.frame_history)
        self.frame_historyTitle.setObjectName(u"frame_historyTitle")
        self.frame_historyTitle.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_52 = QVBoxLayout(self.frame_historyTitle)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.txtframeHistoryTitle = QLabel(self.frame_historyTitle)
        self.txtframeHistoryTitle.setObjectName(u"txtframeHistoryTitle")
        self.txtframeHistoryTitle.setFont(font1)
        self.txtframeHistoryTitle.setStyleSheet(u"")

        self.verticalLayout_52.addWidget(self.txtframeHistoryTitle)


        self.verticalLayout_35.addWidget(self.frame_historyTitle)

        self.frame_historyWidget = QFrame(self.frame_history)
        self.frame_historyWidget.setObjectName(u"frame_historyWidget")
        sizePolicy5.setHeightForWidth(self.frame_historyWidget.sizePolicy().hasHeightForWidth())
        self.frame_historyWidget.setSizePolicy(sizePolicy5)
        self.frame_historyWidget.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(26, 29, 36);")
        self.verticalLayout_53 = QVBoxLayout(self.frame_historyWidget)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(1, 1, 1, 1)
        self.txtLichSu1 = QLineEdit(self.frame_historyWidget)
        self.txtLichSu1.setObjectName(u"txtLichSu1")
        self.txtLichSu1.setMinimumSize(QSize(434, 35))
        self.txtLichSu1.setFont(font8)
        self.txtLichSu1.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtLichSu1.setAlignment(Qt.AlignCenter)
        self.txtLichSu1.setReadOnly(True)

        self.verticalLayout_53.addWidget(self.txtLichSu1)

        self.txtLichSu2 = QLineEdit(self.frame_historyWidget)
        self.txtLichSu2.setObjectName(u"txtLichSu2")
        self.txtLichSu2.setMinimumSize(QSize(434, 35))
        self.txtLichSu2.setFont(font8)
        self.txtLichSu2.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtLichSu2.setAlignment(Qt.AlignCenter)
        self.txtLichSu2.setReadOnly(True)

        self.verticalLayout_53.addWidget(self.txtLichSu2)

        self.txtLichSu3 = QLineEdit(self.frame_historyWidget)
        self.txtLichSu3.setObjectName(u"txtLichSu3")
        self.txtLichSu3.setMinimumSize(QSize(434, 35))
        self.txtLichSu3.setFont(font8)
        self.txtLichSu3.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtLichSu3.setAlignment(Qt.AlignCenter)
        self.txtLichSu3.setReadOnly(True)

        self.verticalLayout_53.addWidget(self.txtLichSu3)

        self.txtLichSu4 = QLineEdit(self.frame_historyWidget)
        self.txtLichSu4.setObjectName(u"txtLichSu4")
        self.txtLichSu4.setMinimumSize(QSize(434, 35))
        self.txtLichSu4.setFont(font8)
        self.txtLichSu4.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtLichSu4.setAlignment(Qt.AlignCenter)
        self.txtLichSu4.setReadOnly(True)

        self.verticalLayout_53.addWidget(self.txtLichSu4)


        self.verticalLayout_35.addWidget(self.frame_historyWidget)


        self.verticalLayout_33.addWidget(self.frame_history)


        self.verticalLayout_34.addWidget(self.findFrame)

        self.stackedWidget.addWidget(self.page_find)
        self.page_chart = QWidget()
        self.page_chart.setObjectName(u"page_chart")
        self.verticalLayout_32 = QVBoxLayout(self.page_chart)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(1, 1, 1, 1)
        self.chartFrame = QFrame(self.page_chart)
        self.chartFrame.setObjectName(u"chartFrame")
        self.horizontalLayout_21 = QHBoxLayout(self.chartFrame)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.chartFrameLeft = QFrame(self.chartFrame)
        self.chartFrameLeft.setObjectName(u"chartFrameLeft")
        self.verticalLayout_54 = QVBoxLayout(self.chartFrameLeft)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(1, 1, 1, 1)
        self.chartFrameLeft_Title = QFrame(self.chartFrameLeft)
        self.chartFrameLeft_Title.setObjectName(u"chartFrameLeft_Title")
        self.chartFrameLeft_Title.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_55 = QVBoxLayout(self.chartFrameLeft_Title)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.txtchartFrameLeft_Title = QLabel(self.chartFrameLeft_Title)
        self.txtchartFrameLeft_Title.setObjectName(u"txtchartFrameLeft_Title")
        self.txtchartFrameLeft_Title.setFont(font1)
        self.txtchartFrameLeft_Title.setStyleSheet(u"")

        self.verticalLayout_55.addWidget(self.txtchartFrameLeft_Title)


        self.verticalLayout_54.addWidget(self.chartFrameLeft_Title)

        self.chartFrameLeft_Monitor = QFrame(self.chartFrameLeft)
        self.chartFrameLeft_Monitor.setObjectName(u"chartFrameLeft_Monitor")
        sizePolicy5.setHeightForWidth(self.chartFrameLeft_Monitor.sizePolicy().hasHeightForWidth())
        self.chartFrameLeft_Monitor.setSizePolicy(sizePolicy5)
        self.chartFrameLeft_Monitor.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.horizontalLayout_24 = QHBoxLayout(self.chartFrameLeft_Monitor)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(1, 1, 1, 1)
        self.frame_chartLeft = QFrame(self.chartFrameLeft_Monitor)
        self.frame_chartLeft.setObjectName(u"frame_chartLeft")
        self.verticalLayout_57 = QVBoxLayout(self.frame_chartLeft)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_chartLeft_title = QFrame(self.frame_chartLeft)
        self.frame_chartLeft_title.setObjectName(u"frame_chartLeft_title")
        self.verticalLayout_58 = QVBoxLayout(self.frame_chartLeft_title)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.txtframe_chartLeft_title = QLabel(self.frame_chartLeft_title)
        self.txtframe_chartLeft_title.setObjectName(u"txtframe_chartLeft_title")
        self.txtframe_chartLeft_title.setFont(font1)
        self.txtframe_chartLeft_title.setStyleSheet(u"")

        self.verticalLayout_58.addWidget(self.txtframe_chartLeft_title)


        self.verticalLayout_57.addWidget(self.frame_chartLeft_title)

        self.frame_chartLeft_monitor = QFrame(self.frame_chartLeft)
        self.frame_chartLeft_monitor.setObjectName(u"frame_chartLeft_monitor")
        sizePolicy5.setHeightForWidth(self.frame_chartLeft_monitor.sizePolicy().hasHeightForWidth())
        self.frame_chartLeft_monitor.setSizePolicy(sizePolicy5)
        self.verticalLayout_59 = QVBoxLayout(self.frame_chartLeft_monitor)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.txtLuotKHNgay = QLabel(self.frame_chartLeft_monitor)
        self.txtLuotKHNgay.setObjectName(u"txtLuotKHNgay")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(25)
        font9.setBold(True)
        font9.setWeight(75)
        self.txtLuotKHNgay.setFont(font9)
        self.txtLuotKHNgay.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.txtLuotKHNgay.setAlignment(Qt.AlignCenter)

        self.verticalLayout_59.addWidget(self.txtLuotKHNgay)


        self.verticalLayout_57.addWidget(self.frame_chartLeft_monitor)


        self.horizontalLayout_24.addWidget(self.frame_chartLeft)

        self.frame_chartRight = QFrame(self.chartFrameLeft_Monitor)
        self.frame_chartRight.setObjectName(u"frame_chartRight")
        self.verticalLayout_56 = QVBoxLayout(self.frame_chartRight)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_chartRight_title = QFrame(self.frame_chartRight)
        self.frame_chartRight_title.setObjectName(u"frame_chartRight_title")
        self.verticalLayout_60 = QVBoxLayout(self.frame_chartRight_title)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.txtframe_chartRight_title = QLabel(self.frame_chartRight_title)
        self.txtframe_chartRight_title.setObjectName(u"txtframe_chartRight_title")
        self.txtframe_chartRight_title.setFont(font1)
        self.txtframe_chartRight_title.setStyleSheet(u"")

        self.verticalLayout_60.addWidget(self.txtframe_chartRight_title)


        self.verticalLayout_56.addWidget(self.frame_chartRight_title)

        self.frame_chartRight_monitor = QFrame(self.frame_chartRight)
        self.frame_chartRight_monitor.setObjectName(u"frame_chartRight_monitor")
        sizePolicy5.setHeightForWidth(self.frame_chartRight_monitor.sizePolicy().hasHeightForWidth())
        self.frame_chartRight_monitor.setSizePolicy(sizePolicy5)
        self.verticalLayout_61 = QVBoxLayout(self.frame_chartRight_monitor)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.txtLuotKNgay = QLabel(self.frame_chartRight_monitor)
        self.txtLuotKNgay.setObjectName(u"txtLuotKNgay")
        self.txtLuotKNgay.setFont(font9)
        self.txtLuotKNgay.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.txtLuotKNgay.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.txtLuotKNgay)


        self.verticalLayout_56.addWidget(self.frame_chartRight_monitor)


        self.horizontalLayout_24.addWidget(self.frame_chartRight)


        self.verticalLayout_54.addWidget(self.chartFrameLeft_Monitor)

        self.chartFrameLeft_Total = QFrame(self.chartFrameLeft)
        self.chartFrameLeft_Total.setObjectName(u"chartFrameLeft_Total")
        self.chartFrameLeft_Total.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_62 = QVBoxLayout(self.chartFrameLeft_Total)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(1, 1, 1, 1)
        self.frame_chartTotal_title = QFrame(self.chartFrameLeft_Total)
        self.frame_chartTotal_title.setObjectName(u"frame_chartTotal_title")
        self.verticalLayout_64 = QVBoxLayout(self.frame_chartTotal_title)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.txtframe_chartTotal_title = QLabel(self.frame_chartTotal_title)
        self.txtframe_chartTotal_title.setObjectName(u"txtframe_chartTotal_title")
        self.txtframe_chartTotal_title.setFont(font1)
        self.txtframe_chartTotal_title.setStyleSheet(u"")

        self.verticalLayout_64.addWidget(self.txtframe_chartTotal_title)


        self.verticalLayout_62.addWidget(self.frame_chartTotal_title)

        self.frame_chartTotal_monitor = QFrame(self.chartFrameLeft_Total)
        self.frame_chartTotal_monitor.setObjectName(u"frame_chartTotal_monitor")
        self.frame_chartTotal_monitor.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(26, 29, 36);")
        self.horizontalLayout_23 = QHBoxLayout(self.frame_chartTotal_monitor)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(1, 1, 1, 1)
        self.frame_chartTotalMonitor_left = QFrame(self.frame_chartTotal_monitor)
        self.frame_chartTotalMonitor_left.setObjectName(u"frame_chartTotalMonitor_left")
        self.verticalLayout_65 = QVBoxLayout(self.frame_chartTotalMonitor_left)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(1, 1, 1, 1)
        self.txtQTongSoNgay = QLineEdit(self.frame_chartTotalMonitor_left)
        self.txtQTongSoNgay.setObjectName(u"txtQTongSoNgay")
        sizePolicy6.setHeightForWidth(self.txtQTongSoNgay.sizePolicy().hasHeightForWidth())
        self.txtQTongSoNgay.setSizePolicy(sizePolicy6)
        self.txtQTongSoNgay.setMinimumSize(QSize(100, 35))
        self.txtQTongSoNgay.setMaximumSize(QSize(100, 35))
        self.txtQTongSoNgay.setFont(font7)
        self.txtQTongSoNgay.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQTongSoNgay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQTongSoNgay.setReadOnly(True)

        self.verticalLayout_65.addWidget(self.txtQTongSoNgay)


        self.horizontalLayout_23.addWidget(self.frame_chartTotalMonitor_left)

        self.frame_chartTotalMonitor_right = QFrame(self.frame_chartTotal_monitor)
        self.frame_chartTotalMonitor_right.setObjectName(u"frame_chartTotalMonitor_right")
        self.verticalLayout_66 = QVBoxLayout(self.frame_chartTotalMonitor_right)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(1, 1, 1, 1)
        self.txtTongSoNgay = QLineEdit(self.frame_chartTotalMonitor_right)
        self.txtTongSoNgay.setObjectName(u"txtTongSoNgay")
        self.txtTongSoNgay.setMinimumSize(QSize(434, 35))
        self.txtTongSoNgay.setFont(font8)
        self.txtTongSoNgay.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtTongSoNgay.setAlignment(Qt.AlignCenter)
        self.txtTongSoNgay.setReadOnly(True)
        self.txtTongSoNgay.setClearButtonEnabled(False)

        self.verticalLayout_66.addWidget(self.txtTongSoNgay)


        self.horizontalLayout_23.addWidget(self.frame_chartTotalMonitor_right)


        self.verticalLayout_62.addWidget(self.frame_chartTotal_monitor)


        self.verticalLayout_54.addWidget(self.chartFrameLeft_Total)


        self.horizontalLayout_21.addWidget(self.chartFrameLeft)

        self.chartFrameRight = QFrame(self.chartFrame)
        self.chartFrameRight.setObjectName(u"chartFrameRight")
        self.verticalLayout_31 = QVBoxLayout(self.chartFrameRight)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(1, 1, 1, 1)
        self.chartFrameRight_Title = QFrame(self.chartFrameRight)
        self.chartFrameRight_Title.setObjectName(u"chartFrameRight_Title")
        self.chartFrameRight_Title.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_73 = QVBoxLayout(self.chartFrameRight_Title)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.txtchartFrameRight_Title = QLabel(self.chartFrameRight_Title)
        self.txtchartFrameRight_Title.setObjectName(u"txtchartFrameRight_Title")
        self.txtchartFrameRight_Title.setFont(font1)
        self.txtchartFrameRight_Title.setStyleSheet(u"")

        self.verticalLayout_73.addWidget(self.txtchartFrameRight_Title)


        self.verticalLayout_31.addWidget(self.chartFrameRight_Title)

        self.chartFrameRight_Monitor = QFrame(self.chartFrameRight)
        self.chartFrameRight_Monitor.setObjectName(u"chartFrameRight_Monitor")
        sizePolicy5.setHeightForWidth(self.chartFrameRight_Monitor.sizePolicy().hasHeightForWidth())
        self.chartFrameRight_Monitor.setSizePolicy(sizePolicy5)
        self.chartFrameRight_Monitor.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.horizontalLayout_25 = QHBoxLayout(self.chartFrameRight_Monitor)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(1, 1, 1, 1)
        self.frame_chartMonitor_left = QFrame(self.chartFrameRight_Monitor)
        self.frame_chartMonitor_left.setObjectName(u"frame_chartMonitor_left")
        self.verticalLayout_67 = QVBoxLayout(self.frame_chartMonitor_left)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.frame_chartLeftMonitor_title = QFrame(self.frame_chartMonitor_left)
        self.frame_chartLeftMonitor_title.setObjectName(u"frame_chartLeftMonitor_title")
        self.verticalLayout_68 = QVBoxLayout(self.frame_chartLeftMonitor_title)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(1, 1, 1, 1)
        self.txtframe_chartLeftMonitor_title = QLabel(self.frame_chartLeftMonitor_title)
        self.txtframe_chartLeftMonitor_title.setObjectName(u"txtframe_chartLeftMonitor_title")
        self.txtframe_chartLeftMonitor_title.setFont(font1)
        self.txtframe_chartLeftMonitor_title.setStyleSheet(u"")

        self.verticalLayout_68.addWidget(self.txtframe_chartLeftMonitor_title)


        self.verticalLayout_67.addWidget(self.frame_chartLeftMonitor_title)

        self.frame_chartLeftMonitor_monitor = QFrame(self.frame_chartMonitor_left)
        self.frame_chartLeftMonitor_monitor.setObjectName(u"frame_chartLeftMonitor_monitor")
        sizePolicy5.setHeightForWidth(self.frame_chartLeftMonitor_monitor.sizePolicy().hasHeightForWidth())
        self.frame_chartLeftMonitor_monitor.setSizePolicy(sizePolicy5)
        self.verticalLayout_69 = QVBoxLayout(self.frame_chartLeftMonitor_monitor)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.txtLuotKHThang = QLabel(self.frame_chartLeftMonitor_monitor)
        self.txtLuotKHThang.setObjectName(u"txtLuotKHThang")
        self.txtLuotKHThang.setFont(font9)
        self.txtLuotKHThang.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.txtLuotKHThang.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.txtLuotKHThang)


        self.verticalLayout_67.addWidget(self.frame_chartLeftMonitor_monitor)


        self.horizontalLayout_25.addWidget(self.frame_chartMonitor_left)

        self.frame_chartMonitor_right = QFrame(self.chartFrameRight_Monitor)
        self.frame_chartMonitor_right.setObjectName(u"frame_chartMonitor_right")
        self.verticalLayout_70 = QVBoxLayout(self.frame_chartMonitor_right)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.frame_chartRightMonitor_title = QFrame(self.frame_chartMonitor_right)
        self.frame_chartRightMonitor_title.setObjectName(u"frame_chartRightMonitor_title")
        self.verticalLayout_71 = QVBoxLayout(self.frame_chartRightMonitor_title)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(1, 1, 1, 1)
        self.txtframe_chartRightMonitor_title = QLabel(self.frame_chartRightMonitor_title)
        self.txtframe_chartRightMonitor_title.setObjectName(u"txtframe_chartRightMonitor_title")
        self.txtframe_chartRightMonitor_title.setFont(font1)
        self.txtframe_chartRightMonitor_title.setStyleSheet(u"")

        self.verticalLayout_71.addWidget(self.txtframe_chartRightMonitor_title)


        self.verticalLayout_70.addWidget(self.frame_chartRightMonitor_title)

        self.frame_chartRightMonitor_monitor = QFrame(self.frame_chartMonitor_right)
        self.frame_chartRightMonitor_monitor.setObjectName(u"frame_chartRightMonitor_monitor")
        sizePolicy5.setHeightForWidth(self.frame_chartRightMonitor_monitor.sizePolicy().hasHeightForWidth())
        self.frame_chartRightMonitor_monitor.setSizePolicy(sizePolicy5)
        self.verticalLayout_72 = QVBoxLayout(self.frame_chartRightMonitor_monitor)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.txtLuotKThang = QLabel(self.frame_chartRightMonitor_monitor)
        self.txtLuotKThang.setObjectName(u"txtLuotKThang")
        self.txtLuotKThang.setFont(font9)
        self.txtLuotKThang.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.txtLuotKThang.setAlignment(Qt.AlignCenter)

        self.verticalLayout_72.addWidget(self.txtLuotKThang)


        self.verticalLayout_70.addWidget(self.frame_chartRightMonitor_monitor)


        self.horizontalLayout_25.addWidget(self.frame_chartMonitor_right)


        self.verticalLayout_31.addWidget(self.chartFrameRight_Monitor)

        self.chartFrameRight_Total = QFrame(self.chartFrameRight)
        self.chartFrameRight_Total.setObjectName(u"chartFrameRight_Total")
        self.chartFrameRight_Total.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_74 = QVBoxLayout(self.chartFrameRight_Total)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(1, 1, 1, 1)
        self.frame_chartRightTotal_title = QFrame(self.chartFrameRight_Total)
        self.frame_chartRightTotal_title.setObjectName(u"frame_chartRightTotal_title")
        self.verticalLayout_75 = QVBoxLayout(self.frame_chartRightTotal_title)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.txtframe_chartRightTotal_title = QLabel(self.frame_chartRightTotal_title)
        self.txtframe_chartRightTotal_title.setObjectName(u"txtframe_chartRightTotal_title")
        self.txtframe_chartRightTotal_title.setFont(font1)
        self.txtframe_chartRightTotal_title.setStyleSheet(u"")

        self.verticalLayout_75.addWidget(self.txtframe_chartRightTotal_title)


        self.verticalLayout_74.addWidget(self.frame_chartRightTotal_title)

        self.frame_chartRightTotal_monitor = QFrame(self.chartFrameRight_Total)
        self.frame_chartRightTotal_monitor.setObjectName(u"frame_chartRightTotal_monitor")
        self.frame_chartRightTotal_monitor.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(26, 29, 36);")
        self.horizontalLayout_26 = QHBoxLayout(self.frame_chartRightTotal_monitor)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(1, 1, 1, 1)
        self.frame_chartRightTotal_left = QFrame(self.frame_chartRightTotal_monitor)
        self.frame_chartRightTotal_left.setObjectName(u"frame_chartRightTotal_left")
        self.verticalLayout_76 = QVBoxLayout(self.frame_chartRightTotal_left)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(1, 1, 1, 1)
        self.txtQTongSoThang = QLineEdit(self.frame_chartRightTotal_left)
        self.txtQTongSoThang.setObjectName(u"txtQTongSoThang")
        sizePolicy6.setHeightForWidth(self.txtQTongSoThang.sizePolicy().hasHeightForWidth())
        self.txtQTongSoThang.setSizePolicy(sizePolicy6)
        self.txtQTongSoThang.setMinimumSize(QSize(110, 35))
        self.txtQTongSoThang.setMaximumSize(QSize(110, 35))
        self.txtQTongSoThang.setFont(font7)
        self.txtQTongSoThang.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQTongSoThang.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQTongSoThang.setReadOnly(True)

        self.verticalLayout_76.addWidget(self.txtQTongSoThang)


        self.horizontalLayout_26.addWidget(self.frame_chartRightTotal_left)

        self.frame_chartRightTotal_right = QFrame(self.frame_chartRightTotal_monitor)
        self.frame_chartRightTotal_right.setObjectName(u"frame_chartRightTotal_right")
        self.verticalLayout_77 = QVBoxLayout(self.frame_chartRightTotal_right)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(1, 1, 1, 1)
        self.txtTongSoThang = QLineEdit(self.frame_chartRightTotal_right)
        self.txtTongSoThang.setObjectName(u"txtTongSoThang")
        self.txtTongSoThang.setMinimumSize(QSize(434, 35))
        self.txtTongSoThang.setFont(font8)
        self.txtTongSoThang.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtTongSoThang.setAlignment(Qt.AlignCenter)
        self.txtTongSoThang.setReadOnly(True)

        self.verticalLayout_77.addWidget(self.txtTongSoThang)


        self.horizontalLayout_26.addWidget(self.frame_chartRightTotal_right)


        self.verticalLayout_74.addWidget(self.frame_chartRightTotal_monitor)


        self.verticalLayout_31.addWidget(self.chartFrameRight_Total)


        self.horizontalLayout_21.addWidget(self.chartFrameRight)


        self.verticalLayout_32.addWidget(self.chartFrame)

        self.stackedWidget.addWidget(self.page_chart)
        self.page_nv = QWidget()
        self.page_nv.setObjectName(u"page_nv")
        self.verticalLayout_79 = QVBoxLayout(self.page_nv)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(1, 1, 1, 1)
        self.nvFrame = QFrame(self.page_nv)
        self.nvFrame.setObjectName(u"nvFrame")
        self.verticalLayout_63 = QVBoxLayout(self.nvFrame)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(1, 1, 1, 1)
        self.thongtinFrame_2 = QFrame(self.nvFrame)
        self.thongtinFrame_2.setObjectName(u"thongtinFrame_2")
        sizePolicy5.setHeightForWidth(self.thongtinFrame_2.sizePolicy().hasHeightForWidth())
        self.thongtinFrame_2.setSizePolicy(sizePolicy5)
        self.thongtinFrame = QVBoxLayout(self.thongtinFrame_2)
        self.thongtinFrame.setObjectName(u"thongtinFrame")
        self.thongtinFrame.setContentsMargins(1, 1, 1, 1)
        self.thongtinFrameTitle = QFrame(self.thongtinFrame_2)
        self.thongtinFrameTitle.setObjectName(u"thongtinFrameTitle")
        self.thongtinFrameTitle.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_80 = QVBoxLayout(self.thongtinFrameTitle)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.txtthongtinFrameTitle = QLabel(self.thongtinFrameTitle)
        self.txtthongtinFrameTitle.setObjectName(u"txtthongtinFrameTitle")
        self.txtthongtinFrameTitle.setFont(font1)
        self.txtthongtinFrameTitle.setStyleSheet(u"")

        self.verticalLayout_80.addWidget(self.txtthongtinFrameTitle)


        self.thongtinFrame.addWidget(self.thongtinFrameTitle)

        self.thongtinFrameMonitor = QFrame(self.thongtinFrame_2)
        self.thongtinFrameMonitor.setObjectName(u"thongtinFrameMonitor")
        sizePolicy5.setHeightForWidth(self.thongtinFrameMonitor.sizePolicy().hasHeightForWidth())
        self.thongtinFrameMonitor.setSizePolicy(sizePolicy5)
        self.thongtinFrameMonitor.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_123 = QVBoxLayout(self.thongtinFrameMonitor)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(1, 1, 1, 1)
        self.thongtinFrameMonitorUp = QFrame(self.thongtinFrameMonitor)
        self.thongtinFrameMonitorUp.setObjectName(u"thongtinFrameMonitorUp")
        sizePolicy5.setHeightForWidth(self.thongtinFrameMonitorUp.sizePolicy().hasHeightForWidth())
        self.thongtinFrameMonitorUp.setSizePolicy(sizePolicy5)
        self.horizontalLayout_11 = QHBoxLayout(self.thongtinFrameMonitorUp)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.thongtinFrameMonitorLeft = QFrame(self.thongtinFrameMonitorUp)
        self.thongtinFrameMonitorLeft.setObjectName(u"thongtinFrameMonitorLeft")
        sizePolicy3.setHeightForWidth(self.thongtinFrameMonitorLeft.sizePolicy().hasHeightForWidth())
        self.thongtinFrameMonitorLeft.setSizePolicy(sizePolicy3)
        self.horizontalLayout_38 = QHBoxLayout(self.thongtinFrameMonitorLeft)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(1, 1, 9, 1)
        self.thongtinFrameMonitorLeftQ_3 = QFrame(self.thongtinFrameMonitorLeft)
        self.thongtinFrameMonitorLeftQ_3.setObjectName(u"thongtinFrameMonitorLeftQ_3")
        self.verticalLayout_119 = QVBoxLayout(self.thongtinFrameMonitorLeftQ_3)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(1, 1, 1, 1)
        self.txtQTenKhach = QLineEdit(self.thongtinFrameMonitorLeftQ_3)
        self.txtQTenKhach.setObjectName(u"txtQTenKhach")
        sizePolicy6.setHeightForWidth(self.txtQTenKhach.sizePolicy().hasHeightForWidth())
        self.txtQTenKhach.setSizePolicy(sizePolicy6)
        self.txtQTenKhach.setMinimumSize(QSize(130, 35))
        self.txtQTenKhach.setMaximumSize(QSize(130, 35))
        self.txtQTenKhach.setFont(font7)
        self.txtQTenKhach.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQTenKhach.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQTenKhach.setReadOnly(True)

        self.verticalLayout_119.addWidget(self.txtQTenKhach)

        self.txtQDiaChi = QLineEdit(self.thongtinFrameMonitorLeftQ_3)
        self.txtQDiaChi.setObjectName(u"txtQDiaChi")
        sizePolicy6.setHeightForWidth(self.txtQDiaChi.sizePolicy().hasHeightForWidth())
        self.txtQDiaChi.setSizePolicy(sizePolicy6)
        self.txtQDiaChi.setMinimumSize(QSize(130, 35))
        self.txtQDiaChi.setMaximumSize(QSize(130, 35))
        self.txtQDiaChi.setFont(font7)
        self.txtQDiaChi.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQDiaChi.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQDiaChi.setReadOnly(True)

        self.verticalLayout_119.addWidget(self.txtQDiaChi)

        self.txtQSdt = QLineEdit(self.thongtinFrameMonitorLeftQ_3)
        self.txtQSdt.setObjectName(u"txtQSdt")
        sizePolicy6.setHeightForWidth(self.txtQSdt.sizePolicy().hasHeightForWidth())
        self.txtQSdt.setSizePolicy(sizePolicy6)
        self.txtQSdt.setMinimumSize(QSize(130, 35))
        self.txtQSdt.setMaximumSize(QSize(130, 35))
        self.txtQSdt.setFont(font7)
        self.txtQSdt.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQSdt.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQSdt.setReadOnly(True)

        self.verticalLayout_119.addWidget(self.txtQSdt)

        self.float_17 = QFrame(self.thongtinFrameMonitorLeftQ_3)
        self.float_17.setObjectName(u"float_17")
        self.verticalLayout_120 = QVBoxLayout(self.float_17)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")

        self.verticalLayout_119.addWidget(self.float_17)


        self.horizontalLayout_38.addWidget(self.thongtinFrameMonitorLeftQ_3)

        self.thongtinFrameMonitorLeftText_3 = QFrame(self.thongtinFrameMonitorLeft)
        self.thongtinFrameMonitorLeftText_3.setObjectName(u"thongtinFrameMonitorLeftText_3")
        self.verticalLayout_121 = QVBoxLayout(self.thongtinFrameMonitorLeftText_3)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(1, 1, 1, 1)
        self.txtTenKhach = QLineEdit(self.thongtinFrameMonitorLeftText_3)
        self.txtTenKhach.setObjectName(u"txtTenKhach")
        self.txtTenKhach.setMinimumSize(QSize(434, 35))
        self.txtTenKhach.setFont(font8)
        self.txtTenKhach.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtTenKhach.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_121.addWidget(self.txtTenKhach)

        self.txtDiaChi = QLineEdit(self.thongtinFrameMonitorLeftText_3)
        self.txtDiaChi.setObjectName(u"txtDiaChi")
        self.txtDiaChi.setMinimumSize(QSize(434, 35))
        self.txtDiaChi.setFont(font8)
        self.txtDiaChi.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtDiaChi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_121.addWidget(self.txtDiaChi)

        self.txtSdt = QLineEdit(self.thongtinFrameMonitorLeftText_3)
        self.txtSdt.setObjectName(u"txtSdt")
        self.txtSdt.setMinimumSize(QSize(434, 35))
        self.txtSdt.setFont(font8)
        self.txtSdt.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtSdt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_121.addWidget(self.txtSdt)

        self.float_18 = QFrame(self.thongtinFrameMonitorLeftText_3)
        self.float_18.setObjectName(u"float_18")
        self.verticalLayout_122 = QVBoxLayout(self.float_18)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")

        self.verticalLayout_121.addWidget(self.float_18)


        self.horizontalLayout_38.addWidget(self.thongtinFrameMonitorLeftText_3)


        self.horizontalLayout_11.addWidget(self.thongtinFrameMonitorLeft)

        self.thongtinFrameMonitorRight = QFrame(self.thongtinFrameMonitorUp)
        self.thongtinFrameMonitorRight.setObjectName(u"thongtinFrameMonitorRight")
        self.horizontalLayout_37 = QHBoxLayout(self.thongtinFrameMonitorRight)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(9, 1, 1, 1)
        self.thongtinFrameMonitorRightQ_3 = QFrame(self.thongtinFrameMonitorRight)
        self.thongtinFrameMonitorRightQ_3.setObjectName(u"thongtinFrameMonitorRightQ_3")
        self.verticalLayout_115 = QVBoxLayout(self.thongtinFrameMonitorRightQ_3)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(1, 1, 1, 1)
        self.txtQLoaiXe = QLineEdit(self.thongtinFrameMonitorRightQ_3)
        self.txtQLoaiXe.setObjectName(u"txtQLoaiXe")
        sizePolicy6.setHeightForWidth(self.txtQLoaiXe.sizePolicy().hasHeightForWidth())
        self.txtQLoaiXe.setSizePolicy(sizePolicy6)
        self.txtQLoaiXe.setMinimumSize(QSize(130, 35))
        self.txtQLoaiXe.setMaximumSize(QSize(130, 35))
        self.txtQLoaiXe.setFont(font7)
        self.txtQLoaiXe.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQLoaiXe.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQLoaiXe.setReadOnly(True)

        self.verticalLayout_115.addWidget(self.txtQLoaiXe)

        self.txtQSoXe = QLineEdit(self.thongtinFrameMonitorRightQ_3)
        self.txtQSoXe.setObjectName(u"txtQSoXe")
        sizePolicy6.setHeightForWidth(self.txtQSoXe.sizePolicy().hasHeightForWidth())
        self.txtQSoXe.setSizePolicy(sizePolicy6)
        self.txtQSoXe.setMinimumSize(QSize(130, 35))
        self.txtQSoXe.setMaximumSize(QSize(130, 35))
        self.txtQSoXe.setFont(font7)
        self.txtQSoXe.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQSoXe.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQSoXe.setReadOnly(True)

        self.verticalLayout_115.addWidget(self.txtQSoXe)

        self.txtQNhanVien = QLineEdit(self.thongtinFrameMonitorRightQ_3)
        self.txtQNhanVien.setObjectName(u"txtQNhanVien")
        sizePolicy6.setHeightForWidth(self.txtQNhanVien.sizePolicy().hasHeightForWidth())
        self.txtQNhanVien.setSizePolicy(sizePolicy6)
        self.txtQNhanVien.setMinimumSize(QSize(130, 35))
        self.txtQNhanVien.setMaximumSize(QSize(130, 35))
        self.txtQNhanVien.setFont(font7)
        self.txtQNhanVien.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQNhanVien.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQNhanVien.setReadOnly(True)

        self.verticalLayout_115.addWidget(self.txtQNhanVien)

        self.float_15 = QFrame(self.thongtinFrameMonitorRightQ_3)
        self.float_15.setObjectName(u"float_15")
        self.verticalLayout_116 = QVBoxLayout(self.float_15)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")

        self.verticalLayout_115.addWidget(self.float_15)


        self.horizontalLayout_37.addWidget(self.thongtinFrameMonitorRightQ_3)

        self.thongtinFrameMonitorRightText_3 = QFrame(self.thongtinFrameMonitorRight)
        self.thongtinFrameMonitorRightText_3.setObjectName(u"thongtinFrameMonitorRightText_3")
        self.verticalLayout_117 = QVBoxLayout(self.thongtinFrameMonitorRightText_3)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(1, 1, 1, 1)
        self.cboLoaiXe = QComboBox(self.thongtinFrameMonitorRightText_3)
        self.cboLoaiXe.setObjectName(u"cboLoaiXe")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.cboLoaiXe.sizePolicy().hasHeightForWidth())
        self.cboLoaiXe.setSizePolicy(sizePolicy8)
        self.cboLoaiXe.setFont(font7)
        self.cboLoaiXe.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")

        self.verticalLayout_117.addWidget(self.cboLoaiXe)

        self.txtSoXe = QLineEdit(self.thongtinFrameMonitorRightText_3)
        self.txtSoXe.setObjectName(u"txtSoXe")
        self.txtSoXe.setMinimumSize(QSize(434, 35))
        self.txtSoXe.setFont(font8)
        self.txtSoXe.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtSoXe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_117.addWidget(self.txtSoXe)

        self.txtNhanVien = QLineEdit(self.thongtinFrameMonitorRightText_3)
        self.txtNhanVien.setObjectName(u"txtNhanVien")
        self.txtNhanVien.setMinimumSize(QSize(434, 35))
        self.txtNhanVien.setFont(font8)
        self.txtNhanVien.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtNhanVien.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txtNhanVien.setReadOnly(True)

        self.verticalLayout_117.addWidget(self.txtNhanVien)

        self.float_16 = QFrame(self.thongtinFrameMonitorRightText_3)
        self.float_16.setObjectName(u"float_16")
        self.verticalLayout_118 = QVBoxLayout(self.float_16)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")

        self.verticalLayout_117.addWidget(self.float_16)


        self.horizontalLayout_37.addWidget(self.thongtinFrameMonitorRightText_3)


        self.horizontalLayout_11.addWidget(self.thongtinFrameMonitorRight)


        self.verticalLayout_123.addWidget(self.thongtinFrameMonitorUp)

        self.thongtinFrameMonitorDown = QFrame(self.thongtinFrameMonitor)
        self.thongtinFrameMonitorDown.setObjectName(u"thongtinFrameMonitorDown")
        self.horizontalLayout_12 = QHBoxLayout(self.thongtinFrameMonitorDown)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.matkhauFrameMonitorPass = QFrame(self.thongtinFrameMonitorDown)
        self.matkhauFrameMonitorPass.setObjectName(u"matkhauFrameMonitorPass")
        self.horizontalLayout_31 = QHBoxLayout(self.matkhauFrameMonitorPass)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(1, 1, 1, 1)
        self.matkhauFrameMPleft = QFrame(self.matkhauFrameMonitorPass)
        self.matkhauFrameMPleft.setObjectName(u"matkhauFrameMPleft")
        self.verticalLayout_89 = QVBoxLayout(self.matkhauFrameMPleft)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(1, 1, 1, 1)
        self.txtQTenTK = QLineEdit(self.matkhauFrameMPleft)
        self.txtQTenTK.setObjectName(u"txtQTenTK")
        sizePolicy6.setHeightForWidth(self.txtQTenTK.sizePolicy().hasHeightForWidth())
        self.txtQTenTK.setSizePolicy(sizePolicy6)
        self.txtQTenTK.setMinimumSize(QSize(130, 35))
        self.txtQTenTK.setMaximumSize(QSize(130, 35))
        self.txtQTenTK.setFont(font7)
        self.txtQTenTK.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQTenTK.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQTenTK.setReadOnly(True)

        self.verticalLayout_89.addWidget(self.txtQTenTK)

        self.txtQMatKhau = QLineEdit(self.matkhauFrameMPleft)
        self.txtQMatKhau.setObjectName(u"txtQMatKhau")
        sizePolicy6.setHeightForWidth(self.txtQMatKhau.sizePolicy().hasHeightForWidth())
        self.txtQMatKhau.setSizePolicy(sizePolicy6)
        self.txtQMatKhau.setMinimumSize(QSize(130, 35))
        self.txtQMatKhau.setMaximumSize(QSize(130, 35))
        self.txtQMatKhau.setFont(font7)
        self.txtQMatKhau.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQMatKhau.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQMatKhau.setReadOnly(True)

        self.verticalLayout_89.addWidget(self.txtQMatKhau)

        self.txtQNhapLai = QLineEdit(self.matkhauFrameMPleft)
        self.txtQNhapLai.setObjectName(u"txtQNhapLai")
        sizePolicy6.setHeightForWidth(self.txtQNhapLai.sizePolicy().hasHeightForWidth())
        self.txtQNhapLai.setSizePolicy(sizePolicy6)
        self.txtQNhapLai.setMinimumSize(QSize(130, 35))
        self.txtQNhapLai.setMaximumSize(QSize(130, 35))
        self.txtQNhapLai.setFont(font7)
        self.txtQNhapLai.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQNhapLai.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQNhapLai.setReadOnly(True)

        self.verticalLayout_89.addWidget(self.txtQNhapLai)


        self.horizontalLayout_31.addWidget(self.matkhauFrameMPleft)

        self.matkhauFrameMPright = QFrame(self.matkhauFrameMonitorPass)
        self.matkhauFrameMPright.setObjectName(u"matkhauFrameMPright")
        self.verticalLayout_88 = QVBoxLayout(self.matkhauFrameMPright)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(1, 1, 1, 1)
        self.txtTenTK = QLineEdit(self.matkhauFrameMPright)
        self.txtTenTK.setObjectName(u"txtTenTK")
        self.txtTenTK.setMinimumSize(QSize(434, 35))
        self.txtTenTK.setFont(font8)
        self.txtTenTK.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtTenTK.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.txtTenTK)

        self.txtMatKhau = QLineEdit(self.matkhauFrameMPright)
        self.txtMatKhau.setObjectName(u"txtMatKhau")
        self.txtMatKhau.setMinimumSize(QSize(434, 35))
        self.txtMatKhau.setFont(font8)
        self.txtMatKhau.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtMatKhau.setEchoMode(QLineEdit.Password)
        self.txtMatKhau.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.txtMatKhau)

        self.txtNhapLai = QLineEdit(self.matkhauFrameMPright)
        self.txtNhapLai.setObjectName(u"txtNhapLai")
        self.txtNhapLai.setMinimumSize(QSize(434, 35))
        self.txtNhapLai.setFont(font8)
        self.txtNhapLai.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtNhapLai.setEchoMode(QLineEdit.Password)
        self.txtNhapLai.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.txtNhapLai)


        self.horizontalLayout_31.addWidget(self.matkhauFrameMPright)


        self.horizontalLayout_12.addWidget(self.matkhauFrameMonitorPass)

        self.matkhauFrameMonitorButton = QFrame(self.thongtinFrameMonitorDown)
        self.matkhauFrameMonitorButton.setObjectName(u"matkhauFrameMonitorButton")
        self.verticalLayout_83 = QVBoxLayout(self.matkhauFrameMonitorButton)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(1, 1, 1, 1)
        self.float_2 = QFrame(self.matkhauFrameMonitorButton)
        self.float_2.setObjectName(u"float_2")
        self.verticalLayout_90 = QVBoxLayout(self.float_2)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")

        self.verticalLayout_83.addWidget(self.float_2)

        self.btnDangKy = QPushButton(self.matkhauFrameMonitorButton)
        self.btnDangKy.setObjectName(u"btnDangKy")
        self.btnDangKy.setMinimumSize(QSize(150, 30))
        self.btnDangKy.setFont(font4)
        self.btnDangKy.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/16x16/icons/16x16/cil-share-boxed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDangKy.setIcon(icon9)

        self.verticalLayout_83.addWidget(self.btnDangKy)


        self.horizontalLayout_12.addWidget(self.matkhauFrameMonitorButton)


        self.verticalLayout_123.addWidget(self.thongtinFrameMonitorDown)


        self.thongtinFrame.addWidget(self.thongtinFrameMonitor)


        self.verticalLayout_63.addWidget(self.thongtinFrame_2)

        self.matkhauFrame = QFrame(self.nvFrame)
        self.matkhauFrame.setObjectName(u"matkhauFrame")
        self.verticalLayout_81 = QVBoxLayout(self.matkhauFrame)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(1, 1, 1, 1)
        self.loaixeFrameTitle = QFrame(self.matkhauFrame)
        self.loaixeFrameTitle.setObjectName(u"loaixeFrameTitle")
        self.loaixeFrameTitle.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_82 = QVBoxLayout(self.loaixeFrameTitle)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.txtloaixeFrameTitle = QLabel(self.loaixeFrameTitle)
        self.txtloaixeFrameTitle.setObjectName(u"txtloaixeFrameTitle")
        self.txtloaixeFrameTitle.setFont(font1)
        self.txtloaixeFrameTitle.setStyleSheet(u"")

        self.verticalLayout_82.addWidget(self.txtloaixeFrameTitle)


        self.verticalLayout_81.addWidget(self.loaixeFrameTitle)

        self.loaixeFrameMonitor = QFrame(self.matkhauFrame)
        self.loaixeFrameMonitor.setObjectName(u"loaixeFrameMonitor")
        sizePolicy5.setHeightForWidth(self.loaixeFrameMonitor.sizePolicy().hasHeightForWidth())
        self.loaixeFrameMonitor.setSizePolicy(sizePolicy5)
        self.loaixeFrameMonitor.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.horizontalLayout_27 = QHBoxLayout(self.loaixeFrameMonitor)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.matkhauFrameMonitorPass_3 = QFrame(self.loaixeFrameMonitor)
        self.matkhauFrameMonitorPass_3.setObjectName(u"matkhauFrameMonitorPass_3")
        self.horizontalLayout_39 = QHBoxLayout(self.matkhauFrameMonitorPass_3)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(1, 1, 1, 1)
        self.matkhauFrameMPleft_3 = QFrame(self.matkhauFrameMonitorPass_3)
        self.matkhauFrameMPleft_3.setObjectName(u"matkhauFrameMPleft_3")
        self.verticalLayout_126 = QVBoxLayout(self.matkhauFrameMPleft_3)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(1, 1, 1, 1)
        self.txtQTenTK_3 = QLineEdit(self.matkhauFrameMPleft_3)
        self.txtQTenTK_3.setObjectName(u"txtQTenTK_3")
        sizePolicy6.setHeightForWidth(self.txtQTenTK_3.sizePolicy().hasHeightForWidth())
        self.txtQTenTK_3.setSizePolicy(sizePolicy6)
        self.txtQTenTK_3.setMinimumSize(QSize(130, 35))
        self.txtQTenTK_3.setMaximumSize(QSize(130, 35))
        self.txtQTenTK_3.setFont(font7)
        self.txtQTenTK_3.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQTenTK_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQTenTK_3.setReadOnly(True)

        self.verticalLayout_126.addWidget(self.txtQTenTK_3)

        self.txtQMatKhau_3 = QLineEdit(self.matkhauFrameMPleft_3)
        self.txtQMatKhau_3.setObjectName(u"txtQMatKhau_3")
        sizePolicy6.setHeightForWidth(self.txtQMatKhau_3.sizePolicy().hasHeightForWidth())
        self.txtQMatKhau_3.setSizePolicy(sizePolicy6)
        self.txtQMatKhau_3.setMinimumSize(QSize(130, 35))
        self.txtQMatKhau_3.setMaximumSize(QSize(130, 35))
        self.txtQMatKhau_3.setFont(font7)
        self.txtQMatKhau_3.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQMatKhau_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQMatKhau_3.setReadOnly(True)

        self.verticalLayout_126.addWidget(self.txtQMatKhau_3)

        self.txtQNhapLai_3 = QLineEdit(self.matkhauFrameMPleft_3)
        self.txtQNhapLai_3.setObjectName(u"txtQNhapLai_3")
        sizePolicy6.setHeightForWidth(self.txtQNhapLai_3.sizePolicy().hasHeightForWidth())
        self.txtQNhapLai_3.setSizePolicy(sizePolicy6)
        self.txtQNhapLai_3.setMinimumSize(QSize(130, 35))
        self.txtQNhapLai_3.setMaximumSize(QSize(130, 35))
        self.txtQNhapLai_3.setFont(font7)
        self.txtQNhapLai_3.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQNhapLai_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQNhapLai_3.setReadOnly(True)

        self.verticalLayout_126.addWidget(self.txtQNhapLai_3)


        self.horizontalLayout_39.addWidget(self.matkhauFrameMPleft_3)

        self.matkhauFrameMPright_3 = QFrame(self.matkhauFrameMonitorPass_3)
        self.matkhauFrameMPright_3.setObjectName(u"matkhauFrameMPright_3")
        self.verticalLayout_127 = QVBoxLayout(self.matkhauFrameMPright_3)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(1, 1, 1, 1)
        self.txtTenLoai = QLineEdit(self.matkhauFrameMPright_3)
        self.txtTenLoai.setObjectName(u"txtTenLoai")
        self.txtTenLoai.setMinimumSize(QSize(434, 35))
        self.txtTenLoai.setFont(font8)
        self.txtTenLoai.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtTenLoai.setAlignment(Qt.AlignCenter)

        self.verticalLayout_127.addWidget(self.txtTenLoai)

        self.txtSoCho = QLineEdit(self.matkhauFrameMPright_3)
        self.txtSoCho.setObjectName(u"txtSoCho")
        self.txtSoCho.setMinimumSize(QSize(434, 35))
        self.txtSoCho.setFont(font8)
        self.txtSoCho.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtSoCho.setAlignment(Qt.AlignCenter)

        self.verticalLayout_127.addWidget(self.txtSoCho)

        self.txtDonGia = QLineEdit(self.matkhauFrameMPright_3)
        self.txtDonGia.setObjectName(u"txtDonGia")
        self.txtDonGia.setMinimumSize(QSize(434, 35))
        self.txtDonGia.setFont(font8)
        self.txtDonGia.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtDonGia.setAlignment(Qt.AlignCenter)

        self.verticalLayout_127.addWidget(self.txtDonGia)


        self.horizontalLayout_39.addWidget(self.matkhauFrameMPright_3)


        self.horizontalLayout_27.addWidget(self.matkhauFrameMonitorPass_3)

        self.matkhauFrameMonitorButton_3 = QFrame(self.loaixeFrameMonitor)
        self.matkhauFrameMonitorButton_3.setObjectName(u"matkhauFrameMonitorButton_3")
        self.verticalLayout_124 = QVBoxLayout(self.matkhauFrameMonitorButton_3)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(1, 1, 1, 1)
        self.float_19 = QFrame(self.matkhauFrameMonitorButton_3)
        self.float_19.setObjectName(u"float_19")
        self.verticalLayout_125 = QVBoxLayout(self.float_19)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")

        self.verticalLayout_124.addWidget(self.float_19)

        self.btnThemLoai = QPushButton(self.matkhauFrameMonitorButton_3)
        self.btnThemLoai.setObjectName(u"btnThemLoai")
        self.btnThemLoai.setMinimumSize(QSize(150, 30))
        self.btnThemLoai.setFont(font4)
        self.btnThemLoai.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/16x16/icons/16x16/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnThemLoai.setIcon(icon10)

        self.verticalLayout_124.addWidget(self.btnThemLoai)


        self.horizontalLayout_27.addWidget(self.matkhauFrameMonitorButton_3)


        self.verticalLayout_81.addWidget(self.loaixeFrameMonitor)


        self.verticalLayout_63.addWidget(self.matkhauFrame)


        self.verticalLayout_79.addWidget(self.nvFrame)

        self.stackedWidget.addWidget(self.page_nv)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.verticalLayout_78 = QVBoxLayout(self.page_admin)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(1, 1, 1, 1)
        self.adminFrame = QFrame(self.page_admin)
        self.adminFrame.setObjectName(u"adminFrame")
        self.verticalLayout_113 = QVBoxLayout(self.adminFrame)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.thongtinFrame_3 = QFrame(self.adminFrame)
        self.thongtinFrame_3.setObjectName(u"thongtinFrame_3")
        sizePolicy5.setHeightForWidth(self.thongtinFrame_3.sizePolicy().hasHeightForWidth())
        self.thongtinFrame_3.setSizePolicy(sizePolicy5)
        self.thongtinFrame_4 = QVBoxLayout(self.thongtinFrame_3)
        self.thongtinFrame_4.setObjectName(u"thongtinFrame_4")
        self.thongtinFrame_4.setContentsMargins(1, 1, 1, 1)
        self.thongtinFrameTitle_2 = QFrame(self.thongtinFrame_3)
        self.thongtinFrameTitle_2.setObjectName(u"thongtinFrameTitle_2")
        self.thongtinFrameTitle_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_98 = QVBoxLayout(self.thongtinFrameTitle_2)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.txtthongtinFrameTitle_2 = QLabel(self.thongtinFrameTitle_2)
        self.txtthongtinFrameTitle_2.setObjectName(u"txtthongtinFrameTitle_2")
        self.txtthongtinFrameTitle_2.setFont(font1)
        self.txtthongtinFrameTitle_2.setStyleSheet(u"")

        self.verticalLayout_98.addWidget(self.txtthongtinFrameTitle_2)


        self.thongtinFrame_4.addWidget(self.thongtinFrameTitle_2)

        self.thongtinFrameMonitor_2 = QFrame(self.thongtinFrame_3)
        self.thongtinFrameMonitor_2.setObjectName(u"thongtinFrameMonitor_2")
        sizePolicy5.setHeightForWidth(self.thongtinFrameMonitor_2.sizePolicy().hasHeightForWidth())
        self.thongtinFrameMonitor_2.setSizePolicy(sizePolicy5)
        self.thongtinFrameMonitor_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.horizontalLayout_32 = QHBoxLayout(self.thongtinFrameMonitor_2)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.thongtinFrameMonitorLeft_2 = QFrame(self.thongtinFrameMonitor_2)
        self.thongtinFrameMonitorLeft_2.setObjectName(u"thongtinFrameMonitorLeft_2")
        sizePolicy3.setHeightForWidth(self.thongtinFrameMonitorLeft_2.sizePolicy().hasHeightForWidth())
        self.thongtinFrameMonitorLeft_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_33 = QHBoxLayout(self.thongtinFrameMonitorLeft_2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(1, 1, 9, 1)
        self.thongtinFrameMonitorLeftQ_2 = QFrame(self.thongtinFrameMonitorLeft_2)
        self.thongtinFrameMonitorLeftQ_2.setObjectName(u"thongtinFrameMonitorLeftQ_2")
        self.verticalLayout_99 = QVBoxLayout(self.thongtinFrameMonitorLeftQ_2)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(1, 1, 1, 1)
        self.txtQTenNv = QLineEdit(self.thongtinFrameMonitorLeftQ_2)
        self.txtQTenNv.setObjectName(u"txtQTenNv")
        sizePolicy6.setHeightForWidth(self.txtQTenNv.sizePolicy().hasHeightForWidth())
        self.txtQTenNv.setSizePolicy(sizePolicy6)
        self.txtQTenNv.setMinimumSize(QSize(130, 35))
        self.txtQTenNv.setMaximumSize(QSize(130, 35))
        self.txtQTenNv.setFont(font7)
        self.txtQTenNv.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQTenNv.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQTenNv.setReadOnly(True)

        self.verticalLayout_99.addWidget(self.txtQTenNv)

        self.txtQDiaChi_2 = QLineEdit(self.thongtinFrameMonitorLeftQ_2)
        self.txtQDiaChi_2.setObjectName(u"txtQDiaChi_2")
        sizePolicy6.setHeightForWidth(self.txtQDiaChi_2.sizePolicy().hasHeightForWidth())
        self.txtQDiaChi_2.setSizePolicy(sizePolicy6)
        self.txtQDiaChi_2.setMinimumSize(QSize(130, 35))
        self.txtQDiaChi_2.setMaximumSize(QSize(130, 35))
        self.txtQDiaChi_2.setFont(font7)
        self.txtQDiaChi_2.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQDiaChi_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQDiaChi_2.setReadOnly(True)

        self.verticalLayout_99.addWidget(self.txtQDiaChi_2)

        self.float_10 = QFrame(self.thongtinFrameMonitorLeftQ_2)
        self.float_10.setObjectName(u"float_10")
        self.verticalLayout_100 = QVBoxLayout(self.float_10)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")

        self.verticalLayout_99.addWidget(self.float_10)


        self.horizontalLayout_33.addWidget(self.thongtinFrameMonitorLeftQ_2)

        self.thongtinFrameMonitorLeftText_2 = QFrame(self.thongtinFrameMonitorLeft_2)
        self.thongtinFrameMonitorLeftText_2.setObjectName(u"thongtinFrameMonitorLeftText_2")
        self.verticalLayout_101 = QVBoxLayout(self.thongtinFrameMonitorLeftText_2)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(1, 1, 1, 1)
        self.txtTenNv = QLineEdit(self.thongtinFrameMonitorLeftText_2)
        self.txtTenNv.setObjectName(u"txtTenNv")
        self.txtTenNv.setMinimumSize(QSize(434, 35))
        self.txtTenNv.setFont(font8)
        self.txtTenNv.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtTenNv.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_101.addWidget(self.txtTenNv)

        self.txtDiaChiNv = QLineEdit(self.thongtinFrameMonitorLeftText_2)
        self.txtDiaChiNv.setObjectName(u"txtDiaChiNv")
        self.txtDiaChiNv.setMinimumSize(QSize(434, 35))
        self.txtDiaChiNv.setFont(font8)
        self.txtDiaChiNv.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtDiaChiNv.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_101.addWidget(self.txtDiaChiNv)

        self.float_11 = QFrame(self.thongtinFrameMonitorLeftText_2)
        self.float_11.setObjectName(u"float_11")
        self.verticalLayout_102 = QVBoxLayout(self.float_11)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")

        self.verticalLayout_101.addWidget(self.float_11)


        self.horizontalLayout_33.addWidget(self.thongtinFrameMonitorLeftText_2)


        self.horizontalLayout_32.addWidget(self.thongtinFrameMonitorLeft_2)

        self.thongtinFrameMonitorRight_2 = QFrame(self.thongtinFrameMonitor_2)
        self.thongtinFrameMonitorRight_2.setObjectName(u"thongtinFrameMonitorRight_2")
        self.horizontalLayout_34 = QHBoxLayout(self.thongtinFrameMonitorRight_2)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(9, 1, 1, 1)
        self.thongtinFrameMonitorRightQ_2 = QFrame(self.thongtinFrameMonitorRight_2)
        self.thongtinFrameMonitorRightQ_2.setObjectName(u"thongtinFrameMonitorRightQ_2")
        self.verticalLayout_103 = QVBoxLayout(self.thongtinFrameMonitorRightQ_2)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(1, 1, 1, 1)
        self.txtQNhanVien_2 = QLineEdit(self.thongtinFrameMonitorRightQ_2)
        self.txtQNhanVien_2.setObjectName(u"txtQNhanVien_2")
        sizePolicy6.setHeightForWidth(self.txtQNhanVien_2.sizePolicy().hasHeightForWidth())
        self.txtQNhanVien_2.setSizePolicy(sizePolicy6)
        self.txtQNhanVien_2.setMinimumSize(QSize(130, 35))
        self.txtQNhanVien_2.setMaximumSize(QSize(130, 35))
        self.txtQNhanVien_2.setFont(font7)
        self.txtQNhanVien_2.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQNhanVien_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQNhanVien_2.setReadOnly(True)

        self.verticalLayout_103.addWidget(self.txtQNhanVien_2)

        self.txtQSdt_2 = QLineEdit(self.thongtinFrameMonitorRightQ_2)
        self.txtQSdt_2.setObjectName(u"txtQSdt_2")
        sizePolicy6.setHeightForWidth(self.txtQSdt_2.sizePolicy().hasHeightForWidth())
        self.txtQSdt_2.setSizePolicy(sizePolicy6)
        self.txtQSdt_2.setMinimumSize(QSize(130, 35))
        self.txtQSdt_2.setMaximumSize(QSize(130, 35))
        self.txtQSdt_2.setFont(font7)
        self.txtQSdt_2.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQSdt_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQSdt_2.setReadOnly(True)

        self.verticalLayout_103.addWidget(self.txtQSdt_2)

        self.float_12 = QFrame(self.thongtinFrameMonitorRightQ_2)
        self.float_12.setObjectName(u"float_12")
        self.verticalLayout_104 = QVBoxLayout(self.float_12)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")

        self.verticalLayout_103.addWidget(self.float_12)


        self.horizontalLayout_34.addWidget(self.thongtinFrameMonitorRightQ_2)

        self.thongtinFrameMonitorRightText_2 = QFrame(self.thongtinFrameMonitorRight_2)
        self.thongtinFrameMonitorRightText_2.setObjectName(u"thongtinFrameMonitorRightText_2")
        self.verticalLayout_105 = QVBoxLayout(self.thongtinFrameMonitorRightText_2)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(1, 1, 1, 1)
        self.txtSdtNv = QLineEdit(self.thongtinFrameMonitorRightText_2)
        self.txtSdtNv.setObjectName(u"txtSdtNv")
        self.txtSdtNv.setMinimumSize(QSize(434, 35))
        self.txtSdtNv.setFont(font8)
        self.txtSdtNv.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtSdtNv.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_105.addWidget(self.txtSdtNv)

        self.txtAdmin = QLineEdit(self.thongtinFrameMonitorRightText_2)
        self.txtAdmin.setObjectName(u"txtAdmin")
        self.txtAdmin.setMinimumSize(QSize(434, 35))
        self.txtAdmin.setFont(font8)
        self.txtAdmin.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtAdmin.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txtAdmin.setReadOnly(True)

        self.verticalLayout_105.addWidget(self.txtAdmin)

        self.float_13 = QFrame(self.thongtinFrameMonitorRightText_2)
        self.float_13.setObjectName(u"float_13")
        self.verticalLayout_106 = QVBoxLayout(self.float_13)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")

        self.verticalLayout_105.addWidget(self.float_13)


        self.horizontalLayout_34.addWidget(self.thongtinFrameMonitorRightText_2)


        self.horizontalLayout_32.addWidget(self.thongtinFrameMonitorRight_2)


        self.thongtinFrame_4.addWidget(self.thongtinFrameMonitor_2)


        self.verticalLayout_113.addWidget(self.thongtinFrame_3)

        self.matkhauFrame_2 = QFrame(self.adminFrame)
        self.matkhauFrame_2.setObjectName(u"matkhauFrame_2")
        self.verticalLayout_107 = QVBoxLayout(self.matkhauFrame_2)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(1, 1, 1, 1)
        self.matkhauFrameTitle_2 = QFrame(self.matkhauFrame_2)
        self.matkhauFrameTitle_2.setObjectName(u"matkhauFrameTitle_2")
        self.matkhauFrameTitle_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_108 = QVBoxLayout(self.matkhauFrameTitle_2)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.txtmatkhauFrameTitle_2 = QLabel(self.matkhauFrameTitle_2)
        self.txtmatkhauFrameTitle_2.setObjectName(u"txtmatkhauFrameTitle_2")
        self.txtmatkhauFrameTitle_2.setFont(font1)
        self.txtmatkhauFrameTitle_2.setStyleSheet(u"")

        self.verticalLayout_108.addWidget(self.txtmatkhauFrameTitle_2)


        self.verticalLayout_107.addWidget(self.matkhauFrameTitle_2)

        self.matkhauFrameMonitor_2 = QFrame(self.matkhauFrame_2)
        self.matkhauFrameMonitor_2.setObjectName(u"matkhauFrameMonitor_2")
        sizePolicy5.setHeightForWidth(self.matkhauFrameMonitor_2.sizePolicy().hasHeightForWidth())
        self.matkhauFrameMonitor_2.setSizePolicy(sizePolicy5)
        self.matkhauFrameMonitor_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.horizontalLayout_35 = QHBoxLayout(self.matkhauFrameMonitor_2)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(1, 1, 1, 1)
        self.matkhauFrameMonitorPass_2 = QFrame(self.matkhauFrameMonitor_2)
        self.matkhauFrameMonitorPass_2.setObjectName(u"matkhauFrameMonitorPass_2")
        self.horizontalLayout_36 = QHBoxLayout(self.matkhauFrameMonitorPass_2)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(1, 1, 1, 1)
        self.matkhauFrameMPleft_2 = QFrame(self.matkhauFrameMonitorPass_2)
        self.matkhauFrameMPleft_2.setObjectName(u"matkhauFrameMPleft_2")
        self.verticalLayout_109 = QVBoxLayout(self.matkhauFrameMPleft_2)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(1, 1, 1, 1)
        self.txtQTenTK_2 = QLineEdit(self.matkhauFrameMPleft_2)
        self.txtQTenTK_2.setObjectName(u"txtQTenTK_2")
        sizePolicy6.setHeightForWidth(self.txtQTenTK_2.sizePolicy().hasHeightForWidth())
        self.txtQTenTK_2.setSizePolicy(sizePolicy6)
        self.txtQTenTK_2.setMinimumSize(QSize(130, 35))
        self.txtQTenTK_2.setMaximumSize(QSize(130, 35))
        self.txtQTenTK_2.setFont(font7)
        self.txtQTenTK_2.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQTenTK_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQTenTK_2.setReadOnly(True)

        self.verticalLayout_109.addWidget(self.txtQTenTK_2)

        self.txtQMatKhau_2 = QLineEdit(self.matkhauFrameMPleft_2)
        self.txtQMatKhau_2.setObjectName(u"txtQMatKhau_2")
        sizePolicy6.setHeightForWidth(self.txtQMatKhau_2.sizePolicy().hasHeightForWidth())
        self.txtQMatKhau_2.setSizePolicy(sizePolicy6)
        self.txtQMatKhau_2.setMinimumSize(QSize(130, 35))
        self.txtQMatKhau_2.setMaximumSize(QSize(130, 35))
        self.txtQMatKhau_2.setFont(font7)
        self.txtQMatKhau_2.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQMatKhau_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQMatKhau_2.setReadOnly(True)

        self.verticalLayout_109.addWidget(self.txtQMatKhau_2)

        self.txtQNhapLai_2 = QLineEdit(self.matkhauFrameMPleft_2)
        self.txtQNhapLai_2.setObjectName(u"txtQNhapLai_2")
        sizePolicy6.setHeightForWidth(self.txtQNhapLai_2.sizePolicy().hasHeightForWidth())
        self.txtQNhapLai_2.setSizePolicy(sizePolicy6)
        self.txtQNhapLai_2.setMinimumSize(QSize(130, 35))
        self.txtQNhapLai_2.setMaximumSize(QSize(130, 35))
        self.txtQNhapLai_2.setFont(font7)
        self.txtQNhapLai_2.setStyleSheet(u"background-color: rgb(26, 29, 36);")
        self.txtQNhapLai_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtQNhapLai_2.setReadOnly(True)

        self.verticalLayout_109.addWidget(self.txtQNhapLai_2)


        self.horizontalLayout_36.addWidget(self.matkhauFrameMPleft_2)

        self.matkhauFrameMPright_2 = QFrame(self.matkhauFrameMonitorPass_2)
        self.matkhauFrameMPright_2.setObjectName(u"matkhauFrameMPright_2")
        self.verticalLayout_110 = QVBoxLayout(self.matkhauFrameMPright_2)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(1, 1, 1, 1)
        self.txtTenTKNv = QLineEdit(self.matkhauFrameMPright_2)
        self.txtTenTKNv.setObjectName(u"txtTenTKNv")
        self.txtTenTKNv.setMinimumSize(QSize(434, 35))
        self.txtTenTKNv.setFont(font8)
        self.txtTenTKNv.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtTenTKNv.setAlignment(Qt.AlignCenter)

        self.verticalLayout_110.addWidget(self.txtTenTKNv)

        self.txtMatKhauNv = QLineEdit(self.matkhauFrameMPright_2)
        self.txtMatKhauNv.setObjectName(u"txtMatKhauNv")
        self.txtMatKhauNv.setMinimumSize(QSize(434, 35))
        self.txtMatKhauNv.setFont(font8)
        self.txtMatKhauNv.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtMatKhauNv.setEchoMode(QLineEdit.Password)
        self.txtMatKhauNv.setAlignment(Qt.AlignCenter)

        self.verticalLayout_110.addWidget(self.txtMatKhauNv)

        self.txtNhapLaiNv = QLineEdit(self.matkhauFrameMPright_2)
        self.txtNhapLaiNv.setObjectName(u"txtNhapLaiNv")
        self.txtNhapLaiNv.setMinimumSize(QSize(434, 35))
        self.txtNhapLaiNv.setFont(font8)
        self.txtNhapLaiNv.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-color: rgb(26, 29, 36);")
        self.txtNhapLaiNv.setEchoMode(QLineEdit.Password)
        self.txtNhapLaiNv.setAlignment(Qt.AlignCenter)

        self.verticalLayout_110.addWidget(self.txtNhapLaiNv)


        self.horizontalLayout_36.addWidget(self.matkhauFrameMPright_2)


        self.horizontalLayout_35.addWidget(self.matkhauFrameMonitorPass_2)

        self.matkhauFrameMonitorButton_2 = QFrame(self.matkhauFrameMonitor_2)
        self.matkhauFrameMonitorButton_2.setObjectName(u"matkhauFrameMonitorButton_2")
        self.verticalLayout_111 = QVBoxLayout(self.matkhauFrameMonitorButton_2)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(1, 1, 1, 1)
        self.float_14 = QFrame(self.matkhauFrameMonitorButton_2)
        self.float_14.setObjectName(u"float_14")
        self.verticalLayout_112 = QVBoxLayout(self.float_14)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")

        self.verticalLayout_111.addWidget(self.float_14)

        self.btnDangKyNv = QPushButton(self.matkhauFrameMonitorButton_2)
        self.btnDangKyNv.setObjectName(u"btnDangKyNv")
        self.btnDangKyNv.setMinimumSize(QSize(150, 30))
        self.btnDangKyNv.setFont(font4)
        self.btnDangKyNv.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btnDangKyNv.setIcon(icon9)

        self.verticalLayout_111.addWidget(self.btnDangKyNv)


        self.horizontalLayout_35.addWidget(self.matkhauFrameMonitorButton_2)


        self.verticalLayout_107.addWidget(self.matkhauFrameMonitor_2)


        self.verticalLayout_113.addWidget(self.matkhauFrame_2)


        self.verticalLayout_78.addWidget(self.adminFrame)

        self.stackedWidget.addWidget(self.page_admin)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.widgetFrame = QFrame(self.page_widgets)
        self.widgetFrame.setObjectName(u"widgetFrame")
        self.widgetFrame.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.verticalLayout_7 = QVBoxLayout(self.widgetFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.widgetFrameUp = QFrame(self.widgetFrame)
        self.widgetFrameUp.setObjectName(u"widgetFrameUp")
        self.verticalLayout_8 = QVBoxLayout(self.widgetFrameUp)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.float_7 = QFrame(self.widgetFrameUp)
        self.float_7.setObjectName(u"float_7")
        sizePolicy5.setHeightForWidth(self.float_7.sizePolicy().hasHeightForWidth())
        self.float_7.setSizePolicy(sizePolicy5)
        self.verticalLayout_15 = QVBoxLayout(self.float_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")

        self.verticalLayout_8.addWidget(self.float_7)

        self.txtwidgetFrameUp = QLabel(self.widgetFrameUp)
        self.txtwidgetFrameUp.setObjectName(u"txtwidgetFrameUp")
        self.txtwidgetFrameUp.setFont(font7)
        self.txtwidgetFrameUp.setStyleSheet(u"")
        self.txtwidgetFrameUp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.txtwidgetFrameUp)


        self.verticalLayout_7.addWidget(self.widgetFrameUp)

        self.widgetFrameDown = QFrame(self.widgetFrame)
        self.widgetFrameDown.setObjectName(u"widgetFrameDown")
        self.horizontalLayout_9 = QHBoxLayout(self.widgetFrameDown)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.widgetFrameDownLeft = QFrame(self.widgetFrameDown)
        self.widgetFrameDownLeft.setObjectName(u"widgetFrameDownLeft")
        self.verticalLayout_91 = QVBoxLayout(self.widgetFrameDownLeft)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(1, 1, 1, 1)
        self.btnOLai = QPushButton(self.widgetFrameDownLeft)
        self.btnOLai.setObjectName(u"btnOLai")
        self.btnOLai.setMinimumSize(QSize(150, 30))
        self.btnOLai.setMaximumSize(QSize(150, 30))
        self.btnOLai.setFont(font4)
        self.btnOLai.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/16x16/icons/16x16/cil-account-logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnOLai.setIcon(icon11)
        self.btnOLai.setCheckable(False)

        self.verticalLayout_91.addWidget(self.btnOLai, 0, Qt.AlignRight|Qt.AlignTop)

        self.float_8 = QFrame(self.widgetFrameDownLeft)
        self.float_8.setObjectName(u"float_8")
        self.verticalLayout_92 = QVBoxLayout(self.float_8)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")

        self.verticalLayout_91.addWidget(self.float_8)


        self.horizontalLayout_9.addWidget(self.widgetFrameDownLeft)

        self.widgetFrameDownRight = QFrame(self.widgetFrameDown)
        self.widgetFrameDownRight.setObjectName(u"widgetFrameDownRight")
        self.verticalLayout_11 = QVBoxLayout(self.widgetFrameDownRight)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.btnThoat = QPushButton(self.widgetFrameDownRight)
        self.btnThoat.setObjectName(u"btnThoat")
        self.btnThoat.setMinimumSize(QSize(150, 30))
        self.btnThoat.setMaximumSize(QSize(150, 30))
        self.btnThoat.setFont(font4)
        self.btnThoat.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/16x16/icons/16x16/cil-exit-to-app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnThoat.setIcon(icon12)

        self.verticalLayout_11.addWidget(self.btnThoat, 0, Qt.AlignLeft|Qt.AlignTop)

        self.float_9 = QFrame(self.widgetFrameDownRight)
        self.float_9.setObjectName(u"float_9")
        self.verticalLayout_93 = QVBoxLayout(self.float_9)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")

        self.verticalLayout_11.addWidget(self.float_9)


        self.horizontalLayout_9.addWidget(self.widgetFrameDownRight)


        self.verticalLayout_7.addWidget(self.widgetFrameDown)


        self.verticalLayout_6.addWidget(self.widgetFrame)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)

        self.label_version.raise_()
        self.label_credits.raise_()

        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btnOLai, self.btnThoat)
        QWidget.setTabOrder(self.btnThoat, self.txtTenNv)
        QWidget.setTabOrder(self.txtTenNv, self.txtDiaChiNv)
        QWidget.setTabOrder(self.txtDiaChiNv, self.txtSdtNv)
        QWidget.setTabOrder(self.txtSdtNv, self.txtAdmin)
        QWidget.setTabOrder(self.txtAdmin, self.txtTenTKNv)
        QWidget.setTabOrder(self.txtTenTKNv, self.txtMatKhauNv)
        QWidget.setTabOrder(self.txtMatKhauNv, self.txtNhapLaiNv)
        QWidget.setTabOrder(self.txtNhapLaiNv, self.btnDangKyNv)
        QWidget.setTabOrder(self.btnDangKyNv, self.txtTenKhach)
        QWidget.setTabOrder(self.txtTenKhach, self.txtDiaChi)
        QWidget.setTabOrder(self.txtDiaChi, self.txtSdt)
        QWidget.setTabOrder(self.txtSdt, self.cboLoaiXe)
        QWidget.setTabOrder(self.cboLoaiXe, self.txtSoXe)
        QWidget.setTabOrder(self.txtSoXe, self.txtNhanVien)
        QWidget.setTabOrder(self.txtNhanVien, self.txtTenTK)
        QWidget.setTabOrder(self.txtTenTK, self.txtMatKhau)
        QWidget.setTabOrder(self.txtMatKhau, self.txtNhapLai)
        QWidget.setTabOrder(self.txtNhapLai, self.btnDangKy)
        QWidget.setTabOrder(self.btnDangKy, self.txtTenLoai)
        QWidget.setTabOrder(self.txtTenLoai, self.txtSoCho)
        QWidget.setTabOrder(self.txtSoCho, self.txtDonGia)
        QWidget.setTabOrder(self.txtDonGia, self.btnThemLoai)
        QWidget.setTabOrder(self.btnThemLoai, self.txtfindName)
        QWidget.setTabOrder(self.txtfindName, self.btnTimKiem)
        QWidget.setTabOrder(self.btnTimKiem, self.btnXoaTrang)
        QWidget.setTabOrder(self.btnXoaTrang, self.txtfindNum)
        QWidget.setTabOrder(self.txtfindNum, self.btnTimKiem_2)
        QWidget.setTabOrder(self.btnTimKiem_2, self.btnXoaTrang_2)
        QWidget.setTabOrder(self.btnXoaTrang_2, self.btnChonAnh)
        QWidget.setTabOrder(self.btnChonAnh, self.btnXuLy)
        QWidget.setTabOrder(self.btnXuLy, self.btnTachChu)
        QWidget.setTabOrder(self.btnTachChu, self.btnLuu)
        QWidget.setTabOrder(self.btnLuu, self.btnChonAnh_2)
        QWidget.setTabOrder(self.btnChonAnh_2, self.btnXuLy_2)
        QWidget.setTabOrder(self.btnXuLy_2, self.btnTachChu_2)
        QWidget.setTabOrder(self.btnTachChu_2, self.btnLuu_2)
        QWidget.setTabOrder(self.btnLuu_2, self.btn_minimize)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.txtChuSo_2)
        QWidget.setTabOrder(self.txtChuSo_2, self.txtQTenKhach)
        QWidget.setTabOrder(self.txtQTenKhach, self.txtQDiaChi)
        QWidget.setTabOrder(self.txtQDiaChi, self.txtQTenTK)
        QWidget.setTabOrder(self.txtQTenTK, self.txtQMatKhau)
        QWidget.setTabOrder(self.txtQMatKhau, self.txtQNhapLai)
        QWidget.setTabOrder(self.txtQNhapLai, self.txtQThoiGianRa)
        QWidget.setTabOrder(self.txtQThoiGianRa, self.txtBienSo)
        QWidget.setTabOrder(self.txtBienSo, self.txtThoiGianVao)
        QWidget.setTabOrder(self.txtThoiGianVao, self.txtThoiGianRa)
        QWidget.setTabOrder(self.txtThoiGianRa, self.txtQTenTK_3)
        QWidget.setTabOrder(self.txtQTenTK_3, self.txtQMatKhau_3)
        QWidget.setTabOrder(self.txtQMatKhau_3, self.txtQNhapLai_3)
        QWidget.setTabOrder(self.txtQNhapLai_3, self.txtLichSu1)
        QWidget.setTabOrder(self.txtLichSu1, self.txtLichSu2)
        QWidget.setTabOrder(self.txtLichSu2, self.txtQBienSo)
        QWidget.setTabOrder(self.txtQBienSo, self.txtQThoiGianVao)
        QWidget.setTabOrder(self.txtQThoiGianVao, self.txtQTenNv)
        QWidget.setTabOrder(self.txtQTenNv, self.txtQDiaChi_2)
        QWidget.setTabOrder(self.txtQDiaChi_2, self.txtQLoaiXe)
        QWidget.setTabOrder(self.txtQLoaiXe, self.txtQSoXe)
        QWidget.setTabOrder(self.txtQSoXe, self.txtQNhanVien_2)
        QWidget.setTabOrder(self.txtQNhanVien_2, self.txtQSdt_2)
        QWidget.setTabOrder(self.txtQSdt_2, self.txtQNhanVien)
        QWidget.setTabOrder(self.txtQNhanVien, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.txtQTenTK_2)
        QWidget.setTabOrder(self.txtQTenTK_2, self.txtQMatKhau_2)
        QWidget.setTabOrder(self.txtQMatKhau_2, self.txtQNhapLai_2)
        QWidget.setTabOrder(self.txtQNhapLai_2, self.txtLichSu3)
        QWidget.setTabOrder(self.txtLichSu3, self.txtLichSu4)
        QWidget.setTabOrder(self.txtLichSu4, self.txtChuSo)
        QWidget.setTabOrder(self.txtChuSo, self.txtQTongSoNgay)
        QWidget.setTabOrder(self.txtQTongSoNgay, self.txtQSdt)
        QWidget.setTabOrder(self.txtQSdt, self.txtTongSoNgay)
        QWidget.setTabOrder(self.txtTongSoNgay, self.txtQTongSoThang)
        QWidget.setTabOrder(self.txtQTongSoThang, self.txtTongSoThang)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)

        #design QMessenger
        self.qm = QMessageBox()
        self.qm.setObjectName(u"qm")
        #self.qm.setMinimumSize(QSize(434, 80))
        self.qm.setFont(font6)
        self.qm.setStyleSheet(u"color: rgb(254, 121, 199);\n"
                                      "background-color: rgb(26, 29, 36);")


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"TP", None))
        self.btnChonAnh.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn \u1ea2nh", None))
        self.btnXuLy.setText(QCoreApplication.translate("MainWindow", u"X\u1eed L\u00fd", None))
        self.btnTachChu.setText(QCoreApplication.translate("MainWindow", u"T\u00e1ch Ch\u1eef", None))
        self.btnLuu.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u", None))
        self.btnChonAnh_2.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn \u1ea2nh", None))
        self.btnXuLy_2.setText(QCoreApplication.translate("MainWindow", u"X\u1eed L\u00fd", None))
        self.btnTachChu_2.setText(QCoreApplication.translate("MainWindow", u"T\u00e1ch Ch\u1eef", None))
        self.btnLuu_2.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u", None))
        self.txtfindNameTitle.setText(QCoreApplication.translate("MainWindow", u"T\u00ccM THEO T\u00caN KH\u00c1CH H\u00c0NG", None))
        self.txtfindName.setText("")
        self.btnTimKiem.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm", None))
        self.btnXoaTrang.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a tr\u1eafng", None))
        self.txtfindNumTitle.setText(QCoreApplication.translate("MainWindow", u"T\u00ccM THEO BI\u1ec2N S\u1ed0", None))
        self.txtfindNum.setText("")
        self.btnTimKiem_2.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm", None))
        self.btnXoaTrang_2.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a tr\u1eafng", None))
        self.txtframeDisplayTitle.setText(QCoreApplication.translate("MainWindow", u"K\u1ebeT QU\u1ea2 T\u00ccM KI\u1ebeM", None))
        self.txtQBienSo.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3n s\u1ed1:", None))
        self.txtQThoiGianVao.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian v\u00e0o:", None))
        self.txtQThoiGianRa.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian ra:", None))
        self.txtBienSo.setText("")
        self.txtThoiGianVao.setText("")
        self.txtThoiGianRa.setText("")
        self.txtframeHistoryTitle.setText(QCoreApplication.translate("MainWindow", u"L\u1ecaCH S\u1eec T\u00ccM KI\u1ebeM", None))
        self.txtLichSu1.setText("")
        self.txtLichSu2.setText("")
        self.txtLichSu3.setText("")
        self.txtLichSu4.setText("")
        self.txtchartFrameLeft_Title.setText(QCoreApplication.translate("MainWindow", u"TH\u1ed0NG K\u00ca THEO NG\u00c0Y", None))
        self.txtframe_chartLeft_title.setText(QCoreApplication.translate("MainWindow", u"L\u01af\u1ee2T KH\u00c1CH H\u00c0NG", None))
        self.txtLuotKHNgay.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtframe_chartRight_title.setText(QCoreApplication.translate("MainWindow", u"L\u01af\u1ee2T KH\u00c1CH V\u00c3N LAI", None))
        self.txtLuotKNgay.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtframe_chartTotal_title.setText(QCoreApplication.translate("MainWindow", u"S\u1ed0 L\u01af\u1ee2T THEO NG\u00c0Y", None))
        self.txtQTongSoNgay.setText(QCoreApplication.translate("MainWindow", u"L\u01b0\u1ee3t ng\u00e0y:", None))
        self.txtTongSoNgay.setText("")
        self.txtchartFrameRight_Title.setText(QCoreApplication.translate("MainWindow", u"TH\u1ed0NG K\u00ca THEO TH\u00c1NG", None))
        self.txtframe_chartLeftMonitor_title.setText(QCoreApplication.translate("MainWindow", u"L\u01af\u1ee2T KH\u00c1CH H\u00c0NG", None))
        self.txtLuotKHThang.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtframe_chartRightMonitor_title.setText(QCoreApplication.translate("MainWindow", u"L\u01af\u1ee2T KH\u00c1CH V\u00c3N LAI", None))
        self.txtLuotKThang.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txtframe_chartRightTotal_title.setText(QCoreApplication.translate("MainWindow", u"S\u1ed0 L\u01af\u1ee2T THEO TH\u00c1NG", None))
        self.txtQTongSoThang.setText(QCoreApplication.translate("MainWindow", u"L\u01b0\u1ee3t th\u00e1ng:", None))
        self.txtTongSoThang.setText("")
        self.txtthongtinFrameTitle.setText(QCoreApplication.translate("MainWindow", u"TH\u00d4NG TIN KH\u00c1CH H\u00c0NG", None))
        self.txtQTenKhach.setText(QCoreApplication.translate("MainWindow", u"T\u00ean kh\u00e1ch:", None))
        self.txtQDiaChi.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9:", None))
        self.txtQSdt.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i:", None))
        self.txtTenKhach.setText("")
        self.txtDiaChi.setText("")
        self.txtSdt.setText("")
        self.txtQLoaiXe.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i xe:", None))
        self.txtQSoXe.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 xe:", None))
        self.txtQNhanVien.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e2n vi\u00ean:", None))
        self.txtSoXe.setText("")
        self.txtNhanVien.setText("")
        self.txtQTenTK.setText(QCoreApplication.translate("MainWindow", u"T\u00ean t\u00e0i kho\u1ea3n:", None))
        self.txtQMatKhau.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u:", None))
        self.txtQNhapLai.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp l\u1ea1i:", None))
        self.txtTenTK.setText("")
        self.txtMatKhau.setText("")
        self.txtNhapLai.setText("")
        self.btnDangKy.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng k\u00fd", None))
        self.txtloaixeFrameTitle.setText(QCoreApplication.translate("MainWindow", u"TH\u00d4NG TIN LO\u1ea0I XE", None))
        self.txtQTenTK_3.setText(QCoreApplication.translate("MainWindow", u"T\u00ean lo\u1ea1i:", None))
        self.txtQMatKhau_3.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 ch\u1ed7:", None))
        self.txtQNhapLai_3.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a1n gi\u00e1:", None))
        self.txtTenLoai.setText("")
        self.txtSoCho.setText("")
        self.txtDonGia.setText("")
        self.btnThemLoai.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam lo\u1ea1i", None))
        self.txtthongtinFrameTitle_2.setText(QCoreApplication.translate("MainWindow", u"TH\u00d4NG TIN NH\u00c2N VI\u00caN", None))
        self.txtQTenNv.setText(QCoreApplication.translate("MainWindow", u"T\u00ean nh\u00e2n vi\u00ean:", None))
        self.txtQDiaChi_2.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9:", None))
        self.txtTenNv.setText("")
        self.txtDiaChiNv.setText("")
        self.txtQNhanVien_2.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i:", None))
        self.txtQSdt_2.setText(QCoreApplication.translate("MainWindow", u"Admin:", None))
        self.txtSdtNv.setText("")
        self.txtAdmin.setText("")
        self.txtmatkhauFrameTitle_2.setText(QCoreApplication.translate("MainWindow", u"TH\u00d4NG T\u00c0I KHO\u1ea2N", None))
        self.txtQTenTK_2.setText(QCoreApplication.translate("MainWindow", u"T\u00ean t\u00e0i kho\u1ea3n:", None))
        self.txtQMatKhau_2.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u:", None))
        self.txtQNhapLai_2.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp l\u1ea1i:", None))
        self.txtTenTKNv.setText("")
        self.txtMatKhauNv.setText("")
        self.txtNhapLaiNv.setText("")
        self.btnDangKyNv.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng k\u00fd", None))
        self.txtwidgetFrameUp.setText(QCoreApplication.translate("MainWindow", u"B\u1ea1n c\u00f3 th\u1eadt s\u1ef1 mu\u1ed1n tho\u00e1t kh\u00f4ng?", None))
        self.btnOLai.setText(QCoreApplication.translate("MainWindow", u"\u1ede l\u1ea1i", None))
        self.btnThoat.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadn di\u1ec7n bi\u1ec3n s\u1ed1 xe", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.2", None))
    # retranslateUi

