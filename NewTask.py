from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_newtask import *
import task as tk
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


# Signal Class using PyQt5
from PyQt5.Qt import QObject
class NewTaskCommuciate(QObject):
	from PyQt5.Qt import pyqtSignal
	mySignal = pyqtSignal([tk.Task], [str])

	def __init__(self):
		super().__init__()

	def run(self, task):
		self.mySignal[tk.Task].emit(task)
		#self.mySignal[str].emit("emmm")


class NewTask(QDialog, Ui_NewTask):
	def __init__(self):
		super(NewTask, self).__init__()
		self.setupUi(self)
		self.setWindowTitle('New task')
		# set modal : user can only operate main window when closed this dialog
		self.setWindowModality(Qt.ApplicationModal)
		self.communicate = NewTaskCommuciate()


	def submit(self):
		task = self.getInformation()
		self.communicate.run(task)
		self.close()

	def cancel(self):
		task = None
		# TODO: need to complete
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

		task = tk.Task(title=title,
					text=text,
					creatTime=getNetTime(),
					description=description,
					importance=importance,
					isDaily=frequency,
					type=type,
					ddl=ddl,
					state=state)

		return task

