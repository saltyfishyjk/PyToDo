from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from NewTask import Tasks
from database import modify_task_database
from task import *
import user

default_creatTime='----/--/--'
demo_creatTime='2022/01/15/18/00'
demo_ddl='2022/08/15/23/55'
demo_startTime= '2022/07/30/00/00'

default_Task = Task(
	title='None',
	text='',
	author='anonymity',
	creatTime=default_creatTime,
	description='',
	importance=1,
	isDaily=False,
	type='Others',
	ddl='0000/00/00',
	state=TASK_NOTSTART)

demotask = Task(
	title='demo title',
	text='demo text',
	author='demo author',
	creatTime=demo_creatTime,
	description='demo description',
	importance=3,
	isDaily=True,
	type='Sport',
	ddl=demo_ddl,
	state=TASK_UNDERWAY,
	startTime=demo_startTime
)

tasklist = []
task00 = []
task01 = []
task10 = []
task11 = []
curEditTask = None
ui = None
loginuser = user.User(
	id=11,
	account="test12",
	password="1234"
)


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

	for i in range(0, 4):
		task00.append(matrix_new_defaultTask())
		task10.append(matrix_new_defaultTask())
		task01.append(matrix_new_defaultTask())
		task11.append(matrix_new_defaultTask())

	matrix_distributeTask()
	for i in range(0, 4):
		matrix_displayTask(i)


def matrix_my_compare(a, b):
	return b.matrix_time_compare() - a.matrix_time_compare()


def matrix_distributeTask():
	import functools
	global tasklist
	if loginuser!=None:
		from database import get_task_list_database
		tasklist=get_task_list_database(loginuser)
	tasklist.sort(key=functools.cmp_to_key(matrix_my_compare))
	cnt = 0
	tasknum = len(tasklist)
	for task in tasklist:
		if task.state != TASK_FINISHED and task.state != TASK_OVERDUE:
			if task.importance < TASK_IMPORTANCE_LINE and cnt < tasknum / 2 + 1:
				task11.append(task)
				#print('in')
				task11.sort(key=functools.cmp_to_key(matrix_my_compare))
				#for task in task11:
				#	print(task.title, end=' ')
			elif task.importance >= TASK_IMPORTANCE_LINE and cnt < tasknum / 2 + 1:
				task01.append(task)
				task01.sort(key=functools.cmp_to_key(matrix_my_compare))
			elif task.importance < TASK_IMPORTANCE_LINE and cnt >= tasknum / 2 + 1:
				task10.append(task)
				task10.sort(key=functools.cmp_to_key(matrix_my_compare))
			else:
				task00.append(task)
				task00.sort(key=functools.cmp_to_key(matrix_my_compare))
		cnt += 1


def matrix_displayTask(i):
	global ui
	global task00
	global task01
	global task10
	global task11
	ar = ui.matrix_dataArray
	for j in range(0, 4):
		task = task00[i]
		# print(task.title)
		ar[0][i][0].setText(task.title)
		ar[0][i][1].setText(task.matrix_time_display())
		ar[0][i][2].setText(task.description)
		task = task01[i]
		# print(task.title)

		ar[1][i][0].setText(task.title)
		ar[1][i][1].setText(task.matrix_time_display())
		ar[1][i][2].setText(task.description)
		task = task10[i]
		# print(task.title)

		ar[2][i][0].setText(task.title)
		ar[2][i][1].setText(task.matrix_time_display())
		ar[2][i][2].setText(task.description)
		task = task11[i]
		# print(task.title)

		ar[3][i][0].setText(task.title)
		ar[3][i][1].setText(task.matrix_time_display())
		ar[3][i][2].setText(task.description)


def matrix_new_defaultTask():
	return Task(
		title='None',
		text='',
		author='anonymity',
		creatTime=default_creatTime,
		description='',
		importance=1,
		isDaily=False,
		type='Others',
		ddl='0000/00/00',
		state='unfinished')

