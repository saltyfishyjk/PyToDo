from PySide6.QtCore import Qt
from PyQt6.Qt6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


def calendar_ui_init(ui):

    ui.calendar_layout = QVBoxLayout(ui.calendar_page)
    ui.calendar_layout.setObjectName(u"calendar_layout")

    ui.calendar_month=QHBoxLayout()
    ui.calendar_month.setObjectName(u"calendar_month")
    ui.calendar_leftMonthButton=QPushButton("leftMonthButton")
    #ui.calendar_leftMonthButton.setFont(button_font)
    ui.calendar_leftMonthButton.setText(' Last ')
    ui.calendar_leftMonthButton.setStyleSheet("font-size: 20px;color: black;background-color: #FFFFFF;border-radius: 15px;")
    ui.calendar_month.addWidget(ui.calendar_leftMonthButton)
    ui.calendar_leftMonthButton.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Expanding)
    # ui.calendar_leftMonthButton.clicked.connect(ui.login)

    ui.CalendarTitle = QTextEdit(ui.calendar_page)
    ui.CalendarTitle.setObjectName(u"CalendarTitle")
    #import time
    #time_tuple = time.localtime(time.time())
    #monthName=['','January','February','March','April','May','June','July','August','September','October','November','December']
    #ui.CalendarTitle.setText('<font size="6", color=\"#FFFFFF\">'+str(time_tuple[0])+'&emsp'+monthName[time_tuple[1]]+'</font>')
    ui.CalendarTitle.setAlignment(Qt.AlignCenter)
    ui.CalendarTitle.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    ui.CalendarTitle.setReadOnly(True)
    ui.calendar_month.addWidget(ui.CalendarTitle)

    ui.calendar_rightMonthButton=QPushButton("rightMonthButton")
    ui.calendar_rightMonthButton.setText(' Next ')
    ui.calendar_rightMonthButton.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Expanding)
    ui.calendar_rightMonthButton.setStyleSheet("font-size: 20px;color: black;background-color: #FFFFFF;border-radius: 15px;")
    ui.calendar_month.addWidget(ui.calendar_rightMonthButton)
    # ui.calendar_leftMonthButton.clicked.connect(ui.login)

    ui.calendar_layout.addLayout(ui.calendar_month)

    ui.calendar_week = QHBoxLayout()
    ui.calendar_week.setObjectName(u"calendar_week")
    ui.calendar_Sun = QTextEdit(ui.calendar_page)
    ui.calendar_Sun.setObjectName(u"calendar_Sun")
    ui.calendar_Sun.setText('<font size="6", color=\"#FFFFFF\">Sun</font>')
    ui.calendar_Sun.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    ui.calendar_Sun.setAlignment(Qt.AlignCenter)
    ui.calendar_Sun.setFrameShape(QFrame.Box)
    ui.calendar_Sun.setReadOnly(True)
    ui.calendar_week.addWidget(ui.calendar_Sun)

    ui.calendar_Mon = QTextEdit(ui.calendar_page)
    ui.calendar_Mon.setObjectName(u"calendar_Mon")
    ui.calendar_Mon.setText('<font size="6", color=\"#FFFFFF\">Mon</font>')
    ui.calendar_Mon.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    ui.calendar_Mon.setAlignment(Qt.AlignCenter)
    ui.calendar_Mon.setReadOnly(True)
    ui.calendar_week.addWidget(ui.calendar_Mon)

    ui.calendar_Thue = QTextEdit(ui.calendar_page)
    ui.calendar_Thue.setObjectName(u"calendar_Thue")
    ui.calendar_Thue.setText('<font size="6", color=\"#FFFFFF\">Thue</font>')
    ui.calendar_Thue.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    ui.calendar_Thue.setAlignment(Qt.AlignCenter)
    ui.calendar_Thue.setReadOnly(True)
    ui.calendar_week.addWidget(ui.calendar_Thue)

    ui.calendar_Wed = QTextEdit(ui.calendar_page)
    ui.calendar_Wed.setObjectName(u"calendar_Wed")
    ui.calendar_Wed.setText('<font size="6", color=\"#FFFFFF\">Wed</font>')
    ui.calendar_Wed.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    ui.calendar_Wed.setAlignment(Qt.AlignCenter)
    ui.calendar_Wed.setReadOnly(True)
    ui.calendar_week.addWidget(ui.calendar_Wed)

    ui.calendar_Thur = QTextEdit(ui.calendar_page)
    ui.calendar_Thur.setObjectName(u"calendar_Thur")
    ui.calendar_Thur.setText('<font size="6", color=\"#FFFFFF\">Thur</font>')
    ui.calendar_Thur.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    ui.calendar_Thur.setAlignment(Qt.AlignCenter)
    ui.calendar_Thur.setReadOnly(True)
    ui.calendar_week.addWidget(ui.calendar_Thur)

    ui.calendar_Fri = QTextEdit(ui.calendar_page)
    ui.calendar_Fri.setObjectName(u"calendar_Fri")
    ui.calendar_Fri.setText('<font size="6", color=\"#FFFFFF\">Fri</font>')
    ui.calendar_Fri.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    ui.calendar_Fri.setAlignment(Qt.AlignCenter)
    ui.calendar_Fri.setReadOnly(True)
    ui.calendar_week.addWidget(ui.calendar_Fri)

    ui.calendar_Sat = QTextEdit(ui.calendar_page)
    ui.calendar_Sat.setObjectName(u"calendar_Sat")
    ui.calendar_Sat.setText('<font size="6", color=\"#FFFFFF\">Sat</font>')
    ui.calendar_Sat.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    ui.calendar_Sat.setAlignment(Qt.AlignCenter)
    ui.calendar_Sat.setReadOnly(True)
    ui.calendar_week.addWidget(ui.calendar_Sat)


    ui.calendar_layout.addLayout(ui.calendar_week)

    ui.CalendarTable = QGridLayout()
    ui.CalendarTable.setObjectName(u"CalendarTable")
    ui.calendar15 = QPlainTextEdit(ui.calendar_page)
    ui.calendar15.setObjectName(u"calendar15")
    '''
    text='Task1 in 2022-8-4<br>Task2 in 2022-8-4<br>Task3 in 2022-8-4'
    ui.calendar15.appendHtml('<font size="4",align="center", color=\"#000000\">'+text+'</font>')
    '''
    #print(ui.calendar15.toPlainText())

    ui.CalendarTable.addWidget(ui.calendar15, 0, 4, 1, 1)

    ui.calendar41 = QPlainTextEdit(ui.calendar_page)
    ui.calendar41.setObjectName(u"calendar41")

    ui.CalendarTable.addWidget(ui.calendar41, 3, 0, 1, 1)

    ui.calendar36 = QPlainTextEdit(ui.calendar_page)
    ui.calendar36.setObjectName(u"calendar36")

    ui.CalendarTable.addWidget(ui.calendar36, 2, 5, 1, 1)

    ui.calendar46 = QPlainTextEdit(ui.calendar_page)
    ui.calendar46.setObjectName(u"calendar46")

    ui.CalendarTable.addWidget(ui.calendar46, 3, 5, 1, 1)

    ui.calendar52 = QPlainTextEdit(ui.calendar_page)
    ui.calendar52.setObjectName(u"calendar52")

    ui.CalendarTable.addWidget(ui.calendar52, 4, 1, 1, 1)

    ui.calendar27 = QPlainTextEdit(ui.calendar_page)
    ui.calendar27.setObjectName(u"calendar27")

    ui.CalendarTable.addWidget(ui.calendar27, 1, 6, 1, 1)

    ui.calendar55 = QPlainTextEdit(ui.calendar_page)
    ui.calendar55.setObjectName(u"calendar55")

    ui.CalendarTable.addWidget(ui.calendar55, 4, 4, 1, 1)

    ui.calendar43 = QPlainTextEdit(ui.calendar_page)
    ui.calendar43.setObjectName(u"calendar43")

    ui.CalendarTable.addWidget(ui.calendar43, 3, 2, 1, 1)

    ui.calendar44 = QPlainTextEdit(ui.calendar_page)
    ui.calendar44.setObjectName(u"calendar44")

    ui.CalendarTable.addWidget(ui.calendar44, 3, 3, 1, 1)

    ui.calendar67 = QPlainTextEdit(ui.calendar_page)
    ui.calendar67.setObjectName(u"calendar67")

    ui.CalendarTable.addWidget(ui.calendar67, 5, 6, 1, 1)

    ui.calendar47 = QPlainTextEdit(ui.calendar_page)
    ui.calendar47.setObjectName(u"calendar47")

    ui.CalendarTable.addWidget(ui.calendar47, 3, 6, 1, 1)

    ui.calendar21 = QPlainTextEdit(ui.calendar_page)
    ui.calendar21.setObjectName(u"calendar21")

    ui.CalendarTable.addWidget(ui.calendar21, 1, 0, 1, 1)

    ui.calendar66 = QPlainTextEdit(ui.calendar_page)
    ui.calendar66.setObjectName(u"calendar66")

    ui.CalendarTable.addWidget(ui.calendar66, 5, 5, 1, 1)

    ui.calendar45 = QPlainTextEdit(ui.calendar_page)
    ui.calendar45.setObjectName(u"calendar45")

    ui.CalendarTable.addWidget(ui.calendar45, 3, 4, 1, 1)

    ui.calendar64 = QPlainTextEdit(ui.calendar_page)
    ui.calendar64.setObjectName(u"calendar64")

    ui.CalendarTable.addWidget(ui.calendar64, 5, 3, 1, 1)

    ui.calendar16 = QPlainTextEdit(ui.calendar_page)
    ui.calendar16.setObjectName(u"calendar16")

    ui.CalendarTable.addWidget(ui.calendar16, 0, 5, 1, 1)

    ui.calendar22 = QPlainTextEdit(ui.calendar_page)
    ui.calendar22.setObjectName(u"calendar22")

    ui.CalendarTable.addWidget(ui.calendar22, 1, 1, 1, 1)

    ui.calendar11 = QPlainTextEdit(ui.calendar_page)
    ui.calendar11.setObjectName(u"calendar11")

    ui.CalendarTable.addWidget(ui.calendar11, 0, 0, 1, 1)

    ui.calendar42 = QPlainTextEdit(ui.calendar_page)
    ui.calendar42.setObjectName(u"calendar42")

    ui.CalendarTable.addWidget(ui.calendar42, 3, 1, 1, 1)

    ui.calendar33 = QPlainTextEdit(ui.calendar_page)
    ui.calendar33.setObjectName(u"calendar33")

    ui.CalendarTable.addWidget(ui.calendar33, 2, 2, 1, 1)

    ui.calendar61 = QPlainTextEdit(ui.calendar_page)
    ui.calendar61.setObjectName(u"calendar61")

    ui.CalendarTable.addWidget(ui.calendar61, 5, 0, 1, 1)

    ui.calendar14 = QPlainTextEdit(ui.calendar_page)
    ui.calendar14.setObjectName(u"calendar14")

    ui.CalendarTable.addWidget(ui.calendar14, 0, 3, 1, 1)

    ui.calendar56 = QPlainTextEdit(ui.calendar_page)
    ui.calendar56.setObjectName(u"calendar56")

    ui.CalendarTable.addWidget(ui.calendar56, 4, 5, 1, 1)

    ui.calendar12 = QPlainTextEdit(ui.calendar_page)
    ui.calendar12.setObjectName(u"calendar12")

    ui.CalendarTable.addWidget(ui.calendar12, 0, 1, 1, 1)

    ui.calendar54 = QPlainTextEdit(ui.calendar_page)
    ui.calendar54.setObjectName(u"calendar54")

    ui.CalendarTable.addWidget(ui.calendar54, 4, 3, 1, 1)

    ui.calendar53 = QPlainTextEdit(ui.calendar_page)
    ui.calendar53.setObjectName(u"calendar53")

    ui.CalendarTable.addWidget(ui.calendar53, 4, 2, 1, 1)

    ui.calendar25 = QPlainTextEdit(ui.calendar_page)
    ui.calendar25.setObjectName(u"calendar25")

    ui.CalendarTable.addWidget(ui.calendar25, 1, 4, 1, 1)

    ui.calendar57 = QPlainTextEdit(ui.calendar_page)
    ui.calendar57.setObjectName(u"calendar57")

    ui.CalendarTable.addWidget(ui.calendar57, 4, 6, 1, 1)

    ui.calendar65 = QPlainTextEdit(ui.calendar_page)
    ui.calendar65.setObjectName(u"calendar65")

    ui.CalendarTable.addWidget(ui.calendar65, 5, 4, 1, 1)

    ui.calendar31 = QPlainTextEdit(ui.calendar_page)
    ui.calendar31.setObjectName(u"calendar31")

    ui.CalendarTable.addWidget(ui.calendar31, 2, 0, 1, 1)

    ui.calendar34 = QPlainTextEdit(ui.calendar_page)
    ui.calendar34.setObjectName(u"calendar34")

    ui.CalendarTable.addWidget(ui.calendar34, 2, 3, 1, 1)

    ui.calendar62 = QPlainTextEdit(ui.calendar_page)
    ui.calendar62.setObjectName(u"calendar62")

    ui.CalendarTable.addWidget(ui.calendar62, 5, 1, 1, 1)

    ui.calendar24 = QPlainTextEdit(ui.calendar_page)
    ui.calendar24.setObjectName(u"calendar24")

    ui.CalendarTable.addWidget(ui.calendar24, 1, 3, 1, 1)

    ui.calendar32 = QPlainTextEdit(ui.calendar_page)
    ui.calendar32.setObjectName(u"calendar32")

    ui.CalendarTable.addWidget(ui.calendar32, 2, 1, 1, 1)

    ui.calendar26 = QPlainTextEdit(ui.calendar_page)
    ui.calendar26.setObjectName(u"calendar26")

    ui.CalendarTable.addWidget(ui.calendar26, 1, 5, 1, 1)

    ui.calendar51 = QPlainTextEdit(ui.calendar_page)
    ui.calendar51.setObjectName(u"calendar51")

    ui.CalendarTable.addWidget(ui.calendar51, 4, 0, 1, 1)

    ui.calendar35 = QPlainTextEdit(ui.calendar_page)
    ui.calendar35.setObjectName(u"calendar35")

    ui.CalendarTable.addWidget(ui.calendar35, 2, 4, 1, 1)

    ui.calendar17 = QPlainTextEdit(ui.calendar_page)
    ui.calendar17.setObjectName(u"calendar17")

    ui.CalendarTable.addWidget(ui.calendar17, 0, 6, 1, 1)

    ui.calendar23 = QPlainTextEdit(ui.calendar_page)
    ui.calendar23.setObjectName(u"calendar23")

    ui.CalendarTable.addWidget(ui.calendar23, 1, 2, 1, 1)

    ui.calendar37 = QPlainTextEdit(ui.calendar_page)
    ui.calendar37.setObjectName(u"calendar37")

    ui.CalendarTable.addWidget(ui.calendar37, 2, 6, 1, 1)

    ui.calendar63 = QPlainTextEdit(ui.calendar_page)
    ui.calendar63.setObjectName(u"calendar63")

    ui.CalendarTable.addWidget(ui.calendar63, 5, 2, 1, 1)

    ui.calendar13 = QPlainTextEdit(ui.calendar_page)
    ui.calendar13.setObjectName(u"calendar13")

    ui.CalendarTable.addWidget(ui.calendar13, 0, 2, 1, 1)


    ui.calendar_layout.addLayout(ui.CalendarTable)

    ui.calendar_DayMap=[
    [None,None,None,None,None,None,None],
    [ui.calendar11,ui.calendar12,ui.calendar13,ui.calendar14,ui.calendar15,ui.calendar16,ui.calendar17],
    [ui.calendar21,ui.calendar22,ui.calendar23,ui.calendar24,ui.calendar25,ui.calendar26,ui.calendar27],
    [ui.calendar31,ui.calendar32,ui.calendar33,ui.calendar34,ui.calendar35,ui.calendar36,ui.calendar37],
    [ui.calendar41,ui.calendar42,ui.calendar43,ui.calendar44,ui.calendar45,ui.calendar46,ui.calendar47],
    [ui.calendar51,ui.calendar52,ui.calendar53,ui.calendar54,ui.calendar55,ui.calendar56,ui.calendar57],
    [ui.calendar61,ui.calendar62,ui.calendar63,ui.calendar64,ui.calendar65,ui.calendar66,ui.calendar67]
    ]
    for row in range(1,7):
        for col in range(0,7):
            #ui.calendar_DayMap[row][col].setStyleSheet("QMenu{background:#6272a4;}")
            ui.calendar_DayMap[row][col].setStyleSheet("font-size: 15px;color: black;background-color: #FFFFFF;border-radius: 15px;")
            ui.calendar_DayMap[row][col].setFrameShadow(QFrame.Sunken)
            ui.calendar_DayMap[row][col].setReadOnly(True)

