# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newtask.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from task import *
import time
time_tuple = time.localtime(time.time())
curYear=time_tuple[0]
curMonth=time_tuple[1]
curDay=time_tuple[2]
curHour=time_tuple[3]

class Ui_NewTask(object):
    def setupUi(self, NewTask):
        NewTask.setObjectName("NewTask")
        NewTask.resize(766, 544)
        self.horizontalLayoutWidget = QWidget(NewTask)
        self.horizontalLayoutWidget.setGeometry(QRect(20, 460, 731, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submit_push_button = QPushButton(self.horizontalLayoutWidget)
        self.submit_push_button.setObjectName("submit_push_button")
        # submit func defined in NewTask.py
        self.submit_push_button.clicked.connect(self.submit)
        self.submit_push_button.setToolTip("Submit the new task")
        self.horizontalLayout.addWidget(self.submit_push_button)
        self.cancel_push_button = QPushButton(self.horizontalLayoutWidget)
        self.cancel_push_button.setObjectName("cancel_push_button")
        # cancel func defined in NewTask.py
        self.cancel_push_button.clicked.connect(self.cancel)
        self.cancel_push_button.setToolTip("Cancel submission")
        self.horizontalLayout.addWidget(self.cancel_push_button)
        self.delete_push_button = QPushButton(self.horizontalLayoutWidget)
        self.delete_push_button.setObjectName("delete_push_button")
        self.delete_push_button.clicked.connect(self.delete)
        self.delete_push_button.setToolTip("Delete task")
        self.horizontalLayout.addWidget(self.delete_push_button)
        self.verticalLayoutWidget = QWidget(NewTask)
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 731, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.title_label = QLabel(self.verticalLayoutWidget)
        self.title_label.setObjectName("title_label")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.title_label)
        self.title_edit = QLineEdit(self.verticalLayoutWidget)
        self.title_edit.setObjectName("title_edit")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.title_edit)
        self.description_label = QLabel(self.verticalLayoutWidget)
        self.description_label.setObjectName("description_label")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.description_label)
        self.description_edit = QLineEdit(self.verticalLayoutWidget)
        self.description_edit.setObjectName("description_edit")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.description_edit)
        self.text_label = QLabel(self.verticalLayoutWidget)
        self.text_label.setObjectName("text_label")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.text_label)
        self.text_edit = QTextEdit(self.verticalLayoutWidget)
        self.text_edit.setObjectName("text_edit")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.text_edit)
        self.importance_label = QLabel(self.verticalLayoutWidget)
        self.importance_label.setObjectName("importance_label")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.importance_label)
        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox)
        self.frequency_label = QLabel(self.verticalLayoutWidget)
        self.frequency_label.setObjectName("frequency_label")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.frequency_label)
        self.dailytask_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.dailytask_checkbox.setObjectName("dailytask_checkbox")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.dailytask_checkbox)
        self.type_label = QLabel(self.verticalLayoutWidget)
        self.type_label.setObjectName("type_label")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.type_label)
        self.type_combo_box = QComboBox(self.verticalLayoutWidget)
        self.type_combo_box.setObjectName("type_combo_box")
        self.type_combo_box.addItem("")
        self.type_combo_box.addItem("")
        self.type_combo_box.addItem("")
        self.type_combo_box.addItem("")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.type_combo_box)
        self.state_label = QLabel(self.verticalLayoutWidget)
        self.state_label.setObjectName("state_label")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.state_label)
        self.state_comboBox = QComboBox(self.verticalLayoutWidget)
        self.state_comboBox.setObjectName("state_comboBox")
        self.state_comboBox.addItem("")
        self.state_comboBox.addItem("")
        self.state_comboBox.addItem("")
        self.state_comboBox.addItem("")
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.state_comboBox)
        self.ddl_label = QLabel(self.verticalLayoutWidget)
        self.ddl_label.setObjectName("ddl_label")
        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.ddl_label)
        self.ddi_timeedit = QDateTimeEdit(self.verticalLayoutWidget)
        self.ddi_timeedit.setDateTime(QDateTime(QDate(curYear, curMonth, curDay), QTime(curHour, 0, 0)))
        self.ddi_timeedit.setObjectName("ddi_timeedit")
        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.ddi_timeedit)
        self.starttime_label = QLabel(self.verticalLayoutWidget)
        self.starttime_label.setObjectName("starttime_label")
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.starttime_label)
        self.start_timeedit = QDateTimeEdit(self.verticalLayoutWidget)
        self.start_timeedit.setDateTime(QDateTime(QDate(curYear, curMonth, curDay), QTime(curHour, 0, 0)))
        self.start_timeedit.setObjectName("start_timeedit")
        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.start_timeedit)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(NewTask)
        QMetaObject.connectSlotsByName(NewTask)

    def retranslateUi(self, NewTask):
        _translate = QCoreApplication.translate
        NewTask.setWindowTitle(_translate("NewTask", "Dialog"))
        self.submit_push_button.setText(_translate("NewTask", "Submit"))
        self.cancel_push_button.setText(_translate("NewTask", "Cancel"))
        self.delete_push_button.setText(_translate("NewTask", "Delete"))
        self.title_label.setText(_translate("NewTask", "Title"))
        self.title_edit.setText(_translate("NewTask", "New task"))
        self.description_label.setText(_translate("NewTask", "Description"))
        self.description_edit.setText(_translate("NewTask", "Describe the task in one line"))
        self.text_label.setText(_translate("NewTask", "Text"))
        self.text_edit.setHtml(_translate("NewTask", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Task text</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.importance_label.setText(_translate("NewTask", "Importance"))
        self.comboBox.setItemText(0, _translate("NewTask", "1(bigger the number,  more important the task)"))
        self.comboBox.setItemText(1, _translate("NewTask", "2(bigger the number,  more important the task)"))
        self.comboBox.setItemText(2, _translate("NewTask", "3(bigger the number,  more important the task)"))
        self.comboBox.setItemText(3, _translate("NewTask", "4(bigger the number,  more important the task)"))
        self.comboBox.setItemText(4, _translate("NewTask", "5(bigger the number,  more important the task)"))
        self.frequency_label.setText(_translate("NewTask", "Frequence"))
        self.dailytask_checkbox.setText(_translate("NewTask", "Daily task"))
        self.type_label.setText(_translate("NewTask", "Type"))
        self.type_combo_box.setItemText(0, _translate("NewTask", TASK_TYPE_OTHER))
        self.type_combo_box.setItemText(1, _translate("NewTask", TASK_TYPE_STUDY))
        self.type_combo_box.setItemText(2, _translate("NewTask", TASK_TYPE_SPORT))
        self.type_combo_box.setItemText(3, _translate("NewTask", TASK_TYPE_WORK))
        self.state_label.setText(_translate("NewTask", "State"))
        self.state_comboBox.setItemText(0, _translate("NewTask", TASK_NOTSTART))
        self.state_comboBox.setItemText(1, _translate("NewTask", TASK_UNDERWAY))
        self.state_comboBox.setItemText(2, _translate("NewTask", TASK_FINISHED))
        self.state_comboBox.setItemText(3, _translate("NewTask", TASK_OVERDUE))
        self.ddl_label.setText(_translate("NewTask", "DDL"))
        self.starttime_label.setText(_translate("NewTask", "Start Time"))
