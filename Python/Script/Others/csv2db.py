import csv
import sqlite3


# 存放数据集的文件夹
dataset_directory = "C:/Users/hrzhe/Documents/课程/大一下/可视化/Datasets/"
# 数据库的名称
database_name = "database.db"

# 数据集的名称
dataset_name = "Environment_LandCover_E_All_Data.csv"
# 存放表名，如 food_prices，不可包含空格
tabel_name = "population"
# 依次存放列名，不可有空格
columns = ["Area_Code","Area_Code_M49","Area","Item_Code","Item_Code_CPC","Item","Element_Code","Element","Unit","Y2010","Y2010F","Y2011","Y2011F","Y2012","Y2012F","Y2013","Y2013F","Y2014","Y2014F","Y2015","Y2015F","Y2016","Y2016F","Y2017","Y2017F","Y2018","Y2018F","Y2019","Y2019F","Y2020","Y2020F"]
# 依次存放列的数据类型，0代表text，1代表integer，2代表real
t = [1,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]


types = []
for i in t:
    if i == 0:
        types.append("text")
    elif i == 1:
        types.append("integer")
    elif i == 2:
        types.append("real")

conn = sqlite3.connect(dataset_directory + database_name)
c = conn.cursor()

sql_create = "CREATE TABLE IF NOT EXISTS " + tabel_name + " ("
for i in range(len(columns)):
    sql_create += columns[i] + " " + types[i] + ","
sql_create = sql_create[:-1] + ")"
c.execute(sql_create)

sql_insert = "INSERT INTO " + tabel_name + " VALUES ("
for i in range(len(columns)):
    sql_insert += "?,"
sql_insert = sql_insert[:-1] + ")"

with open(dataset_directory + dataset_name) as fid:
    cr = csv.DictReader(fid)
    for row in cr:
        values = (lambda *args: args)(*row.values())[:len(columns)] # type: ignore
        c.execute(sql_insert, values)

conn.commit()
conn.close()
