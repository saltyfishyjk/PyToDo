from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


import database
from ui_newtask import *
import task as tk
from gettime import *
from database import *

default_Task = tk.Task(
	title='None',
	text='',
	author='anonymity',
	creatTime='---- / -- / --',
	description='',
	importance=1,
	isDaily=False,
	type='Others',
	ddl='0000/00/00',
	state='unfinished')

# IN : QTimeDate
def qtime_to_timestr(qtime):
	year = qtime.date().year()
	month = qtime.date().month()
	day = qtime.date().day()
	hour = qtime.time().hour()
	min = qtime.time().minute()
	s = str(year) + '/' + str(month) + '/' + str(day) + '/' + str(hour) + '/' + str(min)
	return s


class Tasks:
	def __init__(self):
		self.ls = []

	def add_task(self, task):
		self.ls.append(task)

	def get_ls(self):
		return self.ls


def tasklist2Tasks(task_list):
	tasks = Tasks()
	if len(task_list) != 0:
		for task in task_list:
			tasks.add_task(task)
	return tasks


# Signal Class using PyQt5
from PyQt5.Qt import QObject


class NewTaskCommuciate(QObject):
	from PyQt5.Qt import pyqtSignal
	# mySignal = pyqtSignal([tk.Task], [str], [Tasks])
	mySignal = pyqtSignal([Tasks])

	def __init__(self):
		super().__init__()

# IN : task:obj & hint:str & task_list:
	def run(self, task=None, hint="", task_list=None):
		# self.mySignal[tk.Task].emit(task)
		# self.mySignal[str].emit(hint)
		self.mySignal[Tasks].emit(task_list)


class NewTask(QDialog, Ui_NewTask):
	# IN : user:obj
	def __init__(self, user, task=None):
		super(NewTask, self).__init__()
		self.icon = QIcon('./images/images/inboxtodo.png')
		self.setWindowIcon(self.icon)
		# set background image
		self.pix = QPixmap('img/Slight Ocean View.png')

		self.lb1 = QLabel(self)
		self.lb1.setGeometry(0, 0, 766, 544)
		self.lb1.setStyleSheet("border: 1px solid black")
		self.lb1.setPixmap(self.pix)

		self.user = user
		self.setupUi(self)
		self.setWindowTitle('New task')
		self.intask = task
		if task is not None:
			self.showExistTask(task)
		# set modal : user can only operate main window when closed this dialog
		self.setWindowModality(Qt.ApplicationModal)
		self.communicate = NewTaskCommuciate()


	def submit(self):
		task = self.getInformation()
		# self.communicate.run(task, "Success")
		if self.intask is not None:
			database.modify_task_database(user=self.user, new_task=task)
		else:
			database.add_task_database(user=self.user, task=task)
		task_list = get_task_list_database(self.user)
		tasks = tasklist2Tasks(task_list)
		flag = True
		if flag:
			print("PASS TYPE : " + str(type(tasks)))
		self.communicate.run(task=task, hint="Success", task_list=tasks)
		self.close()

	def cancel(self):
		# self.communicate.run(default_Task, "Fail")
		# if not == non-None
		task_list = get_task_list_database(self.user)
		tasks = tasklist2Tasks(task_list)
		# if self.intask is not None:
		self.communicate.run(task=self.intask, hint="Success", task_list=tasks)
		self.close()

	def delete(self):
		print("Deleting")
		if self.intask is not None:
			database.delete_task_database(user=self.user, old_task=self.intask)
		task_list = get_task_list_database(self.user)
		tasks = tasklist2Tasks(task_list)
		self.communicate.run(task=default_Task, hint="Success", task_list=tasks)
		self.close()

	# RET : task:obj
	def getInformation(self):
		from pymysql.converters import escape_string
		title = escape_string(self.title_edit.text())
		description = escape_string(self.description_edit.text())
		text = escape_string(self.text_edit.toPlainText())
		importance = int(self.comboBox.currentText()[0])
		frequency = self.dailytask_checkbox.isChecked()
		type = escape_string(self.type_combo_box.currentText())
		state = escape_string(self.state_comboBox.currentText())
		start_time = qtime_to_timestr(self.start_timeedit.dateTime())
		ddl= qtime_to_timestr(self.ddi_timeedit.dateTime())
		# test
		print("start time : " + str(start_time))

		task = tk.Task(title=title,
					text=text,
					creatTime=getNetTime(),
					description=description,
					importance=importance,
					isDaily=frequency,
					type=type,
					ddl=ddl,
					state=state,
					startTime=start_time)

		return task

	type2index = {"Other":0, "Study":1, "Sport":2, "Work":3}
	state2index = {TASK_NOTSTART:0, TASK_UNDERWAY:1, TASK_FINISHED:2, TASK_OVERDUE:3}

	# IN  : timestr:str
	# RET : year, month, day, hour, minute : all str
	def analyseTimeStr(self, timestr):
		timelist = list(map(int, timestr.split('/')))
		year = timelist[0]
		month = timelist[1]
		day = timelist[2]
		hour = timelist[3]
		minute = timelist[4]
		return year, month, day, hour, minute

	def showExistTask(self, task):
		self.title_edit.setText(task.title)
		self.description_edit.setText(task.description)
		self.text_edit.setText(task.text)
		self.comboBox.setCurrentIndex(task.importance - 1)
		self.dailytask_checkbox.setChecked(task.isDaily)
		self.type_combo_box.setCurrentIndex(self.type2index[task.type])
		self.state_comboBox.setCurrentIndex(self.state2index[task.state])
		styear, stmonth, stday, sthour, stminute = self.analyseTimeStr(task.startTime)
		self.start_timeedit.setDateTime(QDateTime(QDate(styear, stmonth, stday), QTime(sthour, stminute, 0)))
		ddlyear, ddlmonth, ddlday, ddlhour, ddlminute = self.analyseTimeStr(task.ddl)
		self.ddi_timeedit.setDateTime(QDateTime(QDate(ddlyear, ddlmonth, ddlday), QTime(ddlhour, ddlminute, 0)))

