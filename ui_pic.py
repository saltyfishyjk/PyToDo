from PySide6.QtCore import Qt
from PyQt6.Qt6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

def pic_ui_init(ui):
    ui.pic_page_layout=QVBoxLayout(ui.pic_page)
    pix = QPixmap('img/fox.png')
    #pix = pix.scaled(1024, 576)
    lb1 = QLabel()
    lb1.setScaledContents(True)
    lb1.setStyleSheet("border: 2px solid red")
    lb1.setPixmap(pix)
    ui.pic_page_layout.addWidget(lb1)