import pyodbc


def getConnection():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=PHONG-THINKPAD\SQLEXPRESS;'
                          'Database=SmartParking;'
                          'Trusted_Connection=yes;')
    return conn


# type
class ADMIN():
    def __init__(self, AdminID, TenTK, MatKhauTK):
        self.AdminID = AdminID
        self.AdminID = TenTK
        self.AdminID = MatKhauTK

class NHANVIEN():
    def __init__(self, NhanVienId, TenTK, MatKhauTK, TenNhanVien, DiaChi, SDT, AdminID):
        self.NhanVienID = NhanVienId
        self.TenTK = TenTK
        self.MatKhauTK = MatKhauTK
        self.TenNhanVien = TenNhanVien
        self.DiaChi = DiaChi
        self.SDT = SDT
        self.AdminID = AdminID


class KHACHHANG():
    def __init__(self, KhachHangID, TenKhachHang, DiaChi, SDT, NhanVienID):
        self.KhachHangID = KhachHangID
        self.TenKhachHang = TenKhachHang
        self.DiaChi = DiaChi
        self.SDT = SDT
        self.NhanVienID = NhanVienID

class XE():
    def __init__(self, XeID, SoXe, KhachHangID, NhanVienID, LoaiID):
        self.XeID = XeID
        self.SoXe = SoXe
        self.KhachHangID = KhachHangID
        self.NhanVienID = NhanVienID
        self.LoaiID = LoaiID

class LOAIXE():
    def __init__(self, LoaiID, TenLoai, SoCho, DonGia):
        self.LoaiID = LoaiID
        self.TenLoai = TenLoai
        self.SoCho = SoCho
        self.DonGia = DonGia

class XEVAO():
    def __init__(self, XeVaoID, ThoiGianVao, XeID):
        self.XeVaoID = XeVaoID
        self.ThoiGianVao = ThoiGianVao
        self.XeID = XeID

class XERA():
    def __init__(self, XeRaID, ThoiGianRa, XeID):
        self.XeRaID = XeRaID
        self.ThoiGianRa = ThoiGianRa
        self.XeID = XeID
#########################################################################

def getADMIN(All):
    arr = []
    conn = getConnection()
    sql="SELECT AdminID FROM ADMIN WHERE TenTK=? and MatKhauTK=?"
    usr,psw = All.split(',')
    cursor=conn.cursor()
    cursor.execute(sql,(usr,psw))
    for row in cursor:
        arr.append(row)
    conn.close()
    return arr

######

def getNHANVIEN(All=True):
    arr = []
    conn = getConnection()
    if All == True:
        sql = "SELECT * FROM NHANVIEN"
    elif isinstance(All, str):
        sql = "SELECT NhanVienID FROM NHANVIEN WHERE TenTK=? and MatKhauTK=?"
        usr, psw = All.split(',')
        cursor = conn.cursor()
        cursor.execute(sql, (usr,psw))
        for row in cursor:
            arr.append(row)
        conn.close()
        return arr
    else:
        sql = "SELECT TOP 1 NhanVienID FROM NHANVIEN ORDER BY NhanVienID DESC"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in cursor:
            arr.append(row)
    finally:
        conn.close()
    return arr


def setNHANVIEN(n):
    lastKey = getNHANVIEN(False).pop(0)[0]
    lastKey += 1
    conn = getConnection()
    sql = "INSERT INTO NHANVIEN VALUES(?,?,?,?,?,?,?)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (lastKey, n.TenTK, n.MatKhauTK, n.TenNhanVien, n.DiaChi, n.SDT, n.AdminID))
        conn.commit()
    finally:
        conn.close()


######

def getKHACHHANG(All=True):
    arr = []
    conn = getConnection()
    if All == True:
        sql = "SELECT * FROM KHACHHANG"
    elif isinstance(All, str):
        sql = "SELECT x.SoXe, xv.ThoiGianVao, xr.ThoiGianRa FROM KHACHHANG K, XE x, XEVAO xv, XERA xr WHERE " \
              "k.KhachHangID=x.KhachHangID and x.XeID=xv.XeID and x.XeID=xr.XeID and k.TenKhachHang=? " \
              "GROUP BY x.SoXe, xv.ThoiGianVao, xr.ThoiGianRa"
        cursor = conn.cursor()
        cursor.execute(sql, (All))
        for row in cursor:
            arr.append(row)
        conn.close()
        return arr

    else:
        sql = "SELECT TOP 1 KhachHangID FROM KHACHHANG ORDER BY KhachHangID DESC"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in cursor:
            arr.append(row)
    finally:
        conn.close()
    return arr


def setKHACHHANG(k):
    #lastKey = getKHACHHANG(False).pop(0)[0]
    #lastKey += 1
    conn = getConnection()
    sql = "INSERT INTO KHACHHANG VALUES(?,?,?,?,?)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (k.KhachHangID, k.TenKhachHang, k.DiaChi, k.SDT, k.NhanVienID))
        conn.commit()
    finally:
        conn.close()