def fill_tasks_in_database():
	global tasklist
	for task in tasklist:
		if not isDefaultBlankTask(task):
			modify_task_database(loginuser, task)

def isDefaultBlankTask(task):
	return default_creatTime==task.creatTime

def send_user_to_matrix(para_loginuser):
	global loginuser
	loginuser = para_loginuser


def openNewTaskDialog0000(self):
	import NewTask
	my = None
	print(task00[0].creatTime)
	if isDefaultBlankTask(task00[0]):

		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task00[0])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog0001(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task00[1]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task00[1])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog0010(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task00[2]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task00[2])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog0011(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task00[3]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task00[3])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog0100(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task01[0]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task01[0])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog0101(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task01[1]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task01[1])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog0110(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task01[2]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task01[2])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog0111(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task01[3]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task01[3])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog1000(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task10[0]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task10[0])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog1001(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task10[1]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task10[1])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog1010(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task10[2]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task10[2])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog1011(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task10[3]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task10[3])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog1100(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task11[0]):
		my = NewTask.NewTask(loginuser)
	else:
		print(loginuser.account)
		my = NewTask.NewTask(loginuser, task11[0])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog1101(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task11[1]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task11[1])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog1110(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task11[2]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task11[2])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()

def openNewTaskDialog1111(self):
	import NewTask
	my = None
	if isDefaultBlankTask(task11[3]):
		my = NewTask.NewTask(loginuser)
	else:
		my = NewTask.NewTask(loginuser, task11[3])
	my.show()
	my.communicate.mySignal[Tasks].connect(getDialogSignal)
	my.exec()
"""
# TEST
def teststr(s):
	print(s)
"""

def getDialogSignal(tasks):
	global tasklist
	#print(type(tasks))
	tasklist=tasks.get_ls()
	#print('\n###\nreturn error type '+str(type(tasklist))+'\n###\n')
	matrix_distributeTask()
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
	for i in range(0, 4):
		task00.append(matrix_new_defaultTask())
		task10.append(matrix_new_defaultTask())
		task01.append(matrix_new_defaultTask())
		task11.append(matrix_new_defaultTask())
	ar = ui.matrix_dataArray
	ar[0][0][4].clicked.connect(matrix_finishTask0000)
	ar[0][1][4].clicked.connect(matrix_finishTask0001)
	ar[0][2][4].clicked.connect(matrix_finishTask0010)
	ar[0][3][4].clicked.connect(matrix_finishTask0011)
	ar[1][0][4].clicked.connect(matrix_finishTask0100)
	ar[1][1][4].clicked.connect(matrix_finishTask0101)
	ar[1][2][4].clicked.connect(matrix_finishTask0110)
	ar[1][3][4].clicked.connect(matrix_finishTask0111)
	ar[2][0][4].clicked.connect(matrix_finishTask1000)
	ar[2][1][4].clicked.connect(matrix_finishTask1001)
	ar[2][2][4].clicked.connect(matrix_finishTask1010)
	ar[2][3][4].clicked.connect(matrix_finishTask1011)
	ar[3][0][4].clicked.connect(matrix_finishTask1100)
	ar[3][1][4].clicked.connect(matrix_finishTask1101)
	ar[3][2][4].clicked.connect(matrix_finishTask1110)
	ar[3][3][4].clicked.connect(matrix_finishTask1111)

	ar[0][0][3].clicked.connect(openNewTaskDialog0000)
	ar[0][1][3].clicked.connect(openNewTaskDialog0001)
	ar[0][2][3].clicked.connect(openNewTaskDialog0010)
	ar[0][3][3].clicked.connect(openNewTaskDialog0011)
	ar[1][0][3].clicked.connect(openNewTaskDialog0100)
	ar[1][1][3].clicked.connect(openNewTaskDialog0101)
	ar[1][2][3].clicked.connect(openNewTaskDialog0110)
	ar[1][3][3].clicked.connect(openNewTaskDialog0111)
	ar[2][0][3].clicked.connect(openNewTaskDialog1000)
	ar[2][1][3].clicked.connect(openNewTaskDialog1001)
	ar[2][2][3].clicked.connect(openNewTaskDialog1010)
	ar[2][3][3].clicked.connect(openNewTaskDialog1011)
	ar[3][0][3].clicked.connect(openNewTaskDialog1100)
	ar[3][1][3].clicked.connect(openNewTaskDialog1101)
	ar[3][2][3].clicked.connect(openNewTaskDialog1110)
	ar[3][3][3].clicked.connect(openNewTaskDialog1111)



