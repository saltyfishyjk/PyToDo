import pymysql
import time

# database
global db
# cursor
global cursor


def connect_database():
	global db, cursor
	# connect to database in ALI CLOUD server test_database
	db = pymysql.connect(host='8.130.21.170',
						user='root',
						password='PyToDo2006!',
						database='test_database')
	# make a cursor object
	cursor = db.cursor()


# register, return if sign up successfully
def sign_up_database(account, password):
	connect_database()
	if str(account) == 0 or str(password) == 0:
		return False, "Please enter non-null account and password"
	global db, cursor
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