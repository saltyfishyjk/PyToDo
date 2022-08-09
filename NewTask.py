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

# DEMO : how to use NewTask
if __name__ == "__main__":

	import sys
	app = QApplication(sys.argv)

	class Window(QWidget):

		def __init__(self):
			super(Window, self).__init__()
			self.initUI()

		def initUI(self):
			self.button = QPushButton('open', self)
			self.button.clicked.connect(self.openNewTaskDialog)
			self.button.move(10, 10)
			self.label = QLabel("hello", self)
			self.label.move(10, 50)
			self.setWindowTitle('Window')
			self.setGeometry(300, 300, 300, 200)
			self.show()

		def openNewTaskDialog(self):
			my = NewTask()
			my.show()
			# 在主窗口中连接信号和槽
			my.mySignal.connect(self.getDialogSignal)
			my.exec_()

		# task : 注册的task对象
		def getDialogSignal(self, task):
			task.show_task()

	mainwindow = Window()
	mainwindow.show()
	app.exec()