def matrix_finishTask0000():
	global task00
	task00[0].state = TASK_FINISHED
	if not isDefaultBlankTask(task00[0]):
		modify_task_database(loginuser, task00[0])
	matrix_refresh()


def matrix_finishTask0001():
	global task00
	task00[1].state = TASK_FINISHED
	if not isDefaultBlankTask(task00[1]):
		modify_task_database(loginuser, task00[1])
	matrix_refresh()


def matrix_finishTask0010():
	global task00
	task00[2].state = TASK_FINISHED
	if not isDefaultBlankTask(task00[2]):
		modify_task_database(loginuser, task00[2])
	matrix_refresh()


def matrix_finishTask0011():
	global task00
	task00[3].state = TASK_FINISHED
	if not isDefaultBlankTask(task00[3]):
		modify_task_database(loginuser, task00[3])
	matrix_refresh()


def matrix_finishTask0100():
	global task01
	task01[0].state = TASK_FINISHED
	if not isDefaultBlankTask(task01[0]):
		modify_task_database(loginuser, task01[0])
	matrix_refresh()


def matrix_finishTask0101():
	global task01
	task01[1].state = TASK_FINISHED
	if not isDefaultBlankTask(task01[1]):
		modify_task_database(loginuser, task01[1])
	matrix_refresh()


def matrix_finishTask0110():
	global task01
	task01[2].state = TASK_FINISHED
	if not isDefaultBlankTask(task01[2]):
		modify_task_database(loginuser, task01[2])
	matrix_refresh()


def matrix_finishTask0111():
	global task01
	task01[3].state = TASK_FINISHED
	if not isDefaultBlankTask(task01[3]):
		modify_task_database(loginuser, task01[3])
	matrix_refresh()


def matrix_finishTask1000():
	global task10
	task10[0].state = TASK_FINISHED
	if not isDefaultBlankTask(task10[0]):
		modify_task_database(loginuser, task10[0])
	matrix_refresh()


def matrix_finishTask1001():
	global task10
	task10[1].state = TASK_FINISHED
	if not isDefaultBlankTask(task10[1]):
		modify_task_database(loginuser, task10[1])
	matrix_refresh()


def matrix_finishTask1010():
	global task10
	task10[2].state = TASK_FINISHED
	if not isDefaultBlankTask(task10[2]):
		modify_task_database(loginuser, task10[2])
	matrix_refresh()


def matrix_finishTask1011():
	global task10
	task10[3].state = TASK_FINISHED
	if not isDefaultBlankTask(task10[3]):
		modify_task_database(loginuser, task10[3])
	matrix_refresh()


def matrix_finishTask1100():
	global task11
	task11[0].state = TASK_FINISHED
	if not isDefaultBlankTask(task11[0]):
		modify_task_database(loginuser, task11[0])
	matrix_refresh()


def matrix_finishTask1101():
	global task11
	task11[1].state = TASK_FINISHED
	if not isDefaultBlankTask(task11[1]):
		modify_task_database(loginuser, task11[1])
	matrix_refresh()


def matrix_finishTask1110():
	global task11
	task11[2].state = TASK_FINISHED
	if not isDefaultBlankTask(task11[2]):
		modify_task_database(loginuser, task11[2])
	matrix_refresh()


def matrix_finishTask1111():
	global task11
	task11[3].state = TASK_FINISHED
	if not isDefaultBlankTask(task11[3]):
		modify_task_database(loginuser, task11[3])
	matrix_refresh()