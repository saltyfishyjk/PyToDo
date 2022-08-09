from PySide6.QtCore import Qt
from PyQt6.Qt6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


def calendar_ui_init(self):

    self.calendar_layout = QVBoxLayout(self.calendar_page)
    self.calendar_layout.setObjectName(u"calendar_layout")

    self.calendar_month=QHBoxLayout()
    self.calendar_month.setObjectName(u"calendar_month")
    self.calendar_leftMonthButton=QPushButton("leftMonthButton")
    #self.calendar_leftMonthButton.setFont(button_font)
    self.calendar_leftMonthButton.setText(' Last ')
    self.calendar_leftMonthButton.setStyleSheet("font-size: 20px;color: black;background-color: #FFFFFF;border-radius: 15px;")
    self.calendar_month.addWidget(self.calendar_leftMonthButton)
    self.calendar_leftMonthButton.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Expanding)
    # self.calendar_leftMonthButton.clicked.connect(self.login)

    self.CalendarTitle = QTextEdit(self.calendar_page)
    self.CalendarTitle.setObjectName(u"CalendarTitle")
    import time
    time_tuple = time.localtime(time.time())
    monthName=['','January','February','March','April','May','June','July','August','September','October','November','December']
    self.CalendarTitle.setText('<font size="6", color=\"#FFFFFF\">'+monthName[time_tuple[1]]+'</font>')
    self.CalendarTitle.setAlignment(Qt.AlignCenter)
    self.CalendarTitle.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    self.CalendarTitle.setReadOnly(True)
    self.calendar_month.addWidget(self.CalendarTitle)

    self.calendar_rightMonthButton=QPushButton("rightMonthButton")
    self.calendar_rightMonthButton.setText(' Next ')
    self.calendar_rightMonthButton.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Expanding)
    self.calendar_rightMonthButton.setStyleSheet("font-size: 20px;color: black;background-color: #FFFFFF;border-radius: 15px;")
    self.calendar_month.addWidget(self.calendar_rightMonthButton)
    # self.calendar_leftMonthButton.clicked.connect(self.login)

    self.calendar_layout.addLayout(self.calendar_month)

    self.calendar_week = QHBoxLayout()
    self.calendar_week.setObjectName(u"calendar_week")
    self.calendar_Sun = QTextEdit(self.calendar_page)
    self.calendar_Sun.setObjectName(u"calendar_Sun")
    self.calendar_Sun.setText('<font size="6", color=\"#FFFFFF\">Sun</font>')
    self.calendar_Sun.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    self.calendar_Sun.setAlignment(Qt.AlignCenter)
    self.calendar_Sun.setFrameShape(QFrame.Box)
    self.calendar_Sun.setReadOnly(True)
    self.calendar_week.addWidget(self.calendar_Sun)

    self.calendar_Mon = QTextEdit(self.calendar_page)
    self.calendar_Mon.setObjectName(u"calendar_Mon")
    self.calendar_Mon.setText('<font size="6", color=\"#FFFFFF\">Mon</font>')
    self.calendar_Mon.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    self.calendar_Mon.setAlignment(Qt.AlignCenter)
    self.calendar_Mon.setReadOnly(True)
    self.calendar_week.addWidget(self.calendar_Mon)

    self.calendar_Thue = QTextEdit(self.calendar_page)
    self.calendar_Thue.setObjectName(u"calendar_Thue")
    self.calendar_Thue.setText('<font size="6", color=\"#FFFFFF\">Thue</font>')
    self.calendar_Thue.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    self.calendar_Thue.setAlignment(Qt.AlignCenter)
    self.calendar_Thue.setReadOnly(True)
    self.calendar_week.addWidget(self.calendar_Thue)

    self.calendar_Wed = QTextEdit(self.calendar_page)
    self.calendar_Wed.setObjectName(u"calendar_Wed")
    self.calendar_Wed.setText('<font size="6", color=\"#FFFFFF\">Wed</font>')
    self.calendar_Wed.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    self.calendar_Wed.setAlignment(Qt.AlignCenter)
    self.calendar_Wed.setReadOnly(True)
    self.calendar_week.addWidget(self.calendar_Wed)

    self.calendar_Thur = QTextEdit(self.calendar_page)
    self.calendar_Thur.setObjectName(u"calendar_Thur")
    self.calendar_Thur.setText('<font size="6", color=\"#FFFFFF\">Thur</font>')
    self.calendar_Thur.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    self.calendar_Thur.setAlignment(Qt.AlignCenter)
    self.calendar_Thur.setReadOnly(True)
    self.calendar_week.addWidget(self.calendar_Thur)

    self.calendar_Fri = QTextEdit(self.calendar_page)
    self.calendar_Fri.setObjectName(u"calendar_Fri")
    self.calendar_Fri.setText('<font size="6", color=\"#FFFFFF\">Fri</font>')
    self.calendar_Fri.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    self.calendar_Fri.setAlignment(Qt.AlignCenter)
    self.calendar_Fri.setReadOnly(True)
    self.calendar_week.addWidget(self.calendar_Fri)

    self.calendar_Sat = QTextEdit(self.calendar_page)
    self.calendar_Sat.setObjectName(u"calendar_Sat")
    self.calendar_Sat.setText('<font size="6", color=\"#FFFFFF\">Sat</font>')
    self.calendar_Sat.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    self.calendar_Sat.setAlignment(Qt.AlignCenter)
    self.calendar_Sat.setReadOnly(True)
    self.calendar_week.addWidget(self.calendar_Sat)


    self.calendar_layout.addLayout(self.calendar_week)

    self.CalendarTable = QGridLayout()
    self.CalendarTable.setObjectName(u"CalendarTable")
    self.calendar15 = QPlainTextEdit(self.calendar_page)
    self.calendar15.setObjectName(u"calendar15")
    '''
    text='Task1 in 2022-8-4<br>Task2 in 2022-8-4<br>Task3 in 2022-8-4'
    self.calendar15.appendHtml('<font size="4",align="center", color=\"#000000\">'+text+'</font>')
    '''
    #print(self.calendar15.toPlainText())

    self.CalendarTable.addWidget(self.calendar15, 0, 4, 1, 1)

    self.calendar41 = QPlainTextEdit(self.calendar_page)
    self.calendar41.setObjectName(u"calendar41")

    self.CalendarTable.addWidget(self.calendar41, 3, 0, 1, 1)

    self.calendar36 = QPlainTextEdit(self.calendar_page)
    self.calendar36.setObjectName(u"calendar36")

    self.CalendarTable.addWidget(self.calendar36, 2, 5, 1, 1)

    self.calendar46 = QPlainTextEdit(self.calendar_page)
    self.calendar46.setObjectName(u"calendar46")

    self.CalendarTable.addWidget(self.calendar46, 3, 5, 1, 1)

    self.calendar52 = QPlainTextEdit(self.calendar_page)
    self.calendar52.setObjectName(u"calendar52")

    self.CalendarTable.addWidget(self.calendar52, 4, 1, 1, 1)

    self.calendar27 = QPlainTextEdit(self.calendar_page)
    self.calendar27.setObjectName(u"calendar27")

    self.CalendarTable.addWidget(self.calendar27, 1, 6, 1, 1)

    self.calendar55 = QPlainTextEdit(self.calendar_page)
    self.calendar55.setObjectName(u"calendar55")

    self.CalendarTable.addWidget(self.calendar55, 4, 4, 1, 1)

    self.calendar43 = QPlainTextEdit(self.calendar_page)
    self.calendar43.setObjectName(u"calendar43")

    self.CalendarTable.addWidget(self.calendar43, 3, 2, 1, 1)

    self.calendar44 = QPlainTextEdit(self.calendar_page)
    self.calendar44.setObjectName(u"calendar44")

    self.CalendarTable.addWidget(self.calendar44, 3, 3, 1, 1)

    self.calendar67 = QPlainTextEdit(self.calendar_page)
    self.calendar67.setObjectName(u"calendar67")

    self.CalendarTable.addWidget(self.calendar67, 5, 6, 1, 1)

    self.calendar47 = QPlainTextEdit(self.calendar_page)
    self.calendar47.setObjectName(u"calendar47")

    self.CalendarTable.addWidget(self.calendar47, 3, 6, 1, 1)

    self.calendar21 = QPlainTextEdit(self.calendar_page)
    self.calendar21.setObjectName(u"calendar21")

    self.CalendarTable.addWidget(self.calendar21, 1, 0, 1, 1)

    self.calendar66 = QPlainTextEdit(self.calendar_page)
    self.calendar66.setObjectName(u"calendar66")

    self.CalendarTable.addWidget(self.calendar66, 5, 5, 1, 1)

    self.calendar45 = QPlainTextEdit(self.calendar_page)
    self.calendar45.setObjectName(u"calendar45")

    self.CalendarTable.addWidget(self.calendar45, 3, 4, 1, 1)

    self.calendar64 = QPlainTextEdit(self.calendar_page)
    self.calendar64.setObjectName(u"calendar64")

    self.CalendarTable.addWidget(self.calendar64, 5, 3, 1, 1)

    self.calendar16 = QPlainTextEdit(self.calendar_page)
    self.calendar16.setObjectName(u"calendar16")

    self.CalendarTable.addWidget(self.calendar16, 0, 5, 1, 1)

    self.calendar22 = QPlainTextEdit(self.calendar_page)
    self.calendar22.setObjectName(u"calendar22")

    self.CalendarTable.addWidget(self.calendar22, 1, 1, 1, 1)

    self.calendar11 = QPlainTextEdit(self.calendar_page)
    self.calendar11.setObjectName(u"calendar11")

    self.CalendarTable.addWidget(self.calendar11, 0, 0, 1, 1)

    self.calendar42 = QPlainTextEdit(self.calendar_page)
    self.calendar42.setObjectName(u"calendar42")

    self.CalendarTable.addWidget(self.calendar42, 3, 1, 1, 1)

    self.calendar33 = QPlainTextEdit(self.calendar_page)
    self.calendar33.setObjectName(u"calendar33")

    self.CalendarTable.addWidget(self.calendar33, 2, 2, 1, 1)

    self.calendar61 = QPlainTextEdit(self.calendar_page)
    self.calendar61.setObjectName(u"calendar61")

    self.CalendarTable.addWidget(self.calendar61, 5, 0, 1, 1)

    self.calendar14 = QPlainTextEdit(self.calendar_page)
    self.calendar14.setObjectName(u"calendar14")

    self.CalendarTable.addWidget(self.calendar14, 0, 3, 1, 1)

    self.calendar56 = QPlainTextEdit(self.calendar_page)
    self.calendar56.setObjectName(u"calendar56")

    self.CalendarTable.addWidget(self.calendar56, 4, 5, 1, 1)

    self.calendar12 = QPlainTextEdit(self.calendar_page)
    self.calendar12.setObjectName(u"calendar12")

    self.CalendarTable.addWidget(self.calendar12, 0, 1, 1, 1)

    self.calendar54 = QPlainTextEdit(self.calendar_page)
    self.calendar54.setObjectName(u"calendar54")

    self.CalendarTable.addWidget(self.calendar54, 4, 3, 1, 1)

    self.calendar53 = QPlainTextEdit(self.calendar_page)
    self.calendar53.setObjectName(u"calendar53")

    self.CalendarTable.addWidget(self.calendar53, 4, 2, 1, 1)

    self.calendar25 = QPlainTextEdit(self.calendar_page)
    self.calendar25.setObjectName(u"calendar25")

    self.CalendarTable.addWidget(self.calendar25, 1, 4, 1, 1)

    self.calendar57 = QPlainTextEdit(self.calendar_page)
    self.calendar57.setObjectName(u"calendar57")

    self.CalendarTable.addWidget(self.calendar57, 4, 6, 1, 1)

    self.calendar65 = QPlainTextEdit(self.calendar_page)
    self.calendar65.setObjectName(u"calendar65")

    self.CalendarTable.addWidget(self.calendar65, 5, 4, 1, 1)

    self.calendar31 = QPlainTextEdit(self.calendar_page)
    self.calendar31.setObjectName(u"calendar31")

    self.CalendarTable.addWidget(self.calendar31, 2, 0, 1, 1)

    self.calendar34 = QPlainTextEdit(self.calendar_page)
    self.calendar34.setObjectName(u"calendar34")

    self.CalendarTable.addWidget(self.calendar34, 2, 3, 1, 1)

    self.calendar62 = QPlainTextEdit(self.calendar_page)
    self.calendar62.setObjectName(u"calendar62")

    self.CalendarTable.addWidget(self.calendar62, 5, 1, 1, 1)

    self.calendar24 = QPlainTextEdit(self.calendar_page)
    self.calendar24.setObjectName(u"calendar24")

    self.CalendarTable.addWidget(self.calendar24, 1, 3, 1, 1)

    self.calendar32 = QPlainTextEdit(self.calendar_page)
    self.calendar32.setObjectName(u"calendar32")

    self.CalendarTable.addWidget(self.calendar32, 2, 1, 1, 1)

    self.calendar26 = QPlainTextEdit(self.calendar_page)
    self.calendar26.setObjectName(u"calendar26")

    self.CalendarTable.addWidget(self.calendar26, 1, 5, 1, 1)

    self.calendar51 = QPlainTextEdit(self.calendar_page)
    self.calendar51.setObjectName(u"calendar51")

    self.CalendarTable.addWidget(self.calendar51, 4, 0, 1, 1)

    self.calendar35 = QPlainTextEdit(self.calendar_page)
    self.calendar35.setObjectName(u"calendar35")

    self.CalendarTable.addWidget(self.calendar35, 2, 4, 1, 1)

    self.calendar17 = QPlainTextEdit(self.calendar_page)
    self.calendar17.setObjectName(u"calendar17")

    self.CalendarTable.addWidget(self.calendar17, 0, 6, 1, 1)

    self.calendar23 = QPlainTextEdit(self.calendar_page)
    self.calendar23.setObjectName(u"calendar23")

    self.CalendarTable.addWidget(self.calendar23, 1, 2, 1, 1)

    self.calendar37 = QPlainTextEdit(self.calendar_page)
    self.calendar37.setObjectName(u"calendar37")

    self.CalendarTable.addWidget(self.calendar37, 2, 6, 1, 1)

    self.calendar63 = QPlainTextEdit(self.calendar_page)
    self.calendar63.setObjectName(u"calendar63")

    self.CalendarTable.addWidget(self.calendar63, 5, 2, 1, 1)

    self.calendar13 = QPlainTextEdit(self.calendar_page)
    self.calendar13.setObjectName(u"calendar13")

    self.CalendarTable.addWidget(self.calendar13, 0, 2, 1, 1)


    self.calendar_layout.addLayout(self.CalendarTable)

    self.calendar_DayMap=[
    [None,None,None,None,None,None,None],
    [self.calendar11,self.calendar12,self.calendar13,self.calendar14,self.calendar15,self.calendar16,self.calendar17],
    [self.calendar21,self.calendar22,self.calendar23,self.calendar24,self.calendar25,self.calendar26,self.calendar27],
    [self.calendar31,self.calendar32,self.calendar33,self.calendar34,self.calendar35,self.calendar36,self.calendar37],
    [self.calendar41,self.calendar42,self.calendar43,self.calendar44,self.calendar45,self.calendar46,self.calendar47],
    [self.calendar51,self.calendar52,self.calendar53,self.calendar54,self.calendar55,self.calendar56,self.calendar57],
    [self.calendar61,self.calendar62,self.calendar63,self.calendar64,self.calendar65,self.calendar66,self.calendar67]
    ]
    for row in range(1,7):
        for col in range(0,7):
            #self.calendar_DayMap[row][col].setStyleSheet("QMenu{background:#6272a4;}")
            self.calendar_DayMap[row][col].setStyleSheet("font-size: 15px;color: black;background-color: #FFFFFF;border-radius: 15px;")
            self.calendar_DayMap[row][col].setFrameShadow(QFrame.Sunken)
            self.calendar_DayMap[row][col].setReadOnly(True)
