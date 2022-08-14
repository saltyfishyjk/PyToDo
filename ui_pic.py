import matplotlib.pyplot as plt
from PySide6.QtCore import Qt
from PyQt6.Qt6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from task import *

loginuser=None
labels_state=['Finished','Underway','NotStart','OverDue']
labels_type = [TASK_TYPE_STUDY, TASK_TYPE_SPORT, TASK_TYPE_WORK, TASK_TYPE_OTHER]

def pic_ui_init(ui):
    #ui.pic_page_Vlayout=QVBoxLayout(ui.pic_page)
    ui.pic_page_Hlayout_up=QHBoxLayout(ui.pic_page)
    #ui.pic_page_Hlayout_down=QHBoxLayout()
    #pix = QPixmap('img/pic_dataProcess.png')
    #pix = pix.scaled(1024, 576)
    ui.pic_page_lb00 = QLabel()
    ui.pic_page_lb00.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
    ui.pic_page_lb01 = QLabel()
    ui.pic_page_lb01.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
    #ui.pic_page_lb10 = QLabel()
    #ui.pic_page_lb11 = QLabel()
    #ui.pic_page_lb1.setScaledContents(True)
    #ui.pic_page_lb1.setStyleSheet("border: 1px solid black")
    #ui.pic_page_lb1.setPixmap(pix)
    #ui.pic_page_Vlayout.addLayout(ui.pic_page_Hlayout_up)
    #ui.pic_page_Vlayout.addLayout(ui.pic_page_Hlayout_down)
    #print('error')

def pic_page_refresh(ui):
    generatePics()
    pix = QPixmap('img/pic_dataProcess00.png')
    ui.pic_page_lb00.clear()
    ui.pic_page_lb00.setPixmap(pix)
    ui.pic_page_Hlayout_up.addWidget(ui.pic_page_lb00)
    pix = QPixmap('img/pic_dataProcess01.png')
    ui.pic_page_lb01.clear()
    ui.pic_page_lb01.setPixmap(pix)
    ui.pic_page_Hlayout_up.addWidget(ui.pic_page_lb01)
    '''
    pix = QPixmap('img/pic_dataProcess10.png')
    ui.pic_page_lb10.clear()
    ui.pic_page_lb10.setPixmap(pix)
    ui.pic_page_Hlayout_down.addWidget(ui.pic_page_lb10)
    pix = QPixmap('img/pic_dataProcess11.png')
    ui.pic_page_lb11.clear()
    ui.pic_page_lb11.setPixmap(pix)
    ui.pic_page_Hlayout_down.addWidget(ui.pic_page_lb11)
    '''

def send_user_to_pics(para_user):
    global loginuser
    loginuser=para_user

def generatePics():
    from database import get_task_list_database
    tasks=get_task_list_database(loginuser)
    statesType=getStates(tasks)
    my_dpi=96
    plt.figure(figsize=(7, 7),dpi=my_dpi)
    patches, texts, autotexts = plt.pie(
            x=statesType,                                    
            labels=labels_state,
            colors=plt.cm.get_cmap('Set3')(range(4)),
            autopct='%.2f%%',
            )
    plt.legend(patches, 
            labels_state,
            title="TODO states",
            loc="center",
            bbox_to_anchor=(0.9, 0, 0, 0),
            )
    plt.savefig('img/pic_dataProcess00.png', bbox_inches = 'tight')
    plt.clf()
    taskType=getTaskType(tasks)
    patches, texts, autotexts = plt.pie(
            x=taskType,                                    
            labels=labels_type,
            colors=plt.cm.get_cmap('Set2')(range(4)),
            autopct='%.2f%%',
            )
    plt.legend(patches, 
            labels_type,
            title="TODO Type",
            loc="center",
            bbox_to_anchor=(0.9, 0, 0, 0),
            )
    plt.savefig('img/pic_dataProcess01.png', bbox_inches = 'tight')

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

def getTaskType(tasks):
    taskType = [0,0,0,1]
    for task in tasks:
        #print(task.type)
        if task.type == TASK_TYPE_STUDY:
            taskType[0]+=1
        elif task.type == TASK_TYPE_SPORT:
            taskType[1]+=1
        elif task.type == TASK_TYPE_WORK:
            taskType[2]+=1
        elif task.type == TASK_TYPE_OTHER:
            taskType[3]+=1
    #print(taskType)
    return taskType
