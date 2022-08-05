import pymysql
from task import Task

from user import User

# database object


global db
# cursor
global cursor

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
						database='test_database')
	# make a cursor object
	cursor = db.cursor()


# FUNC : support sign_up action
# IN   : account:str & password:str
# RET  : isSuccessful:boolean & hint:str
def sign_up_database(account, password):
	global db, cursor
	if str(account) == 0 or str(password) == 0:
		return False, "Please enter non-null account and password"
	sql = 'select account from test_database.user where account = "{}"'.format(account)
	cursor.execute(sql)
	if cursor.rowcount:
		return False, "This account has been signed up!\n"
	else:
		cursor.execute('select count(*) from user')
		line_num = int(cursor.fetchone()[0])
		# create a user column in table user
		sql = "insert into user(id, account, password) values('{0}', '{1}', '{2}')".format(line_num, account, password)
		cursor.execute(sql)
		db.commit()
		# create a user_task table for this user
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
			  'state varchar(500) comment "状态"' \
			  ')comment "user{}\'s task table"'.format(line_num, line_num)
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
		task = Task(index[1],
					index[2],
					index[3],
					index[4],
					index[5],
					index[6],
					index[7],
					index[8],
					index[9],
					index[10])
		task.id = int(index[0])
		ls.append(task)
	return ls

# FUNC : support login in action
# IN   : account:str & password:str
# RET  : isSuccessful:boolean & user:object(None when False) & tasks:list of task object & hint:str
def login_in_database(account, password):
	# check non-null account and password
	if account is None or str(account) == 0:
		return False, None, "ERROR : Get null account!"
	# check if account exists
	sql = 'select account from test_database.user where account = "{}"'.format(account)
	cursor.execute(sql)
	if cursor.rowcount == 0:
		return False, None, None, "ERROR : non-exist account!"
	# check if password correct
	sql = 'select password from test_database.user where account = "{}"'.format(account)
	cursor.execute(sql)
	password_in_database = cursor.fetchone()[0]
	if password_in_database != password:
		return False, None, None, "ERROR : incorrect password!"
	# get user info
	# get user
	sql = 'select * from test_database.user where account = "{}"'.format(account)
	cursor.execute(sql)
	user_info_tuple = cursor.fetchone()
	u = get_user(user_info_tuple)
	"""
	u = User(user_info_tuple[0],
				  user_info_tuple[1],
				  user_info_tuple[2],
				  user_info_tuple[3],
				  user_info_tuple[4],
				  user_info_tuple[5],
				  user_info_tuple[6])
	"""
	id = int(user_info_tuple[0])
	# get user_task
	sql = 'select * from test_database.user_{}_task'.format(id)
	cursor.execute(sql)
	user_task_tuple = cursor.fetchall()
	tasks = get_task_list(user_task_tuple)
	return True, u, tasks, 'Login in successfully!\nWelcome, {}'.format(account)


# FUNC : add a new task in user's account
# IN   : user:object & task:object
# RET  : isSuccessful:boolean & hint:str
def add_task_database(user, task):
	id = user.id
	sql = 'select account from test_database.user where id = "{}"'.format(id)
	cursor.execute(sql)
	# check if available user
	if not cursor.rowcount:
		return False, "ERROR : unavailable account!"
	sql = 'select count(*) from user_{}_task'.format(id)
	cursor.execute(sql)
	task_num = int(cursor.fetchone()[0])
	sql = 'select max(id) from user_{}_task'.format(id)
	cursor.execute(sql)
	task_id_max = int(cursor.fetchone()[0])
	task.id = max(task_num, task_id_max + 1)
	sql = "insert into user_{0}_task(id, text, title, author, creatTime, description, importance, isDaily, type, ddl, state) " \
		  "values('{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')".\
		format(id, task.id, task.text, task.title, task.author, task.creatTime, task.description,
			   task.importance, str(task.isDaily), task.type, task.ddl, task.state)
	cursor.execute(sql)
	db.commit()
	return True, "Successfully added a new task {} in user {}\'s account".format(task.title, user.account)


# FUNC : modify an existing task in user's account
# IN   : user:object & ols_task:object
# RET  : isSuccessful:boolean & hint:str
def delete_task_database(user, old_task):
	id = user.id
	sql = 'select account from test_database.user where id = "{}"'.format(id)
	cursor.execute(sql)
	# check if available user
	if not cursor.rowcount:
		return False, "ERROR : unavailable account!"
	task_id = old_task.id
	sql = "delete from user_{}_task where id = {}".format(id, task_id)
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