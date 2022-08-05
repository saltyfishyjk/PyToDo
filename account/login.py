import sys
from PyQt6.Qt6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from account.database import connect_database, login_in_database, sign_up_database

from . signup import SignWindow

loginState=False
class Login(QMainWindow, QFrame):
	def __init__(self):
		super().__init__()
		self.icon = QIcon('./img/EMT.png')
		self.sign_up_win = SignWindow()  # 注册窗口
		# self.admin_win = AdminWindow()  # 用户管理窗口
		# self.main_win = Main()  # 登陆后的主页面
		# self.admin_win.set_main_window(self.main_win)
		self.set_ui()
		connect_database()

	def set_ui(self):
		self.setFixedSize(640, 400)  # 设置窗口大小
		self.setWindowTitle('PyToDo - Login in')  # 设置窗口标题
		self.setWindowIcon(self.icon)  # 设置窗口ico
		#self.set_background_image()
		self.add_label()
		self.add_line_edit()
		self.add_button()


	def set_background_image(self):
		"""添加背景图片"""
		self.frame = QFrame(self)  # 使用QFrame
		self.frame.resize(400, 240)
		#self.frame.move(40, 150)
		self.frame.setStyleSheet(
			'background-image: url("./img.jpg");'
			' background-repeat: no-repeat;'
			' text-align:center;')


	def add_label(self):
		"""添加相应标签"""

		# 设置字体
		label_font = QFont()
		label_font.setFamily('Consolas')
		label_font.setPixelSize(30)

		# 创建文本标签
		self.username_label = QLabel(self)
		self.password_label = QLabel(self)

		# 设置标签中的文本
		self.username_label.setText("username")
		self.password_label.setText("password")

		# 设置标签的大小
		self.username_label.setFixedSize(240, 40)
		self.password_label.setFixedSize(240, 40)

		# 设置标签的位置
		self.username_label.move(100, 240)
		self.password_label.move(100, 300)

		self.username_label.setFont(label_font)
		self.password_label.setFont(label_font)

	def add_line_edit(self):
		"""添加输入框"""
		line_edit_font = QFont()
		line_edit_font.setFamily('Consolas')
		line_edit_font.setPixelSize(30)

		# 创建
		self.username_edit = QLineEdit(self)
		self.password_edit = QLineEdit(self)

		# 设置密码格式（回显形式）
		self.password_edit.setEchoMode(QLineEdit.Password)

		# 设置字体
		self.username_edit.setFont(line_edit_font)
		self.password_edit.setFont(line_edit_font)

		# 设置占位符
		self.username_edit.setPlaceholderText("username")
		self.password_edit.setPlaceholderText("password")

		# 设置大小
		self.username_edit.setFixedSize(240, 40)
		self.password_edit.setFixedSize(240, 40)

		# 设置位置
		self.username_edit.move(100, 240)
		self.password_edit.move(100, 300)

	def add_button(self):
		"""添加按钮"""
		button_font = QFont()
		button_font.setFamily('Consolas')
		button_font.setPixelSize(30)

		# 创建按钮对象
		self.login_button = QPushButton("Login", self)
		self.sign_button = QPushButton(self)

		# 修改大小并且固定
		self.login_button.setFixedSize(160, 40)
		self.sign_button.setFixedSize(160, 40)

		# 设置字体
		self.login_button.setFont(button_font)
		self.sign_button.setFont(button_font)

		# 设置位置
		self.login_button.move(400, 240)
		self.sign_button.move(400, 300)

		# 设置文本提示内容
		self.login_button.setText("Login in")
		self.sign_button.setText("Sign up")

		# 实现功能，按钮点击之后执行的动作
		self.login_button.clicked.connect(self.login)
		self.sign_button.clicked.connect(self.sign_up_window)

		self.login_button.setShortcut("Return")

	def login(self):
		global loginState
		"""实现登录功能"""
		username = self.username_edit.text()
		password = self.password_edit.text()
		result,list,judge=login_in_database(username,password)
		if result:
			QMessageBox.information(self, 'Successfully',
									'Login in successfully \n Welcome {}'.format(username),
									QMessageBox.Yes | QMessageBox.No)
			self.username_edit.setText('')
			self.password_edit.setText('')
			self.close()
			loginState=True
		else:
			QMessageBox.information(self, 'Failed',
									judge,
									QMessageBox.Yes | QMessageBox.No)
			self.username_edit.setText('')
			self.password_edit.setText('')			

	def sign_up_window(self):
		self.sign_up_win.setWindowIcon(self.icon)
		self.sign_up_win.move(self.x() + 100, self.y() + 100)  # 移动以下注册窗口，避免和之前的重复
		#frame = QFrame(self.sign_up_win)
		self.sign_up_win.setWindowFlag(Qt.Dialog)
		#frame.resize(640, 400)
		#frame.setStyleSheet('background-image: url("./img/bg.png");'
		#					'backgrounf-repeat: no-repeat;')
		#frame.move(40, 150)
		# 打开注册窗口时，清除原来的信息
		self.password_edit.setText('')
		self.username_edit.setText('')
		self.sign_up_win.show()

	def closeEvent(self, event):
		self.sign_up_win.close()
		"""
		self.label = QLabel(self)
		self.label.setText('username')
		self.label.setFixedSize(240, 40)
		self.label.move(120, 530)
		"""

def loginWindow(app):
	window = Login()  
	window.show()
	app.exec()  # 获取系统信息，如命令行，并承担关闭窗口后完全退出的责任
	return loginState

