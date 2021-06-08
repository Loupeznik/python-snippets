'''
Perform basic database operations (CRUD)
'''

def insert(connection, table : str):
    with connection.cursor() as cursor:
        sql = 'INSERT INTO {} (text) VALUES (%s)'.format(table)
        cursor.execute(sql, ('test'))
    connection.commit()

def update(connection, table : str, record : int):
    with connection.cursor() as cursor:
        sql = 'UPDATE {} SET {} = %s WHERE id = %s'.format(table, 'text')
        cursor.execute(sql, ('test-test', record))
    connection.commit()

def select(connection, table : str):
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM {}'.format(table)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

def delete(connection, table : str, record : int):
    with connection.cursor() as cursor:
        sql = 'DELETE FROM {} WHERE id = %s'.format(table, 'text')
        cursor.execute(sql, (record))
    connection.commit()
