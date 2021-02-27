import os
try:
    os.unlink('investment.db')
except:
    print('首次建檔')

import sqlite3
conn = sqlite3.connect('investment.db')
cur = conn.cursor()

def show_all_rows(all_rows):
    for row in all_rows:
        print(row)
    print()

# 外幣表
cur.execute('''CREATE TABLE CURRENCY
    (ID integer, CURRENCY text, RATIO real, FLUCTUATION text)''')
conn.commit()
# 外幣表批次新增資料
row_id = 0
fin = open('foreign_currency.txt', 'rt')
lines = fin.readlines()
for line in lines:
    row_id += 1
    currency, ratio, fluctuation = line.split()
    cur.execute("INSERT INTO WORDS VALUES (?, ?, ?, ?)", (row_id, currency, ratio, fluctuation))
conn.commit()    
fin.close()
# 查詢外幣表
cur.execute("SELECT * FROM CURRENCY")
show_all_rows(cur.fetchall())

# 存摺表
cur.execute('''CREATE TABLE PASSBOOK
    (ID integer, ACCOUNT text, DATE text, CURRENCY text, WITHDRAWAL integer, DEPOSIT integer, BALANCE integer)''')
conn.commit()

# 投資者表
cur.execute('''CREATE TABLE INVESTOR
    (ID integer, ACCOUNT text, NAME text, GENDER integer, BIRTH_YEAR integer)''')

conn.close()
