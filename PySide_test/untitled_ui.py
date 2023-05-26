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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        self.btn1 = QPushButton(Form)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(580, 290, 214, 24))
        self.btn1.setMaximumSize(QSize(500, 50))
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(200, 540, 674, 222))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.edit_inquire = QLineEdit(self.horizontalLayoutWidget)
        self.edit_inquire.setObjectName(u"edit_inquire")
        self.edit_inquire.setMaximumSize(QSize(500, 50))

        self.verticalLayout_2.addWidget(self.edit_inquire)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_H = QPushButton(self.horizontalLayoutWidget)
        self.btn_H.setObjectName(u"btn_H")
        self.btn_H.setMinimumSize(QSize(50, 50))
        self.btn_H.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_H, 0, 7, 1, 1)

        self.btn_D = QPushButton(self.horizontalLayoutWidget)
        self.btn_D.setObjectName(u"btn_D")
        self.btn_D.setMinimumSize(QSize(50, 50))
        self.btn_D.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_D, 0, 3, 1, 1)

        self.btn_M = QPushButton(self.horizontalLayoutWidget)
        self.btn_M.setObjectName(u"btn_M")
        self.btn_M.setMinimumSize(QSize(50, 50))
        self.btn_M.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_M, 1, 3, 1, 1)

        self.btn_W = QPushButton(self.horizontalLayoutWidget)
        self.btn_W.setObjectName(u"btn_W")
        self.btn_W.setMinimumSize(QSize(50, 50))
        self.btn_W.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_W, 2, 4, 1, 1)

        self.btn_L = QPushButton(self.horizontalLayoutWidget)
        self.btn_L.setObjectName(u"btn_L")
        self.btn_L.setMinimumSize(QSize(50, 50))
        self.btn_L.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_L, 1, 2, 1, 1)

        self.btn_B = QPushButton(self.horizontalLayoutWidget)
        self.btn_B.setObjectName(u"btn_B")
        self.btn_B.setMinimumSize(QSize(50, 50))
        self.btn_B.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_B, 0, 1, 1, 1)

        self.btn_A = QPushButton(self.horizontalLayoutWidget)
        self.btn_A.setObjectName(u"btn_A")
        self.btn_A.setMinimumSize(QSize(50, 50))
        self.btn_A.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_A, 0, 0, 1, 1)

        self.btn_X = QPushButton(self.horizontalLayoutWidget)
        self.btn_X.setObjectName(u"btn_X")
        self.btn_X.setMinimumSize(QSize(50, 50))
        self.btn_X.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_X, 2, 5, 1, 1)

        self.btn_E = QPushButton(self.horizontalLayoutWidget)
        self.btn_E.setObjectName(u"btn_E")
        self.btn_E.setMinimumSize(QSize(50, 50))
        self.btn_E.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_E, 0, 4, 1, 1)

        self.btn_P = QPushButton(self.horizontalLayoutWidget)
        self.btn_P.setObjectName(u"btn_P")
        self.btn_P.setMinimumSize(QSize(50, 50))
        self.btn_P.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_P, 1, 6, 1, 1)

        self.btn_O = QPushButton(self.horizontalLayoutWidget)
        self.btn_O.setObjectName(u"btn_O")
        self.btn_O.setMinimumSize(QSize(50, 50))
        self.btn_O.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_O, 1, 5, 1, 1)

        self.btn_K = QPushButton(self.horizontalLayoutWidget)
        self.btn_K.setObjectName(u"btn_K")
        self.btn_K.setMinimumSize(QSize(50, 50))
        self.btn_K.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_K, 1, 1, 1, 1)

        self.btn_J = QPushButton(self.horizontalLayoutWidget)
        self.btn_J.setObjectName(u"btn_J")
        self.btn_J.setMinimumSize(QSize(50, 50))
        self.btn_J.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_J, 1, 0, 1, 1)

        self.btn_N = QPushButton(self.horizontalLayoutWidget)
        self.btn_N.setObjectName(u"btn_N")
        self.btn_N.setMinimumSize(QSize(50, 50))
        self.btn_N.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_N, 1, 4, 1, 1)

        self.btn_G = QPushButton(self.horizontalLayoutWidget)
        self.btn_G.setObjectName(u"btn_G")
        self.btn_G.setMinimumSize(QSize(50, 50))
        self.btn_G.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_G, 0, 6, 1, 1)

        self.btn_R = QPushButton(self.horizontalLayoutWidget)
        self.btn_R.setObjectName(u"btn_R")
        self.btn_R.setMinimumSize(QSize(50, 50))
        self.btn_R.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_R, 1, 8, 1, 1)

        self.btn_F = QPushButton(self.horizontalLayoutWidget)
        self.btn_F.setObjectName(u"btn_F")
        self.btn_F.setMinimumSize(QSize(50, 50))
        self.btn_F.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_F, 0, 5, 1, 1)

        self.btn_I = QPushButton(self.horizontalLayoutWidget)
        self.btn_I.setObjectName(u"btn_I")
        self.btn_I.setMinimumSize(QSize(50, 50))
        self.btn_I.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_I, 0, 8, 1, 1)

        self.btn_inquire = QPushButton(self.horizontalLayoutWidget)
        self.btn_inquire.setObjectName(u"btn_inquire")
        self.btn_inquire.setMinimumSize(QSize(50, 50))
        self.btn_inquire.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_inquire, 2, 8, 1, 1)

        self.btn_U = QPushButton(self.horizontalLayoutWidget)
        self.btn_U.setObjectName(u"btn_U")
        self.btn_U.setMinimumSize(QSize(50, 50))
        self.btn_U.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_U, 2, 2, 1, 1)

        self.btn_V = QPushButton(self.horizontalLayoutWidget)
        self.btn_V.setObjectName(u"btn_V")
        self.btn_V.setMinimumSize(QSize(50, 50))
        self.btn_V.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_V, 2, 3, 1, 1)

        self.btn_S = QPushButton(self.horizontalLayoutWidget)
        self.btn_S.setObjectName(u"btn_S")
        self.btn_S.setMinimumSize(QSize(50, 50))
        self.btn_S.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_S, 2, 0, 1, 1)

        self.btn_T = QPushButton(self.horizontalLayoutWidget)
        self.btn_T.setObjectName(u"btn_T")
        self.btn_T.setMinimumSize(QSize(50, 50))
        self.btn_T.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_T, 2, 1, 1, 1)

        self.btn_Y = QPushButton(self.horizontalLayoutWidget)
        self.btn_Y.setObjectName(u"btn_Y")
        self.btn_Y.setMinimumSize(QSize(50, 50))
        self.btn_Y.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_Y, 2, 6, 1, 1)

        self.btn_Z = QPushButton(self.horizontalLayoutWidget)
        self.btn_Z.setObjectName(u"btn_Z")
        self.btn_Z.setMinimumSize(QSize(50, 50))
        self.btn_Z.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_Z, 2, 7, 1, 1)

        self.btn_C = QPushButton(self.horizontalLayoutWidget)
        self.btn_C.setObjectName(u"btn_C")
        self.btn_C.setMinimumSize(QSize(50, 50))
        self.btn_C.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_C, 0, 2, 1, 1)

        self.btn_Q = QPushButton(self.horizontalLayoutWidget)
        self.btn_Q.setObjectName(u"btn_Q")
        self.btn_Q.setMinimumSize(QSize(50, 50))
        self.btn_Q.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.btn_Q, 1, 7, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_n5 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n5.setObjectName(u"btn_n5")
        self.btn_n5.setMinimumSize(QSize(50, 50))
        self.btn_n5.setMaximumSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.btn_n5, 1, 1, 1, 1)

        self.btn_n8 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n8.setObjectName(u"btn_n8")
        self.btn_n8.setMinimumSize(QSize(50, 50))
        self.btn_n8.setMaximumSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.btn_n8, 0, 1, 1, 1)

        self.btn_n3 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n3.setObjectName(u"btn_n3")
        self.btn_n3.setMinimumSize(QSize(50, 50))
        self.btn_n3.setMaximumSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.btn_n3, 2, 2, 1, 1)

        self.btn_n4 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n4.setObjectName(u"btn_n4")
        self.btn_n4.setMinimumSize(QSize(50, 50))
        self.btn_n4.setMaximumSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.btn_n4, 1, 0, 1, 1)

        self.btn_n1 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n1.setObjectName(u"btn_n1")
        self.btn_n1.setMinimumSize(QSize(50, 50))
        self.btn_n1.setMaximumSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.btn_n1, 2, 0, 1, 1)

        self.btn_n2 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n2.setObjectName(u"btn_n2")
        self.btn_n2.setMinimumSize(QSize(50, 50))
        self.btn_n2.setMaximumSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.btn_n2, 2, 1, 1, 1)

        self.btn_n9 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n9.setObjectName(u"btn_n9")
        self.btn_n9.setMinimumSize(QSize(50, 50))
        self.btn_n9.setMaximumSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.btn_n9, 0, 2, 1, 1)

        self.btn_n6 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n6.setObjectName(u"btn_n6")
        self.btn_n6.setMinimumSize(QSize(50, 50))
        self.btn_n6.setMaximumSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.btn_n6, 1, 2, 1, 1)

        self.btn_n7 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n7.setObjectName(u"btn_n7")
        self.btn_n7.setMinimumSize(QSize(50, 50))
        self.btn_n7.setMaximumSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.btn_n7, 0, 0, 1, 1)

        self.btn_dash = QPushButton(self.horizontalLayoutWidget)
        self.btn_dash.setObjectName(u"btn_dash")
        self.btn_dash.setMinimumSize(QSize(50, 50))
        self.btn_dash.setMaximumSize(QSize(50, 50))
        self.btn_dash.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.btn_dash, 3, 0, 1, 1)

        self.btn_n0 = QPushButton(self.horizontalLayoutWidget)
        self.btn_n0.setObjectName(u"btn_n0")
        self.btn_n0.setMinimumSize(QSize(50, 50))
        self.btn_n0.setMaximumSize(QSize(50, 50))
        self.btn_n0.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.btn_n0, 3, 1, 1, 1)

        self.btn_del = QPushButton(self.horizontalLayoutWidget)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setMinimumSize(QSize(50, 50))
        self.btn_del.setMaximumSize(QSize(50, 50))
        self.btn_del.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.btn_del, 3, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn1.setText(QCoreApplication.translate("Form", u"\u67e5\u8a62", None))
        self.btn_H.setText(QCoreApplication.translate("Form", u"H", None))
        self.btn_D.setText(QCoreApplication.translate("Form", u"D", None))
        self.btn_M.setText(QCoreApplication.translate("Form", u"M", None))
        self.btn_W.setText(QCoreApplication.translate("Form", u"W", None))
        self.btn_L.setText(QCoreApplication.translate("Form", u"L", None))
        self.btn_B.setText(QCoreApplication.translate("Form", u"B", None))
        self.btn_A.setText(QCoreApplication.translate("Form", u"A", None))
        self.btn_X.setText(QCoreApplication.translate("Form", u"X", None))
        self.btn_E.setText(QCoreApplication.translate("Form", u"E", None))
        self.btn_P.setText(QCoreApplication.translate("Form", u"P", None))
        self.btn_O.setText(QCoreApplication.translate("Form", u"O", None))
        self.btn_K.setText(QCoreApplication.translate("Form", u"K", None))
        self.btn_J.setText(QCoreApplication.translate("Form", u"J", None))
        self.btn_N.setText(QCoreApplication.translate("Form", u"N", None))
        self.btn_G.setText(QCoreApplication.translate("Form", u"G", None))
        self.btn_R.setText(QCoreApplication.translate("Form", u"R", None))
        self.btn_F.setText(QCoreApplication.translate("Form", u"F", None))
        self.btn_I.setText(QCoreApplication.translate("Form", u"I", None))
        self.btn_inquire.setText(QCoreApplication.translate("Form", u"\u67e5\u8a62", None))
        self.btn_U.setText(QCoreApplication.translate("Form", u"U", None))
        self.btn_V.setText(QCoreApplication.translate("Form", u"V", None))
        self.btn_S.setText(QCoreApplication.translate("Form", u"S", None))
        self.btn_T.setText(QCoreApplication.translate("Form", u"T", None))
        self.btn_Y.setText(QCoreApplication.translate("Form", u"Y", None))
        self.btn_Z.setText(QCoreApplication.translate("Form", u"Z", None))
        self.btn_C.setText(QCoreApplication.translate("Form", u"C", None))
        self.btn_Q.setText(QCoreApplication.translate("Form", u"Q", None))
        self.btn_n5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_n8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_n3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_n4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_n1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_n2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_n9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_n6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_n7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_dash.setText(QCoreApplication.translate("Form", u"cls", None))
        self.btn_n0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_del.setText(QCoreApplication.translate("Form", u"del", None))
    # retranslateUi

