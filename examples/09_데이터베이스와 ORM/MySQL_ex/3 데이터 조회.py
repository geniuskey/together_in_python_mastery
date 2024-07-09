import mysql.connector

# 데이터베이스 연결
conn = mysql.connector.connect(
    host='localhost',
    user='yourusername',
    password='yourpassword',
    database='exampledb'
)

cur = conn.cursor()

# 데이터 조회
cur.execute('SELECT * FROM users')
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
