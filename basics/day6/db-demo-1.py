import psycopg2 as pg

conn = pg.connect(
    host="localhost",
    dabase="mydb",
    user="postgres",
    password="postgres"
)
if conn:
    print("Connected to DB")
    cur = conn.cursor()
    cur.execute('Select * from emp_list')
    for rec in cur:
        print(rec)  # each row as tumple
else:
    print("Unable to connect")
conn.close()
