from PyQt6.Qt6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import time
time_tuple = time.localtime(time.time())
curYear=time_tuple[0]
curMonth=time_tuple[1]
curDay=time_tuple[2]
# micro definitions
TASK_FINISHED = 'finished'
TASK_OVERDUE = "overdue"
TASK_UNDERWAY = "underway"
TASK_NOTSTART = "notstarted"
TASK_UNFINISHED = "unfinished"
TASK_IMPORTANCE_LINE = 3

TASK_TYPE_OTHER = "Other"
TASK_TYPE_WORK = "Work"
TASK_TYPE_STUDY = "Study"
TASK_TYPE_SPORT = "Sport"

class Task():
    def __init__(self,
                 title,
                 text = None,
                 author = 'anonymity',
                 creatTime = str(curYear)+'/'+str(curMonth)+'/'+str(curDay),
                 description = '',
                 importance = 1,
                 isDaily = False,
                 type = TASK_TYPE_OTHER,
                 ddl = str(curYear)+'/'+str(curMonth)+'/'+str(curDay),
                 state = TASK_UNFINISHED,
                 startTime = str(curYear)+'/'+str(curMonth)+'/'+str(curDay)) -> None:
        self.id = None                  # int
        self.text = text                # str
        self.title = title              # str
        self.author = author            # str
        self.creatTime = creatTime      # str
        self.description = description  # str
        self.importance = importance    # int
        self.isDaily = isDaily          # boolean
        self.type = type                # str, one of ['Other', 'Study', 'Sport', 'Work']
        self.ddl = ddl                  # str: year/month/day, for example: 2022/8/7
        self.state = state              # str
        self.startTime = startTime

    def show_task(self):
        print("title : " + str(self.title))
        print("text : " + str(self.text))
        print("author : " + str(self.author))
        print("creatTime : " + str(self.creatTime))
        print("description : " + str(self.description))
        print("importance : " + str(self.importance))
        print("isDaily : " + str(self.isDaily))
        print("type : " + str(self.type))
        print("ddl : " + str(self.ddl))
        print("state : " + str(self.state))
        print("startTime : " + str(self.startTime))

    def matrix_time_display(self):
        timelist=self.ddl.split('/')
        return timelist[0]+'-'+timelist[1]+'-'+timelist[2]
    
    def matrix_time_compare(self):
        timelist=self.ddl.split('/')
        return int(timelist[0])*10000+int(timelist[1])*100+int(timelist[2])
