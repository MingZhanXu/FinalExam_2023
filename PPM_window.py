import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget)
from PySide6.QtCore import (QFile)
from PySide6.QtGui import  (Qt, QGuiApplication)

from lib.PPM.PPM import PPM
from lib.keyboardScreen.keyboardScreen_ui import Ui_Form as keyboardScreen
from lib.paymentScreen.paymentScreen_ui import Ui_Form as paymentScreen
class keyboardWindow(QMainWindow):
    def __init__(self, parent=None):
        super(keyboardWindow, self).__init__(parent)
        self.ui = keyboardScreen()
        self.ui.setupUi(self)
        #查詢車牌文字
        self.txt = ""
        #調整畫面
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.screen = QGuiApplication.primaryScreen().geometry()
        self.width = self.screen.width()
        self.height = self.screen.height()
        #鍵盤寬度660，鍵盤高度225，挑高50
        self.ui.keyboradWidget.setGeometry(self.width/2 - 330, self.height - 275, self.ui.keyboradWidget.width(), self.ui.keyboradWidget.height())

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
    #查詢
    def inquire(self):
        # print(self.txt)
        # print([ord(txt) for txt in self.txt])
        if(len(self.txt) > 7):
            self.hide()
            self.PW = patmentWindow(self, self.txt)
            self.PW.showMaximized()
        return self.txt
    #螢幕鍵盤
    def keyboard(self):
        key = self.sender().text()
        if (ord(key) >= ord("A") and ord(key) <= ord("Z") and len(self.txt) < 3):
            self.txt += self.sender().text()
            if (len(self.txt) == 3):
                self.txt += "-"
            self.ui.edit_inquire.setText(self.txt)
        elif (ord(key) >= ord("0") and ord(key) <= ord("9") and len(self.txt) < 8 and len(self.txt) > 3):
            self.txt = self.txt + self.sender().text()
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
    def __init__(self, parent=None, txt=""):
        super(patmentWindow, self).__init__(parent)
        self.ui = paymentScreen()
        self.ui.setupUi(self)
        #調整畫面
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.screen = QGuiApplication.primaryScreen().geometry()
        self.width = self.screen.width()
        self.height = self.screen.height()
        #初始化變數
        self.txt = txt
        self.PPM = PPM(self.txt)
        self.ui.label_print.setText(self.txt)
        #綁定事件
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_check.clicked.connect(self.check)
    def cancel(self):
        self.hide()
        self.KS = keyboardWindow(self)
        self.KS.showMaximized()
    def check(self):
        self.hide()
        self.KS = keyboardWindow(self)
        self.KS.showMaximized()

# class mainWindow():
#     def __init__(self):
        
if __name__ == "__main__":
    app = QApplication([])
    window = keyboardWindow()
    window.showMaximized()
    sys.exit(app.exec_())