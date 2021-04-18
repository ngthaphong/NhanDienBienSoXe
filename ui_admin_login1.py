# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_AdminLogWindow(object):
    def setupUi(self, AdminLogWindow):
        if not AdminLogWindow.objectName():
            AdminLogWindow.setObjectName(u"MainWindow")
        AdminLogWindow.resize(674, 469)
        self.centralwidget = QWidget(AdminLogWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frmAdmin = QFrame(self.centralwidget)
        self.frmAdmin.setObjectName(u"frmAdmin")
        self.frmAdmin.setGeometry(QRect(10, 10, 654, 427))
        self.frmAdmin.setStyleSheet(u"QFrame {	\n"
"	background-color: rgb(56, 58, 89);	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.frmAdmin.setFrameShape(QFrame.StyledPanel)
        self.frmAdmin.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frmAdmin)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 80, 661, 71))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.frmAdmin)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.btnDangNhap = QPushButton(self.frmAdmin)
        self.btnDangNhap.setObjectName(u"btnDangNhap")
        self.btnDangNhap.setGeometry(QRect(290, 280, 121, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        self.btnDangNhap.setFont(font2)
        self.btnDangNhap.setStyleSheet(u"background-color: rgb(74, 77, 117);\n"
"color: rgb(254, 121, 199);\n"
"border-color: rgb(128, 133, 203);\n"
"selection-background-color: rgb(20, 21, 33);")
        self.txtTenTK = QLineEdit(self.frmAdmin)
        self.txtTenTK.setObjectName(u"txtTenTK")
        self.txtTenTK.setGeometry(QRect(240, 190, 291, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.txtTenTK.setFont(font3)
        self.txtTenTK.setStyleSheet(u"background-color: rgb(96, 100, 153);\n"
"color: rgb(254, 121, 199);")
        self.label_description_2 = QLabel(self.frmAdmin)
        self.label_description_2.setObjectName(u"label_description_2")
        self.label_description_2.setGeometry(QRect(70, 190, 161, 31))
        self.label_description_2.setFont(font3)
        self.label_description_2.setCursor(QCursor(Qt.IBeamCursor))
        self.label_description_2.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description_2.setAlignment(Qt.AlignCenter)
        self.label_description_3 = QLabel(self.frmAdmin)
        self.label_description_3.setObjectName(u"label_description_3")
        self.label_description_3.setGeometry(QRect(70, 230, 161, 31))
        self.label_description_3.setFont(font3)
        self.label_description_3.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description_3.setAlignment(Qt.AlignCenter)
        self.txtMatKhau = QLineEdit(self.frmAdmin)
        self.txtMatKhau.setObjectName(u"txtMatKhau")
        self.txtMatKhau.setGeometry(QRect(240, 230, 291, 31))
        self.txtMatKhau.setFont(font3)
        self.txtMatKhau.setEchoMode(QLineEdit.Password)
        self.txtMatKhau.setStyleSheet(u"background-color: rgb(96, 100, 153);\n"
"color: rgb(254, 121, 199);")
        self.btnTroVe = QCommandLinkButton(self.frmAdmin)
        self.btnTroVe.setObjectName(u"btnTroVe")
        self.btnTroVe.setGeometry(QRect(540, 370, 91, 41))
        self.btnTroVe.setFont(font3)
        self.btnTroVe.setStyleSheet(u"color: rgb(254, 121, 199);")
        icon = QIcon()
        icon.addFile(u":/20x20/icons/20x20/cil-exit-to-app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnTroVe.setIcon(icon)
        AdminLogWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AdminLogWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 674, 21))
        AdminLogWindow.setMenuBar(self.menubar)

        self.retranslateUi(AdminLogWindow)

        QMetaObject.connectSlotsByName(AdminLogWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<strong>ADMINISTRATOR</strong> LOGIN", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"<strong>VUI L\u00d2NG</strong> \u0110I\u1ec0N \u0110\u1ea6Y \u0110\u1ee6 TH\u00d4NG TIN V\u00c0O B\u00caN D\u01af\u1edaI", None))
        self.btnDangNhap.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0102NG NH\u1eacP", None))
#if QT_CONFIG(tooltip)
        self.label_description_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_description_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><strong><p align=\"right\">T\u00caN T\u00c0I KHO\u1ea2N</p></strong></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_description_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_description_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><strong><p align=\"right\">M\u1eacT KH\u1ea8U</p></strong></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btnTroVe.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><strong><p align=\"center\">QU\u00caN M\u1eacT KH\u1ea8U</p></strong></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnTroVe.setText(QCoreApplication.translate("MainWindow", u"TR\u1ede V\u1ec0", None))
    # retranslateUi

