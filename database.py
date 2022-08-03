from modules.user import User
import pymysql

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
	# connect_database()
	global db, cursor
	if str(account) == 0 or str(password) == 0:
		return False, "Please enter non-null account and password"
	sql = 'select account from user where account = "{}"'.format(account)
	cursor.execute(sql)
	if cursor.rowcount:
		return False, "This account has been signed up!\n"
	else:
		cursor.execute('select count(*) from user')
		line_num = int(cursor.fetchone()[0])
		sql = "insert into user(id, account, password) values('{0}', '{1}', '{2}')".format(line_num, account, password)
		cursor.execute(sql)
		db.commit()
		return True, "Sign up successfully, please login in your new account"


# FUNC : support login in action
# IN   : account:str & password:str
# RET  : isSuccessful:boolean & User object(None when False) & hint:str
def login_in_database(account, password):
	if account is None or str(account) == 0:
		return False, None, "ERROR : Get null account!"
	sql = 'select account from user where account = "{}"'.format(account)
	cursor.execute(sql)
	if cursor.rowcount == 0:
		return False, None, "ERROR : non-exist account!"
	sql = 'select password from user where account = "{}"'.format(account)
	cursor.execute(sql)
	password_in_database = cursor.fetchone()[0]
	if password_in_database != password:
		return False, None, "ERROR : incorrect password!"
	sql = 'select * from user where account = "{}"'.format(account)
	cursor.execute(sql)
	user_info_tuple = cursor.fetchone()
	u = User(user_info_tuple[0],
				  user_info_tuple[1],
				  user_info_tuple[2],
				  user_info_tuple[3],
				  user_info_tuple[4],
				  user_info_tuple[5],
				  user_info_tuple[6])
	return True, u, 'Login in successfully!\nWelcome, {}'.format(account)
