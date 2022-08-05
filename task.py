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
                 description) -> None:
        self.id = None
        self.text = text
        self.title = title
        self.author = author
        self.creatTime = creatTime
        self.description = description
class TaskView():
    def __init__(self):
        pass
    
