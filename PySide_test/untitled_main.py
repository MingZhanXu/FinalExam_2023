import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QButtonGroup)
from PySide6.QtCore import (QFile)
from untitled_ui import Ui_Form
from PySide6.QtGui import  (Qt, QGuiApplication)
import re
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
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
        
        self.ui.btn_inquire.clicked.connect(self.inquire)
    #查詢
    def inquire(self):
        print(self.txt)
        print([ord(txt) for txt in self.txt])
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
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())