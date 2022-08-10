from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import task


# default settings

default_Task = task.Task(
                title='None',
                text = '',
                author = 'anonymity',
                creatTime = '---- / -- / --',
                description = '',
                importance = 1,
                isDaily = False,
                type = 'Others',
                ddl = '---- / -- / --',
                state = 'unfinished')

# cell style
default_title_style = "font-size: 20px;color: black;background-color: #f8f8f2;border-radius: 15px;"
default_title_alignment = Qt.AlignCenter
default_title_frameShape = QFrame.Box

default_time_style = "font-size: 20px;color: black;background-color: #f8f8f2;border-radius: 15px;"
default_time_alignment = Qt.AlignCenter
default_time_frameShape = QFrame.Box

default_discription_style = "font-size: 20px;color: black;background-color: #f8f8f2;border-radius: 15px;"
default_discription_alignment = Qt.AlignCenter
default_discription_frameShape = QFrame.Box

default_edit_button_style = "font-size: 20px;color: black;background-color: #f8f8f2;border-radius: 15px;"
default_edit_button_horizon_style = QSizePolicy.Policy.Preferred
default_edit_button_vertical_style = QSizePolicy.Policy.Fixed

default_del_button_style = "font-size: 20px;color: black;background-color: #f8f8f2;border-radius: 15px;"
default_del_button_horizon_style = QSizePolicy.Policy.Preferred
default_del_button_vertical_style = QSizePolicy.Policy.Fixed

default_vline_text1 = "I\nm\np\no\nr\nt\na\nn\nt"
default_vline_text2 = "U\nn\ni\nm\np\no\nr\nt\na\nn\nt"
default_vline_style = "font-size: 15px;color: white;background-color: #6272a4;border-radius: 5px;"
default_vline_alignment = Qt.AlignCenter
default_vline_frameShape = QFrame.Box

default_hline_text1 = "Not Urgent"
default_hline_text2 = "Urgent"
default_hline_style = "font-size: 15px;color: white;background-color: #6272a4;border-radius: 5px;"
default_hline_alignment = Qt.AlignCenter
default_hline_frameShape = QFrame.Box

