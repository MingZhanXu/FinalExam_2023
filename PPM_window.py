import sys
from pymysql import connect
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtCore import (QTimer)
from PySide6.QtGui import  (Qt, QGuiApplication)

from time import sleep

from lib.PPM.PPM import PPM
from lib.keyboardScreen.keyboardScreen_ui import Ui_Form as keyboardScreen
from lib.paymentScreen.paymentScreen_ui import Ui_Form as paymentScreen
from lib.PPM_DB.PPM_DB import PPM_DB as db
#mac位置 (之後要改為用動態)
myPlace = "00-FF-5E-74-DB-73"
#1 啟用 0 關閉
#sqlPwd=  "hz5EUrxOzyjDpaHn"
#my = connect(host="vm3pc.ddns.net", port=3306,user="ppm", password = "hz5EUrxOzyjDpaHn", database = "ppm_procedure")
class keyboardWindow(QMainWindow):
    def __init__(self, parent=None, PW=None):
        super(keyboardWindow, self).__init__(parent)
        self.ui = keyboardScreen()
        self.ui.setupUi(self)
        #調整畫面
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.screen = QGuiApplication.primaryScreen().geometry()
        self.width = self.screen.width()
        self.height = self.screen.height()
        #鍵盤寬度660，鍵盤高度225，挑高50
        self.ui.keyboradWidget.setGeometry(self.width/2 - 330, self.height - 275, self.ui.keyboradWidget.width(), self.ui.keyboradWidget.height())
        #初始化變數
        self.txt = ""
        if(PW == None):
            self.PW = patmentWindow(KW=self)
        else:
            self.PW = PW
        self.showMaximized()
        self.isShow = 1
        self.PW.hide()
        self.PW.isShow = 0
        #將鍵盤添加事件
        btn = "btn_n"
        for i in range(10):
            getattr(self.ui ,(btn + str(i))).clicked.connect(self.keyboard)
        btn = "btn_"
        for i in range(26):
            getattr(self.ui ,(btn + chr(65 + i))).clicked.connect(self.keyboard)
        self.ui.btn_del.clicked.connect(self.keyboard_del)
        self.ui.btn_cls.clicked.connect(self.keyboard_cls)
        #將查詢鍵添加事件
        self.ui.btn_inquire.clicked.connect(self.inquire)
        #將模擬停車添加事件
        self.ui.btn_test.clicked.connect(self.test_stop)
    #模擬停車
    def test_stop(self):
        #缺少停車
        return 0
    #查詢
    def inquire(self):
        # print(self.txt)
        # print([ord(txt) for txt in self.txt])
        if(len(self.txt) > 7):
            self.PW.PPM.licensePlateNumber = self.txt
            #轉換格式 2023-06-02 08:50:32.924445 => 2023-06-02 08:50:32
            starT = self.PW.db.inquire_startT(self.txt, myPlace)
            stopT = self.PW.db.inquire_stopT(self.txt, myPlace)
            if(len(starT) > 18 and len(stopT) > 18):
                self.PW.time = 300 * 1000
                #計算金額
                self.PW.PPM.setStartTime(self.PW.db.inquire_startT(self.txt, myPlace)[:19])
                self.PW.PPM.setEndTime(self.PW.db.inquire_stopT(self.txt, myPlace)[:19])
                self.PW.txt = self.txt
                self.PW.PPM.needMoney()
                self.PW.txt = self.PW.PPM.check()
                self.PW.ui.label_print.setText(self.PW.txt)
                self.PW.ui.btn_check.hide()
                self.PW.ui.btn_cancel.show()
                self.PW.payShow()
                self.PW.startTimer()
                self.PW.showMaximized()
                self.PW.isShow = 1
                self.hide()
                self.isShow = 0
            else:
                self.PW.time = 10 * 1000
                self.PW.ui.btn_check.hide()
                self.PW.ui.btn_cancel.hide()
                self.PW.payHide()
                self.PW.ui.label_print.setText("查無此資料，十秒後返回")
                self.PW.startTimer()
                self.PW.showMaximized()
                self.PW.isShow = 1
                self.hide()
                self.isShow = 0
            #print(f"PW.isShow = {self.PW.isShow}\t\t KW.isShow = {self.isShow}")
        return self.txt
    #螢幕鍵盤
    def keyboard(self):
        key = self.sender().text()
        if (key >= "A" and key <= "Z" and len(self.txt) < 3):
            self.txt += key
            if (len(self.txt) == 3):
                self.txt += "-"
            self.ui.edit_inquire.setText(self.txt)
        elif (key >= "0" and key <= "9" and len(self.txt) < 8 and len(self.txt) > 3):
            self.txt = self.txt + key
            self.ui.edit_inquire.setText(self.txt)
        return self.txt
    #刪除按鍵
    def keyboard_del(self):
        if (len(self.txt) == 4):
            self.txt = self.txt[:-2]
        else:
            self.txt = self.txt[:-1]
        self.ui.edit_inquire.setText(self.txt)
        return self.txt
    #清空按鍵
    def keyboard_cls(self):
        self.txt = ""
        self.ui.edit_inquire.setText(self.txt)
        return self.txt

