# 这个程序可以帮助你录入物品
# 物品列表应该使用UTF-8编码，一个物品一行

import os
import pymysql
import time

# 物品列表文件路径
file_name = ('item.txt')
# 数据库配置，请先配置，确保有数据库
mysql_host = ("localhost")
mysql_name = ("root")
mysql_pass = ("123456")
mysql_db = ("anime_name")
item_list_file = open(file_name, 'r', encoding='utf-8')
new_item_count = 0
duplicate_item_count = 0
print("--------------------")
print("[*]自动录入物品工具")
print("--------------------")
print("[*]列表文件：" + os.path.realpath(file_name))
print("[*]正在连接数据库...")
db = pymysql.connect(mysql_host, mysql_name, mysql_pass, mysql_db)
print("[*]成功连接数据库")
print("[*]构建浮标，开始录入")
for line in item_list_file.readlines():
    line = line.strip('\n')
    new_item = str('"' + str(line) + '"')
    try:
        input_cursor = db.cursor()
        command = str("insert into ITEM values(" + new_item + ")")
        input = input_cursor.execute(command)
        input_cursor.close()
        new_item_count += 1
        print("[+]成功添加新物品" + new_item)
    except pymysql.err.IntegrityError:
        duplicate_item_count += 1
        print("[*]已存在物品" + new_item)
    finally:
        db.commit()
item_list_file.close()
print("--------------------")
print("[*]导入完成")
print("[*]已经导入：" + str(new_item_count))
print("[*]重复数据：" + str(duplicate_item_count))
print("[*]文件内物品数量：" + str(duplicate_item_count + new_item_count))
print("--------------------")
count_cursor = db.cursor()
count_item = count_cursor.execute("select count(*) from ITEM")
count_item_data = count_cursor.fetchone()
item_number = int(count_item_data[0])
count_cursor.close()
print("[*]当前数据库物品数量：" + str(item_number))
print("--------------------")
print("10秒后自动退出...")
time.sleep(10)
