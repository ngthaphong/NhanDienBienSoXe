
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtGui import QImage
from collections import deque

import cv2
import numpy as np
from PIL.ImageQt import ImageQt
from skimage.feature import hog
from sklearn.svm import LinearSVC
from keras.datasets import mnist
from sklearn.metrics import accuracy_score

# GUI FILE
from app_modules import *
from ui_dangnhap import Ui_LogWindow
from ui_admin_login import Ui_AdminLogWindow
from ui_splash_screen import Ui_SplashScreen

#counter
counter = 0

class MainWindow(QMainWindow):
    def __init__(self, isadmin, id, model):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.isadmin = isadmin
        self.id = id
        self.model = model
        self.list = deque()

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## GAN CHUC NANG CHO CAC NUT
        #nut TimKiem1 - find
        self.ui.btnTimKiem.clicked.connect(lambda: Functions.checkTimKiem1(self))
        #nut XoaTrang1 - find
        self.ui.btnXoaTrang.clicked.connect(lambda: Functions.checkXoaTrang1(self))
        # nut TimKiem2 - find
        self.ui.btnTimKiem_2.clicked.connect(lambda: Functions.checkTimKiem2(self))
        # nut XoaTrang2 - find
        self.ui.btnXoaTrang_2.clicked.connect(lambda: (Functions.checkXoaTrang2(self), Functions.checkLichSu(self)))
        #nut Luu1 - home
        self.ui.btnLuu.clicked.connect(lambda: Functions.checkLuu1(self))
        #nut Luu2 - home
        self.ui.btnLuu_2.clicked.connect(lambda: Functions.checkLuu2(self))
        #nut TachChu1 - home
        self.ui.btnTachChu.clicked.connect(lambda: UIFunctions.TachChu1(self, Functions.checkTachChu1(self), self.str))
        #nut TachChu2 - home
        self.ui.btnTachChu_2.clicked.connect(lambda: UIFunctions.TachChu2(self, Functions.checkTachChu2(self), self.str))
        #nut XuLy1 - home
        self.ui.btnXuLy.clicked.connect(lambda : UIFunctions.XuLy1(self, Functions.checkXuLy1(self), self.str))
        #nut XuLy2 - home
        self.ui.btnXuLy_2.clicked.connect(lambda : UIFunctions.XuLy2(self, Functions.checkXuLy2(self), self.str))
        #nutChonAnh1 - home
        self.ui.btnChonAnh.clicked.connect(lambda: UIFunctions.ChonAnh1(self, Functions.checkChonAnh1(self), self.str))
        #nut ChonAnh2 - home
        self.ui.btnChonAnh_2.clicked.connect(lambda: UIFunctions.ChonAnh2(self, Functions.checkChonAnh2(self), self.str))
        #them du lieu vao cbo
        UIFunctions.ThemcboLoaiXe(self)
        #nut Thoat - widget
        self.ui.btnThoat.clicked.connect(lambda:UIFunctions.exit(self))
        #nut OLai - widget
        self.ui.btnOLai.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        #nut DangKyNv - admin
        self.ui.btnDangKyNv.clicked.connect(lambda:UIFunctions.DangKyNv(self, Functions.checkDangKyNv(self), self.str))
        #nut DangKy - nhanvien
        self.ui.btnDangKy.clicked.connect(lambda :UIFunctions.DangKy(self, Functions.checkDangKy(self), self.str))
        #nut ThemLoai - nhanvien
        self.ui.btnThemLoai.clicked.connect(lambda: UIFunctions.ThemLoai(self, Functions.checkThemLoai(self), self.str))

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Trang chính')
        UIFunctions.labelTitle(self, 'Trang chính')
        UIFunctions.labelDescription(self, 'Nguyễn Thanh Phong - 1711060497')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "TRANG CHỦ", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "TÌM KIẾM", "btn_find", "url(:/16x16/icons/16x16/cil-screen-desktop.png)", True)
        UIFunctions.addNewMenu(self, "THỐNG KÊ", "btn_chart", "url(:/16x16/icons/16x16/cil-chart-line.png)", True)
        UIFunctions.addNewMenu(self, "NHÂN VIÊN", "btn_nv", "url(:/16x16/icons/16x16/cil-people.png)", True)
        if self.isadmin:
            UIFunctions.addNewMenu(self, "ADMINISTRATOR", "btn_admin", "url(:/16x16/icons/16x16/cil-people.png)", True)
        UIFunctions.addNewMenu(self, "ĐĂNG XUẤT", "btn_logout", "url(:/16x16/icons/16x16/cil-account-logout.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "TP", "", True)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        #self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "TRANG CHỦ")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE TIM KIEM
        if btnWidget.objectName() == "btn_find":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_find)
            UIFunctions.resetStyle(self, "btn_find")
            UIFunctions.labelPage(self, "TÌM KIẾM")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE THONG KE
        if btnWidget.objectName() == "btn_chart":
            Functions.checkThongKe(self)
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_chart)
            UIFunctions.resetStyle(self, "btn_chart")
            UIFunctions.labelPage(self, "THỐNG KÊ")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NHAN VIEN
        if btnWidget.objectName() == "btn_nv":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_nv)
            UIFunctions.resetStyle(self, "btn_nv")
            UIFunctions.labelPage(self, "NHÂN VIÊN")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE ADMIN
        if btnWidget.objectName() == "btn_admin" and self.isadmin:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_admin)
            UIFunctions.resetStyle(self, "btn_admin")
            UIFunctions.labelPage(self, "ADMINISTRATOR")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_logout":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_logout")
            UIFunctions.labelPage(self, "ĐĂNG XUẤT")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################
