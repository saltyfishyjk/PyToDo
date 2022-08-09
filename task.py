from PyQt6.Qt6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import time
time_tuple = time.localtime(time.time())
curYear=time_tuple[0]
curMonth=time_tuple[1]
curDay=time_tuple[2]

class Task():
    def __init__(self,
                 title,
                 text = None,
                 author = 'anonymity',
                 creatTime = str(curYear)+'/'+str(curMonth)+'/'+str(curDay),
                 description = None,
                 importance = 1,
                 isDaily = False,
                 type = 'Others',
                 ddl = str(curYear)+'/'+str(curMonth)+'/'+str(curDay),
                 state = 'unfinished') -> None:
        self.id = None                  # int
        self.text = text                # str
        self.title = title              # str
        self.author = author            # str
        self.creatTime = creatTime      # str
        self.description = description  # str
        self.importance = importance    # int
        self.isDaily = isDaily          # boolean
        self.type = type                # str
        self.ddl = ddl                  # str: year/month/day, for example: 2022/8/7
        self.state = state              # str

    
