import csv
import sqlite3


# 数据库的路径
database_path = "C:/Users/hrzhe/Documents/课程/大一下/可视化/" \
                "raw_data.db"
# 存放数据集的文件夹
dataset_dir = "C:/Users/hrzhe/Documents/课程/大一下/可视化/Datasets/"
# 数据集的名称
dataset_name = "ConsumerPriceIndices_E_All_Data.csv"
# 存放表名，不可包含空格
tabel_name = "consumer_price_index"

# 依次存放字段名称，不可包含空格
fields = ["Area_Code","Area_Code_M49","Area","Item_Code","Item","Element_Code","Element","Months_Code","Months","Unit"]
for i in range(2000, 2023):
    fields.append("Y" + str(i))
    fields.append("Y" + str(i) + "F")

# 依次存放字段数据类型
t = []

types = []
for i in t:
    if i == 0:
        types.append("text")
    elif i == 1:
        types.append("integer")
    elif i == 2:
        types.append("real")

conn = sqlite3.connect(database_path)
c = conn.cursor()

sql_create = "CREATE TABLE IF NOT EXISTS " + tabel_name + " ("
for i in range(len(fields)):
    sql_create += fields[i] + " " + types[i] + ","
sql_create = sql_create[:-1] + ")"
c.execute(sql_create)

sql_insert = "INSERT INTO " + tabel_name + " VALUES ("
for i in range(len(fields)):
    sql_insert += "?,"
sql_insert = sql_insert[:-1] + ")"

with open(dataset_dir + dataset_name) as fid:
    cr = csv.DictReader(fid)
    for row in cr:
        values = (lambda *args: args)(*row.values())[:len(fields)] # type: ignore
        c.execute(sql_insert, values)

conn.commit()
conn.close()
