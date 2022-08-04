import sys
from PyQt5.Qt import *
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QMessageBox, QPushButton, QWidget

from account.database import sign_up_database

class SignWindow(QWidget):
	def __init__(self):
		super(SignWindow, self).__init__()
		self.setWindowTitle("PyToDo - Sign up")  # 设置窗口标题
		self.resize(1000, 800)  # 设置窗口大小
		self.set_ui()  # 调用其他方法

	def set_ui(self):
		self.add_line_edit()
		self.add_button()
		self.add_label()

	def add_label(self):
		"""设计标签"""
		# 设置文本字体
		label_font = QFont()
		label_font.setFamily('Consolas')
		label_font.setPixelSize(35)

		# 创建三个对应的标签，父窗口为self
		self.username_label = QLabel(self)
		self.password_label = QLabel(self)
		self.confirm_label = QLabel(self)

		# 设置对应标签的文本
		self.username_label.setText("username")
		self.password_label.setText("password")
		self.confirm_label.setText("confirmed")

		# 控制label大小，set fixedsize后无法修改窗口大小
		self.username_label.setFixedSize(240, 40)
		self.password_label.setFixedSize(240, 40)
		self.confirm_label.setFixedSize(240, 40)

		# 设置对应的位置，move是移动到的意思
		self.username_label.move(120, 530)
		self.password_label.move(120, 600)
		self.confirm_label.move(120, 670)

		# 设置字体
		self.username_label.setFont(label_font)
		self.password_label.setFont(label_font)
		self.confirm_label.setFont(label_font)

	def add_line_edit(self):
		"""添加输入框"""
		line_edit_font = QFont()
		line_edit_font.setFamily('Consolas')
		line_edit_font.setPixelSize(30)

		# 创建三个输入框
		self.username_edit = QLineEdit(self)
		self.password_edit = QLineEdit(self)
		self.confirm_edit = QLineEdit(self)

		# 设置回显
		self.password_edit.setEchoMode(QLineEdit.Password)
		self.confirm_edit.setEchoMode(QLineEdit.Password)

		# 设置字体
		self.username_edit.setFont(line_edit_font)
		self.password_edit.setFont(line_edit_font)
		self.confirm_edit.setFont(line_edit_font)

		# 设置输入框的占位符
		self.username_edit.setPlaceholderText("username")
		self.password_edit.setPlaceholderText("password")
		self.confirm_edit.setPlaceholderText("confirm")

		# 控制大小
		self.username_edit.setFixedSize(350, 40)
		self.password_edit.setFixedSize(350, 40)
		self.confirm_edit.setFixedSize(350, 40)

		# 控制位置
		self.username_edit.move(320, 530)
		self.password_edit.move(320, 600)
		self.confirm_edit.move(320, 670)

	def add_button(self):
		"""添加按钮"""
		button_font = QFont()
		button_font.setFamily('Consolas')
		button_font.setPixelSize(30)

		self.sign_button = QPushButton(self)
		self.sign_button.setFixedSize(160, 50)
		self.sign_button.setFont(button_font)
		self.sign_button.move(750, 600)
		self.sign_button.setText("Sign up")

		self.sign_button.setShortcut("Return")

		self.sign_button.clicked.connect(self.sign_up)

	def sign_up(self):
		"""实现注册功能"""
		username = self.username_edit.text()
		password = self.password_edit.text()
		confirm = self.confirm_edit.text()

		if not username or not password or not confirm:
			QMessageBox.information(self, 'ERROR',
									'Please enter non-null username, password and confirmed password',
									QMessageBox.Yes)
		elif password != confirm:
			QMessageBox.information(self, 'ERROR',
									'Please enter the same password in confirmed password box',
									QMessageBox.Yes)
		else:
			sign_up_database(username, password)
			QMessageBox.information(self, 'Success',
									'Sign up successfully',
									QMessageBox.Yes)
			self.close()
	def closeEvent(self, event):
		"""关闭后清空输入框"""
		self.username_edit.setText('')
		self.password_edit.setText('')
		self.confirm_edit.setText('')

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = SignWindow()
	window.show()
	app.closeAllWindows()