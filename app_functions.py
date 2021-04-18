
## ==> GUI FILE
from time import strftime

from PIL import Image, ImageTk
import datetime
from sql import *
from main import *

class Functions(MainWindow):
    def checkDangKyNv(self):
        if len(self.ui.txtTenNv.text()) < 6:
            self.str="tennv"
            return False
        elif len(self.ui.txtDiaChiNv.text()) < 6:
            self.str="diachi"
            return False
        elif len(self.ui.txtSdtNv.text()) != 10:
            self.str="sdt"
            return False
        elif len(self.ui.txtTenTKNv.text()) < 6 or len(self.ui.txtTenTKNv.text()) > 24:
            self.str="tentk"
            return False
        elif len(self.ui.txtMatKhauNv.text()) < 6 or len(self.ui.txtMatKhauNv.text()) > 24:
            self.str="mk"
            return False
        elif self.ui.txtNhapLaiNv.text() != self.ui.txtMatKhauNv.text():
            self.str="mklai"
            return False
        else:
            self.str=""
            nhanvienid = getNHANVIEN(False).pop(0)[0]
            nhanvienid += 1
            tennv = self.ui.txtTenNv.text()
            diachinv = self.ui.txtDiaChiNv.text()
            sdtnv = self.ui.txtSdtNv.text()
            adminid = self.id
            tentknv = self.ui.txtTenTKNv.text()
            matkhaunv = self.ui.txtMatKhauNv.text()
            ####
            setNHANVIEN(NHANVIEN(0, tentknv, matkhaunv, tennv, diachinv, sdtnv, adminid))
            return True


    def checkDangKy(self):
        if len(self.ui.txtTenKhach.text()) < 6:
            self.str = "tennv"
            return False
        elif len(self.ui.txtDiaChi.text()) < 6:
            self.str = "diachi"
            return False
        elif len(self.ui.txtSdt.text()) != 10:
            self.str = "sdt"
            return False
        elif self.ui.cboLoaiXe.currentText() == "":
            self.str = "loaixe"
            return False
        elif len(self.ui.txtSoXe.text()) > 10 or len(self.ui.txtSoXe.text()) < 6:
            self.str = "soxe"
            return False
        else:
            id = getKHACHHANG(False).pop(0)[0]
            id += 1
            tenkhach = self.ui.txtTenKhach.text()
            diachi = self.ui.txtDiaChi.text()
            sdt = self.ui.txtSdt.text()
            loaixe = self.ui.cboLoaiXe.currentText()
            #lay id loai xe
            loaixe = getLOAIXE(loaixe).pop(0)[0]
            soxe = self.ui.txtSoXe.text()
            setKHACHHANG(KHACHHANG(id, tenkhach, diachi, sdt, self.id))
            setXE(XE(0, soxe, id, self.id, loaixe))
            self.str = ""
            return True

    def checkThemLoai(self):
        if len(self.ui.txtTenLoai.text()) < 6:
            self.str = "tenloai"
            return False
        elif not(self.ui.txtSoCho.text().isnumeric()) or int(self.ui.txtSoCho.text()) > 32:
            self.str = "socho"
            return False
        elif int(self.ui.txtDonGia.text()) > 500000:
            self.str = "dongia"
            return False
        else:
            tenloai = self.ui.txtTenLoai.text()
            socho = self.ui.txtSoCho.text()
            dongia = self.ui.txtDonGia.text()
            setLOAIXE(LOAIXE(0, tenloai, socho, dongia))
            self.str = ""
            return True

    def displayImage(self, image):
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
            img = QImage(image.data,
                         image.shape[1],
                         image.shape[0],
                         image.strides[0],  # <--- +++
                         qformat)
            img = img.rgbSwapped()
            return img

    def checkChonAnh1(self):
        fname, filter = QFileDialog.getOpenFileName(self, 'Open File', 'D:\\', "Image Files(*.jpg)")
        if fname:
            self.image1 = cv2.imread(fname, cv2.IMREAD_COLOR)
            self.ui.monitor.setPixmap(QPixmap.fromImage(Functions.displayImage(self, self.image1)))
            self.ui.monitor.setAlignment(QtCore.Qt.AlignCenter)
            self.str="dung"
        else:
            self.str="sai"

    def checkChonAnh2(self):
        fname, filter = QFileDialog.getOpenFileName(self, 'Open File', 'D:\\', "Image Files(*.jpg)")
        if fname:
            self.image2 = cv2.imread(fname, cv2.IMREAD_COLOR)
            self.ui.monitor2.setPixmap(QPixmap.fromImage(Functions.displayImage(self, self.image2)))
            self.ui.monitor2.setAlignment(QtCore.Qt.AlignCenter)
            self.str="dung"
        else:
            self.str="sai"

    def XuLyBien(self, image):
        im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        noise_removal = cv2.bilateralFilter(im_gray, 9, 75, 75)
        equal_histogram = cv2.equalizeHist(noise_removal)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        morph_image = cv2.morphologyEx(equal_histogram, cv2.MORPH_OPEN, kernel, iterations=20)
        sub_morp_image = cv2.subtract(equal_histogram, morph_image)
        ret, thresh_image = cv2.threshold(sub_morp_image, 0, 255, cv2.THRESH_OTSU)
        canny_image = cv2.Canny(thresh_image, 250, 255)
        kernel = np.ones((3, 3), np.uint8)
        dilated_image = cv2.dilate(canny_image, kernel, iterations=1)
        #cat anh
        ImageCopy = image
        contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        screenCnt = None
        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.06 * peri, True)
            if len(approx) == 4:
                screenCnt = approx
                break
        # xuat anh
        x, y, w, h = cv2.boundingRect(screenCnt)
        cv2.rectangle(ImageCopy, (x, y), (x + w, y + h), (0, 0, 0), 2)
        img = ImageCopy[y:y + h, x:x + w]
        self.img_clean = ImageCopy[y:y + h, x:x + w]
        #tach chu
        roi_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        roi_blur = cv2.GaussianBlur(roi_gray, (3, 3), 1)
        ret, thre = cv2.threshold(roi_blur, 120, 255, cv2.THRESH_BINARY_INV)
        kerel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        thre_mor = cv2.morphologyEx(thre, cv2.MORPH_DILATE, kerel3)
        cont, hier = cv2.findContours(thre_mor, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #temp_img = image
        #cv2.drawContours(temp_img, cont, -1, 255, 3)
        #cont.sort(key=lambda x:get_contour_precedence(x, thre_mor.shape[1]))
        areas_ind = {}
        areas = []
        self.roi=[]
        for ind, cnt in enumerate(cont):
            area = cv2.contourArea(cnt)
            areas_ind[area] = ind
            areas.append(area)
        areas = sorted(areas, reverse=True)[2:11]
        areas.sort(key=lambda x:get_contour_precedence(cont[areas_ind[x]],thre_mor.shape[1]))
        for i in areas:
            possibleChar = PossibleChar(cont[areas_ind[i]])
            if (possibleChar.intBoundingRectArea > MIN_PIXEL_AREA and
                    possibleChar.intBoundingRectWidth > MIN_PIXEL_WIDTH and possibleChar.intBoundingRectHeight > MIN_PIXEL_HEIGHT and
                    MIN_ASPECT_RATIO < possibleChar.fltAspectRatio and possibleChar.fltAspectRatio < MAX_ASPECT_RATIO):
                (x, y, w, h) = cv2.boundingRect(cont[areas_ind[i]])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                self.roi.append(thre[y:y + h, x:x + w])
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    def checkXuLy1(self):
        self.ui.monitor.setPixmap(
            QPixmap.fromImage(Functions.displayImage(self, Functions.XuLyBien(self, self.image1))))

    def checkXuLy2(self):
        self.ui.monitor2.setPixmap(
            QPixmap.fromImage(Functions.displayImage(self, Functions.XuLyBien(self, self.image2))))

    def checkTachChu1(self):
        self.str=""
        t=""
        for i in self.roi:
            roi = np.pad(i, (28, 28), 'constant', constant_values=(0, 0))
            roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            roi = cv2.dilate(roi, (3, 3))
            # Calculate the HOG features
            roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), block_norm="L2")
            nbr = self.model.predict(np.array([roi_hog_fd], np.float32))
            t+=str(int(nbr[0]))
        self.ui.txtChuSo.setText(t)

    def checkTachChu2(self):
        self.str = ""
        t=""
        j=0
        for i in self.roi:
            roi = np.pad(i, (28, 28), 'constant', constant_values=(0, 0))
            roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            roi = cv2.dilate(roi, (3, 3))
            cv2.imshow(str(j), roi)
            # Calculate the HOG features
            roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(2, 2), block_norm="L2")
            nbr = self.model.predict(np.array([roi_hog_fd], np.float32))
            t += str(int(nbr[0]))
            j+=1
        self.ui.txtChuSo_2.setText(t)

    def checkLuu1(self):
        bienso = self.ui.txtChuSo.text()
        try:
            id = getXE(bienso).pop(0)[0]
        except:
            id = 0
        now = QDateTime.currentDateTime()
        thoigian = now.toString("yyyy-MM-dd HH:mm:ss")
        if id == 0:
            setXEVAO(XEVAO(0, thoigian, None))
        else:
            setXEVAO(XEVAO(0, thoigian, id))

    def checkLuu2(self):
        bienso = self.ui.txtChuSo_2.text()
        try:
            id = getXE(bienso).pop(0)[0]
        except:
            id = 0
        now = QDateTime.currentDateTime()
        thoigian = now.toString("yyyy-MM-dd HH:mm:ss")
        if id == 0:
            setXERA(XERA(0, thoigian, None))
        else:
            setXERA(XERA(0, thoigian, id))

    def checkTimKiem1(self):
        ten = self.ui.txtfindName.text()
        try:
            kh = getKHACHHANG(ten).pop(0)
            self.ui.txtBienSo.setText(kh[0])
            tgvao = kh[1].strftime('%d-%m-%Y %H:%M:%S')
            self.ui.txtThoiGianVao.setText(tgvao)
            tgra = kh[2].strftime('%d-%m-%Y %H:%M:%S')
            self.ui.txtThoiGianRa.setText(tgra)
            self.list.append(ten)
        except:
            self.str = "sai"


    def checkXoaTrang1(self):
        self.ui.txtfindName.clear()
        self.ui.txtBienSo.clear()
        self.ui.txtThoiGianVao.clear()
        self.ui.txtThoiGianRa.clear()

    def checkTimKiem2(self):
        so = self.ui.txtfindNum.text()
        try:
            bienso = getXEVAO(so).pop(0)
            self.ui.txtBienSo.setText(bienso[0])
            tgvao = bienso[1].strftime('%d-%m-%Y %H:%M:%S')
            self.ui.txtThoiGianVao.setText(tgvao)
            tgra = bienso[2].strftime('%d-%m-%Y %H:%M:%S')
            self.ui.txtThoiGianRa.setText(tgra)
            self.list.append(so)
        except:
            self.str = "sai"

    def checkXoaTrang2(self):
        self.ui.txtfindNum.clear()
        self.ui.txtBienSo.clear()
        self.ui.txtThoiGianVao.clear()
        self.ui.txtThoiGianRa.clear()

    def checkLichSu(self):
        list = self.list
        if len(list) >= 1:
            self.ui.txtLichSu1.setText(list.pop())
        if len(list) >= 2:
            self.ui.txtLichSu2.setText(list.pop())
        if len(list) >= 3:
            self.ui.txtLichSu3.setText(list.pop())
        if len(list) >= 4:
            self.ui.txtLichSu4.setText(list.pop())

    def checkThongKe(self):
        try:
            ngaykh = getTHONGKE(True, True).pop(0)[0]
            self.ui.txtLuotKHNgay.setText(str(ngaykh))
            ngayk = getTHONGKE(True, False).pop(0)[0]
            self.ui.txtLuotKNgay.setText(str(ngayk))
            ngayt = ngaykh + ngayk
            thangkh = getTHONGKE(False, True).pop(0)[0]
            self.ui.txtLuotKHThang.setText(str(thangkh))
            thangk = getTHONGKE(False, False).pop(0)[0]
            self.ui.txtLuotKThang.setText(str(thangk))
            thangt = thangkh + thangk
            self.ui.txtTongSoNgay.setText(str(ngayt))
            self.ui.txtTongSoThang.setText(str(thangt))
        except:
            self.str = "sai"



