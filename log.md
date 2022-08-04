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

## 20220804-v1.0.2-zry

工作：嵌入登录界面

问题：登录界面与软件画风割裂，主题待统一；登录界面账号密码疑似认证有问题，错误密码也能登录；关闭登录界面仍可打开软件，登录失败可能也会打开软件，需要捕捉一个登录失败的信号来反馈给软件。


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

## Add add_task_database in database.py

*Date:2022/08/04*

*Author:YJK*

1. `database.py`支持`add_tast_database`函数接口，支持为一用户添加新任务

## Commit around 23:20 on 2022/08/04

*Date:2022/08/04*

*Author:YJK*

1. `database.py`支持`delete_tast_database`函数接口，支持为一用户删除特定任务
2. `modules/task.py`：为`Task`类增加`id`属性，方便后端数据库操作确定唯一task
3. `database.py`相应修改`sign_up_database`和`add_task_database`
