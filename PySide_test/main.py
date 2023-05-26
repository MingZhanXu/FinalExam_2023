import sys
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QLineEdit, QVBoxLayout)
from PySide6.QtCore import Slot
class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("繳費機")
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("請輸入車牌號碼")
        self.button = QPushButton("查詢")
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.print)
    #傳輸
    def print(self):
        print(f'{self.edit.text()}')

if __name__ == '__main__':
    app = QApplication([])
    form = Form()
    form.show()
    sys.exit(app.exec_())