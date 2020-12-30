import sqlite3

conn = sqlite3.connect("mydate.db")
c = conn.cursor()
print("连接成功")
result = c.execute("select * from FOSU;")
str1 = str()
for i in result:
    str1 = i[0]+str(i[1])+str1
    print(str1)
