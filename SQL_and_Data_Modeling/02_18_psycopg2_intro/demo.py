import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, True))
cursor.execute('INSERT INTO table2 (id, completed)' +
 ' VALUES (%(id)s, %(completed)s);', {
    'id':3,
    'completed': False
})

data = {
    'id':6,
    'completed': True
}

cursor.execute('INSERT INTO table2 (id, completed)' +
 ' VALUES (%(id)s, %(completed)s);', data)

cursor.execute('SELECT * from table2;')

# result = cursor.fetchall()
result = cursor.fetchmany(2)
print(result)

result_one = cursor.fetchone()
print('res one:  ', result_one)


# connection.commit()

connection.close()

cursor.close()