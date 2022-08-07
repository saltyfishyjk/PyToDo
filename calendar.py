from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import time
import datetime
time_tuple = time.localtime(time.time())
def setupCalendar(calendarWidget,tasks,month):
    global calendar
    calendar=calendarWidget
    refresh_calendar(tasks,month)
    testTaskCreate(calendar)
def getTimeStr(year,month,day):
    return str(year)+'-'+str(month)+'-'+str(day)
def getPos(year,month,day):
    d=datetime.datetime.now().weekday()
    t=[0,1,2,3,4,5,6]
    pt=d
    cnt=0
    num=day
    while num!=1:
        if pt==6:
            cnt+=1
        pt=t[pt-1]
        num-=1
    return cnt, t[(d+1)%7]
def testTaskCreate(calendar):
    year=time_tuple[0]
    month=time_tuple[1]
    day=time_tuple[2]
    row, col=getPos(year,month,day)
    calendar.setItem(row, col, QStandardItem("Test Task\n"+getTimeStr(year,month,day)))
def displayTask(task):
    year, month, day=map(int,task.Task(task).ddl.split('/'))
    row, col=getPos(year, month, day)
    calendar.setItem(row, col, QStandardItem(task.title+"\n"+getTimeStr(year,month,day)))
    pass
def refresh_calendar(tasks,m=time_tuple[1]):
    for task in tasks:
        year, month, day=map(int,task.Task(task).ddl.split('/'))
        if month==m and time_tuple[0]==year:
            displayTask(task)

