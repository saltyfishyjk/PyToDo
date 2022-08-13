import matplotlib.pyplot as plt
from PySide6.QtCore import Qt
from PyQt6.Qt6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from task import *

loginuser=None
labels_state=['Finished','Underway','NotStart','OverDue']

def pic_ui_init(ui):
    ui.pic_page_layout=QVBoxLayout(ui.pic_page)
    #pix = QPixmap('img/pic_states.png')
    #pix = pix.scaled(1024, 576)
    ui.pic_page_lb1 = QLabel()
    #ui.pic_page_lb1.setScaledContents(True)
    #ui.pic_page_lb1.setStyleSheet("border: 1px solid black")
    #ui.pic_page_lb1.setPixmap(pix)
    ui.pic_page_layout.addWidget(ui.pic_page_lb1)
    print('error')

def pic_page_refresh(ui):
    generatePics()
    pix = QPixmap('img/pic_states.png')
    ui.pic_page_lb1.clear()
    ui.pic_page_lb1.setPixmap(pix)
    ui.pic_page_layout.addWidget(ui.pic_page_lb1)

def send_user_to_pics(para_user):
    global loginuser
    loginuser=para_user

def generatePics():
    from database import get_task_list_database
    tasks=get_task_list_database(loginuser)
    statesType=getStates(tasks)
    my_dpi=96
    plt.figure(figsize=(480/my_dpi,480/my_dpi),dpi=my_dpi)
    patches, texts, autotexts = plt.pie(
            x=statesType,                                    
            labels=labels_state,
            colors=plt.cm.get_cmap('Set3')(range(4)),
            autopct='%.2f%%',
            )
    plt.legend(patches, 
            labels_state,
            title="TODO states",
            loc="center left",
            bbox_to_anchor=(1.2, 0, 0, 0),
            )
    plt.savefig('img/pic_states.png', bbox_inches = 'tight')

def getStates(tasks):
    statesType = [0,0,1,0]
    for task in tasks:
        if task.state == TASK_FINISHED:
            statesType[0]+=1
        elif task.state == TASK_UNDERWAY:
            statesType[1]+=1
        elif task.state == TASK_NOTSTART:
            statesType[2]+=1
        elif task.state == TASK_OVERDUE:
            statesType[3]+=1
    return statesType