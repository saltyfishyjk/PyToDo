import pymysql

if __name__ == '__main__':
    # connect to database in ALI CLOUD server
    db = pymysql.connect(host='8.130.21.170',
                         user='root',
                         password='PyToDo2006!',
                         database='test_database')
    # make a cursor object
    cursor = db.cursor()
    # execute SQL query
    cursor.execute("SELECT VERSION()")
    # fetch single data
    data = cursor.fetchone()
    # test output
    print("DataBase version : %s " % data)
    # close connection
    db.close()
