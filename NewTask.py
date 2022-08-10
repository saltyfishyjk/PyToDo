from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_newtask import *
from task import Task
from gettime import *

# IN : QTimeDate
def qtime_to_timestr(qtime):
	year = qtime.date().year()
	month = qtime.date().month()
	day = qtime.date().day()
	hour = qtime.time().hour()
	min = qtime.time().minute()
	s = str(year) + '/' + str(month) + '/' + str(day) + '/' + str(hour) + '/' + str(min)
	return s

class NewTask(QDialog, Ui_NewTask):
	mySignal = pyqtSignal(Task)
	def __init__(self):
		super(NewTask, self).__init__()
		self.setupUi(self)
		self.setWindowTitle('New task')
		# set modal : user can only operate main window when closed this dialog
		self.setWindowModality(Qt.ApplicationModal)


	def submit(self):
		task = self.getInformation()
		self.mySignal.emit(task)
		self.close()

	def cancel(self):
		task = None
		self.mySignal.emit(task)
		self.close()

	# RET : task:obj
	def getInformation(self):
		title = self.title_edit.text()
		description = self.description_edit.text()
		text = self.text_edit.toPlainText()
		importance = self.comboBox.currentText()
		frequency = self.dailytask_checkbox.isChecked()
		type = self.type_combo_box.currentText()
		state = self.state_comboBox.currentText()
		start_time = qtime_to_timestr(self.start_timeedit.dateTime())
		ddl= qtime_to_timestr(self.ddi_timeedit.dateTime())

		task = Task(title=title,
					text=text,
					creatTime=getNetTime(),
					description=description,
					importance=importance,
					isDaily=frequency,
					type=type,
					ddl=ddl,
					state=state)

		return task

