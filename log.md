# PyToDo-Log

## 20220803-v1.0.0-zry

工作：为实现可自定义的Calendar，初步尝试使用QT Designer生成表格控件，更新main.ui文件后编译覆盖modules/ui_main.py。

问题：表格内数据类型疑似无法自定义，一是需要统一的Task类进行数据管理，二是需要实现自定义的Task任务显示框。

效果：

![image-20220803223210163](log/image-20220803223210163.png)

## 20220803-v1.0.1-zry

工作：放弃QT Designer中现成的表格控件，直接修改modules/ui_main.py中的代码，使用抽象数据类型QStandardItem及QTableView实现自定义表格。

问题：新建modules/task.py待完善，预计在此实现统一的Task数据类型，并提供各种Task编辑、显示操作接口。

效果：

![image-20220803223548824](log/image-20220803223548824.png)

## add sign_up func in database.py

*Date:2022/08/03*

*Author:YJK*

在database.py中添加sign_up_database()函数，为注册服务提供接口

## Add modules/user.py which defined User class

*Date:2022/08/03*

*Author:YJK*

在modules添加user.py，创建User类，定义User属性

## alter init in modules/user.py & add login_in func in database

*Date:2022/08/04*

*Author:YJK*

在database.py添加log_in_database()函数，为登陆服务提供接口；修改modules.user.py中User类的初始化方法



## Commit around 11:30 on 2022/08/04

*Date:2022/08/04*

*Author:YJK*

1. `database.py`：修改login_in_database函数，支持返回当前用户任务列表
2. `modules.task.py`：修改`__init__`函数，支持初始化创建`task`对象
3. 完善log和README两个md