def matrix_ui_init(ui):
    ui.matrix_Vlayout=QVBoxLayout(ui.matrix_page)
    ui.matrix_Vlayout.setObjectName(u"matrix_Vlayout")
    

    ui.matrix_UPlayout=QHBoxLayout()
    ui.matrix_UPlayout.setObjectName(u"matrix_UPlayout")

    ui.matrix_UPlayout_left=QHBoxLayout()
    ui.matrix_UPlayout_left.setObjectName(u"matrix_UPlayout_left")
    ui.matrix_UPlayout_leftl=QVBoxLayout()
    ui.matrix_UPlayout_leftl.setObjectName(u"matrix_UPlayout_leftl")
    ui.matrix_UPlayout_leftr=QVBoxLayout()
    ui.matrix_UPlayout_leftr.setObjectName(u"matrix_UPlayout_leftr")


    ui.matrix_UPlayout_left_11=QVBoxLayout()
    ui.matrix_UPlayout_left_11.setObjectName(u"matrix_UPlayout_left_11")
    ui.matrix_UPlayout_left_11_up=QHBoxLayout()
    ui.matrix_UPlayout_left_11_up.setObjectName(u"matrix_UPlayout_left_11_up")
    
    # set cell title
    ui.matrix_UPlayout_left_11_title=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_11_title.setObjectName(u"matrix_UPlayout_left_11_title")
    ui.matrix_UPlayout_left_11_title.setText(default_Task.title)
    ui.matrix_UPlayout_left_11_title.setStyleSheet(default_title_style)
    ui.matrix_UPlayout_left_11_title.setAlignment(default_title_alignment)
    ui.matrix_UPlayout_left_11_title.setReadOnly(True)

    # set cell time
    ui.matrix_UPlayout_left_11_time=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_11_time.setObjectName(u"matrix_UPlayout_left_11_time")
    ui.matrix_UPlayout_left_11_time.setText(default_Task.ddl)
    ui.matrix_UPlayout_left_11_time.setStyleSheet(default_time_style)
    ui.matrix_UPlayout_left_11_time.setAlignment(default_time_alignment)
    ui.matrix_UPlayout_left_11_time.setReadOnly(True)

    ui.matrix_UPlayout_left_11_up.addWidget(ui.matrix_UPlayout_left_11_title)
    ui.matrix_UPlayout_left_11_up.addWidget(ui.matrix_UPlayout_left_11_time)

    ui.matrix_UPlayout_left_11_down=QHBoxLayout()
    ui.matrix_UPlayout_left_11_down.setObjectName(u"matrix_UPlayout_left_11_down")
    
    # set cell discription(ddl)
    ui.matrix_UPlayout_left_11_discription=QTextEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_11_discription.setObjectName(u"matrix_UPlayout_left_11_discription")
    ui.matrix_UPlayout_left_11_discription.setText(default_Task.description)
    ui.matrix_UPlayout_left_11_discription.setStyleSheet(default_discription_style)
    ui.matrix_UPlayout_left_11_discription.setAlignment(default_discription_alignment)
    ui.matrix_UPlayout_left_11_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_UPlayout_left_11_discription.setReadOnly(True)


    ui.matrix_UPlayout_left_11_down_format=QVBoxLayout()
    ui.matrix_UPlayout_left_11_down_format.setObjectName(u"matrix_UPlayout_left_11_down_format")

    # set cell edit button
    ui.matrix_UPlayout_left_11_down_edit_button=QPushButton("matrix_UPlayout_left_11_down_edit_button")
    ui.matrix_UPlayout_left_11_down_edit_button.setText(' Edit ')
    ui.matrix_UPlayout_left_11_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_UPlayout_left_11_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_UPlayout_left_11_down_format.addWidget(ui.matrix_UPlayout_left_11_down_edit_button)

    # set cell delete button
    ui.matrix_UPlayout_left_11_down_del_button=QPushButton("matrix_UPlayout_left_11_down_del_button")
    ui.matrix_UPlayout_left_11_down_del_button.setText(' Finish ')
    ui.matrix_UPlayout_left_11_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_UPlayout_left_11_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_UPlayout_left_11_down_format.addWidget(ui.matrix_UPlayout_left_11_down_del_button)

    ui.matrix_UPlayout_left_11_down.addWidget(ui.matrix_UPlayout_left_11_discription)
    ui.matrix_UPlayout_left_11_down.addLayout(ui.matrix_UPlayout_left_11_down_format)

    ui.matrix_UPlayout_left_11.addLayout(ui.matrix_UPlayout_left_11_up)
    ui.matrix_UPlayout_left_11.addLayout(ui.matrix_UPlayout_left_11_down)

    ui.matrix_UPlayout_left_21=QVBoxLayout()
    ui.matrix_UPlayout_left_21.setObjectName(u"matrix_UPlayout_left_21")
    ui.matrix_UPlayout_left_21_up=QHBoxLayout()
    ui.matrix_UPlayout_left_21_up.setObjectName(u"matrix_UPlayout_left_21_up")
    
    # set cell title
    ui.matrix_UPlayout_left_21_title=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_21_title.setObjectName(u"matrix_UPlayout_left_21_title")
    ui.matrix_UPlayout_left_21_title.setText(default_Task.title)
    ui.matrix_UPlayout_left_21_title.setStyleSheet(default_title_style)
    ui.matrix_UPlayout_left_21_title.setAlignment(default_title_alignment)
    ui.matrix_UPlayout_left_21_title.setReadOnly(True)

    # set cell time
    ui.matrix_UPlayout_left_21_time=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_21_time.setObjectName(u"matrix_UPlayout_left_21_time")
    ui.matrix_UPlayout_left_21_time.setText(default_Task.ddl)
    ui.matrix_UPlayout_left_21_time.setStyleSheet(default_time_style)
    ui.matrix_UPlayout_left_21_time.setAlignment(default_time_alignment)
    ui.matrix_UPlayout_left_21_time.setReadOnly(True)

    ui.matrix_UPlayout_left_21_up.addWidget(ui.matrix_UPlayout_left_21_title)
    ui.matrix_UPlayout_left_21_up.addWidget(ui.matrix_UPlayout_left_21_time)

    ui.matrix_UPlayout_left_21_down=QHBoxLayout()
    ui.matrix_UPlayout_left_21_down.setObjectName(u"matrix_UPlayout_left_21_down")
    
    # set cell discription(ddl)
    ui.matrix_UPlayout_left_21_discription=QTextEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_21_discription.setObjectName(u"matrix_UPlayout_left_21_discription")
    ui.matrix_UPlayout_left_21_discription.setText(default_Task.description)
    ui.matrix_UPlayout_left_21_discription.setStyleSheet(default_discription_style)
    ui.matrix_UPlayout_left_21_discription.setAlignment(default_discription_alignment)
    ui.matrix_UPlayout_left_21_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_UPlayout_left_21_discription.setReadOnly(True)


    ui.matrix_UPlayout_left_21_down_format=QVBoxLayout()
    ui.matrix_UPlayout_left_21_down_format.setObjectName(u"matrix_UPlayout_left_21_down_format")

    # set cell edit button
    ui.matrix_UPlayout_left_21_down_edit_button=QPushButton("matrix_UPlayout_left_21_down_edit_button")
    ui.matrix_UPlayout_left_21_down_edit_button.setText(' Edit ')
    ui.matrix_UPlayout_left_21_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_UPlayout_left_21_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_UPlayout_left_21_down_format.addWidget(ui.matrix_UPlayout_left_21_down_edit_button)

    # set cell delete button
    ui.matrix_UPlayout_left_21_down_del_button=QPushButton("matrix_UPlayout_left_21_down_del_button")
    ui.matrix_UPlayout_left_21_down_del_button.setText(' Finish ')
    ui.matrix_UPlayout_left_21_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_UPlayout_left_21_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_UPlayout_left_21_down_format.addWidget(ui.matrix_UPlayout_left_21_down_del_button)

    ui.matrix_UPlayout_left_21_down.addWidget(ui.matrix_UPlayout_left_21_discription)
    ui.matrix_UPlayout_left_21_down.addLayout(ui.matrix_UPlayout_left_21_down_format)

    ui.matrix_UPlayout_left_21.addLayout(ui.matrix_UPlayout_left_21_up)
    ui.matrix_UPlayout_left_21.addLayout(ui.matrix_UPlayout_left_21_down)

    ui.matrix_UPlayout_left_12=QVBoxLayout()
    ui.matrix_UPlayout_left_12.setObjectName(u"matrix_UPlayout_left_12")
    ui.matrix_UPlayout_left_12_up=QHBoxLayout()
    ui.matrix_UPlayout_left_12_up.setObjectName(u"matrix_UPlayout_left_12_up")
    
    # set cell title
    ui.matrix_UPlayout_left_12_title=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_12_title.setObjectName(u"matrix_UPlayout_left_12_title")
    ui.matrix_UPlayout_left_12_title.setText(default_Task.title)
    ui.matrix_UPlayout_left_12_title.setStyleSheet(default_title_style)
    ui.matrix_UPlayout_left_12_title.setAlignment(default_title_alignment)
    ui.matrix_UPlayout_left_12_title.setReadOnly(True)

    # set cell time
    ui.matrix_UPlayout_left_12_time=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_12_time.setObjectName(u"matrix_UPlayout_left_12_time")
    ui.matrix_UPlayout_left_12_time.setText(default_Task.ddl)
    ui.matrix_UPlayout_left_12_time.setStyleSheet(default_time_style)
    ui.matrix_UPlayout_left_12_time.setAlignment(default_time_alignment)
    ui.matrix_UPlayout_left_12_time.setReadOnly(True)

    ui.matrix_UPlayout_left_12_up.addWidget(ui.matrix_UPlayout_left_12_title)
    ui.matrix_UPlayout_left_12_up.addWidget(ui.matrix_UPlayout_left_12_time)

    ui.matrix_UPlayout_left_12_down=QHBoxLayout()
    ui.matrix_UPlayout_left_12_down.setObjectName(u"matrix_UPlayout_left_12_down")
    
    # set cell discription(ddl)
    ui.matrix_UPlayout_left_12_discription=QTextEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_12_discription.setObjectName(u"matrix_UPlayout_left_12_discription")
    ui.matrix_UPlayout_left_12_discription.setText(default_Task.description)
    ui.matrix_UPlayout_left_12_discription.setStyleSheet(default_discription_style)
    ui.matrix_UPlayout_left_12_discription.setAlignment(default_discription_alignment)
    ui.matrix_UPlayout_left_12_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_UPlayout_left_12_discription.setReadOnly(True)


    ui.matrix_UPlayout_left_12_down_format=QVBoxLayout()
    ui.matrix_UPlayout_left_12_down_format.setObjectName(u"matrix_UPlayout_left_12_down_format")

    # set cell edit button
    ui.matrix_UPlayout_left_12_down_edit_button=QPushButton("matrix_UPlayout_left_12_down_edit_button")
    ui.matrix_UPlayout_left_12_down_edit_button.setText(' Edit ')
    ui.matrix_UPlayout_left_12_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_UPlayout_left_12_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_UPlayout_left_12_down_format.addWidget(ui.matrix_UPlayout_left_12_down_edit_button)

    # set cell delete button
    ui.matrix_UPlayout_left_12_down_del_button=QPushButton("matrix_UPlayout_left_12_down_del_button")
    ui.matrix_UPlayout_left_12_down_del_button.setText(' Finish ')
    ui.matrix_UPlayout_left_12_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_UPlayout_left_12_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_UPlayout_left_12_down_format.addWidget(ui.matrix_UPlayout_left_12_down_del_button)

    ui.matrix_UPlayout_left_12_down.addWidget(ui.matrix_UPlayout_left_12_discription)
    ui.matrix_UPlayout_left_12_down.addLayout(ui.matrix_UPlayout_left_12_down_format)

    ui.matrix_UPlayout_left_12.addLayout(ui.matrix_UPlayout_left_12_up)
    ui.matrix_UPlayout_left_12.addLayout(ui.matrix_UPlayout_left_12_down)

    ui.matrix_UPlayout_left_22=QVBoxLayout()
    ui.matrix_UPlayout_left_22.setObjectName(u"matrix_UPlayout_left_22")
    ui.matrix_UPlayout_left_22_up=QHBoxLayout()
    ui.matrix_UPlayout_left_22_up.setObjectName(u"matrix_UPlayout_left_22_up")
    
    # set cell title
    ui.matrix_UPlayout_left_22_title=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_22_title.setObjectName(u"matrix_UPlayout_left_22_title")
    ui.matrix_UPlayout_left_22_title.setText(default_Task.title)
    ui.matrix_UPlayout_left_22_title.setStyleSheet(default_title_style)
    ui.matrix_UPlayout_left_22_title.setAlignment(default_title_alignment)
    ui.matrix_UPlayout_left_22_title.setReadOnly(True)

    # set cell time
    ui.matrix_UPlayout_left_22_time=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_22_time.setObjectName(u"matrix_UPlayout_left_22_time")
    ui.matrix_UPlayout_left_22_time.setText(default_Task.ddl)
    ui.matrix_UPlayout_left_22_time.setStyleSheet(default_time_style)
    ui.matrix_UPlayout_left_22_time.setAlignment(default_time_alignment)
    ui.matrix_UPlayout_left_22_time.setReadOnly(True)

    ui.matrix_UPlayout_left_22_up.addWidget(ui.matrix_UPlayout_left_22_title)
    ui.matrix_UPlayout_left_22_up.addWidget(ui.matrix_UPlayout_left_22_time)

    ui.matrix_UPlayout_left_22_down=QHBoxLayout()
    ui.matrix_UPlayout_left_22_down.setObjectName(u"matrix_UPlayout_left_22_down")
    
    # set cell discription(ddl)
    ui.matrix_UPlayout_left_22_discription=QTextEdit(ui.matrix_page)
    ui.matrix_UPlayout_left_22_discription.setObjectName(u"matrix_UPlayout_left_22_discription")
    ui.matrix_UPlayout_left_22_discription.setText(default_Task.description)
    ui.matrix_UPlayout_left_22_discription.setStyleSheet(default_discription_style)
    ui.matrix_UPlayout_left_22_discription.setAlignment(default_discription_alignment)
    ui.matrix_UPlayout_left_22_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_UPlayout_left_22_discription.setReadOnly(True)


    ui.matrix_UPlayout_left_22_down_format=QVBoxLayout()
    ui.matrix_UPlayout_left_22_down_format.setObjectName(u"matrix_UPlayout_left_22_down_format")

    # set cell edit button
    ui.matrix_UPlayout_left_22_down_edit_button=QPushButton("matrix_UPlayout_left_22_down_edit_button")
    ui.matrix_UPlayout_left_22_down_edit_button.setText(' Edit ')
    ui.matrix_UPlayout_left_22_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_UPlayout_left_22_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_UPlayout_left_22_down_format.addWidget(ui.matrix_UPlayout_left_22_down_edit_button)

    # set cell delete button
    ui.matrix_UPlayout_left_22_down_del_button=QPushButton("matrix_UPlayout_left_22_down_del_button")
    ui.matrix_UPlayout_left_22_down_del_button.setText(' Finish ')
    ui.matrix_UPlayout_left_22_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_UPlayout_left_22_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_UPlayout_left_22_down_format.addWidget(ui.matrix_UPlayout_left_22_down_del_button)

    ui.matrix_UPlayout_left_22_down.addWidget(ui.matrix_UPlayout_left_22_discription)
    ui.matrix_UPlayout_left_22_down.addLayout(ui.matrix_UPlayout_left_22_down_format)

    ui.matrix_UPlayout_left_22.addLayout(ui.matrix_UPlayout_left_22_up)
    ui.matrix_UPlayout_left_22.addLayout(ui.matrix_UPlayout_left_22_down)


    ui.matrix_UPlayout_leftl.addLayout(ui.matrix_UPlayout_left_11)
    ui.matrix_UPlayout_leftl.addLayout(ui.matrix_UPlayout_left_21)
    ui.matrix_UPlayout_leftr.addLayout(ui.matrix_UPlayout_left_12)
    ui.matrix_UPlayout_leftr.addLayout(ui.matrix_UPlayout_left_22)
    ui.matrix_UPlayout_left.addLayout(ui.matrix_UPlayout_leftl)
    ui.matrix_UPlayout_left.addLayout(ui.matrix_UPlayout_leftr)
    ui.matrix_UPlayout.addLayout(ui.matrix_UPlayout_left)

    ui.matrix_UPlayout_line=QLabel(ui.matrix_page)
    ui.matrix_UPlayout_line.setObjectName("matrix_UPlayout_line")
    ui.matrix_UPlayout_line.setText(default_vline_text1)
    ui.matrix_UPlayout_line.setWordWrap(True)
    ui.matrix_UPlayout_line.setStyleSheet(default_vline_style)
    ui.matrix_UPlayout_line.setAlignment(default_vline_alignment)
    ui.matrix_UPlayout_line.setFrameShape(default_vline_frameShape)
    ui.matrix_UPlayout.addWidget(ui.matrix_UPlayout_line)


    ui.matrix_UPlayout_right=QHBoxLayout()
    ui.matrix_UPlayout_right.setObjectName(u"matrix_UPlayout_right")
    ui.matrix_UPlayout_rightl=QVBoxLayout()
    ui.matrix_UPlayout_rightl.setObjectName(u"matrix_UPlayout_rightl")
    ui.matrix_UPlayout_rightr=QVBoxLayout()
    ui.matrix_UPlayout_rightr.setObjectName(u"matrix_UPlayout_rightr")


    ui.matrix_UPlayout_right_11=QVBoxLayout()
    ui.matrix_UPlayout_right_11.setObjectName(u"matrix_UPlayout_right_11")
    ui.matrix_UPlayout_right_11_up=QHBoxLayout()
    ui.matrix_UPlayout_right_11_up.setObjectName(u"matrix_UPlayout_right_11_up")
    
    # set cell title
    ui.matrix_UPlayout_right_11_title=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_11_title.setObjectName(u"matrix_UPlayout_right_11_title")
    ui.matrix_UPlayout_right_11_title.setText(default_Task.title)
    ui.matrix_UPlayout_right_11_title.setStyleSheet(default_title_style)
    ui.matrix_UPlayout_right_11_title.setAlignment(default_title_alignment)
    ui.matrix_UPlayout_right_11_title.setReadOnly(True)

    # set cell time
    ui.matrix_UPlayout_right_11_time=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_11_time.setObjectName(u"matrix_UPlayout_right_11_time")
    ui.matrix_UPlayout_right_11_time.setText(default_Task.ddl)
    ui.matrix_UPlayout_right_11_time.setStyleSheet(default_time_style)
    ui.matrix_UPlayout_right_11_time.setAlignment(default_time_alignment)
    ui.matrix_UPlayout_right_11_time.setReadOnly(True)

    ui.matrix_UPlayout_right_11_up.addWidget(ui.matrix_UPlayout_right_11_title)
    ui.matrix_UPlayout_right_11_up.addWidget(ui.matrix_UPlayout_right_11_time)

    ui.matrix_UPlayout_right_11_down=QHBoxLayout()
    ui.matrix_UPlayout_right_11_down.setObjectName(u"matrix_UPlayout_right_11_down")
    
    # set cell discription(ddl)
    ui.matrix_UPlayout_right_11_discription=QTextEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_11_discription.setObjectName(u"matrix_UPlayout_right_11_discription")
    ui.matrix_UPlayout_right_11_discription.setText(default_Task.description)
    ui.matrix_UPlayout_right_11_discription.setStyleSheet(default_discription_style)
    ui.matrix_UPlayout_right_11_discription.setAlignment(default_discription_alignment)
    ui.matrix_UPlayout_right_11_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_UPlayout_right_11_discription.setReadOnly(True)


    ui.matrix_UPlayout_right_11_down_format=QVBoxLayout()
    ui.matrix_UPlayout_right_11_down_format.setObjectName(u"matrix_UPlayout_right_11_down_format")

    # set cell edit button
    ui.matrix_UPlayout_right_11_down_edit_button=QPushButton("matrix_UPlayout_right_11_down_edit_button")
    ui.matrix_UPlayout_right_11_down_edit_button.setText(' Edit ')
    ui.matrix_UPlayout_right_11_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_UPlayout_right_11_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_UPlayout_right_11_down_format.addWidget(ui.matrix_UPlayout_right_11_down_edit_button)

    # set cell delete button
    ui.matrix_UPlayout_right_11_down_del_button=QPushButton("matrix_UPlayout_right_11_down_del_button")
    ui.matrix_UPlayout_right_11_down_del_button.setText(' Finish ')
    ui.matrix_UPlayout_right_11_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_UPlayout_right_11_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_UPlayout_right_11_down_format.addWidget(ui.matrix_UPlayout_right_11_down_del_button)

    ui.matrix_UPlayout_right_11_down.addWidget(ui.matrix_UPlayout_right_11_discription)
    ui.matrix_UPlayout_right_11_down.addLayout(ui.matrix_UPlayout_right_11_down_format)

    ui.matrix_UPlayout_right_11.addLayout(ui.matrix_UPlayout_right_11_up)
    ui.matrix_UPlayout_right_11.addLayout(ui.matrix_UPlayout_right_11_down)

    ui.matrix_UPlayout_right_21=QVBoxLayout()
    ui.matrix_UPlayout_right_21.setObjectName(u"matrix_UPlayout_right_21")
    ui.matrix_UPlayout_right_21_up=QHBoxLayout()
    ui.matrix_UPlayout_right_21_up.setObjectName(u"matrix_UPlayout_right_21_up")
    
    # set cell title
    ui.matrix_UPlayout_right_21_title=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_21_title.setObjectName(u"matrix_UPlayout_right_21_title")
    ui.matrix_UPlayout_right_21_title.setText(default_Task.title)
    ui.matrix_UPlayout_right_21_title.setStyleSheet(default_title_style)
    ui.matrix_UPlayout_right_21_title.setAlignment(default_title_alignment)
    ui.matrix_UPlayout_right_21_title.setReadOnly(True)

    # set cell time
    ui.matrix_UPlayout_right_21_time=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_21_time.setObjectName(u"matrix_UPlayout_right_21_time")
    ui.matrix_UPlayout_right_21_time.setText(default_Task.ddl)
    ui.matrix_UPlayout_right_21_time.setStyleSheet(default_time_style)
    ui.matrix_UPlayout_right_21_time.setAlignment(default_time_alignment)
    ui.matrix_UPlayout_right_21_time.setReadOnly(True)

    ui.matrix_UPlayout_right_21_up.addWidget(ui.matrix_UPlayout_right_21_title)
    ui.matrix_UPlayout_right_21_up.addWidget(ui.matrix_UPlayout_right_21_time)

    ui.matrix_UPlayout_right_21_down=QHBoxLayout()
    ui.matrix_UPlayout_right_21_down.setObjectName(u"matrix_UPlayout_right_21_down")
    
    # set cell discription(ddl)
    ui.matrix_UPlayout_right_21_discription=QTextEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_21_discription.setObjectName(u"matrix_UPlayout_right_21_discription")
    ui.matrix_UPlayout_right_21_discription.setText(default_Task.description)
    ui.matrix_UPlayout_right_21_discription.setStyleSheet(default_discription_style)
    ui.matrix_UPlayout_right_21_discription.setAlignment(default_discription_alignment)
    ui.matrix_UPlayout_right_21_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_UPlayout_right_21_discription.setReadOnly(True)


    ui.matrix_UPlayout_right_21_down_format=QVBoxLayout()
    ui.matrix_UPlayout_right_21_down_format.setObjectName(u"matrix_UPlayout_right_21_down_format")

    # set cell edit button
    ui.matrix_UPlayout_right_21_down_edit_button=QPushButton("matrix_UPlayout_right_21_down_edit_button")
    ui.matrix_UPlayout_right_21_down_edit_button.setText(' Edit ')
    ui.matrix_UPlayout_right_21_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_UPlayout_right_21_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_UPlayout_right_21_down_format.addWidget(ui.matrix_UPlayout_right_21_down_edit_button)

    # set cell delete button
    ui.matrix_UPlayout_right_21_down_del_button=QPushButton("matrix_UPlayout_right_21_down_del_button")
    ui.matrix_UPlayout_right_21_down_del_button.setText(' Finish ')
    ui.matrix_UPlayout_right_21_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_UPlayout_right_21_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_UPlayout_right_21_down_format.addWidget(ui.matrix_UPlayout_right_21_down_del_button)

    ui.matrix_UPlayout_right_21_down.addWidget(ui.matrix_UPlayout_right_21_discription)
    ui.matrix_UPlayout_right_21_down.addLayout(ui.matrix_UPlayout_right_21_down_format)

    ui.matrix_UPlayout_right_21.addLayout(ui.matrix_UPlayout_right_21_up)
    ui.matrix_UPlayout_right_21.addLayout(ui.matrix_UPlayout_right_21_down)

    ui.matrix_UPlayout_right_12=QVBoxLayout()
    ui.matrix_UPlayout_right_12.setObjectName(u"matrix_UPlayout_right_12")
    ui.matrix_UPlayout_right_12_up=QHBoxLayout()
    ui.matrix_UPlayout_right_12_up.setObjectName(u"matrix_UPlayout_right_12_up")
    
    # set cell title
    ui.matrix_UPlayout_right_12_title=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_12_title.setObjectName(u"matrix_UPlayout_right_12_title")
    ui.matrix_UPlayout_right_12_title.setText(default_Task.title)
    ui.matrix_UPlayout_right_12_title.setStyleSheet(default_title_style)
    ui.matrix_UPlayout_right_12_title.setAlignment(default_title_alignment)
    ui.matrix_UPlayout_right_12_title.setReadOnly(True)

    # set cell time
    ui.matrix_UPlayout_right_12_time=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_12_time.setObjectName(u"matrix_UPlayout_right_12_time")
    ui.matrix_UPlayout_right_12_time.setText(default_Task.ddl)
    ui.matrix_UPlayout_right_12_time.setStyleSheet(default_time_style)
    ui.matrix_UPlayout_right_12_time.setAlignment(default_time_alignment)
    ui.matrix_UPlayout_right_12_time.setReadOnly(True)

    ui.matrix_UPlayout_right_12_up.addWidget(ui.matrix_UPlayout_right_12_title)
    ui.matrix_UPlayout_right_12_up.addWidget(ui.matrix_UPlayout_right_12_time)

    ui.matrix_UPlayout_right_12_down=QHBoxLayout()
    ui.matrix_UPlayout_right_12_down.setObjectName(u"matrix_UPlayout_right_12_down")
    
    # set cell discription(ddl)
    ui.matrix_UPlayout_right_12_discription=QTextEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_12_discription.setObjectName(u"matrix_UPlayout_right_12_discription")
    ui.matrix_UPlayout_right_12_discription.setText(default_Task.description)
    ui.matrix_UPlayout_right_12_discription.setStyleSheet(default_discription_style)
    ui.matrix_UPlayout_right_12_discription.setAlignment(default_discription_alignment)
    ui.matrix_UPlayout_right_12_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_UPlayout_right_12_discription.setReadOnly(True)


    ui.matrix_UPlayout_right_12_down_format=QVBoxLayout()
    ui.matrix_UPlayout_right_12_down_format.setObjectName(u"matrix_UPlayout_right_12_down_format")

    # set cell edit button
    ui.matrix_UPlayout_right_12_down_edit_button=QPushButton("matrix_UPlayout_right_12_down_edit_button")
    ui.matrix_UPlayout_right_12_down_edit_button.setText(' Edit ')
    ui.matrix_UPlayout_right_12_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_UPlayout_right_12_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_UPlayout_right_12_down_format.addWidget(ui.matrix_UPlayout_right_12_down_edit_button)

    # set cell delete button
    ui.matrix_UPlayout_right_12_down_del_button=QPushButton("matrix_UPlayout_right_12_down_del_button")
    ui.matrix_UPlayout_right_12_down_del_button.setText(' Finish ')
    ui.matrix_UPlayout_right_12_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_UPlayout_right_12_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_UPlayout_right_12_down_format.addWidget(ui.matrix_UPlayout_right_12_down_del_button)

    ui.matrix_UPlayout_right_12_down.addWidget(ui.matrix_UPlayout_right_12_discription)
    ui.matrix_UPlayout_right_12_down.addLayout(ui.matrix_UPlayout_right_12_down_format)

    ui.matrix_UPlayout_right_12.addLayout(ui.matrix_UPlayout_right_12_up)
    ui.matrix_UPlayout_right_12.addLayout(ui.matrix_UPlayout_right_12_down)

    ui.matrix_UPlayout_right_22=QVBoxLayout()
    ui.matrix_UPlayout_right_22.setObjectName(u"matrix_UPlayout_right_22")
    ui.matrix_UPlayout_right_22_up=QHBoxLayout()
    ui.matrix_UPlayout_right_22_up.setObjectName(u"matrix_UPlayout_right_22_up")
    
    # set cell title
    ui.matrix_UPlayout_right_22_title=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_22_title.setObjectName(u"matrix_UPlayout_right_22_title")
    ui.matrix_UPlayout_right_22_title.setText(default_Task.title)
    ui.matrix_UPlayout_right_22_title.setStyleSheet(default_title_style)
    ui.matrix_UPlayout_right_22_title.setAlignment(default_title_alignment)
    ui.matrix_UPlayout_right_22_title.setReadOnly(True)

    # set cell time
    ui.matrix_UPlayout_right_22_time=QLineEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_22_time.setObjectName(u"matrix_UPlayout_right_22_time")
    ui.matrix_UPlayout_right_22_time.setText(default_Task.ddl)
    ui.matrix_UPlayout_right_22_time.setStyleSheet(default_time_style)
    ui.matrix_UPlayout_right_22_time.setAlignment(default_time_alignment)
    ui.matrix_UPlayout_right_22_time.setReadOnly(True)

    ui.matrix_UPlayout_right_22_up.addWidget(ui.matrix_UPlayout_right_22_title)
    ui.matrix_UPlayout_right_22_up.addWidget(ui.matrix_UPlayout_right_22_time)

    ui.matrix_UPlayout_right_22_down=QHBoxLayout()
    ui.matrix_UPlayout_right_22_down.setObjectName(u"matrix_UPlayout_right_22_down")
    
    # set cell discription(ddl)
    ui.matrix_UPlayout_right_22_discription=QTextEdit(ui.matrix_page)
    ui.matrix_UPlayout_right_22_discription.setObjectName(u"matrix_UPlayout_right_22_discription")
    ui.matrix_UPlayout_right_22_discription.setText(default_Task.description)
    ui.matrix_UPlayout_right_22_discription.setStyleSheet(default_discription_style)
    ui.matrix_UPlayout_right_22_discription.setAlignment(default_discription_alignment)
    ui.matrix_UPlayout_right_22_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_UPlayout_right_22_discription.setReadOnly(True)


    ui.matrix_UPlayout_right_22_down_format=QVBoxLayout()
    ui.matrix_UPlayout_right_22_down_format.setObjectName(u"matrix_UPlayout_right_22_down_format")

    # set cell edit button
    ui.matrix_UPlayout_right_22_down_edit_button=QPushButton("matrix_UPlayout_right_22_down_edit_button")
    ui.matrix_UPlayout_right_22_down_edit_button.setText(' Edit ')
    ui.matrix_UPlayout_right_22_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_UPlayout_right_22_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_UPlayout_right_22_down_format.addWidget(ui.matrix_UPlayout_right_22_down_edit_button)

    # set cell delete button
    ui.matrix_UPlayout_right_22_down_del_button=QPushButton("matrix_UPlayout_right_22_down_del_button")
    ui.matrix_UPlayout_right_22_down_del_button.setText(' Finish ')
    ui.matrix_UPlayout_right_22_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_UPlayout_right_22_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_UPlayout_right_22_down_format.addWidget(ui.matrix_UPlayout_right_22_down_del_button)

    ui.matrix_UPlayout_right_22_down.addWidget(ui.matrix_UPlayout_right_22_discription)
    ui.matrix_UPlayout_right_22_down.addLayout(ui.matrix_UPlayout_right_22_down_format)

    ui.matrix_UPlayout_right_22.addLayout(ui.matrix_UPlayout_right_22_up)
    ui.matrix_UPlayout_right_22.addLayout(ui.matrix_UPlayout_right_22_down)


    ui.matrix_UPlayout_rightl.addLayout(ui.matrix_UPlayout_right_11)
    ui.matrix_UPlayout_rightl.addLayout(ui.matrix_UPlayout_right_21)
    ui.matrix_UPlayout_rightr.addLayout(ui.matrix_UPlayout_right_12)
    ui.matrix_UPlayout_rightr.addLayout(ui.matrix_UPlayout_right_22)
    ui.matrix_UPlayout_right.addLayout(ui.matrix_UPlayout_rightl)
    ui.matrix_UPlayout_right.addLayout(ui.matrix_UPlayout_rightr)
    ui.matrix_UPlayout.addLayout(ui.matrix_UPlayout_right)



    ui.matrix_DOWNlayout=QHBoxLayout()
    ui.matrix_DOWNlayout.setObjectName(u"matrix_DOWNlayout")

    ui.matrix_DOWNlayout=QHBoxLayout()
    ui.matrix_DOWNlayout.setObjectName(u"matrix_DOWNlayout")

    ui.matrix_DOWNlayout_left=QHBoxLayout()
    ui.matrix_DOWNlayout_left.setObjectName(u"matrix_DOWNlayout_left")
    ui.matrix_DOWNlayout_leftl=QVBoxLayout()
    ui.matrix_DOWNlayout_leftl.setObjectName(u"matrix_DOWNlayout_leftl")
    ui.matrix_DOWNlayout_leftr=QVBoxLayout()
    ui.matrix_DOWNlayout_leftr.setObjectName(u"matrix_DOWNlayout_leftr")


    ui.matrix_DOWNlayout_left_11=QVBoxLayout()
    ui.matrix_DOWNlayout_left_11.setObjectName(u"matrix_DOWNlayout_left_11")
    ui.matrix_DOWNlayout_left_11_up=QHBoxLayout()
    ui.matrix_DOWNlayout_left_11_up.setObjectName(u"matrix_DOWNlayout_left_11_up")
    
    # set cell title
    ui.matrix_DOWNlayout_left_11_title=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_11_title.setObjectName(u"matrix_DOWNlayout_left_11_title")
    ui.matrix_DOWNlayout_left_11_title.setText(default_Task.title)
    ui.matrix_DOWNlayout_left_11_title.setStyleSheet(default_title_style)
    ui.matrix_DOWNlayout_left_11_title.setAlignment(default_title_alignment)
    ui.matrix_DOWNlayout_left_11_title.setReadOnly(True)

    # set cell time
    ui.matrix_DOWNlayout_left_11_time=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_11_time.setObjectName(u"matrix_DOWNlayout_left_11_time")
    ui.matrix_DOWNlayout_left_11_time.setText(default_Task.ddl)
    ui.matrix_DOWNlayout_left_11_time.setStyleSheet(default_time_style)
    ui.matrix_DOWNlayout_left_11_time.setAlignment(default_time_alignment)
    ui.matrix_DOWNlayout_left_11_time.setReadOnly(True)

    ui.matrix_DOWNlayout_left_11_up.addWidget(ui.matrix_DOWNlayout_left_11_title)
    ui.matrix_DOWNlayout_left_11_up.addWidget(ui.matrix_DOWNlayout_left_11_time)

    ui.matrix_DOWNlayout_left_11_down=QHBoxLayout()
    ui.matrix_DOWNlayout_left_11_down.setObjectName(u"matrix_DOWNlayout_left_11_down")
    
    # set cell discription(ddl)
    ui.matrix_DOWNlayout_left_11_discription=QTextEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_11_discription.setObjectName(u"matrix_DOWNlayout_left_11_discription")
    ui.matrix_DOWNlayout_left_11_discription.setText(default_Task.description)
    ui.matrix_DOWNlayout_left_11_discription.setStyleSheet(default_discription_style)
    ui.matrix_DOWNlayout_left_11_discription.setAlignment(default_discription_alignment)
    ui.matrix_DOWNlayout_left_11_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_DOWNlayout_left_11_discription.setReadOnly(True)


    ui.matrix_DOWNlayout_left_11_down_format=QVBoxLayout()
    ui.matrix_DOWNlayout_left_11_down_format.setObjectName(u"matrix_DOWNlayout_left_11_down_format")

    # set cell edit button
    ui.matrix_DOWNlayout_left_11_down_edit_button=QPushButton("matrix_DOWNlayout_left_11_down_edit_button")
    ui.matrix_DOWNlayout_left_11_down_edit_button.setText(' Edit ')
    ui.matrix_DOWNlayout_left_11_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_DOWNlayout_left_11_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_DOWNlayout_left_11_down_format.addWidget(ui.matrix_DOWNlayout_left_11_down_edit_button)

    # set cell delete button
    ui.matrix_DOWNlayout_left_11_down_del_button=QPushButton("matrix_DOWNlayout_left_11_down_del_button")
    ui.matrix_DOWNlayout_left_11_down_del_button.setText(' Finish ')
    ui.matrix_DOWNlayout_left_11_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_DOWNlayout_left_11_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_DOWNlayout_left_11_down_format.addWidget(ui.matrix_DOWNlayout_left_11_down_del_button)

    ui.matrix_DOWNlayout_left_11_down.addWidget(ui.matrix_DOWNlayout_left_11_discription)
    ui.matrix_DOWNlayout_left_11_down.addLayout(ui.matrix_DOWNlayout_left_11_down_format)

    ui.matrix_DOWNlayout_left_11.addLayout(ui.matrix_DOWNlayout_left_11_up)
    ui.matrix_DOWNlayout_left_11.addLayout(ui.matrix_DOWNlayout_left_11_down)

    ui.matrix_DOWNlayout_left_21=QVBoxLayout()
    ui.matrix_DOWNlayout_left_21.setObjectName(u"matrix_DOWNlayout_left_21")
    ui.matrix_DOWNlayout_left_21_up=QHBoxLayout()
    ui.matrix_DOWNlayout_left_21_up.setObjectName(u"matrix_DOWNlayout_left_21_up")
    
    # set cell title
    ui.matrix_DOWNlayout_left_21_title=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_21_title.setObjectName(u"matrix_DOWNlayout_left_21_title")
    ui.matrix_DOWNlayout_left_21_title.setText(default_Task.title)
    ui.matrix_DOWNlayout_left_21_title.setStyleSheet(default_title_style)
    ui.matrix_DOWNlayout_left_21_title.setAlignment(default_title_alignment)
    ui.matrix_DOWNlayout_left_21_title.setReadOnly(True)

    # set cell time
    ui.matrix_DOWNlayout_left_21_time=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_21_time.setObjectName(u"matrix_DOWNlayout_left_21_time")
    ui.matrix_DOWNlayout_left_21_time.setText(default_Task.ddl)
    ui.matrix_DOWNlayout_left_21_time.setStyleSheet(default_time_style)
    ui.matrix_DOWNlayout_left_21_time.setAlignment(default_time_alignment)
    ui.matrix_DOWNlayout_left_21_time.setReadOnly(True)

    ui.matrix_DOWNlayout_left_21_up.addWidget(ui.matrix_DOWNlayout_left_21_title)
    ui.matrix_DOWNlayout_left_21_up.addWidget(ui.matrix_DOWNlayout_left_21_time)

    ui.matrix_DOWNlayout_left_21_down=QHBoxLayout()
    ui.matrix_DOWNlayout_left_21_down.setObjectName(u"matrix_DOWNlayout_left_21_down")
    
    # set cell discription(ddl)
    ui.matrix_DOWNlayout_left_21_discription=QTextEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_21_discription.setObjectName(u"matrix_DOWNlayout_left_21_discription")
    ui.matrix_DOWNlayout_left_21_discription.setText(default_Task.description)
    ui.matrix_DOWNlayout_left_21_discription.setStyleSheet(default_discription_style)
    ui.matrix_DOWNlayout_left_21_discription.setAlignment(default_discription_alignment)
    ui.matrix_DOWNlayout_left_21_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_DOWNlayout_left_21_discription.setReadOnly(True)


    ui.matrix_DOWNlayout_left_21_down_format=QVBoxLayout()
    ui.matrix_DOWNlayout_left_21_down_format.setObjectName(u"matrix_DOWNlayout_left_21_down_format")

    # set cell edit button
    ui.matrix_DOWNlayout_left_21_down_edit_button=QPushButton("matrix_DOWNlayout_left_21_down_edit_button")
    ui.matrix_DOWNlayout_left_21_down_edit_button.setText(' Edit ')
    ui.matrix_DOWNlayout_left_21_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_DOWNlayout_left_21_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_DOWNlayout_left_21_down_format.addWidget(ui.matrix_DOWNlayout_left_21_down_edit_button)

    # set cell delete button
    ui.matrix_DOWNlayout_left_21_down_del_button=QPushButton("matrix_DOWNlayout_left_21_down_del_button")
    ui.matrix_DOWNlayout_left_21_down_del_button.setText(' Finish ')
    ui.matrix_DOWNlayout_left_21_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_DOWNlayout_left_21_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_DOWNlayout_left_21_down_format.addWidget(ui.matrix_DOWNlayout_left_21_down_del_button)

    ui.matrix_DOWNlayout_left_21_down.addWidget(ui.matrix_DOWNlayout_left_21_discription)
    ui.matrix_DOWNlayout_left_21_down.addLayout(ui.matrix_DOWNlayout_left_21_down_format)

    ui.matrix_DOWNlayout_left_21.addLayout(ui.matrix_DOWNlayout_left_21_up)
    ui.matrix_DOWNlayout_left_21.addLayout(ui.matrix_DOWNlayout_left_21_down)

    ui.matrix_DOWNlayout_left_12=QVBoxLayout()
    ui.matrix_DOWNlayout_left_12.setObjectName(u"matrix_DOWNlayout_left_12")
    ui.matrix_DOWNlayout_left_12_up=QHBoxLayout()
    ui.matrix_DOWNlayout_left_12_up.setObjectName(u"matrix_DOWNlayout_left_12_up")
    
    # set cell title
    ui.matrix_DOWNlayout_left_12_title=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_12_title.setObjectName(u"matrix_DOWNlayout_left_12_title")
    ui.matrix_DOWNlayout_left_12_title.setText(default_Task.title)
    ui.matrix_DOWNlayout_left_12_title.setStyleSheet(default_title_style)
    ui.matrix_DOWNlayout_left_12_title.setAlignment(default_title_alignment)
    ui.matrix_DOWNlayout_left_12_title.setReadOnly(True)

    # set cell time
    ui.matrix_DOWNlayout_left_12_time=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_12_time.setObjectName(u"matrix_DOWNlayout_left_12_time")
    ui.matrix_DOWNlayout_left_12_time.setText(default_Task.ddl)
    ui.matrix_DOWNlayout_left_12_time.setStyleSheet(default_time_style)
    ui.matrix_DOWNlayout_left_12_time.setAlignment(default_time_alignment)
    ui.matrix_DOWNlayout_left_12_time.setReadOnly(True)

    ui.matrix_DOWNlayout_left_12_up.addWidget(ui.matrix_DOWNlayout_left_12_title)
    ui.matrix_DOWNlayout_left_12_up.addWidget(ui.matrix_DOWNlayout_left_12_time)

    ui.matrix_DOWNlayout_left_12_down=QHBoxLayout()
    ui.matrix_DOWNlayout_left_12_down.setObjectName(u"matrix_DOWNlayout_left_12_down")
    
    # set cell discription(ddl)
    ui.matrix_DOWNlayout_left_12_discription=QTextEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_12_discription.setObjectName(u"matrix_DOWNlayout_left_12_discription")
    ui.matrix_DOWNlayout_left_12_discription.setText(default_Task.description)
    ui.matrix_DOWNlayout_left_12_discription.setStyleSheet(default_discription_style)
    ui.matrix_DOWNlayout_left_12_discription.setAlignment(default_discription_alignment)
    ui.matrix_DOWNlayout_left_12_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_DOWNlayout_left_12_discription.setReadOnly(True)


    ui.matrix_DOWNlayout_left_12_down_format=QVBoxLayout()
    ui.matrix_DOWNlayout_left_12_down_format.setObjectName(u"matrix_DOWNlayout_left_12_down_format")

    # set cell edit button
    ui.matrix_DOWNlayout_left_12_down_edit_button=QPushButton("matrix_DOWNlayout_left_12_down_edit_button")
    ui.matrix_DOWNlayout_left_12_down_edit_button.setText(' Edit ')
    ui.matrix_DOWNlayout_left_12_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_DOWNlayout_left_12_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_DOWNlayout_left_12_down_format.addWidget(ui.matrix_DOWNlayout_left_12_down_edit_button)

    # set cell delete button
    ui.matrix_DOWNlayout_left_12_down_del_button=QPushButton("matrix_DOWNlayout_left_12_down_del_button")
    ui.matrix_DOWNlayout_left_12_down_del_button.setText(' Finish ')
    ui.matrix_DOWNlayout_left_12_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_DOWNlayout_left_12_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_DOWNlayout_left_12_down_format.addWidget(ui.matrix_DOWNlayout_left_12_down_del_button)

    ui.matrix_DOWNlayout_left_12_down.addWidget(ui.matrix_DOWNlayout_left_12_discription)
    ui.matrix_DOWNlayout_left_12_down.addLayout(ui.matrix_DOWNlayout_left_12_down_format)

    ui.matrix_DOWNlayout_left_12.addLayout(ui.matrix_DOWNlayout_left_12_up)
    ui.matrix_DOWNlayout_left_12.addLayout(ui.matrix_DOWNlayout_left_12_down)

    ui.matrix_DOWNlayout_left_22=QVBoxLayout()
    ui.matrix_DOWNlayout_left_22.setObjectName(u"matrix_DOWNlayout_left_22")
    ui.matrix_DOWNlayout_left_22_up=QHBoxLayout()
    ui.matrix_DOWNlayout_left_22_up.setObjectName(u"matrix_DOWNlayout_left_22_up")
    
    # set cell title
    ui.matrix_DOWNlayout_left_22_title=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_22_title.setObjectName(u"matrix_DOWNlayout_left_22_title")
    ui.matrix_DOWNlayout_left_22_title.setText(default_Task.title)
    ui.matrix_DOWNlayout_left_22_title.setStyleSheet(default_title_style)
    ui.matrix_DOWNlayout_left_22_title.setAlignment(default_title_alignment)
    ui.matrix_DOWNlayout_left_22_title.setReadOnly(True)

    # set cell time
    ui.matrix_DOWNlayout_left_22_time=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_22_time.setObjectName(u"matrix_DOWNlayout_left_22_time")
    ui.matrix_DOWNlayout_left_22_time.setText(default_Task.ddl)
    ui.matrix_DOWNlayout_left_22_time.setStyleSheet(default_time_style)
    ui.matrix_DOWNlayout_left_22_time.setAlignment(default_time_alignment)
    ui.matrix_DOWNlayout_left_22_time.setReadOnly(True)

    ui.matrix_DOWNlayout_left_22_up.addWidget(ui.matrix_DOWNlayout_left_22_title)
    ui.matrix_DOWNlayout_left_22_up.addWidget(ui.matrix_DOWNlayout_left_22_time)

    ui.matrix_DOWNlayout_left_22_down=QHBoxLayout()
    ui.matrix_DOWNlayout_left_22_down.setObjectName(u"matrix_DOWNlayout_left_22_down")
    
    # set cell discription(ddl)
    ui.matrix_DOWNlayout_left_22_discription=QTextEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_left_22_discription.setObjectName(u"matrix_DOWNlayout_left_22_discription")
    ui.matrix_DOWNlayout_left_22_discription.setText(default_Task.description)
    ui.matrix_DOWNlayout_left_22_discription.setStyleSheet(default_discription_style)
    ui.matrix_DOWNlayout_left_22_discription.setAlignment(default_discription_alignment)
    ui.matrix_DOWNlayout_left_22_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_DOWNlayout_left_22_discription.setReadOnly(True)


    ui.matrix_DOWNlayout_left_22_down_format=QVBoxLayout()
    ui.matrix_DOWNlayout_left_22_down_format.setObjectName(u"matrix_DOWNlayout_left_22_down_format")

    # set cell edit button
    ui.matrix_DOWNlayout_left_22_down_edit_button=QPushButton("matrix_DOWNlayout_left_22_down_edit_button")
    ui.matrix_DOWNlayout_left_22_down_edit_button.setText(' Edit ')
    ui.matrix_DOWNlayout_left_22_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_DOWNlayout_left_22_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_DOWNlayout_left_22_down_format.addWidget(ui.matrix_DOWNlayout_left_22_down_edit_button)

    # set cell delete button
    ui.matrix_DOWNlayout_left_22_down_del_button=QPushButton("matrix_DOWNlayout_left_22_down_del_button")
    ui.matrix_DOWNlayout_left_22_down_del_button.setText(' Finish ')
    ui.matrix_DOWNlayout_left_22_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_DOWNlayout_left_22_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_DOWNlayout_left_22_down_format.addWidget(ui.matrix_DOWNlayout_left_22_down_del_button)

    ui.matrix_DOWNlayout_left_22_down.addWidget(ui.matrix_DOWNlayout_left_22_discription)
    ui.matrix_DOWNlayout_left_22_down.addLayout(ui.matrix_DOWNlayout_left_22_down_format)

    ui.matrix_DOWNlayout_left_22.addLayout(ui.matrix_DOWNlayout_left_22_up)
    ui.matrix_DOWNlayout_left_22.addLayout(ui.matrix_DOWNlayout_left_22_down)


    ui.matrix_DOWNlayout_leftl.addLayout(ui.matrix_DOWNlayout_left_11)
    ui.matrix_DOWNlayout_leftl.addLayout(ui.matrix_DOWNlayout_left_21)
    ui.matrix_DOWNlayout_leftr.addLayout(ui.matrix_DOWNlayout_left_12)
    ui.matrix_DOWNlayout_leftr.addLayout(ui.matrix_DOWNlayout_left_22)
    ui.matrix_DOWNlayout_left.addLayout(ui.matrix_DOWNlayout_leftl)
    ui.matrix_DOWNlayout_left.addLayout(ui.matrix_DOWNlayout_leftr)
    ui.matrix_DOWNlayout.addLayout(ui.matrix_DOWNlayout_left)

    ui.matrix_DOWNlayout_line=QLabel(ui.matrix_page)
    ui.matrix_DOWNlayout_line.setObjectName("matrix_DOWNlayout_line")
    ui.matrix_DOWNlayout_line.setText(default_vline_text2)
    ui.matrix_DOWNlayout_line.setWordWrap(True)
    ui.matrix_DOWNlayout_line.setStyleSheet(default_vline_style)
    ui.matrix_DOWNlayout_line.setAlignment(default_vline_alignment)
    ui.matrix_DOWNlayout_line.setFrameShape(default_vline_frameShape)
    ui.matrix_DOWNlayout.addWidget(ui.matrix_DOWNlayout_line)


    ui.matrix_DOWNlayout_right=QHBoxLayout()
    ui.matrix_DOWNlayout_right.setObjectName(u"matrix_DOWNlayout_right")
    ui.matrix_DOWNlayout_rightl=QVBoxLayout()
    ui.matrix_DOWNlayout_rightl.setObjectName(u"matrix_DOWNlayout_rightl")
    ui.matrix_DOWNlayout_rightr=QVBoxLayout()
    ui.matrix_DOWNlayout_rightr.setObjectName(u"matrix_DOWNlayout_rightr")


    ui.matrix_DOWNlayout_right_11=QVBoxLayout()
    ui.matrix_DOWNlayout_right_11.setObjectName(u"matrix_DOWNlayout_right_11")
    ui.matrix_DOWNlayout_right_11_up=QHBoxLayout()
    ui.matrix_DOWNlayout_right_11_up.setObjectName(u"matrix_DOWNlayout_right_11_up")
    
    # set cell title
    ui.matrix_DOWNlayout_right_11_title=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_11_title.setObjectName(u"matrix_DOWNlayout_right_11_title")
    ui.matrix_DOWNlayout_right_11_title.setText(default_Task.title)
    ui.matrix_DOWNlayout_right_11_title.setStyleSheet(default_title_style)
    ui.matrix_DOWNlayout_right_11_title.setAlignment(default_title_alignment)
    ui.matrix_DOWNlayout_right_11_title.setReadOnly(True)

    # set cell time
    ui.matrix_DOWNlayout_right_11_time=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_11_time.setObjectName(u"matrix_DOWNlayout_right_11_time")
    ui.matrix_DOWNlayout_right_11_time.setText(default_Task.ddl)
    ui.matrix_DOWNlayout_right_11_time.setStyleSheet(default_time_style)
    ui.matrix_DOWNlayout_right_11_time.setAlignment(default_time_alignment)
    ui.matrix_DOWNlayout_right_11_time.setReadOnly(True)

    ui.matrix_DOWNlayout_right_11_up.addWidget(ui.matrix_DOWNlayout_right_11_title)
    ui.matrix_DOWNlayout_right_11_up.addWidget(ui.matrix_DOWNlayout_right_11_time)

    ui.matrix_DOWNlayout_right_11_down=QHBoxLayout()
    ui.matrix_DOWNlayout_right_11_down.setObjectName(u"matrix_DOWNlayout_right_11_down")
    
    # set cell discription(ddl)
    ui.matrix_DOWNlayout_right_11_discription=QTextEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_11_discription.setObjectName(u"matrix_DOWNlayout_right_11_discription")
    ui.matrix_DOWNlayout_right_11_discription.setText(default_Task.description)
    ui.matrix_DOWNlayout_right_11_discription.setStyleSheet(default_discription_style)
    ui.matrix_DOWNlayout_right_11_discription.setAlignment(default_discription_alignment)
    ui.matrix_DOWNlayout_right_11_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_DOWNlayout_right_11_discription.setReadOnly(True)


    ui.matrix_DOWNlayout_right_11_down_format=QVBoxLayout()
    ui.matrix_DOWNlayout_right_11_down_format.setObjectName(u"matrix_DOWNlayout_right_11_down_format")

    # set cell edit button
    ui.matrix_DOWNlayout_right_11_down_edit_button=QPushButton("matrix_DOWNlayout_right_11_down_edit_button")
    ui.matrix_DOWNlayout_right_11_down_edit_button.setText(' Edit ')
    ui.matrix_DOWNlayout_right_11_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_DOWNlayout_right_11_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_DOWNlayout_right_11_down_format.addWidget(ui.matrix_DOWNlayout_right_11_down_edit_button)

    # set cell delete button
    ui.matrix_DOWNlayout_right_11_down_del_button=QPushButton("matrix_DOWNlayout_right_11_down_del_button")
    ui.matrix_DOWNlayout_right_11_down_del_button.setText(' Finish ')
    ui.matrix_DOWNlayout_right_11_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_DOWNlayout_right_11_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_DOWNlayout_right_11_down_format.addWidget(ui.matrix_DOWNlayout_right_11_down_del_button)

    ui.matrix_DOWNlayout_right_11_down.addWidget(ui.matrix_DOWNlayout_right_11_discription)
    ui.matrix_DOWNlayout_right_11_down.addLayout(ui.matrix_DOWNlayout_right_11_down_format)

    ui.matrix_DOWNlayout_right_11.addLayout(ui.matrix_DOWNlayout_right_11_up)
    ui.matrix_DOWNlayout_right_11.addLayout(ui.matrix_DOWNlayout_right_11_down)

    ui.matrix_DOWNlayout_right_21=QVBoxLayout()
    ui.matrix_DOWNlayout_right_21.setObjectName(u"matrix_DOWNlayout_right_21")
    ui.matrix_DOWNlayout_right_21_up=QHBoxLayout()
    ui.matrix_DOWNlayout_right_21_up.setObjectName(u"matrix_DOWNlayout_right_21_up")
    
    # set cell title
    ui.matrix_DOWNlayout_right_21_title=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_21_title.setObjectName(u"matrix_DOWNlayout_right_21_title")
    ui.matrix_DOWNlayout_right_21_title.setText(default_Task.title)
    ui.matrix_DOWNlayout_right_21_title.setStyleSheet(default_title_style)
    ui.matrix_DOWNlayout_right_21_title.setAlignment(default_title_alignment)
    ui.matrix_DOWNlayout_right_21_title.setReadOnly(True)

    # set cell time
    ui.matrix_DOWNlayout_right_21_time=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_21_time.setObjectName(u"matrix_DOWNlayout_right_21_time")
    ui.matrix_DOWNlayout_right_21_time.setText(default_Task.ddl)
    ui.matrix_DOWNlayout_right_21_time.setStyleSheet(default_time_style)
    ui.matrix_DOWNlayout_right_21_time.setAlignment(default_time_alignment)
    ui.matrix_DOWNlayout_right_21_time.setReadOnly(True)

    ui.matrix_DOWNlayout_right_21_up.addWidget(ui.matrix_DOWNlayout_right_21_title)
    ui.matrix_DOWNlayout_right_21_up.addWidget(ui.matrix_DOWNlayout_right_21_time)

    ui.matrix_DOWNlayout_right_21_down=QHBoxLayout()
    ui.matrix_DOWNlayout_right_21_down.setObjectName(u"matrix_DOWNlayout_right_21_down")
    
    # set cell discription(ddl)
    ui.matrix_DOWNlayout_right_21_discription=QTextEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_21_discription.setObjectName(u"matrix_DOWNlayout_right_21_discription")
    ui.matrix_DOWNlayout_right_21_discription.setText(default_Task.description)
    ui.matrix_DOWNlayout_right_21_discription.setStyleSheet(default_discription_style)
    ui.matrix_DOWNlayout_right_21_discription.setAlignment(default_discription_alignment)
    ui.matrix_DOWNlayout_right_21_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_DOWNlayout_right_21_discription.setReadOnly(True)


    ui.matrix_DOWNlayout_right_21_down_format=QVBoxLayout()
    ui.matrix_DOWNlayout_right_21_down_format.setObjectName(u"matrix_DOWNlayout_right_21_down_format")

    # set cell edit button
    ui.matrix_DOWNlayout_right_21_down_edit_button=QPushButton("matrix_DOWNlayout_right_21_down_edit_button")
    ui.matrix_DOWNlayout_right_21_down_edit_button.setText(' Edit ')
    ui.matrix_DOWNlayout_right_21_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_DOWNlayout_right_21_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_DOWNlayout_right_21_down_format.addWidget(ui.matrix_DOWNlayout_right_21_down_edit_button)

    # set cell delete button
    ui.matrix_DOWNlayout_right_21_down_del_button=QPushButton("matrix_DOWNlayout_right_21_down_del_button")
    ui.matrix_DOWNlayout_right_21_down_del_button.setText(' Finish ')
    ui.matrix_DOWNlayout_right_21_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_DOWNlayout_right_21_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_DOWNlayout_right_21_down_format.addWidget(ui.matrix_DOWNlayout_right_21_down_del_button)

    ui.matrix_DOWNlayout_right_21_down.addWidget(ui.matrix_DOWNlayout_right_21_discription)
    ui.matrix_DOWNlayout_right_21_down.addLayout(ui.matrix_DOWNlayout_right_21_down_format)

    ui.matrix_DOWNlayout_right_21.addLayout(ui.matrix_DOWNlayout_right_21_up)
    ui.matrix_DOWNlayout_right_21.addLayout(ui.matrix_DOWNlayout_right_21_down)

    ui.matrix_DOWNlayout_right_12=QVBoxLayout()
    ui.matrix_DOWNlayout_right_12.setObjectName(u"matrix_DOWNlayout_right_12")
    ui.matrix_DOWNlayout_right_12_up=QHBoxLayout()
    ui.matrix_DOWNlayout_right_12_up.setObjectName(u"matrix_DOWNlayout_right_12_up")
    
    # set cell title
    ui.matrix_DOWNlayout_right_12_title=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_12_title.setObjectName(u"matrix_DOWNlayout_right_12_title")
    ui.matrix_DOWNlayout_right_12_title.setText(default_Task.title)
    ui.matrix_DOWNlayout_right_12_title.setStyleSheet(default_title_style)
    ui.matrix_DOWNlayout_right_12_title.setAlignment(default_title_alignment)
    ui.matrix_DOWNlayout_right_12_title.setReadOnly(True)

    # set cell time
    ui.matrix_DOWNlayout_right_12_time=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_12_time.setObjectName(u"matrix_DOWNlayout_right_12_time")
    ui.matrix_DOWNlayout_right_12_time.setText(default_Task.ddl)
    ui.matrix_DOWNlayout_right_12_time.setStyleSheet(default_time_style)
    ui.matrix_DOWNlayout_right_12_time.setAlignment(default_time_alignment)
    ui.matrix_DOWNlayout_right_12_time.setReadOnly(True)

    ui.matrix_DOWNlayout_right_12_up.addWidget(ui.matrix_DOWNlayout_right_12_title)
    ui.matrix_DOWNlayout_right_12_up.addWidget(ui.matrix_DOWNlayout_right_12_time)

    ui.matrix_DOWNlayout_right_12_down=QHBoxLayout()
    ui.matrix_DOWNlayout_right_12_down.setObjectName(u"matrix_DOWNlayout_right_12_down")
    
    # set cell discription(ddl)
    ui.matrix_DOWNlayout_right_12_discription=QTextEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_12_discription.setObjectName(u"matrix_DOWNlayout_right_12_discription")
    ui.matrix_DOWNlayout_right_12_discription.setText(default_Task.description)
    ui.matrix_DOWNlayout_right_12_discription.setStyleSheet(default_discription_style)
    ui.matrix_DOWNlayout_right_12_discription.setAlignment(default_discription_alignment)
    ui.matrix_DOWNlayout_right_12_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_DOWNlayout_right_12_discription.setReadOnly(True)


    ui.matrix_DOWNlayout_right_12_down_format=QVBoxLayout()
    ui.matrix_DOWNlayout_right_12_down_format.setObjectName(u"matrix_DOWNlayout_right_12_down_format")

    # set cell edit button
    ui.matrix_DOWNlayout_right_12_down_edit_button=QPushButton("matrix_DOWNlayout_right_12_down_edit_button")
    ui.matrix_DOWNlayout_right_12_down_edit_button.setText(' Edit ')
    ui.matrix_DOWNlayout_right_12_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_DOWNlayout_right_12_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_DOWNlayout_right_12_down_format.addWidget(ui.matrix_DOWNlayout_right_12_down_edit_button)

    # set cell delete button
    ui.matrix_DOWNlayout_right_12_down_del_button=QPushButton("matrix_DOWNlayout_right_12_down_del_button")
    ui.matrix_DOWNlayout_right_12_down_del_button.setText(' Finish ')
    ui.matrix_DOWNlayout_right_12_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_DOWNlayout_right_12_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_DOWNlayout_right_12_down_format.addWidget(ui.matrix_DOWNlayout_right_12_down_del_button)

    ui.matrix_DOWNlayout_right_12_down.addWidget(ui.matrix_DOWNlayout_right_12_discription)
    ui.matrix_DOWNlayout_right_12_down.addLayout(ui.matrix_DOWNlayout_right_12_down_format)

    ui.matrix_DOWNlayout_right_12.addLayout(ui.matrix_DOWNlayout_right_12_up)
    ui.matrix_DOWNlayout_right_12.addLayout(ui.matrix_DOWNlayout_right_12_down)

    ui.matrix_DOWNlayout_right_22=QVBoxLayout()
    ui.matrix_DOWNlayout_right_22.setObjectName(u"matrix_DOWNlayout_right_22")
    ui.matrix_DOWNlayout_right_22_up=QHBoxLayout()
    ui.matrix_DOWNlayout_right_22_up.setObjectName(u"matrix_DOWNlayout_right_22_up")
    
    # set cell title
    ui.matrix_DOWNlayout_right_22_title=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_22_title.setObjectName(u"matrix_DOWNlayout_right_22_title")
    ui.matrix_DOWNlayout_right_22_title.setText(default_Task.title)
    ui.matrix_DOWNlayout_right_22_title.setStyleSheet(default_title_style)
    ui.matrix_DOWNlayout_right_22_title.setAlignment(default_title_alignment)
    ui.matrix_DOWNlayout_right_22_title.setReadOnly(True)

    # set cell time
    ui.matrix_DOWNlayout_right_22_time=QLineEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_22_time.setObjectName(u"matrix_DOWNlayout_right_22_time")
    ui.matrix_DOWNlayout_right_22_time.setText(default_Task.ddl)
    ui.matrix_DOWNlayout_right_22_time.setStyleSheet(default_time_style)
    ui.matrix_DOWNlayout_right_22_time.setAlignment(default_time_alignment)
    ui.matrix_DOWNlayout_right_22_time.setReadOnly(True)

    ui.matrix_DOWNlayout_right_22_up.addWidget(ui.matrix_DOWNlayout_right_22_title)
    ui.matrix_DOWNlayout_right_22_up.addWidget(ui.matrix_DOWNlayout_right_22_time)

    ui.matrix_DOWNlayout_right_22_down=QHBoxLayout()
    ui.matrix_DOWNlayout_right_22_down.setObjectName(u"matrix_DOWNlayout_right_22_down")
    
    # set cell discription(ddl)
    ui.matrix_DOWNlayout_right_22_discription=QTextEdit(ui.matrix_page)
    ui.matrix_DOWNlayout_right_22_discription.setObjectName(u"matrix_DOWNlayout_right_22_discription")
    ui.matrix_DOWNlayout_right_22_discription.setText(default_Task.description)
    ui.matrix_DOWNlayout_right_22_discription.setStyleSheet(default_discription_style)
    ui.matrix_DOWNlayout_right_22_discription.setAlignment(default_discription_alignment)
    ui.matrix_DOWNlayout_right_22_discription.setFrameShape(default_discription_frameShape)
    ui.matrix_DOWNlayout_right_22_discription.setReadOnly(True)


    ui.matrix_DOWNlayout_right_22_down_format=QVBoxLayout()
    ui.matrix_DOWNlayout_right_22_down_format.setObjectName(u"matrix_DOWNlayout_right_22_down_format")

    # set cell edit button
    ui.matrix_DOWNlayout_right_22_down_edit_button=QPushButton("matrix_DOWNlayout_right_22_down_edit_button")
    ui.matrix_DOWNlayout_right_22_down_edit_button.setText(' Edit ')
    ui.matrix_DOWNlayout_right_22_down_edit_button.setSizePolicy(default_edit_button_horizon_style, default_edit_button_vertical_style)
    ui.matrix_DOWNlayout_right_22_down_edit_button.setStyleSheet(default_edit_button_style)
    ui.matrix_DOWNlayout_right_22_down_format.addWidget(ui.matrix_DOWNlayout_right_22_down_edit_button)

    # set cell delete button
    ui.matrix_DOWNlayout_right_22_down_del_button=QPushButton("matrix_DOWNlayout_right_22_down_del_button")
    ui.matrix_DOWNlayout_right_22_down_del_button.setText(' Finish ')
    ui.matrix_DOWNlayout_right_22_down_del_button.setSizePolicy(default_del_button_horizon_style, default_del_button_vertical_style)
    ui.matrix_DOWNlayout_right_22_down_del_button.setStyleSheet(default_del_button_style)
    ui.matrix_DOWNlayout_right_22_down_format.addWidget(ui.matrix_DOWNlayout_right_22_down_del_button)

    ui.matrix_DOWNlayout_right_22_down.addWidget(ui.matrix_DOWNlayout_right_22_discription)
    ui.matrix_DOWNlayout_right_22_down.addLayout(ui.matrix_DOWNlayout_right_22_down_format)

    ui.matrix_DOWNlayout_right_22.addLayout(ui.matrix_DOWNlayout_right_22_up)
    ui.matrix_DOWNlayout_right_22.addLayout(ui.matrix_DOWNlayout_right_22_down)


    ui.matrix_DOWNlayout_rightl.addLayout(ui.matrix_DOWNlayout_right_11)
    ui.matrix_DOWNlayout_rightl.addLayout(ui.matrix_DOWNlayout_right_21)
    ui.matrix_DOWNlayout_rightr.addLayout(ui.matrix_DOWNlayout_right_12)
    ui.matrix_DOWNlayout_rightr.addLayout(ui.matrix_DOWNlayout_right_22)
    ui.matrix_DOWNlayout_right.addLayout(ui.matrix_DOWNlayout_rightl)
    ui.matrix_DOWNlayout_right.addLayout(ui.matrix_DOWNlayout_rightr)
    ui.matrix_DOWNlayout.addLayout(ui.matrix_DOWNlayout_right)


    ui.matrix_Mlayout=QHBoxLayout()
    ui.matrix_Mlayout.setObjectName(u"matrix_Mlayout")

    ui.matrix_Mlayout_left_line=QLabel(ui.matrix_page)
    ui.matrix_Mlayout_left_line.setObjectName("matrix_Mlayout_left_line")
    ui.matrix_Mlayout_left_line.setText(default_hline_text1)
    ui.matrix_Mlayout_left_line.setStyleSheet(default_hline_style)
    ui.matrix_Mlayout_left_line.setAlignment(default_hline_alignment)
    ui.matrix_Mlayout_left_line.setFrameShape(default_hline_frameShape)
    ui.matrix_Mlayout.addWidget(ui.matrix_Mlayout_left_line)

    ui.matrix_Mlayout_right_line=QLabel(ui.matrix_page)
    ui.matrix_Mlayout_right_line.setObjectName("matrix_Mlayout_right_line")
    ui.matrix_Mlayout_right_line.setText(default_hline_text2)
    ui.matrix_Mlayout_right_line.setStyleSheet(default_hline_style)
    ui.matrix_Mlayout_right_line.setAlignment(default_hline_alignment)
    ui.matrix_Mlayout_right_line.setFrameShape(default_hline_frameShape)
    ui.matrix_Mlayout.addWidget(ui.matrix_Mlayout_right_line)

    ui.matrix_Vlayout.addLayout(ui.matrix_UPlayout)
    ui.matrix_Vlayout.addLayout(ui.matrix_Mlayout)
    ui.matrix_Vlayout.addLayout(ui.matrix_DOWNlayout)

    ui.matrix_dataArray=[
        [
            [
                ui.matrix_UPlayout_left_11_title,
                ui.matrix_UPlayout_left_11_time,
                ui.matrix_UPlayout_left_11_discription,
                ui.matrix_UPlayout_left_11_down_edit_button,
                ui.matrix_UPlayout_left_11_down_del_button
            ],
            [
                ui.matrix_UPlayout_left_12_title,
                ui.matrix_UPlayout_left_12_time,
                ui.matrix_UPlayout_left_12_discription,
                ui.matrix_UPlayout_left_12_down_edit_button,
                ui.matrix_UPlayout_left_12_down_del_button
            ],
            [
                ui.matrix_UPlayout_left_21_title,
                ui.matrix_UPlayout_left_21_time,
                ui.matrix_UPlayout_left_21_discription,
                ui.matrix_UPlayout_left_21_down_edit_button,
                ui.matrix_UPlayout_left_21_down_del_button
            ],
            [
                ui.matrix_UPlayout_left_22_title,
                ui.matrix_UPlayout_left_22_time,
                ui.matrix_UPlayout_left_22_discription,
                ui.matrix_UPlayout_left_22_down_edit_button,
                ui.matrix_UPlayout_left_22_down_del_button
            ]
        ],
        [
            [
                ui.matrix_UPlayout_right_11_title,
                ui.matrix_UPlayout_right_11_time,
                ui.matrix_UPlayout_right_11_discription,
                ui.matrix_UPlayout_right_11_down_edit_button,
                ui.matrix_UPlayout_right_11_down_del_button
            ],
            [
                ui.matrix_UPlayout_right_12_title,
                ui.matrix_UPlayout_right_12_time,
                ui.matrix_UPlayout_right_12_discription,
                ui.matrix_UPlayout_right_12_down_edit_button,
                ui.matrix_UPlayout_right_12_down_del_button
            ],
            [
                ui.matrix_UPlayout_right_21_title,
                ui.matrix_UPlayout_right_21_time,
                ui.matrix_UPlayout_right_21_discription,
                ui.matrix_UPlayout_right_21_down_edit_button,
                ui.matrix_UPlayout_right_21_down_del_button
            ],
            [
                ui.matrix_UPlayout_right_22_title,
                ui.matrix_UPlayout_right_22_time,
                ui.matrix_UPlayout_right_22_discription,
                ui.matrix_UPlayout_right_22_down_edit_button,
                ui.matrix_UPlayout_right_22_down_del_button
            ]
        ],
        [
            [
                ui.matrix_DOWNlayout_left_11_title,
                ui.matrix_DOWNlayout_left_11_time,
                ui.matrix_DOWNlayout_left_11_discription,
                ui.matrix_DOWNlayout_left_11_down_edit_button,
                ui.matrix_DOWNlayout_left_11_down_del_button
            ],
            [
                ui.matrix_DOWNlayout_left_12_title,
                ui.matrix_DOWNlayout_left_12_time,
                ui.matrix_DOWNlayout_left_12_discription,
                ui.matrix_DOWNlayout_left_12_down_edit_button,
                ui.matrix_DOWNlayout_left_12_down_del_button
            ],
            [
                ui.matrix_DOWNlayout_left_21_title,
                ui.matrix_DOWNlayout_left_21_time,
                ui.matrix_DOWNlayout_left_21_discription,
                ui.matrix_DOWNlayout_left_21_down_edit_button,
                ui.matrix_DOWNlayout_left_21_down_del_button
            ],
            [
                ui.matrix_DOWNlayout_left_22_title,
                ui.matrix_DOWNlayout_left_22_time,
                ui.matrix_DOWNlayout_left_22_discription,
                ui.matrix_DOWNlayout_left_22_down_edit_button,
                ui.matrix_DOWNlayout_left_22_down_del_button
            ]
        ],
        [
            [
                ui.matrix_DOWNlayout_right_11_title,
                ui.matrix_DOWNlayout_right_11_time,
                ui.matrix_DOWNlayout_right_11_discription,
                ui.matrix_DOWNlayout_right_11_down_edit_button,
                ui.matrix_DOWNlayout_right_11_down_del_button
            ],
            [
                ui.matrix_DOWNlayout_right_12_title,
                ui.matrix_DOWNlayout_right_12_time,
                ui.matrix_DOWNlayout_right_12_discription,
                ui.matrix_DOWNlayout_right_12_down_edit_button,
                ui.matrix_DOWNlayout_right_12_down_del_button
            ],
            [
                ui.matrix_DOWNlayout_right_21_title,
                ui.matrix_DOWNlayout_right_21_time,
                ui.matrix_DOWNlayout_right_21_discription,
                ui.matrix_DOWNlayout_right_21_down_edit_button,
                ui.matrix_DOWNlayout_right_21_down_del_button
            ],
            [
                ui.matrix_DOWNlayout_right_22_title,
                ui.matrix_DOWNlayout_right_22_time,
                ui.matrix_DOWNlayout_right_22_discription,
                ui.matrix_DOWNlayout_right_22_down_edit_button,
                ui.matrix_DOWNlayout_right_22_down_del_button
            ]
        ]
    ]