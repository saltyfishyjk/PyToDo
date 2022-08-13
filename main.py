import sys
import os
import platform
import login
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from  modules import resources_rc

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
account = 'admin'
tasks = []
debug_tag = True


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		# SET AS GLOBAL WIDGETS
		# ///////////////////////////////////////////////////////////////
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		global widgets
		global account
		global tasks
		widgets = self.ui

		from home import home_ui_init
		home_ui_init(widgets)

		# set up calendar
		from ui_calendar import calendar_ui_init
		calendar_ui_init(widgets)

		# set up matrix
		from ui_matrix import matrix_ui_init
		matrix_ui_init(widgets)

		from ui_pic import pic_ui_init
		pic_ui_init(widgets)

		# USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
		# ///////////////////////////////////////////////////////////////
		Settings.ENABLE_CUSTOM_TITLE_BAR = True


		self.ui.Home_buttonGroup.buttonClicked.connect(self.ratioButtonClick)
		self.ui.Home_pushButton.clicked.connect(self.queryTodoWithTime)
		self.ui.Home_pushButton_2.clicked.connect(self.cancel)
		self.showTodo('All', None)
		# APP NAME
		# ///////////////////////////////////////////////////////////////

		# title = "Py TODO"
		description = "TODO"
		# # APPLY TEXTS
		# self.setWindowTitle(title)
		widgets.titleRightInfo.setText(description)

		# TOGGLE MENU
		# ///////////////////////////////////////////////////////////////
		widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

		# SET UI DEFINITIONS
		# ///////////////////////////////////////////////////////////////
		UIFunctions.uiDefinitions(self)

		# QTableWidget PARAMETERS
		# ///////////////////////////////////////////////////////////////
		widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

		# BUTTONS CLICK
		# ///////////////////////////////////////////////////////////////

		# LEFT MENUS
		widgets.btn_home.clicked.connect(self.buttonClick)
		widgets.btn_arrange.clicked.connect(self.buttonClick)
		widgets.btn_calendar.clicked.connect(self.buttonClick)
		widgets.btn_matrix.clicked.connect(self.buttonClick)
		widgets.btn_pic.clicked.connect(self.buttonClick)
		# widgets.btn_exit.clicked.connect(self.buttonClick)
		# setup function
		from mycalendar import setupCalendar
		setupCalendar(widgets, tasks)
		from mymatrix import setupMatrix
		setupMatrix(widgets, tasks)
		# setup function

		# EXTRA LEFT BOX
		def openCloseLeftBox():
			UIFunctions.toggleLeftBox(self, True)

		widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
		widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

		# EXTRA RIGHT BOX
		def openCloseRightBox():
			UIFunctions.toggleRightBox(self, True)

		widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

		# SHOW APP
		# ///////////////////////////////////////////////////////////////
		self.show()

		# SET CUSTOM THEME
		# ///////////////////////////////////////////////////////////////
		useCustomTheme = True
		themeFile = "themes\py_dracula_light.qss"

		# SET THEME AND HACKS
		if useCustomTheme:
			# LOAD AND APPLY STYLE
			UIFunctions.theme(self, themeFile, True)

			# SET HACKS
			AppFunctions.setThemeHack(self)

		# SET HOME PAGE AND SELECT MENU
		# ///////////////////////////////////////////////////////////////
		widgets.stackedWidget.setCurrentWidget(widgets.home)
		widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

	# BUTTONS CLICK
	# Post here your functions for clicked buttons
	# ///////////////////////////////////////////////////////////////
	def buttonClick(self):
		# GET BUTTON CLICKED
		btn = self.sender()
		btnName = btn.objectName()

		# SHOW HOME PAGE
		if btnName == "btn_home":
			widgets.stackedWidget.setCurrentWidget(widgets.home)

		# SHOW WIDGETS PAGE
		if btnName == "btn_arrange":
			widgets.stackedWidget.setCurrentWidget(widgets.arrange_page)
			self.arrange_showList()
			
		# SHOW CALENDAR PAGE
		if btnName == "btn_calendar":
			widgets.stackedWidget.setCurrentWidget(widgets.calendar_page)  # SET PAGE
			from mycalendar import refresh_calendar
			refresh_calendar()

		# SHOW MATRIX PAGE
		if btnName == "btn_matrix":
			widgets.stackedWidget.setCurrentWidget(widgets.matrix_page)  # SET PAGE
			from mymatrix import matrix_refresh
			matrix_refresh()

		if btnName == "btn_pic":
			widgets.stackedWidget.setCurrentWidget(widgets.pic_page)  # SET PAGE
			from ui_pic import pic_page_refresh
			pic_page_refresh(widgets)

		UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
		btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

		if debug_tag:
			# PRINT BTN NAME
			print(f'Button "{btnName}" pressed!')

	# RESIZE EVENTS
	# ///////////////////////////////////////////////////////////////
	def resizeEvent(self, event):
		# Update Size Grips
		UIFunctions.resize_grips(self)

	# MOUSE CLICK EVENTS
	# ///////////////////////////////////////////////////////////////
	def mousePressEvent(self, event):
		# SET DRAG POS WINDOW
		p = event.globalPosition()
		globalPos = p.toPoint()
		self.dragPos = globalPos()

		# PRINT MOUSE EVENTS
		if debug_tag:
			if event.buttons() == Qt.LeftButton:
				print('Mouse click: LEFT CLICK')
			if event.buttons() == Qt.RightButton:
				print('Mouse click: RIGHT CLICK')

	def finishBottomClick(self):
		button = self.sender()
		button = button.mapToGlobal(QPoint(0, 0)) - self.ui.Home_listWidget.mapToGlobal(QPoint(0, 0))
		# 获取到对象
		item = self.ui.Home_listWidget.indexAt(button)
		row = item.row()
		# 获取位置
		item = self.ui.Home_listWidget.item(row)
		widget = self.ui.Home_listWidget.itemWidget(item)
		Id = int(widget.objectName())
		taskMap[Id].state = 'finished'
		# print(row)
		# print(widget.objectName())
		self.ui.Home_listWidget.takeItem(row)

	# del item

	def modifyBottomClick(self):
		button = self.sender()
		butt = button.mapToGlobal(QPoint(0, 0)) - self.ui.Home_listWidget.mapToGlobal(QPoint(0, 0))
		item = self.ui.Home_listWidget.indexAt(butt)
		widget = self.ui.Home_listWidget.itemWidget(item)
		row = item.row()

	def showTodo(self, typeString=None, date=None):
		def struct(task):
			centralwidget = QWidget()
			# centralwidget.setObjectName(u"centralwidget")
			centralwidget.setMaximumSize(QSize(16777215, 90))
			centralwidget.setStyleSheet(u"background-color: rgb(238,239,243);\n"
										"border-radius:10px;")
			horizontalLayout_3 = QHBoxLayout()
			# horizontalLayout_3.setObjectName(u"horizontalLayout_3")
			horizontalLayout_2 = QHBoxLayout()
			# horizontalLayout_2.setObjectName(u"horizontalLayout_2")

			pushButton = QPushButton()
			# pushButton.setObjectName(u"pushButton")
			sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
			sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
			pushButton.setSizePolicy(sizePolicy)
			pushButton.setMinimumSize(QSize(20, 20))
			pushButton.setMaximumSize(QSize(20, 20))
			pushButton.setStyleSheet(u"QPushButton {\n"
									 "	border-style: none;\n"
									 "	border-image: url(:/icons/images/icons/c.png);\n"
									 "}\n"
									 "QPushButton:pressed {\n"
									 "	border-style: none;\n"
									 "	border-image: url(:/icons/images/icons/finish.png);\n"
									 "}")
			pushButton.setObjectName(task.title)
			pushButton.clicked.connect(self.finishBottomClick)
			horizontalLayout_2.addWidget(pushButton)
			horizontalSpacer = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)
			horizontalLayout_2.addItem(horizontalSpacer)

			verticalLayout = QVBoxLayout()
			# self.verticalLayout.setObjectName(u"verticalLayout")
			label = QLabel()
			# self.label.setObjectName(u"label")
			label.setText(task.title)
			verticalLayout.addWidget(label)

			horizontalLayout = QHBoxLayout()
			# horizontalLayout.setObjectName(u"horizontalLayout")
			label_2 = QLabel()
			# self.label_2.setObjectName(u"label_2")
			label_2.setText(task.ddl)
			horizontalLayout.addWidget(label_2)

			label_3 = QLabel()
			# label_3.setObjectName(u"label_3")
			label_3.setText(str(task.importance))
			horizontalLayout.addWidget(label_3)

			label_4 = QLabel()
			# self.label_4.setObjectName(u"label_4")
			label_4.setText(task.state)
			horizontalLayout.addWidget(label_4)

			verticalLayout.addLayout(horizontalLayout)

			horizontalLayout_2.addLayout(verticalLayout)

			obNa = task.title + "_2"
			pushButton_2 = QPushButton()
			pushButton_2.setObjectName(obNa)
			sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
			sizePolicy1.setHorizontalStretch(0)
			sizePolicy1.setVerticalStretch(0)
			sizePolicy1.setHeightForWidth(pushButton_2.sizePolicy().hasHeightForWidth())
			pushButton_2.setSizePolicy(sizePolicy1)
			pushButton_2.setMinimumSize(QSize(25, 25))
			pushButton_2.setMaximumSize(QSize(20, 20))
			pushButton_2.setStyleSheet(u"QPushButton {\n"
									   "	border-style: none;\n"
									   "	border-image: url(:/icons/images/icons/modify.png);\n"
									   "}\n"
									   "QPushButton:pressed {\n"
									   "	border-style: none;\n"
									   "	background-color: rgb(189, 147, 249);\n"
									   "	border-image: url(:/icons/images/icons/modify.png);\n"
									   "}")

			pushButton_2.clicked.connect(self.modifyBottomClick)
			horizontalLayout_2.addWidget(pushButton_2)

			horizontalLayout_3.addLayout(horizontalLayout_2)

			centralwidget.setLayout(horizontalLayout_3)
			return centralwidget

		self.ui.Home_listWidget.clear()
		if typeString is not None:
			for pTask in taskTemp:
				if pTask.state != 'finished':
					if typeString == 'All' or typeString == pTask.type:
						item = QListWidgetItem()
						item.setSizeHint(QSize(200, 50))
						widget = struct(pTask)
						widget.setObjectName(str(pTask.id))
						self.ui.Home_listWidget.addItem(item)
						self.ui.Home_listWidget.setItemWidget(item, widget)
		else:
			for pTask in taskTemp:
				if pTask.state != 'finished':
					if date == pTask.ddl:
						item = QListWidgetItem()
						item.setSizeHint(QSize(200, 50))
						widget = struct(pTask)
						widget.setObjectName(str(pTask.id))
						self.ui.Home_listWidget.addItem(item)
						self.ui.Home_listWidget.setItemWidget(item, widget)

	def ratioButtonClick(self):
		btn = self.ui.Home_buttonGroup.checkedButton()
		typeStr = btn.text()
		if typeStr == 'All':
			self.showTodo('All', None)
		elif typeStr == 'Sport':
			self.showTodo('Sport', None)
		elif typeStr == 'Study':
			self.showTodo('Study', None)
		elif typeStr == 'Work':
			self.showTodo('Work', None)
		elif typeStr == 'Other':
			self.showTodo('Other', None)

	def queryTodoWithTime(self):
		year = self.ui.Home_dateEdit.date().year()
		month = self.ui.Home_dateEdit.date().month()
		day = self.ui.Home_dateEdit.date().day()
		riqi = str(year) + '/' + str(month) + '/' + str(day)
		self.showTodo(None, riqi)

	def cancel(self):
		self.showTodo('All', None)

	def arrange_showList(self):
		def struct1(task):
			centralwidget = QWidget()
			# self.centralwidget.setObjectName(u"centralwidget")
			centralwidget.setStyleSheet(u"background-color: rgb(242,231,249);")
			horizontalLayout = QHBoxLayout(centralwidget)
			horizontalLayout.setSpacing(0)
			horizontalLayout.setObjectName(u"horizontalLayout")
			horizontalLayout.setContentsMargins(0, 0, 0, 0)
			frame = QFrame(centralwidget)
			frame.setObjectName(u"frame")
			frame.setStyleSheet(u"#frame{ \n"
								"		border:2px solid rgb(255, 121, 198);\n"
								"		border-radius: 15px;\n"
								"		background-color:rgb(242,231,249);\n"
								"}\n"
								"")
			frame.setFrameShape(QFrame.StyledPanel)
			frame.setFrameShadow(QFrame.Raised)
			verticalLayout = QVBoxLayout(frame)
			# self.verticalLayout.setObjectName(u"verticalLayout")
			label = QLabel(frame)
			# self.label.setObjectName(u"label")
			sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(1)
			sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
			label.setSizePolicy(sizePolicy)
			label.setStyleSheet(u"background-color:rgb(242,231,249);")
			label.setText(task.title)
			verticalLayout.addWidget(label)

			label_2 = QLabel(frame)
			# self.label_2.setObjectName(u"label_2")
			sizePolicy.setHeightForWidth(label_2.sizePolicy().hasHeightForWidth())
			label_2.setSizePolicy(sizePolicy)
			label_2.setStyleSheet(u"background-color:rgb(242,231,249);")
			label_2.setText(task.ddl)
			verticalLayout.addWidget(label_2)

			textBrowser = QTextBrowser(frame)
			textBrowser.setObjectName(u"textBrowser")
			sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
			sizePolicy1.setHorizontalStretch(0)
			sizePolicy1.setVerticalStretch(3)
			sizePolicy1.setHeightForWidth(textBrowser.sizePolicy().hasHeightForWidth())
			textBrowser.setSizePolicy(sizePolicy1)
			textBrowser.setStyleSheet(u"background-color:rgb(242,231,249);\n"
									  "border:none;")

			textBrowser.setText(task.description)
			verticalLayout.addWidget(textBrowser)

			horizontalLayout.addWidget(frame)
			return centralwidget

		def struct2(task):
			centralwidget = QWidget()
			# self.centralwidget.setObjectName(u"centralwidget")
			horizontalLayout = QHBoxLayout(centralwidget)
			# horizontalLayout.setObjectName(u"horizontalLayout")
			frame = QFrame(centralwidget)
			centralwidget.setStyleSheet(u"QWidget{ \n"
										"		border-radius: 15px;\n"
										"		background-color:rgb(122, 138, 202);\n"
										"       font: bold 18pt ; \n"
										"}\n"
										"")
			# self.frame.setObjectName(u"frame")
			sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
			sizePolicy1.setHorizontalStretch(5)
			sizePolicy1.setVerticalStretch(0)
			sizePolicy1.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
			frame.setSizePolicy(sizePolicy1)
			frame.setFrameShape(QFrame.StyledPanel)
			frame.setFrameShadow(QFrame.Raised)
			verticalLayout = QVBoxLayout(frame)
			verticalLayout.setSpacing(0)
			verticalLayout.setObjectName(u"verticalLayout")
			verticalLayout.setContentsMargins(0, 0, 0, 0)
			label_2 = QLabel(frame)
			# self.label_2.setObjectName(u"label_2")
			label_2.setText(task.title)

			verticalLayout.addWidget(label_2)

			horizontalLayout_2 = QHBoxLayout()
			# self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
			label_3 = QLabel(frame)
			# self.label_3.setObjectName(u"label_3")
			label_3.setText(task.ddl)

			horizontalLayout_2.addWidget(label_3)

			label_4 = QLabel(frame)
			# self.label_4.setObjectName(u"label_4")
			string = "重要性：%d" % task.importance
			label_4.setText(string)

			horizontalLayout_2.addWidget(label_4)

			verticalLayout.addLayout(horizontalLayout_2)

			horizontalLayout.addWidget(frame)

			label = QLabel(centralwidget)
			label.setText(task.state)

			# label.setObjectName(u"label")
			sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
			sizePolicy2.setHorizontalStretch(1)
			sizePolicy2.setVerticalStretch(0)
			sizePolicy2.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
			label.setSizePolicy(sizePolicy2)
			horizontalLayout.addWidget(label)

			return centralwidget

		self.ui.Arrange_listWidget.clear()

		for pTask in taskTemp:
			if pTask.state != 'finished':
				item = QListWidgetItem()
				item.setSizeHint(QSize(100, 100))
				widget = struct1(pTask)
				self.ui.Arrange_listWidget.addItem(item)
				self.ui.Arrange_listWidget.setItemWidget(item, widget)

		self.ui.Arrange_listWidget_2.clear()
		self.ui.Arrange_listWidget_3.clear()
		count = 0
		for pTask in taskTemp:
			if pTask.state != 'finished':
				if count == 0:
					item = QListWidgetItem()
					item.setSizeHint(QSize(120, 100))
					widget = struct2(pTask)
					self.ui.Arrange_listWidget_2.addItem(item)
					self.ui.Arrange_listWidget_2.setItemWidget(item, widget)
					count += 1
				elif count == 1:
					item = QListWidgetItem()
					item.setSizeHint(QSize(80, 100))
					widget = struct2(pTask)
					self.ui.Arrange_listWidget_3.addItem(item)
					self.ui.Arrange_listWidget_3.setItemWidget(item, widget)
					count += 1
				else:
					break

