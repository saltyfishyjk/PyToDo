from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import time
import datetime

from task import Task
from datetime import timedelta

time_tuple = time.localtime(time.time())
curYear=time_tuple[0]
curMonth=time_tuple[1]
curDay=time_tuple[2]
tasklist=[]
ui=None

def setupCalendar(Widgets,tasks,year=time_tuple[0],month=time_tuple[1]):
    global ui_calendar
    global tasklist
    global ui
    ui=Widgets
    tasklist=tasks
    ui_calendar=Widgets.calendar_DayMap
    monthButtonConnect()
    #testTaskCreate()
    refresh_calendar(year, month)

def getTimeStr(year,month,day):
    return str(year)+'-'+str(month)+'-'+str(day)

def getPos(year,month,day):
    d=datetime.date(year, month, day).weekday()
    t=[0,1,2,3,4,5,6]
    pt=d
    cnt=0
    num=day
    while num!=1:
        if pt==6:
            cnt+=1
        pt=t[pt-1]
        num-=1
    return cnt+1, t[(d+1)%7]

init_test_flag=True
def testTaskCreate():
    global ui_calendar
    global init_test_flag
    if init_test_flag:
        tasklist.append(Task("Test Task"))
        init_test_flag=False
    #ui_calendar[row][col].appendHtml('<font size="4",align="center", color=\"#000000\">'+"Test Task<br>"+'</font>')
    #ui_calendar[row][col].clear()

def displayTask(task, row, col):
    global ui_calendar
    ui_calendar[row][col].appendHtml('<font size="3",align="center", color=\"#000000\">'+task.title+'</font>')

def refresh_calendar(y=curYear, m=curMonth):
    global ui_calendar
    global tasklist
    tasks=tasklist
    monthName=['','January','February','March','April','May','June','July','August','September','October','November','December']
    ui.CalendarTitle.setText('<font size="6", color=\"#FFFFFF\">'+str(curYear)+' '+monthName[m]+'</font>')
    ui.CalendarTitle.setAlignment(Qt.AlignCenter)
    ui.CalendarTitle.setStyleSheet("background-color: #6272a4;border-radius: 15px;")
    ui.CalendarTitle.setReadOnly(True)
    fillDate(y,m)
    for task in tasks:
        #print("##"+task.title)
        ddl=list(map(int,task.ddl.split('/')))
        year=ddl[0]
        month=ddl[1]
        day=ddl[2]
        if curMonth==month and year==curYear and task.isDaily==False:
            r, c=getPos(year, month, day)
            displayTask(task, r, c)
        if task.isDaily:
            for row in range(1,7):
                for col in range(0,7):
                    yy,mm,dd=getCellDate(curYear,curMonth,row,col)
                    #print(yy+'-'+mm+'-'+dd)
                    #print(task.matrix_time_compare())
                    #print(int(yy)*10000+int(mm)*100+int(dd))
                    if task.matrix_time_compare()<=(int(yy)*10000+int(mm)*100+int(dd)):
                        #print('in')
                        displayTask(task, row, col)

def getCellDate(y,m,row,col):
    start_row,start_col=getPos(y,m,1)
    today=datetime.datetime(y, m, 1) + timedelta(days = (row-start_row)*7+(col-start_col))
    yy,mm,dd=today.strftime("%Y-%m-%d").split('-')
    return yy,mm,dd

def fillDate(y,m):
    global ui_calendar
    start_row,start_col=getPos(y,m,1)
    for row in range(1,7):
        for col in range(0,7):
            ui_calendar[row][col].clear()
            today=datetime.datetime(y, m, 1) + timedelta(days = (row-start_row)*7+(col-start_col))
            yy,mm,dd=today.strftime("%Y-%m-%d").split('-')
            if int(yy)==time_tuple[0] and int(mm)==time_tuple[1] and int(dd)==time_tuple[2]:
                ui_calendar[row][col].appendHtml('<font size="3",align="center", color=\"#ff79c6\"><b>'+dd+' Today<b></font>')
            else:
                ui_calendar[row][col].appendHtml('<font size="3",align="center", color=\"#000000\">'+dd+'</font>')

def monthButtonConnect():
    global ui
    # calendar_leftMonthButton & calendar_rightMonthButton
    ui.calendar_leftMonthButton.clicked.connect(lastMonth)
    ui.calendar_rightMonthButton.clicked.connect(nextMonth)

def lastMonth():
    global curMonth
    global curYear
    if curMonth==1:
        curYear-=1
        curMonth=12
        refresh_calendar(y=curYear,m=curMonth)
    else:
        curMonth-=1
        refresh_calendar(y=curYear,m=curMonth)

def nextMonth():
    global curMonth
    global curYear
    if curMonth==12:
        curYear+=1
        curMonth=1
        refresh_calendar(y=curYear,m=curMonth)
    else:
        curMonth+=1
        refresh_calendar(y=curYear,m=curMonth)
