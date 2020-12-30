import sqlite3

conn = sqlite3.connect('OSUdatabase.db')
print('创建成功')
c = conn.cursor()
c.execute('''CREATE TABLE FOSU
        (RANK INT PRIMARY KEY   NOT NULL,
        COUNTRY      CHAR(50)   NOT NULL,
        RANKSCORE    CHAR(50)   NOT NULL,
        AVGSCORE     CHAR(50)   NOT NULL
        );''')
print('表已创建')
conn.commit()
conn.close()