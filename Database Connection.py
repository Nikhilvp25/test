import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost',1521, service_name='orcl')
conn = cx_Oracle.connect(user=r'learning_sql', password='Admin_123', dsn=dsn_tns)
c = conn.cursor()
c.execute('''create table temp_123  (Name varchar(20), cell_number number(10))''')
c.execute('''insert into temp_123 values ('Nikhil' , 9036721243)''')
c.execute('commit')
c.execute('''select * from temp_123''')

print(type(c))
for row in c:
    print (row[0], '-', row[1])
c.close()