def admin(form, model):
    if form == 1:
        return LoginWindow(model)
    else:
        return AdminWindow(model)

class LoginWindow(QMainWindow):
    def __init__(self, model):
        QMainWindow.__init__(self)
        self.ui = Ui_LogWindow()
        self.ui.setupUi(self)
        self.str = ""
        self.isadmin = False
        self.id = 1
        self.model = model
        self.main = MainWindow(self.isadmin, self.id, self.model)

        ## UI ==> INTERFACE CODES
        ########################################################################z

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frmDangNhap.setGraphicsEffect(self.shadow)

        # nut LienHeAdmin - form DangNhap
        self.ui.btnAdmin.clicked.connect(lambda: (admin(0, self.model).show(), self.close()))
        # nut LienHeAdmin - form DangNhap
        self.ui.btnDangNhap.clicked.connect(lambda: UiLog.DangNhap(self, FuncLog.checkDangNhap(self), self.str))


    def clicked(self):
        self.main = MainWindow(self.isadmin, self.id, self.model)


class AdminWindow(QMainWindow):
    def __init__(self, model):
        QMainWindow.__init__(self)
        self.ui = Ui_AdminLogWindow()
        self.ui.setupUi(self)
        self.model = model

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frmAdmin.setGraphicsEffect(self.shadow)

        # nut TroVe - form Admin
        self.ui.btnTroVe.clicked.connect(lambda: (admin(1, self.model).show(), self.close()))
        self.ui.btnThoat.clicked.connect(lambda: self.close())

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>ĐANG TẢI</strong> NHỮNG DỮ LIỆU CẦN THIẾT")

        # Change Texts
        QtCore.QTimer.singleShot(2500, lambda: self.ui.label_description.setText("<strong>ĐANG TẢI</strong> GIAO DIỆN NGƯỜI DÙNG"))

        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>ĐANG</strong> HUẤN LUYỆN"))



        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        self.model = FuncSplash.huanLuyen(self)
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.log = LoginWindow(self.model)
            self.log.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


class Seasion():
    def __init__(self, tentk, matkhau):
        self.TenTK = tentk
        self.MatKhau = matkhau

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = SplashScreen()
    sys.exit(app.exec_())
