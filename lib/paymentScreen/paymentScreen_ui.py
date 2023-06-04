# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paymentScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(1920, 1078)
        font = QFont()
        font.setFamilies([u"\u6a19\u6977\u9ad4"])
        font.setPointSize(15)
        Form.setFont(font)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        self.btn_check = QPushButton(Form)
        self.btn_check.setObjectName(u"btn_check")
        self.btn_check.setGeometry(QRect(1670, 950, 100, 50))
        font1 = QFont()
        font1.setFamilies([u"\u6a19\u6977\u9ad4"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.btn_check.setFont(font1)
        self.btn_cancel = QPushButton(Form)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(250, 950, 100, 50))
        self.btn_cancel.setFont(font1)
        self.label_print = QLabel(Form)
        self.label_print.setObjectName(u"label_print")
        self.label_print.setGeometry(QRect(350, 130, 1220, 820))
        font2 = QFont()
        font2.setFamilies([u"\u6a19\u6977\u9ad4"])
        font2.setPointSize(30)
        self.label_print.setFont(font2)
        self.label_print.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_time = QLabel(Form)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(1570, 80, 250, 50))
        self.label_time.setFont(font1)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(400, 920, 323, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_p1 = QPushButton(self.gridLayoutWidget)
        self.btn_p1.setObjectName(u"btn_p1")

        self.gridLayout.addWidget(self.btn_p1, 0, 0, 1, 1)

        self.btn_p5 = QPushButton(self.gridLayoutWidget)
        self.btn_p5.setObjectName(u"btn_p5")

        self.gridLayout.addWidget(self.btn_p5, 0, 1, 1, 1)

        self.btn_p10 = QPushButton(self.gridLayoutWidget)
        self.btn_p10.setObjectName(u"btn_p10")

        self.gridLayout.addWidget(self.btn_p10, 0, 2, 1, 1)

        self.btn_p50 = QPushButton(self.gridLayoutWidget)
        self.btn_p50.setObjectName(u"btn_p50")

        self.gridLayout.addWidget(self.btn_p50, 0, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_check.setText(QCoreApplication.translate("Form", u"\u78ba\u8a8d", None))
        self.btn_cancel.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
        self.label_print.setText(QCoreApplication.translate("Form", u"T", None))
        self.label_time.setText(QCoreApplication.translate("Form", u"\u5269\u9918\u6642\u9593 : 300 \u79d2", None))
        self.btn_p1.setText(QCoreApplication.translate("Form", u"\u4e00\u5143", None))
        self.btn_p5.setText(QCoreApplication.translate("Form", u"\u4e94\u5143", None))
        self.btn_p10.setText(QCoreApplication.translate("Form", u"\u5341\u5143", None))
        self.btn_p50.setText(QCoreApplication.translate("Form", u"\u4e94\u5341\u5143", None))
    # retranslateUi

