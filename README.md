# PyToDo

![License](https://img.shields.io/github/license/saltyfishyjk/PyToDo) ![Python Version](https://img.shields.io/badge/python-3.9-brightgreen)  

## 项目简介

### 环境

python3.9



.../待补全

## 代码简介

### `database.py`

*Author:YJK*

功能：为项目其他模块提供数据库相关接口，在每个函数上方注释中通过FUNC,IN,RET三个部分注明该函数的功能、传入参数约定与返回参数约定

#### 接口与约定

| 函数接口名                   | 功能                       | 传入参数                                         | 返回参数                                                     | 其他                                                         |
| ---------------------------- | -------------------------- | ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `sign_up_database`           | 数据库端实现注册功能       | `account(str), password(str)`                    | `isSuccessful(boolean), hint(str)`                           | 调用者应在前端检查用户两次输入的密码是否一样，一样后才可调用本函数。<br/>第一个返回值为`True`时说明注册成功，为`Flase`说明注册失败，第二个字符串`hint`说明成功/失败的可能原因。 |
| `login_in_database`          | 数据库端实现登录功能       | `account(str), password(str)`                    | `isSuccessful(boolean), user(User obj), tasks(list of Task obj), hint(str)` | `isSuccessful`和`hint`功能同上。<br/>当登录成功时，第二个返回值`user`为非空`User`对象，包含用户在数据库中的信息；第三个返回值`tasks`为`Task`对象的列表，包含用户在数据库中存储的任务们。<br/> |
| `add_task_database`          | 数据库端实现为用户添加任务 | `user(User obj), task(Task obj)`                 | `isSuccessful(boolean), hint(str)`                           | **数据库中通过User的id和Task的id作为与其他User和Task区分的唯一标志，在login_in_database得到的user和tasks需要妥善保存**<br/>调用该接口时，第一个传入参数是登录时得到的`User`对象，第二个传入参数是要添加的`Task`对象。<br/>新建的`Task`对象的`id`不需要写，设为`None`即可（默认构造器就是`None`），数据库会根据库内数据自动生成`id`，**并修改传入Task对象的id**。 |
| `delete_task_database`       | 数据库端实现为用户删除任务 | `user(User obj), old_task(Task obj)`             | `isSuccessful(boolean), hint(str)`                           | 删除某个任务，这里同样以任务的`id`为唯一标识符，需要妥善保存在`add_task_database`传入的`Task`对象。 |
| `modify_task_database`       | 数据库端修改用户任务       | `user(User obj), new_task(Task obj)`             | `isSuccessful(boolean), hint(str)`                           | 修改已经存在的任务。<br/>调用者修改特定Task的除ID外的任意属性，并将其和User对象一同传入本函数，即可修改对象属性。 |
| `modify_task_state_database` | 数据库端修改用户任务状态   | `user(User obj), task(Task obj), new_state(str)` | `isSuccessful(boolean), hint(str)`                           | 修改已经存在的任务的状态。<br/>调用者将用户对象、任务对象和new_state传入，即可修改对象属性。 |

### `NewTask.py`

*Author:YJK*

功能：
