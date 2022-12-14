import pymysql
from task import Task

from user import User

# database object


global db
# cursor
global cursor
# database
global database

# Notice : THIS FUNC HAS TO BE CALLED AT THE VERY BEGINNING OF MAIN FUNCTION
def init_database():
	connect_database()


# FUNC : connect to database on ALI CLOUD
# IN   : NULL
# RET  : NULL
def connect_database():
	global db, cursor
	# connect to database in ALI CLOUD server test_database
	db = pymysql.connect(host='8.130.21.170',
						user='root',
						password='PyToDo2006!',
						 database='official_database')
						#database='test_database')
	# make a cursor object
	cursor = db.cursor()
	global database
	database = 'official_database'


# FUNC : support sign_up action
# IN   : account:str & password:str
# RET  : isSuccessful:boolean & hint:str
def sign_up_database(account, password):
	global db, cursor, database
	if str(account) == 0 or str(password) == 0:
		return False, "Please enter non-null account and password"
	sql = 'select account from {}.user where account = "{}"'.format(database, account)
	cursor.execute(sql)
	if cursor.rowcount:
		return False, "This account has been signed up!\n"
	else:
		cursor.execute('select count(*) from {}.user'.format(database))
		line_num = int(cursor.fetchone()[0])
		if line_num != 0:
			sql = 'select max(id) from {}.user'.format(database)
			cursor.execute(sql)
			max_id = int(cursor.fetchone()[0])
		else:
			max_id = -1
		id = max(max_id + 1, line_num)
		# create a user column in table user
		sql = "insert into {0}.user(id, account, password) values('{1}', '{2}', '{3}')".format(database, id, account, password)
		cursor.execute(sql)
		db.commit()
		# create a user_task table for this user
		sql = 'use {}'.format(database)
		cursor.execute(sql)
		sql = 'create table user_{}_task (' \
			  'id int comment "序号",' \
			  'text varchar(500) comment"文本",' \
			  'title varchar(500) comment"标题",' \
			  'author varchar(500) comment"作者",' \
			  'creatTime varchar(500) comment"创建时间",' \
			  'description varchar(500) comment"描述",' \
			  'importance int comment "重要性",' \
			  'isDaily varchar(500) comment "是否为日常任务",' \
			  'type varchar(500) comment "类别",' \
			  'ddl varchar(500) comment "截止日期",' \
			  'state varchar(500) comment "状态",' \
			  'startTime varchar(500) comment"起始时间"' \
			  ')comment "user{}\'s task table"'.format(id, id)
		cursor.execute(sql)
		db.commit()
		return True, "Sign up successfully, please login in your new account"


# IN  : cursor.fetchone()
# RET : User object
def get_user(fet):
	return User(fet[0],
					fet[1],
					fet[2],
					fet[3],
					fet[4],
					fet[5],
					fet[6])

# IN  : cursor.fetchall()
# RET : list of task object
def get_task_list(fet):
	ls = []
	for index in fet:
		task = Task(text=index[1],
					title=index[2],
					author=index[3],
					creatTime=index[4],
					description=index[5],
					importance=index[6],
					isDaily=True if index[7] == 'True' else False,
					type=index[8],
					ddl=index[9],
					state=index[10],
					startTime=index[11])
		task.id = int(index[0])
		ls.append(task)
	return ls

# FUNC : support login in action
# IN   : account:str & password:str
# RET  : isSuccessful:boolean & user:object(None when False) & tasks:list of task object & hint:str
def login_in_database(account, password):
	global database
	# check non-null account and password
	if account is None or str(account) == 0:
		return False, None, "ERROR : Get null account!"
	# check if account exists
	sql = 'select account from {}.user where account = "{}"'.format(database, account)
	cursor.execute(sql)
	if cursor.rowcount == 0:
		return False, None, None, "ERROR : non-exist account!"
	# check if password correct
	sql = 'select password from {}.user where account = "{}"'.format(database, account)
	cursor.execute(sql)
	password_in_database = cursor.fetchone()[0]
	if password_in_database != password:
		return False, None, None, "ERROR : incorrect password!"
	# get user info
	# get user
	sql = 'select * from {}.user where account = "{}"'.format(database, account)
	cursor.execute(sql)
	user_info_tuple = cursor.fetchone()
	u = get_user(user_info_tuple)
	id = int(user_info_tuple[0])
	# get user_task
	sql = 'select * from {}.user_{}_task'.format(database, id)
	cursor.execute(sql)
	user_task_tuple = cursor.fetchall()
	tasks = get_task_list(user_task_tuple)
	return True, u, tasks, 'Login in successfully!\nWelcome, {}'.format(account)


# FUNC : get task list of given user obj
# IN   : user:obj
# RET  : tasklist:obj[]
def get_task_list_database(user):
	global database
	id = user.id
	sql = 'select * from {}.user_{}_task'.format(database, id)
	cursor.execute(sql)
	user_task_tuple = cursor.fetchall()
	tasks = get_task_list(user_task_tuple)
	return tasks


# FUNC : add a new task in user's account
# IN   : user:object & task:object
# RET  : isSuccessful:boolean & hint:str
def add_task_database(user, task):
	global database
	id = user.id
	sql = 'select account from {}.user where id = "{}"'.format(database, id)
	cursor.execute(sql)
	# check if available user
	if not cursor.rowcount:
		return False, "ERROR : unavailable account!"
	sql = 'select count(*) from {}.user_{}_task'.format(database, id)
	cursor.execute(sql)
	task_num = int(cursor.fetchone()[0])
	sql = 'select max(id) from {}.user_{}_task'.format(database, id)
	cursor.execute(sql)
	if task_num != 0:
		task_id_max = int(cursor.fetchone()[0])
	else:
		task_id_max = 0
	task.id = max(task_num, task_id_max + 1)
	sql = "insert into {0}.user_{1}_task(id, text, title, author, creatTime, description, importance, isDaily, type, ddl, state, startTime) " \
		  "values('{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}')".\
		format(database, id, task.id, task.text, task.title, task.author, task.creatTime, task.description,
			   task.importance, str(task.isDaily), task.type, task.ddl, task.state, task.startTime)
	cursor.execute(sql)
	db.commit()
	return True, "Successfully added a new task {} in user {}\'s account".format(task.title, user.account)


# FUNC : modify an existing task in user's account
# IN   : user:object & ols_task:object
# RET  : isSuccessful:boolean & hint:str
def delete_task_database(user, old_task):
	global database
	id = user.id
	sql = 'select account from {}.user where id = "{}"'.format(database, id)
	cursor.execute(sql)
	# check if available user
	if not cursor.rowcount:
		return False, "ERROR : unavailable account!"
	task_id = old_task.id
	sql = "delete from {}.user_{}_task where id = {}".format(database, id, task_id)
	cursor.execute(sql)
	db.commit()
	return True, "Successfully deleted task {} in user {}\'s account".format(task_id, id)


# FUNC : modify an existing task in user's account
# IN   : user:object & old_task:object
# RET  : isSuccessful:boolean & hint:str
def modify_task_database(user, new_task):
	flag_delete, hint_delete = delete_task_database(user, new_task)
	flag_add, hint_add = add_task_database(user, new_task)
	return flag_add & flag_delete, hint_delete + hint_add


# FUNC : turn an existing task in user's account
# IN   : user:object & new_task:object & new_state:str
# RET  : isSuccessful:boolean & hint:str
def modify_task_state_database(user, new_task, new_state):
	new_task.state = new_state
	return modify_task_database(user, new_task)