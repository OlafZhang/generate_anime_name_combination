#这个程序可以帮助你录入人物
#物品列表应该使用UTF-8编码，使用姓+名+反转值
#即使不符合中国/日本姓名规则，也要先输入姓
#可以只输入名字，或不输入反转值

import pymysql,os,time
#人物列表文件路径
file_name = ('name.txt')
#数据库配置，请先配置，确保有数据库
mysql_host = ("localhost")
mysql_name = ("")
mysql_pass = ("")
mysql_db = ("anime_name")
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
print("！！！！！！！！！！！！！！！")
print("[*]请注意！姓名列表文件不应该用全角逗号分隔！")
print("[*]不要故意只输入反转值！")
print("[*]逗号数量大于2的行会被跳过！")
print("[*]如果你熟知了这一点并确认无误后，10秒后开始...")
time.sleep(10)
print("[*]构建浮标，开始录入")
def count_name():
    count_cursor = db.cursor()
    count_item = count_cursor.execute("select count(*) from NAME")
    count_item_data = count_cursor.fetchone()
    item_number = int(count_item_data[0])
    count_cursor.close()
    return item_number
first_count = int(count_name())
reverse_list = ["0","1","2","100","101"]
for line in name_list_file.readlines():
    line = line.strip('\n')
    new_name = str('"' + str(line) + '"')
    line = line.split(',')
    #默认值
    first_count += 1
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
print("[*]导入完成")
print("[*]已经导入：" + str(new_name_count))
print("[*]重复数据：" + str(duplicate_name_count))
print("[*]错误数据：" + str(error_name_count))
print("[*]文件内人物数量：" + str(error_name_count + new_name_count + duplicate_name_count))
print("--------------------")
print("[*]当前数据库人物数量：" + str(count_name()))
print("--------------------")
print("10秒后自动退出...")