#############
def getXE(All=True):
    arr = []
    conn = getConnection()
    if All == True:
        sql = "SELECT * FROM XE"
    elif isinstance(All, str):
        sql = "SELECT TOP 1 XeID FROM XE WHERE SoXe=? ORDER BY XeID DESC"
        cursor = conn.cursor()
        cursor.execute(sql, (All))
        for row in cursor:
            arr.append(row)
        conn.close()
        return arr
    else:
        sql = "SELECT TOP 1 XeID FROM XE ORDER BY XeID DESC"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in cursor:
            arr.append(row)
    finally:
        conn.close()
    return arr
############
def setXE(v):
    lastKey = getXE(False).pop(0)[0]
    lastKey += 1
    conn = getConnection()
    sql = "INSERT INTO XE VALUES(?,?,?,?,?)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (lastKey, v.SoXe, v.KhachHangID, v.NhanVienID, v.LoaiID))
        conn.commit()
    finally:
        conn.close()


######

def getLOAIXE(All=True):
    arr = []
    conn = getConnection()
    if All == True:
        sql = "SELECT TenLoai FROM LOAIXE"
    elif isinstance(All, str):
        sql = "SELECT TOP 1 LoaiID FROM LOAIXE WHERE TenLoai=? ORDER BY LoaiID DESC"
        cursor = conn.cursor()
        cursor.execute(sql, (All))
        for row in cursor:
            arr.append(row)
        conn.close()
        return arr
    else:
        sql = "SELECT TOP 1 LoaiID FROM LOAIXE ORDER BY LoaiID DESC"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in cursor:
            arr.append(row)
    finally:
        conn.close()
    return arr

def setLOAIXE(v):
    lastKey = getLOAIXE(False).pop(0)[0]
    lastKey += 1
    conn = getConnection()
    sql = "INSERT INTO LOAIXE VALUES(?,?,?,?)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (lastKey, v.TenLoai, v.SoCho, v.DonGia))
        conn.commit()
    finally:
        conn.close()

######

def getXEVAO(All):
    arr = []
    conn = getConnection()
    if All == True:
        sql = "SELECT * FROM XEVAO"
    elif isinstance(All, str):
        sql = "SELECT x.SoXe, xv.ThoiGianVao, xr.ThoiGianRa FROM XE x, XEVAO xv, XERA xr WHERE x.XeID=xv.XeID and " \
              "x.XeID=xr.XeID and x.SoXe=? GROUP BY x.SoXe, xv.ThoiGianVao, xr.ThoiGianRa"
        cursor = conn.cursor()
        cursor.execute(sql, (All))
        for row in cursor:
            arr.append(row)
        conn.close()
        return arr
    else:
        sql = "SELECT TOP 1 XeVaoID FROM XEVAO ORDER BY XeVaoID DESC"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in cursor:
            arr.append(row)
    finally:
        conn.close()
    return arr


def setXEVAO(v):
    lastKey = getXEVAO(False).pop(0)[0]
    lastKey += 1
    conn = getConnection()
    sql = "INSERT INTO XEVAO VALUES(?,?,?)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (lastKey , v.ThoiGianVao, v.XeID))
        conn.commit()
    finally:
        conn.close()


######

def getXERA(All):
    arr = []
    conn = getConnection()
    if All == True:
        sql = "SELECT * FROM XERA"
    elif isinstance(All, str):
        sql = "SELECT Plate,MemberID,CostumerID,InputID FROM XERA WHERE OutputID=?"
        cursor = conn.cursor()
        cursor.execute(sql, (int(All)))
        for row in cursor:
            arr.append(row)
        conn.close()
        return arr
    else:
        sql = "SELECT TOP 1 XeRaID FROM XERA ORDER BY XeRaID DESC"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in cursor:
            arr.append(row)
    finally:
        conn.close()
    return arr


def setXERA(r):
    lastKey = getXERA(False).pop(0)[0]
    lastKey += 1
    conn = getConnection()
    sql = "INSERT INTO XERA VALUES(?,?,?)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (lastKey, r.ThoiGianRa, r.XeID))
        conn.commit()
    finally:
        conn.close()

def getTHONGKE(isDay, isKH):
    arr = []
    conn = getConnection()
    if isDay and isKH:
        sql = "SELECT COUNT(XeVaoID), DAY(ThoiGianVao) FROM XEVAO xv, XE x WHERE x.XeID = xv.XeID GROUP BY DAY(ThoiGianVao)"
    if isDay and not isKH:
        sql = "SELECT COUNT(XeVaoID), DAY(ThoiGianVao) FROM XEVAO WHERE XeID IS NULL GROUP BY DAY(ThoiGianVao)"
    if not isDay and isKH:
        sql = "SELECT COUNT(XeVaoID), MONTH(ThoiGianVao) FROM XEVAO xv, XE x WHERE x.XeID = xv.XeID GROUP BY MONTH(ThoiGianVao)"
    if not isDay and not isKH:
        sql = "SELECT COUNT(XeVaoID), MONTH(ThoiGianVao) FROM XEVAO WHERE XeID IS NULL GROUP BY MONTH(ThoiGianVao)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in cursor:
            arr.append(row)
    finally:
        conn.close()
    return arr

# setXERA(XERA(0,'1794673D1', int('2'), None, int('1')))
