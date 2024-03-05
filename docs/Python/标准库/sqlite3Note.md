
### 连接数据库
```py
# 若不存在则会创建
conn = sqlite3.connect('example.db')
```

<br>

### 创建游标
```py
c = conn.cursor()
```

<br>

### 创建表单
```py
c.execute('''CREATE TABLE IF NOT EXISTS table_name
             (date text, trans text, symbol text, qty real, price real)''')
```

<br>

### 插入数据
```py
c.execute('''INSERT INTO table_name VALUES
             ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)''')

sql = "INSERT INTO table_name VALUES (?,?,?,?,?)"
c.execute(sql, (data, trans, symbol, qty, price))
```

<br>

### 查询数据
```py
for row in c.execute('SELECT * FROM table_name ORDER BY price'):
    print(row)
```

<br>

### 提交并保存
```py
conn.commit()
conn.close()
```
