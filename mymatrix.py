import imp
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import task
default_Task = task.Task(
                title='None',
                text = '',
                author = 'anonymity',
                creatTime = '---- / -- / --',
                description = '',
                importance = 1,
                isDaily = False,
                type = 'Others',
                ddl = '0000 / 00 / 00',
                state = 'unfinished')


TASK_FINISHED = 'finished'
TASK_UNFINISHED = 'unfinished'
TASK_IMPORTANCE = 5

tasklist=[]
task00=[]
task01=[]
task10=[]
task11=[]
ui=None
def setupMatrix(Widgets, tasks):
    global tasklist
    global ui
    tasklist = tasks
    ui = Widgets
    matrix_button_connect()
    matrix_refresh()


def matrix_refresh():
    global task00
    global task01
    global task10
    global task11
    task00.clear()
    task01.clear()
    task10.clear()
    task11.clear()

    for i in range(0,4):
        task00.append(matrix_new_defaultTask())
        task10.append(matrix_new_defaultTask())
        task01.append(matrix_new_defaultTask())
        task11.append(matrix_new_defaultTask())
    
    matrix_distributeTask()
    for i in range(0,4):
        matrix_displayTask(task00, i)
        matrix_displayTask(task01, i)
        matrix_displayTask(task10, i)
        matrix_displayTask(task11, i)

def matrix_my_compare(a,b):
    return a.ddl>b.ddl

def matrix_distributeTask():
    import functools
    global tasklist
    tasklist.sort(key=functools.cmp_to_key(matrix_my_compare))
    cnt = 0
    tasknum = len(tasklist)
    for task in tasklist:
        if task.state==TASK_UNFINISHED:
            if task.importance < TASK_IMPORTANCE and cnt < tasknum / 2 + 1:
                task11.append(task)
            elif task.importance >= TASK_IMPORTANCE and cnt < tasknum / 2 + 1:
                task01.append(task)
            elif task.importance < TASK_IMPORTANCE and cnt >= tasknum / 2 + 1:
                task10.append(task)
            else:
                task00.append(task)

def matrix_displayTask(tasks, i):
    global ui
    ar=ui.matrix_dataArray
    for task in tasks:
        ar[i][0][0].setText(task.title)
        ar[i][0][1].setText(task.matrix_time_display())
        ar[i][0][2].setText(task.description)

        ar[i][1][0].setText(task.title)
        ar[i][1][1].setText(task.matrix_time_display())
        ar[i][1][2].setText(task.description)

        ar[i][2][0].setText(task.title)
        ar[i][2][1].setText(task.matrix_time_display())
        ar[i][2][2].setText(task.description)

        ar[i][3][0].setText(task.title)
        ar[i][3][1].setText(task.matrix_time_display())
        ar[i][3][2].setText(task.description)

def matrix_new_defaultTask():
    return task.Task(
                title='None',
                text = '',
                author = 'anonymity',
                creatTime = '---- / -- / --',
                description = '',
                importance = 1,
                isDaily = False,
                type = 'Others',
                ddl = '---- / -- / --',
                state = 'unfinished')



def openNewTaskDialog(self):
    import NewTask
    my = NewTask.NewTask()
    my.show()
    my.mySignal.connect(self.getDialogSignal)

def getDialogSignal(self, task):
    global tasklist
    tasklist.append(task)
    matrix_refresh()

def matrix_button_connect():
    global ui
    global task00
    global task01
    global task10
    global task11
    task00.clear()
    task01.clear()
    task10.clear()
    task11.clear()
    for i in range(0,4):
        task00.append(matrix_new_defaultTask())
        task10.append(matrix_new_defaultTask())
        task01.append(matrix_new_defaultTask())
        task11.append(matrix_new_defaultTask())
    ar=ui.matrix_dataArray
    ar[0][0][4].clicked.connect(matrix_finishTask0000())
    ar[0][1][4].clicked.connect(matrix_finishTask0001())
    ar[0][2][4].clicked.connect(matrix_finishTask0010())
    ar[0][3][4].clicked.connect(matrix_finishTask0011())
    ar[1][0][4].clicked.connect(matrix_finishTask0100())
    ar[1][1][4].clicked.connect(matrix_finishTask0101())
    ar[1][2][4].clicked.connect(matrix_finishTask0110())
    ar[1][3][4].clicked.connect(matrix_finishTask0111())
    ar[2][0][4].clicked.connect(matrix_finishTask1000())
    ar[2][1][4].clicked.connect(matrix_finishTask1001())
    ar[2][2][4].clicked.connect(matrix_finishTask1010())
    ar[2][3][4].clicked.connect(matrix_finishTask1011())
    ar[3][0][4].clicked.connect(matrix_finishTask1100())
    ar[3][1][4].clicked.connect(matrix_finishTask1101())
    ar[3][2][4].clicked.connect(matrix_finishTask1110())
    ar[3][3][4].clicked.connect(matrix_finishTask1111())
    for i in range(0,4):
        for j in range(0,4):
            ar[i][j][3].clicked.connect(openNewTaskDialog)


def matrix_finishTask0000():
    global task00
    task00[0].state= TASK_FINISHED

def matrix_finishTask0001():
    global task00
    task00[1].state= TASK_FINISHED

def matrix_finishTask0010():
    global task00
    task00[2].state= TASK_FINISHED

def matrix_finishTask0011():
    global task00
    task00[3].state= TASK_FINISHED

def matrix_finishTask0100():
    global task01
    task01[0].state= TASK_FINISHED

def matrix_finishTask0101():
    global task01
    task01[1].state= TASK_FINISHED

def matrix_finishTask0110():
    global task01
    task01[2].state= TASK_FINISHED

def matrix_finishTask0111():
    global task01
    task01[3].state= TASK_FINISHED

def matrix_finishTask1000():
    global task10
    task10[0].state= TASK_FINISHED

def matrix_finishTask1001():
    global task10
    task10[1].state= TASK_FINISHED

def matrix_finishTask1010():
    global task10
    task10[2].state= TASK_FINISHED

def matrix_finishTask1011():
    global task10
    task10[3].state= TASK_FINISHED

def matrix_finishTask1100():
    global task11
    task11[0].state= TASK_FINISHED

def matrix_finishTask1101():
    global task11
    task11[1].state= TASK_FINISHED

def matrix_finishTask1110():
    global task11
    task11[2].state= TASK_FINISHED

def matrix_finishTask1111():
    global task11
    task11[3].state= TASK_FINISHED