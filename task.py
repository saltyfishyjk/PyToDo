import sys
from PyQt6.Qt6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
class Task():
    def __init__(self,
                 text,
                 title,
                 author,
                 creatTime,
                 description,
                 importance,
                 isDaily,
                 type,
                 ddl,
                 state) -> None:
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

    