class FuncLog(LoginWindow):
    def checkDangNhap(self):
        tentk = self.ui.txtTenTK.text()
        mk = self.ui.txtMatKhau.text()
        try:
            self.id = getADMIN(tentk + ',' + mk).pop(0)[0]
            self.str = ""
            self.isadmin = True
        except IndexError:
            nhanvien = getNHANVIEN(tentk + ',' + mk)
            self.str = ""
        except:
            self.str = "sai"
        #print("\n\n"+nhanvien)

class FuncSplash(SplashScreen):
    def huanLuyen(self):
        # load data
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        # cho x_train
        X_train_feature = []
        for i in range(len(X_train)):
            feature = hog(X_train[i], orientations=9, pixels_per_cell=(14, 14), cells_per_block=(2, 2), block_norm="L2")
            X_train_feature.append(feature)
        X_train_feature = np.array(X_train_feature, dtype=np.float32)

        # cho x_test
        X_test_feature = []
        for i in range(len(X_test)):
            feature = hog(X_test[i], orientations=9, pixels_per_cell=(14, 14), cells_per_block=(2, 2), block_norm="L2")
            X_test_feature.append(feature)
        X_test_feature = np.array(X_test_feature, dtype=np.float32)
        model = LinearSVC(C=10)
        model.fit(X_train_feature, y_train)
        y_pre = model.predict(X_test_feature)
        print(accuracy_score(y_test, y_pre) * 100)
        return model