from task import Task
### 测试用样例
taskTemp = []
taskMap = {}
for i in range(1, 21):
	string = "第%d个TODO" % i
	if i < 6:
		newTask = Task(string, "random", "jsh", "2022/8/2", "no more", 10, False, "Study", "2022/8/2", "未完成")
	elif i < 11:
		newTask = Task(string, "random", "jsh", "2022/8/5", "no more", 10, False, "Sport", "2022/8/5", "未完成")
	elif i < 16:
		newTask = Task(string, "random", "jsh", "2022/8/2", "no more", 10, False, "Work", "2022/8/2", "未完成")
	elif i < 21:
		newTask = Task(string, "random", "jsh", "2022/8/10", "no more", 10, False, "Other", "2022/8/10", "未完成")

	newTask.id = i
	taskTemp.append(newTask)
	taskMap[i] = newTask


if __name__ == "__main__":
	app = QApplication(sys.argv)
	# cancel the login model to test other function conveniently
	loginState, loginuser, tasks=login.loginWindow(app)
	#loginState = True
	from mymatrix import send_user_to_matrix
	send_user_to_matrix(loginuser)
	from ui_pic import send_user_to_pics
	send_user_to_pics(loginuser)
	'''
	print(loginuser)
	for task in tasks:
		print(task.title,end=',')
		print(task.description,end=',')
		print(task.text,end=',')
		print(task.author,end=',')
	'''
	app.setWindowIcon(QIcon('inboxtodo.png'))
	window = MainWindow()
	if loginState:
		sys.exit(app.exec())
	else:
		sys.exit(1)