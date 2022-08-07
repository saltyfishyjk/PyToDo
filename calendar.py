from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import time
import datetime
time_tuple = time.localtime(time.time())
def setupCalendar(calendar):
    testTaskCreate(calendar)
def getTimeStr():
    return str(time_tuple[0])+'-'+str(time_tuple[1])+'-'+str(time_tuple[2])
def getPos():
    d=datetime.datetime.now().weekday()
    t=[0,1,2,3,4,5,6]
    pt=d
    cnt=0
    num=time_tuple[2]
    while num!=1:
        if pt==6:
            cnt+=1
        pt=t[pt-1]
        num-=1
    return cnt, t[(d+1)%7]
def testTaskCreate(calendar):
    row, col=getPos()
    calendar.setItem(row, col,QStandardItem("Test Task\n"+getTimeStr()))