def get_contour_precedence(contour, cols):
    #tolen 14 pixel
    tolerance_factor = 14
    origin = cv2.boundingRect(contour)
    return ((origin[1] // tolerance_factor) * tolerance_factor) * cols + origin[0]

MIN_PIXEL_WIDTH = 15
MIN_PIXEL_HEIGHT = 28
MIN_ASPECT_RATIO = 0.28
MAX_ASPECT_RATIO = 1.0
MIN_PIXEL_AREA = 400

class PossibleChar:
    def __init__(self, _contour):
        self.contour = _contour

        self.boundingRect = cv2.boundingRect(self.contour)

        [intX, intY, intWidth, intHeight] = self.boundingRect

        self.intBoundingRectX = intX
        self.intBoundingRectY = intY
        self.intBoundingRectWidth = intWidth
        self.intBoundingRectHeight = intHeight

        self.intBoundingRectArea = self.intBoundingRectWidth * self.intBoundingRectHeight

        self.intCenterX = (self.intBoundingRectX + self.intBoundingRectX + self.intBoundingRectWidth) / 2
        self.intCenterY = (self.intBoundingRectY + self.intBoundingRectY + self.intBoundingRectHeight) / 2

        self.fltAspectRatio = float(self.intBoundingRectWidth) / float(self.intBoundingRectHeight)