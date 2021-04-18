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
            AdminLogWindow.setObjectName(u"AdminLogWindow")
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
        font1.setPointSize(9)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.label_description_2 = QLabel(self.frmAdmin)
        self.label_description_2.setObjectName(u"label_description_2")
        self.label_description_2.setGeometry(QRect(70, 190, 511, 131))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_description_2.setFont(font2)
        self.label_description_2.setCursor(QCursor(Qt.IBeamCursor))
        self.label_description_2.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description_2.setAlignment(Qt.AlignCenter)
        self.btnTroVe = QCommandLinkButton(self.frmAdmin)
        self.btnTroVe.setObjectName(u"btnTroVe")
        self.btnTroVe.setGeometry(QRect(540, 330, 91, 41))
        self.btnTroVe.setFont(font2)
        self.btnTroVe.setStyleSheet(u"color: rgb(254, 121, 199);")
        icon = QIcon()
        icon.addFile(u":/login/icons/24x24/cil-exit-to-app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnTroVe.setIcon(icon)
        self.btnThoat = QCommandLinkButton(self.frmAdmin)
        self.btnThoat.setObjectName(u"btnThoat")
        self.btnThoat.setGeometry(QRect(540, 370, 91, 41))
        self.btnThoat.setFont(font2)
        self.btnThoat.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.btnThoat.setIcon(icon)
        AdminLogWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AdminLogWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 674, 21))
        AdminLogWindow.setMenuBar(self.menubar)

        self.retranslateUi(AdminLogWindow)

        QMetaObject.connectSlotsByName(AdminLogWindow)
    # setupUi

    def retranslateUi(self, AdminLogWindow):
        AdminLogWindow.setWindowTitle(QCoreApplication.translate("AdminLogWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("AdminLogWindow", u"<strong>TH\u00d4NG TIN</strong> ADMIN", None))
        self.label_description.setText(QCoreApplication.translate("AdminLogWindow", u"<strong>B\u00caN D\u01af\u1edaI</strong> L\u00c0 TH\u00d4NG TIN ADMIN", None))
#if QT_CONFIG(tooltip)
        self.label_description_2.setToolTip(QCoreApplication.translate("AdminLogWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_description_2.setText(QCoreApplication.translate("AdminLogWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nguy\u1ec5n Thanh Phong - 1711060497</span></p><p align=\"center\"><span style=\" font-weight:600;\">Sinh vi\u00ean t\u1ea1i HUTECH, kh\u00f3a 17</span></p><p align=\"center\"><span style=\" font-weight:600;\">S\u1ed1 \u0111i\u1ec7n tho\u1ea1i: 0789631459</span></p><p align=\"center\"><span style=\" font-weight:600;\">N\u1ebfu c\u00f3 b\u1ea5t k\u1ef3 th\u1eafc m\u1eafc vui l\u00f2ng li\u00ean h\u1ec7 s\u1ed1 \u0111i\u1ec7n tho\u1ea1i \u1edf tr\u00ean!</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btnTroVe.setToolTip(QCoreApplication.translate("AdminLogWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Tr\u1edf v\u1ec1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnTroVe.setText(QCoreApplication.translate("AdminLogWindow", u"TR\u1ede V\u1ec0", None))
        self.btnTroVe.setDescription("")
#if QT_CONFIG(tooltip)
        self.btnThoat.setToolTip(QCoreApplication.translate("AdminLogWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Tho\u00e1t</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnThoat.setText(QCoreApplication.translate("AdminLogWindow", u"THO\u00c1T", None))
        self.btnThoat.setDescription("")
    # retranslateUi

