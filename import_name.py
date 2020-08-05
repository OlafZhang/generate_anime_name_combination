#这个程序可以帮助你录入人物
#物品列表应该使用UTF-8编码，使用姓+名+反转值
#即使不符合中国/日本姓名规则，也要先输入姓
#可以只输入名字，或不输入反转值

import pymysql,os,time
#人物列表文件路径
file_name = ('name.txt')
#数据库配置，请先配置，确保有数据库
mysql_host = ("localhost")
mysql_name = ("root")
mysql_pass = ("123456")
mysql_db = ("anime_name")
#忽视警告，真时不显示警告，且立刻开始录入
skip_error = True
name_list_file = open(file_name, 'r', encoding='utf-8')
new_name_count = 0
error_name_count = 0
duplicate_name_count = 0
print("--------------------")
print("[*]自动录入人物工具")
print("--------------------")
print("[*]列表文件：" + os.path.realpath(file_name))
print("[*]正在连接数据库...")
db = pymysql.connect(mysql_host ,mysql_name ,mysql_pass ,mysql_db )
print("[*]成功连接数据库")
if skip_error:
    pass
else:
    print("！！！！！！！！！！！！！！！")
    print("[*]请注意！姓名列表文件不应该用全角逗号分隔！")
    print("[*]不要故意只输入反转值！")
    print("[*]逗号数量大于2的行会被跳过！")
    print("[*]如果你熟知了这一点并确认无误后，10秒后开始...")
    time.sleep(10)
print("[*]构建浮标，开始录入")
print("--------------------")
def count_name():
    count_cursor = db.cursor()
    count_item = count_cursor.execute("select count(*) from NAME")
    count_item_data = count_cursor.fetchone()
    item_number = int(count_item_data[0])
    count_cursor.close()
    return item_number
makeup_count = 0
makeup_error_count = 0
def makeup_database():
    global makeup_count
    global makeup_error_count
    makeup_cursor = db.cursor()
    last_id_command = str('select * from name order by NO desc limit 0,1')
    last_id_exc = makeup_cursor.execute(last_id_command)
    find_id_data = makeup_cursor.fetchone()
    last_id = int(find_id_data[0])
    makeup_cursor.close()
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
                print(("[*]正在处理第%s个数据") % (str(fix_data_list[i])))
                makeup_count += 1
            except:
                print(("[*]在处理第%s个数据遇到了错误") % (str(fix_data_list[i])))
                makeup_error_count += 1
            update_cursor.close()
            if fix_data_list[i] == fix_data_list[-1]:
                break
            else:
                pass
        print("[*]数据库整理完毕")
    else:
        print("[*]数据库不需要整理")
first_count = int(count_name())
reverse_list = ["0","1","2","100","101"]
for line in name_list_file.readlines():
    line = line.strip('\n')
    new_name = str('"' + str(line) + '"')
    line = line.split(',')
    #默认值
    reverse_value = 0
    #判断语句1
    if len(line) == 1:
        family_name = str("")
        last_name = str(line[0])
        reverse_value = 2
    elif len(line) == 2:
        if line[1] in reverse_list:
            reverse_value = int(line[1])
            family_name = str("")
            last_name = str(line[0])
        else:
            family_name = str(line[0])
            last_name = str(line[1])
            reverse_value = 0
    elif len(line) == 3:
        family_name = str(line[0])
        last_name = str(line[1])
        reverse_value = int(line[2])
    else:
        continue
    #判断语句2
    if reverse_value == 0 or reverse_value == 100:
        full_name = str(('"%s%s"') % (family_name, last_name))
    elif reverse_value == 1 or reverse_value == 101:
        full_name = str(('"%s·%s"') % (last_name,family_name))
    elif reverse_value == 2:
        full_name = str(('"%s"') % (last_name))
    else:
        continue
    #查重
    find_cursor = db.cursor()
    if family_name == str(""):
        search_name = str(('select * from name where FAMILY IS NULL and NAME = "%s" and reverse = %d;') % (last_name, reverse_value))
    else:
        search_name  = str(('select * from name where FAMILY = "%s" and NAME = "%s" and reverse = %d;')%(family_name, last_name, reverse_value))
    find_item = find_cursor.execute(search_name)
    try:
        find_item_data = find_cursor.fetchone()
        item_number = int(find_item_data[0])
        find_cursor.close()
        name_exist = True
    except:
        name_exist = False
        find_cursor.close()
    if name_exist:
        duplicate_name_count += 1
        print("[*]已经存在" + full_name)
    else:
        try:
            first_count += 1
            if family_name == str(""):
                new_name = str(('"%s",NULL,"%s",%d')%(first_count, last_name, reverse_value))
            else:
                new_name = str(('"%s","%s","%s",%d') % (first_count, family_name, last_name, reverse_value))
            input_cursor = db.cursor()
            command = str("insert into NAME values(" + new_name + ")")
            input = input_cursor.execute(command)
            input_cursor.close()
            new_name_count += 1
            print("[+]成功添加人物" + full_name )
        except:
            error_name_count += 1
            print("[!]出现未知错误" + full_name)
        finally:
            db.commit()
name_list_file.close()
print("--------------------")
makeup_database()
print("--------------------")
print("[*]导入完成")
print("[*]已经导入：" + str(new_name_count))
print("[*]重复数据：" + str(duplicate_name_count))
print("[*]错误数据：" + str(error_name_count))
print("[*]整理数据：" + str(makeup_count))
print("[*]失败整理：" + str(makeup_error_count))
print("[*]文件内人物数量：" + str(error_name_count + new_name_count + duplicate_name_count))
print("--------------------")
print("[*]当前数据库人物数量：" + str(count_name()))
print("--------------------")
print("10秒后自动退出...")
time.sleep(10)

