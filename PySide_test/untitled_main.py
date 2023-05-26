import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QButtonGroup)
from PySide6.QtCore import (QFile)
from untitled_ui import Ui_Form
import re
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.txt = ""

        #將數字鍵添加事件
        btn = "btn_n"
        for i in range(10):
            getattr(self.ui ,(btn + str(i))).clicked.connect(self.keyboard)
        #將英文鍵添加事件
        btn = "btn_"
        for i in range(26):
            getattr(self.ui ,(btn + chr(65 + i))).clicked.connect(self.keyboard)

        self.ui.btn_inquire.clicked.connect(self.inquire)
        self.ui.btn_del.clicked.connect(self.keyboard_del)
        self.ui.btn_dash.clicked.connect(self.keyboard_cls)
    #查詢
    def inquire(self):
        print(self.txt)
        print([ord(txt) for txt in self.txt])
        return self.txt
    #螢幕鍵盤
    def keyboard(self):
        self.txt = self.txt + self.sender().text()
        self.ui.edit_inquire.setText(self.txt)
        return self.txt
    #del按鍵
    def keyboard_del(self):
        self.txt = self.txt[:-1]
        self.ui.edit_inquire.setText(self.txt)
        return self.txt
    #cls按鍵
    def keyboard_cls(self):
        self.txt = ""
        self.ui.edit_inquire.setText(self.txt)
        return self.txt
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())