# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'integrate.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

## TODO 每次展示task前调用compare函数

import sys

from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
                               QMainWindow, QSizePolicy, QWidget, QSpacerItem, QPushButton, QVBoxLayout, QLabel, QFrame,
                               QRadioButton, QButtonGroup, QDateEdit)

from main import MainWindow
from modules import resources_rc, Ui_MainWindow

from task import Task


def home_ui_init(ui):

    # ui.Home_centralwidget = QWidget(MainWindow)
    # self.Home_centralwidget.setObjectName(u"Home_centralwidget")
    ui.home.setStyleSheet(
        u"background-color: rgb(122, 138, 202);\n"
        "font: 20px;\n"
        "QRadioButton::indicator {\n"
        "    border: 3px solid #6272a4;\n"
        "	width: 15px;\n"
        "	height: 15px;\n"
        "	border-radius: 10px;\n"
        "    background: #6272a4;\n"
        "}\n"
        "QRadioButton::indicator:hover {\n"
        "    border: 3px solid rgb(119, 136, 187);\n"
        "}\n"
        "QRadioButton::indicator:checked {\n"
        "    background: 3px solid #bd93f9;\n"
        "	border: 3px solid #bd93f9;	\n"
        "}\n"
        "")
    # ui.horizontalLayout = QHBoxLayout(ui.Home_centralwidget)
    # ui.horizontalLayout.setObjectName(u"Home_horizontalLayout")
    ui.Home_verticalLayout = QVBoxLayout(ui.home)
    ui.Home_verticalLayout.setObjectName(u"Home_verticalLayout")
    # self.Home_frame = QFrame(self.Home_centralwidget)
    ui.Home_frame = QFrame()
    ui.Home_frame.setObjectName(u"Home_frame")
    sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(1)
    sizePolicy.setHeightForWidth(ui.Home_frame.sizePolicy().hasHeightForWidth())
    ui.Home_frame.setSizePolicy(sizePolicy)
    ui.Home_frame.setMaximumSize(QSize(16777215, 80))
    ui.Home_frame.setStyleSheet(u"border-radius: 15px;\n"
                                  "padding: 2px;\n"
                                  "background-color:rgb(253,253,253);\n"
                                  " ")
    ui.Home_frame.setFrameShape(QFrame.StyledPanel)
    ui.Home_frame.setFrameShadow(QFrame.Raised)
    ui.Home_horizontalLayout_4 = QHBoxLayout(ui.Home_frame)
    ui.Home_horizontalLayout_4.setObjectName(u"horizontalLayout_4")
    ui.Home_label = QLabel(ui.Home_frame)
    ui.Home_label.setObjectName(u"Home_label")
    sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    sizePolicy1.setHorizontalStretch(0)
    sizePolicy1.setVerticalStretch(0)
    sizePolicy1.setHeightForWidth(ui.Home_label.sizePolicy().hasHeightForWidth())
    ui.Home_label.setSizePolicy(sizePolicy1)
    ui.Home_label.setMaximumSize(QSize(30, 30))
    ui.Home_label.setStyleSheet(u"border-image: url(:/icons/images/icons/screening.png);")

    ui.Home_horizontalLayout_4.addWidget(ui.Home_label)

    ui.Home_horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

    ui.Home_horizontalLayout_4.addItem(ui.Home_horizontalSpacer_3)

    ui.Home_verticalLayout_2 = QVBoxLayout()
    ui.Home_verticalLayout_2.setObjectName(u"Home_verticalLayout_2")
    ui.Home_horizontalLayout_2 = QHBoxLayout()
    ui.Home_horizontalLayout_2.setObjectName(u"Home_horizontalLayout_2")
    ui.All_radioButton = QRadioButton(ui.Home_frame)
    ui.Home_buttonGroup = QButtonGroup()
    ui.Home_buttonGroup.setObjectName(u"Home_buttonGroup")
    ui.Home_buttonGroup.addButton(ui.All_radioButton)
    ui.All_radioButton.setObjectName(u"All_radioButton")
    sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    sizePolicy2.setHorizontalStretch(1)
    sizePolicy2.setVerticalStretch(0)
    sizePolicy2.setHeightForWidth(ui.All_radioButton.sizePolicy().hasHeightForWidth())
    ui.All_radioButton.setSizePolicy(sizePolicy2)
    ui.All_radioButton.setChecked(True)

    ui.Home_horizontalLayout_2.addWidget(ui.All_radioButton)

    ui.Sport_radioButton = QRadioButton(ui.Home_frame)
    ui.Home_buttonGroup.addButton(ui.Sport_radioButton)
    ui.Sport_radioButton.setObjectName(u"Sport_radioButton")
    sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
    sizePolicy3.setHorizontalStretch(1)
    sizePolicy3.setVerticalStretch(0)
    sizePolicy3.setHeightForWidth(ui.Sport_radioButton.sizePolicy().hasHeightForWidth())
    ui.Sport_radioButton.setSizePolicy(sizePolicy3)

    ui.Home_horizontalLayout_2.addWidget(ui.Sport_radioButton)

    ui.Study_radioButton = QRadioButton(ui.Home_frame)
    ui.Home_buttonGroup.addButton(ui.Study_radioButton)
    ui.Study_radioButton.setObjectName(u"Study_radioButton")
    sizePolicy3.setHeightForWidth(ui.Study_radioButton.sizePolicy().hasHeightForWidth())
    ui.Study_radioButton.setSizePolicy(sizePolicy3)

    ui.Home_horizontalLayout_2.addWidget(ui.Study_radioButton)

    ui.Work_radioButton = QRadioButton(ui.Home_frame)
    ui.Home_buttonGroup.addButton(ui.Work_radioButton)
    ui.Work_radioButton.setObjectName(u"Work_radioButton")
    sizePolicy3.setHeightForWidth(ui.Work_radioButton.sizePolicy().hasHeightForWidth())
    ui.Work_radioButton.setSizePolicy(sizePolicy3)

    ui.Home_horizontalLayout_2.addWidget(ui.Work_radioButton)

    ui.Other_radioButton = QRadioButton(ui.Home_frame)
    ui.Home_buttonGroup.addButton(ui.Other_radioButton)
    ui.Other_radioButton.setObjectName(u"Other_radioButton")
    sizePolicy3.setHeightForWidth(ui.Other_radioButton.sizePolicy().hasHeightForWidth())
    ui.Other_radioButton.setSizePolicy(sizePolicy3)

    ui.Home_horizontalLayout_2.addWidget(ui.Other_radioButton)

    ui.Home_verticalLayout_2.addLayout(ui.Home_horizontalLayout_2)

    ui.Home_horizontalLayout_3 = QHBoxLayout()
    ui.Home_horizontalLayout_3.setObjectName(u"Home_horizontalLayout_3")
    ui.Home_dateEdit = QDateEdit(ui.Home_frame)
    ui.Home_dateEdit.setObjectName(u"Home_dateEdit")
    sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    sizePolicy4.setHorizontalStretch(0)
    sizePolicy4.setVerticalStretch(0)
    sizePolicy4.setHeightForWidth(ui.Home_dateEdit.sizePolicy().hasHeightForWidth())
    ui.Home_dateEdit.setSizePolicy(sizePolicy4)
    ui.Home_dateEdit.setMaximumSize(QSize(150, 16777215))

    ui.Home_horizontalLayout_3.addWidget(ui.Home_dateEdit)

    ui.Home_horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

    ui.Home_horizontalLayout_3.addItem(ui.Home_horizontalSpacer)

    ui.Home_pushButton = QPushButton(ui.Home_frame)
    ui.Home_pushButton.setObjectName(u"Home_pushButton")
    sizePolicy3.setHeightForWidth(ui.Home_pushButton.sizePolicy().hasHeightForWidth())
    ui.Home_pushButton.setSizePolicy(sizePolicy3)
    ui.Home_pushButton.setMaximumSize(QSize(80, 80))
    ui.Home_pushButton.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-style: none;\n"
