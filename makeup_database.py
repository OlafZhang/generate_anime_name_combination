# 这个是用来整理数据库的，已经集成到import_name.py，可以不下载此文件
# 早期遇到了录入数据库跳号的问题，现在已经修复
# 如果仍然遇到这个问题，import_name.py会自动整理
import pymysql

# 物品列表文件路径
file_name = ('item.txt')
# 数据库配置，请先配置，确保有数据库
mysql_host = ("localhost")
mysql_name = ("root")
mysql_pass = ("123456")
mysql_db = ("anime_name")
db = pymysql.connect(mysql_host, mysql_name, mysql_pass, mysql_db)
makeup_cursor = db.cursor()
last_id_command = str('select * from name order by NO desc limit 0,1')
last_id_exc = makeup_cursor.execute(last_id_command)
find_id_data = makeup_cursor.fetchone()
last_id = int(find_id_data[0])
makeup_cursor.close()


def count_name():
    count_cursor = db.cursor()
    count_item = count_cursor.execute("select count(*) from NAME")
    count_item_data = count_cursor.fetchone()
    item_number = int(count_item_data[0])
    count_cursor.close()
    return item_number


no_data_list = []
fix_data_list = []
if int(last_id) != int(count_name()):
    print("[*]数据库需要整理,正在整理")
    for id in range(1, int(last_id) + 1):
        search_name = str(('select * from name where NO = %d') % (id))
        find_cursor = db.cursor()
        try:
            find_item = find_cursor.execute(search_name)
            find_item_data = find_cursor.fetchone()
            item_number = int(find_item_data[0])
            find_cursor.close()
            fix_data_list.append(int(id))
        except:
            find_cursor.close()
            no_data_list.append(int(id))
    count = 0
    for i in range(no_data_list[0], int(count_name()) + 1):
        count += 1
    blank_list = []
    for i in range(0, int(count)):
        blank_list.append(no_data_list[i])
    no_data_list = blank_list
    blank_list = []
    last_var = 0
    while len(fix_data_list) != 0:
        if int(fix_data_list[0]) - last_var == 1:
            last_var = fix_data_list[0]
            fix_data_list.pop(0)
        else:
            break
    for i in range(0, len(fix_data_list)):
        update_name = str(('update name set NO = %s where NO = %s') % (str(no_data_list[i]), str(fix_data_list[i])))
        try:
            update_cursor = db.cursor()
            update_item = update_cursor.execute(update_name)
            db.commit()
            print(("[*]在处理第%s个数据") % (str(fix_data_list[i])))
        except Exception as e:
            print(("[*]在处理第%s个数据遇到了错误:%s") % (str(fix_data_list[i]),str(e)))
        update_cursor.close()
        if fix_data_list[i] == fix_data_list[-1]:
            break
        else:
            pass
    print("[*]数据库整理完毕")
else:
    print("[*]数据库不需要整理")