class patmentWindow(QMainWindow):
    def __init__(self, parent=None, KW = None):
        super(patmentWindow, self).__init__(parent)
        self.ui = paymentScreen()
        self.ui.setupUi(self)
        #調整畫面
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.screen = QGuiApplication.primaryScreen().geometry()
        self.width = self.screen.width()
        self.height = self.screen.height()
        self.ui.label_print.setGeometry(self.width * (350 / 1920), self.height * (130 / 1080), self.width * (1220 / 1920), self.height * (820 / 1080))
        self.ui.label_time.setGeometry(self.width * (1570 / 1920), self.height * (80 / 1080), 250, 50)
        self.ui.btn_cancel.setGeometry(self.width * (250 / 1920), self.height * (950 / 1080), self.width * (100 / 1920), self.height * (50 / 1080))
        self.ui.btn_check.setGeometry(self.width * (1670 / 1920), self.height * (950 / 1080), self.width * (100 / 1920), self.height * (50 / 1080))
        #初始化變數
        if(KW == None):
            self.KW = keyboardWindow(PW=self)
        else:
            self.KW = KW
        self.showMaximized()
        self.isShow = 1
        self.KW.hide()
        self.KW.isShow = 0
        self.txt = self.KW.txt
        self.db = db()
        #self.PPM = PPM(self.txt)
        self.PPM = PPM("")
        self.ui.label_print.setText(self.txt)
        #綁定事件
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_check.clicked.connect(self.check)
        self.ui.btn_p1.clicked.connect(self.pay1)
        self.ui.btn_p5.clicked.connect(self.pay5)
        self.ui.btn_p10.clicked.connect(self.pay10)
        self.ui.btn_p50.clicked.connect(self.pay50)
        #計時器
        self.time = 300 * 1000
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.startTimer()
    #到計時
    def showTime(self):
        self.time -= 1
        self.ui.label_time.setText(f'剩餘時間 : {str(int(self.time / 1000))} 秒')
        if self.time == 0:
            self.timer.stop()
            self.KW.showMaximized()
            self.KW.isShow = 1
            self.KW.txt = ""
            self.KW.ui.edit_inquire.setText(self.KW.txt)
            self.hide()
            self.isShow = 0
    def startTimer(self):
        self.timer.start(1)
    #取消
    def cancel(self):
        self.time = 10 * 1000
        self.PPM.checkPay(1)
        self.ui.label_print.setText(self.PPM.printStr2 + "\n並在將十秒後返回主頁面")
        self.ui.btn_check.hide()
        self.ui.btn_cancel.hide()
        self.payHide()
        #print(f"PW.isShow = {self.isShow}\t\t KW.isShow = {self.KW.isShow}")
    #確認
    def check(self):
        self.time = 10 * 1000
        self.PPM.checkPay()
        self.ui.label_print.setText(self.PPM.printStr2 + "\n並在將十秒後返回主頁面")
        self.ui.btn_check.hide()
        self.ui.btn_cancel.hide()
        self.payHide()
        #print(f"PW.isShow = {self.isShow}\t\t KW.isShow = {self.KW.isShow}")
    def pay1(self):
        self.PPM.input(20, 0)
        self.ui.label_print.setText(self.PPM.printStr2)
        if(self.PPM.money - self.PPM.nowMoney <= 0):
            self.ui.btn_check.show()
    def pay5(self):
        self.PPM.input(22, 1)
        self.ui.label_print.setText(self.PPM.printStr2)
        if(self.PPM.money - self.PPM.nowMoney <= 0):
            self.ui.btn_check.show()
    def pay10(self):
        self.PPM.input(26, 2)
        self.ui.label_print.setText(self.PPM.printStr2)
        if(self.PPM.money - self.PPM.nowMoney <= 0):
            self.ui.btn_check.show()
    def pay50(self):
        self.PPM.input(28, 3)
        self.ui.label_print.setText(self.PPM.printStr2)
        if(self.PPM.money - self.PPM.nowMoney <= 0):
            self.ui.btn_check.show()
    def payHide(self):
        self.ui.btn_p1.hide()
        self.ui.btn_p5.hide()
        self.ui.btn_p10.hide()
        self.ui.btn_p50.hide()
    def payShow(self):
        self.ui.btn_p1.show()
        self.ui.btn_p5.show()
        self.ui.btn_p10.show()
        self.ui.btn_p50.show()
if __name__ == "__main__":
    testInquire = 1
    try:
        db()
    except:
        testInquire = 0
    print(myPlace)
    app = QApplication([])
    window = keyboardWindow()
    sys.exit(app.exec_())