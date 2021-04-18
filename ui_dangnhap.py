# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_LogWindow(object):
    def setupUi(self, LogWindow):
        if not LogWindow.objectName():
            LogWindow.setObjectName(u"MainWindow")
        LogWindow.resize(672, 467)
        self.centralwidget = QWidget(LogWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frmDangNhap = QFrame(self.centralwidget)
        self.frmDangNhap.setObjectName(u"frmDangNhap")
        self.frmDangNhap.setStyleSheet(u"QFrame {	\n"
                                       "	background-color: rgb(56, 58, 89);	\n"
                                       "	color: rgb(220, 220, 220);\n"
                                       "	border-radius: 10px;\n"
                                       "}")
        self.frmDangNhap.setFrameShape(QFrame.StyledPanel)
        self.frmDangNhap.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frmDangNhap)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 80, 661, 71))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.frmDangNhap)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.btnDangNhap = QPushButton(self.frmDangNhap)
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
        self.txtTenTK = QLineEdit(self.frmDangNhap)
        self.txtTenTK.setObjectName(u"txtTenTK")
        self.txtTenTK.setGeometry(QRect(240, 190, 291, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.txtTenTK.setFont(font3)
        self.txtTenTK.setStyleSheet(u"background-color: rgb(96, 100, 153);\n"
                                    "color: rgb(254, 121, 199);")
        self.label_description_2 = QLabel(self.frmDangNhap)
        self.label_description_2.setObjectName(u"label_description_2")
        self.label_description_2.setGeometry(QRect(70, 190, 161, 31))
        self.label_description_2.setFont(font3)
        self.label_description_2.setCursor(QCursor(Qt.IBeamCursor))
        self.label_description_2.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description_2.setAlignment(Qt.AlignCenter)
        self.label_description_3 = QLabel(self.frmDangNhap)
        self.label_description_3.setObjectName(u"label_description_3")
        self.label_description_3.setGeometry(QRect(70, 230, 161, 31))
        self.label_description_3.setFont(font3)
        self.label_description_3.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description_3.setAlignment(Qt.AlignCenter)
        self.txtMatKhau = QLineEdit(self.frmDangNhap)
        self.txtMatKhau.setObjectName(u"txtMatKhau")
        self.txtMatKhau.setGeometry(QRect(240, 230, 291, 31))
        self.txtMatKhau.setFont(font3)
        self.txtMatKhau.setEchoMode(QLineEdit.Password)
        self.txtMatKhau.setStyleSheet(u"background-color: rgb(96, 100, 153);\n"
                                      "color: rgb(254, 121, 199);")
        self.btnQuenMK = QCommandLinkButton(self.frmDangNhap)
        self.btnQuenMK.setObjectName(u"btnQuenMK")
        self.btnQuenMK.setGeometry(QRect(450, 330, 185, 41))
        self.btnQuenMK.setFont(font3)
        self.btnQuenMK.setStyleSheet(u"color: rgb(254, 121, 199);")
        icon = QIcon()
        icon.addFile(u":/20x20/icons/20x20/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnQuenMK.setIcon(icon)
        self.btnQuenMK.hide()
        self.btnAdmin = QCommandLinkButton(self.frmDangNhap)
        self.btnAdmin.setObjectName(u"btnAdmin")
        self.btnAdmin.setGeometry(QRect(450, 380, 185, 41))
        self.btnAdmin.setFont(font3)
        self.btnAdmin.setStyleSheet(u"color: rgb(254, 121, 199);")
        icon1 = QIcon()
        icon1.addFile(u":/20x20/icons/20x20/cil-input.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAdmin.setIcon(icon1)

        self.verticalLayout.addWidget(self.frmDangNhap)

        LogWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LogWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 672, 21))
        LogWindow.setMenuBar(self.menubar)

        self.retranslateUi(LogWindow)

        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(16)

        # design QMessenger
        self.qm = QMessageBox()
        self.qm.setObjectName(u"qm")
        # self.qm.setMinimumSize(QSize(434, 80))
        self.qm.setFont(font6)
        self.qm.setStyleSheet(u"color: rgb(254, 121, 199);\n"
                              "background-color: rgb(26, 29, 36);")

        QMetaObject.connectSlotsByName(LogWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(
            QCoreApplication.translate("MainWindow", u"<strong>NH\u1eacN DI\u1ec6N</strong> BI\u1ec2N S\u1ed0 XE",
                                       None))
        self.label_description.setText(QCoreApplication.translate("MainWindow",
                                                                  u"<strong>VUI L\u00d2NG</strong> \u0110I\u1ec0N \u0110\u1ea6Y \u0110\u1ee6 TH\u00d4NG TIN V\u00c0O B\u00caN D\u01af\u1edaI",
                                                                  None))
        self.btnDangNhap.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0102NG NH\u1eacP", None))
        # if QT_CONFIG(tooltip)
        self.label_description_2.setToolTip(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>",
                                       None))
        # endif // QT_CONFIG(tooltip)
        self.label_description_2.setText(QCoreApplication.translate("MainWindow",
                                                                    u"<html><head/><body><strong><p align=\"right\">T\u00caN T\u00c0I KHO\u1ea2N</p></strong></body></html>",
                                                                    None))
        # if QT_CONFIG(tooltip)
        self.label_description_3.setToolTip(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>",
                                       None))
        # endif // QT_CONFIG(tooltip)
        self.label_description_3.setText(QCoreApplication.translate("MainWindow",
                                                                    u"<html><head/><body><strong><p align=\"right\">M\u1eacT KH\u1ea8U</p></strong></body></html>",
                                                                    None))
        # if QT_CONFIG(tooltip)
        self.btnQuenMK.setToolTip(QCoreApplication.translate("MainWindow",
                                                             u"<html><head/><body><strong><p align=\"center\">QU\u00caN M\u1eacT KH\u1ea8U</p></strong></body></html>",
                                                             None))
        # endif // QT_CONFIG(tooltip)
        self.btnQuenMK.setText(QCoreApplication.translate("MainWindow", u"QU\u00caN M\u1eacT KH\u1ea8U", None))
        # if QT_CONFIG(tooltip)
        self.btnAdmin.setToolTip(QCoreApplication.translate("MainWindow",
                                                            u"<html><head/><body><strong><p align=\"center\">QU\u00caN M\u1eacT KH\u1ea8U</p></strong></body></html>",
                                                            None))
        # endif // QT_CONFIG(tooltip)
        self.btnAdmin.setText(QCoreApplication.translate("MainWindow", u"LI\u00caN H\u1ec6 ADMIN", None))
    # retranslateUi
