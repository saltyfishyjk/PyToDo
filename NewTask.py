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


# Signal Class using PyQt5
from PyQt5.Qt import QObject
class NewTaskCommuciate(QObject):
	from PyQt5.Qt import pyqtSignal
	mySignal = pyqtSignal([tk.Task], [str])

	def __init__(self):
		super().__init__()

# IN : task:obj & hint:str
	def run(self, task, hint):
		self.mySignal[tk.Task].emit(task)
		self.mySignal[str].emit(hint)


class NewTask(QDialog, Ui_NewTask):
	# IN : user:obj
	def __init__(self, user, task=None):
		super(NewTask, self).__init__()
		self.user = user
		self.setupUi(self)
		self.setWindowTitle('New task')
		if task:
			self.showExistTask(task)
		# set modal : user can only operate main window when closed this dialog
		self.setWindowModality(Qt.ApplicationModal)
		self.communicate = NewTaskCommuciate()

	def submit(self):
		task = self.getInformation()
		self.communicate.run(task, "Success")
		database.add_task_database(user=self.user, task=task)
		self.close()

	def cancel(self):
		# TODO: need to complete
		# self.communicate.run(default_Task, "Fail")
		self.close()

	# RET : task:obj
	def getInformation(self):
		title = self.title_edit.text()
		description = self.description_edit.text()
		text = self.text_edit.toPlainText()
		importance = int(self.comboBox.currentText()[0])
		frequency = self.dailytask_checkbox.isChecked()
		type = self.type_combo_box.currentText()
		state = self.state_comboBox.currentText()
		start_time = qtime_to_timestr(self.start_timeedit.dateTime())
		ddl= qtime_to_timestr(self.ddi_timeedit.dateTime())
		# TODO:strings including ' or \ .etc need to be translated

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

