import pymysql

global db
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

def init_user_table():
    global db, cursor
    sql = """create table if not exists user(
                id int comment '用户编号',
                account varchar(50) comment '账号',
                password varchar(50) comment '密码',
                name varchar(50) comment '用户名',
                email varchar(50) comment '邮箱',
                phone varchar(50) comment '手机号',
                head_image varchar(2083) comment '头像URL'
                ) """
    cursor.execute(sql)
    db.commit()
if __name__ == '__main__':
    connect_database()
    init_user_table()
    # execute SQL query
    cursor.execute("SELECT VERSION()")
    # fetch single data
    data = cursor.fetchone()
    # test output
    print("DataBase version : %s " % data)
    # close connection
    db.close()
