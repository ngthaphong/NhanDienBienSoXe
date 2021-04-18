
## ==> GUI FILE
from main import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

class UIFunctions(MainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    ## ==> RETURN STATUS
    def returStatus():
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()


    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ## ==> USER ICON
    ########################################################################
    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            # SET TEXT
            self.ui.label_user_icon.setText(initialsTooltip)

            # SET ICON
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################


    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()


        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())

    def exit(self):
        self.close()

    def ThemcboLoaiXe(self):
        self.ui.cboLoaiXe.clear()
        list = getLOAIXE(True)
        for i in list:
            self.ui.cboLoaiXe.addItem(i[0])

    def DangKyNv(self, done, str):
        qm = QMessageBox()
        if str == "tennv":
            qm.setInformativeText("Tên tài khoản lỗi vui lòng nhập lại")
            self.ui.txtTenNv.setFocus()
        if str == "diachi":
            qm.setInformativeText("Địa chỉ lỗi vui lòng nhập lại")
            self.ui.txtDiaChiNv.setFocus()
        if str == "sdt":
            qm.setInformativeText("Số điện thoại gồm 10 số vui lòng nhập lại")
            self.ui.txtSdtNv.setFocus()
        if str == "tentk":
            qm.setInformativeText("Tên tài khoản không đúng quy định, tên tài khoản lớn hơn 6 và bé hơn 24")
            self.ui.txtTenTKNv.setFocus()
        if str == "mk":
            qm.setInformativeText("Mật khẩu không đúng quy định, mật khẩu lớn hơn 6 và bé hơn 24")
            self.ui.txtMatKhauNv.setFocus()
        if str == "mklai":
            qm.setInformativeText("Mật khẩu nhập lại không chính xác vui lòng nhập lại")
            self.ui.txtNhapLaiNv.setFocus()
        if done:
            self.ui.btnDangKyNv.setText("Thành công")
        else:
            qm.setIcon(QMessageBox.Warning)
            qm.setWindowTitle("Đăng ký")
            qm.setText("Đăng ký không thành công")
            qm.setStandardButtons(QMessageBox.Ok)
            qm.setDefaultButton(QMessageBox.Ok)
            qm.exec_()

    def DangKy(self, done, str):
        if str == "tennv":
            self.ui.qm.setInformativeText("Tên tài khoản lỗi vui lòng nhập lại")
            self.ui.txtTenKhach.setFocus()
        if str == "diachi":
            self.ui.qm.setInformativeText("Địa chỉ lỗi vui lòng nhập lại")
            self.ui.txtDiaChi.setFocus()
        if str == "sdt":
            self.ui.qm.setInformativeText("Số điện thoại gồm 10 số vui lòng nhập lại")
            self.ui.txtSdt.setFocus()
        if str == "loaixe":
            self.ui.qm.setInformativeText("Vui lòng chọn loại xe")
            self.ui.cboLoaiXe.setFocus()
        if str == "soxe":
            self.ui.qm.setInformativeText("Số xe không hợp lệ, biển số xe dưới 10 kí tự")
            self.ui.txtSoXe.setFocus()
        if done:
            self.ui.btnDangKy.setText("Thành công")
        else:
            self.ui.qm.setIcon(QMessageBox.Warning)
            self.ui.qm.setWindowTitle("Đăng ký")
            self.ui.qm.setText("Đăng ký không thành công")
            self.ui.qm.setStandardButtons(QMessageBox.Ok)
            self.ui.qm.setDefaultButton(QMessageBox.Ok)
            self.ui.qm.exec_()

    def ThemLoai(self, done, str):
        if str == "tenloai":
            self.ui.qm.setInformativeText("Tên loại không đúng quy định, tên tài khoản lớn hơn 6 và bé hơn 24")
            self.ui.txtTenTK.setFocus()
        if str == "socho":
            self.ui.qm.setInformativeText("Số chỗ không đúng quy định, mật khẩu lớn hơn 6 và bé hơn 24")
            self.ui.txtMatKhau.setFocus()
        if str == "dongia":
            self.ui.qm.setInformativeText("Đơn giá nhập lại không chính xác vui lòng nhập lại")
            self.ui.txtNhapLai.setFocus()
        if done:
            self.ui.btnThemLoai.setText("Thành công")
            UIFunctions.ThemcboLoaiXe(self)
        else:
            self.ui.qm.setIcon(QMessageBox.Warning)
            self.ui.qm.setWindowTitle("Thêm loại")
            self.ui.qm.setText("Thêm loại không thành công")
            self.ui.qm.setStandardButtons(QMessageBox.Ok)
            self.ui.qm.setDefaultButton(QMessageBox.Ok)
            self.ui.qm.exec_()

    def ChonAnh1(self, done, str):
        if str == "dung":
            pass
        elif str == "sai":
            self.ui.btnChonAnh.setText("Thất bại")

    def ChonAnh2(self, done, str):
        if str == "dung":
            pass
        elif str == "sai":
            self.ui.btnChonAnh.setText("Thất bại")

    def XuLy1(self, done, str):
        pass
    def XuLy2(self, done, str):
        pass
    def TachChu1(self, done, str):
        pass
    def TachChu2(self, done, str):
        pass

    def Luu1(self, done, str):
        pass
    def Luu2(self,done, str):
        pass



class UiLog(LoginWindow):
    def DangNhap(self, isadmin, str):
        if self.str=="sai":
            self.ui.qm.setInformativeText("Tài khoản hoặc mật khẩu không chính xác, vui lòng nhập lại!")
            self.ui.qm.setIcon(QMessageBox.Warning)
            self.ui.qm.setWindowTitle("Đăng nhập")
            self.ui.qm.setText("Đăng nhập không thành công")
            self.ui.qm.setStandardButtons(QMessageBox.Ok)
            self.ui.qm.setDefaultButton(QMessageBox.Ok)
            self.ui.qm.exec_()
            self.ui.txtTenTK.setFocus()
        else:
            self.clicked()
            self.main.show()
            self.close()

    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################
