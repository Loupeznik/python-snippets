import pymysql

'''
Connect to a database
'''

def connect(host, user, password, db):
    return pymysql.connect(host=host,
                             user=user, 
                             password=password,
                             db=db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
    )
