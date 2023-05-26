# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(330, 490, 216, 26))
        self.gridLayout = QGridLayout(self.horizontalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.edit1 = QLineEdit(self.horizontalLayoutWidget)
        self.edit1.setObjectName(u"edit1")
        self.edit1.setMaximumSize(QSize(500, 50))

        self.gridLayout.addWidget(self.edit1, 0, 0, 1, 1)

        self.btn1 = QPushButton(self.horizontalLayoutWidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMaximumSize(QSize(500, 50))

        self.gridLayout.addWidget(self.btn1, 0, 1, 1, 1)

        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.btn_n2 = QPushButton(self.buttonGroup)
        self.btn_n2.setObjectName(u"btn_n2")
        self.btn_n2.setGeometry(QRect(180, 30, 50, 50))
        self.btn_n2.setMinimumSize(QSize(50, 50))
        self.btn_n2.setMaximumSize(QSize(50, 50))
        self.btn_n3 = QPushButton(self.buttonGroup)
        self.btn_n3.setObjectName(u"btn_n3")
        self.btn_n3.setGeometry(QRect(261, 30, 50, 50))
        self.btn_n3.setMinimumSize(QSize(50, 50))
        self.btn_n3.setMaximumSize(QSize(50, 50))
        self.btn_n8 = QPushButton(self.buttonGroup)
        self.btn_n8.setObjectName(u"btn_n8")
        self.btn_n8.setGeometry(QRect(666, 30, 50, 50))
        self.btn_n8.setMinimumSize(QSize(50, 50))
        self.btn_n8.setMaximumSize(QSize(50, 50))
        self.btn_n6 = QPushButton(self.buttonGroup)
        self.btn_n6.setObjectName(u"btn_n6")
        self.btn_n6.setGeometry(QRect(504, 30, 50, 50))
        self.btn_n6.setMinimumSize(QSize(50, 50))
        self.btn_n6.setMaximumSize(QSize(50, 50))
        self.btn_n7 = QPushButton(self.buttonGroup)
        self.btn_n7.setObjectName(u"btn_n7")
        self.btn_n7.setGeometry(QRect(585, 30, 50, 50))
        self.btn_n7.setMinimumSize(QSize(50, 50))
        self.btn_n7.setMaximumSize(QSize(50, 50))
        self.btn_n5 = QPushButton(self.buttonGroup)
        self.btn_n5.setObjectName(u"btn_n5")
        self.btn_n5.setGeometry(QRect(423, 30, 50, 50))
        self.btn_n5.setMinimumSize(QSize(50, 50))
        self.btn_n5.setMaximumSize(QSize(50, 50))
        self.btn_n0 = QPushButton(self.buttonGroup)
        self.btn_n0.setObjectName(u"btn_n0")
        self.btn_n0.setGeometry(QRect(18, 30, 50, 50))
        self.btn_n0.setMinimumSize(QSize(50, 50))
        self.btn_n0.setMaximumSize(QSize(50, 50))
        self.btn_n0.setAutoFillBackground(False)
        self.btn_n1 = QPushButton(self.buttonGroup)
        self.btn_n1.setObjectName(u"btn_n1")
        self.btn_n1.setGeometry(QRect(99, 30, 50, 50))
        self.btn_n1.setMinimumSize(QSize(50, 50))
        self.btn_n1.setMaximumSize(QSize(50, 50))
        self.btn_n4 = QPushButton(self.buttonGroup)
        self.btn_n4.setObjectName(u"btn_n4")
        self.btn_n4.setGeometry(QRect(342, 30, 50, 50))
        self.btn_n4.setMinimumSize(QSize(50, 50))
        self.btn_n4.setMaximumSize(QSize(50, 50))
        self.btn_n9 = QPushButton(self.buttonGroup)
        self.btn_n9.setObjectName(u"btn_n9")
        self.btn_n9.setGeometry(QRect(747, 30, 50, 50))
        self.btn_n9.setMinimumSize(QSize(50, 50))
        self.btn_n9.setMaximumSize(QSize(50, 50))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn1.setText(QCoreApplication.translate("Form", u"\u67e5\u8a62", None))
        self.buttonGroup.setProperty("title", QCoreApplication.translate("Form", u"QButtonGroup", None))
        self.btn_n2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_n3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_n8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_n6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_n7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_n5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_n0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_n1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_n4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_n9.setText(QCoreApplication.translate("Form", u"9", None))
    # retranslateUi