"	background-color: rgb(189, 147, 249);\n"
"	border-radius: 5px;\n"
"}")

    ui.Home_horizontalLayout_3.addWidget(ui.Home_pushButton)

    ui.Home_horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

    ui.Home_horizontalLayout_3.addItem(ui.Home_horizontalSpacer_2)

    ui.Home_pushButton_2 = QPushButton(ui.Home_frame)
    ui.Home_pushButton_2.setObjectName(u"Home_pushButton_2")
    sizePolicy2.setHeightForWidth(ui.Home_pushButton_2.sizePolicy().hasHeightForWidth())
    ui.Home_pushButton_2.setSizePolicy(sizePolicy2)
    ui.Home_pushButton_2.setMaximumSize(QSize(80, 16777215))
    ui.Home_pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-style: none;\n"
"	background-color: rgb(189, 147, 249);\n"
"	border-radius: 5px;\n"
"}")

    ui.Home_horizontalLayout_3.addWidget(ui.Home_pushButton_2)

    ui.Home_verticalLayout_2.addLayout(ui.Home_horizontalLayout_3)

    ui.Home_horizontalLayout_4.addLayout(ui.Home_verticalLayout_2)

    ui.Home_verticalLayout.addWidget(ui.Home_frame)

    ui.Home_listWidget = QListWidget()
    ui.Home_listWidget.setObjectName(u"Home_listWidget")
    sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy5.setHorizontalStretch(0)
    sizePolicy5.setVerticalStretch(4)
    sizePolicy5.setHeightForWidth(ui.Home_listWidget.sizePolicy().hasHeightForWidth())
    ui.Home_listWidget.setSizePolicy(sizePolicy5)
    ui.Home_listWidget.setStyleSheet(u"border:none;")

    ui.Home_label.setText("")
    ui.All_radioButton.setText("All")
    ui.Sport_radioButton.setText("Sport")
    ui.Study_radioButton.setText("Study")
    ui.Work_radioButton.setText("Work")
    ui.Other_radioButton.setText("Other")
    ui.Home_pushButton.setText("Confirm")
    ui.Home_pushButton_2.setText("Cancel")

    ui.Home_verticalLayout.addWidget(ui.Home_listWidget)



## TODO 在Main中初始化tasks

