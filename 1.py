import sqlite3
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
a='00032'
aa=(a,'St', 'Ste', 'female')
#cur.execute("""INSERT INTO users(userid, fname, lname, gender)
#   VALUES(f'{aa}', 'St', 'Ste', 'female');""")
#cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", aa)
#conn.commit()



#cur.execute("select * from users where fname = 'Alex'")
cur.execute("select * from users ")
results = cur.fetchall()
print(results)

cur.execute("""SELECT   users.fname, users.lname ,orderid, orders.total FROM orders
   LEFT JOIN users ON users.userid=orders.userid;""")
res = '\n'.join(map(str,cur.fetchall()))
print(res)
cur.execute("SELECT * FROM users  where userid = max(userid)")
#SELECT *
#    FROM    TABLE
#    WHERE   ID = (SELECT MAX(ID)  FROM TABLE);
results = cur.fetchone()
print(results)