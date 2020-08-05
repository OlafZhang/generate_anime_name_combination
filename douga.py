#连接数据库，并检索两个表的内容数量
#用户发出一次请求，就在内容数量范围内挑出一个人物和一个物品，并组合，即为结果
#灵感来自docker中对容器的默认取名方式
#反转值为0时，对应中国/日本等国家地区的人名命名方式
#反转值为1时，对应欧美等国家地区的人名命名方式
#反转值为2时，则只有名字
#反转值为100时，对应中国/日本等国家地区的人名命名方式，但短名字模式使用姓而不是名
#反转值为101时，对应欧美等国家地区的人名命名方式，但短名字模式使用姓而不是名
import pymysql,random,time
def generate_name():
    #短名字开关，真时不会输出姓
    short_name = False
    #数据库配置，请先配置，确保有数据库
    mysql_host = ("localhost")
    mysql_name = ("")
    mysql_pass = ("")
    mysql_db = ("anime_name")
    db = pymysql.connect(mysql_host ,mysql_name ,mysql_pass ,mysql_db )
    #检索名字数量的游标
    count_cursor = db.cursor()
    count_name = count_cursor.execute("select count(*) from NAME")
    count_name_data = count_cursor.fetchone()
    name_number = int(count_name_data[0])
    count_cursor.close()
    #检索物品数量的游标
    count_cursor = db.cursor()
    count_item = count_cursor.execute("select count(*) from ITEM")
    count_item_data = count_cursor.fetchone()
    item_number = int(count_item_data[0])
    count_cursor.close()
    #挑出范围内的任何一个名字
    name_cursor = db.cursor()
    random_name_count = int(random.randint(0,int(name_number) - 1))
    name_data_cursor = name_cursor.execute("select * from NAME limit " + str(random_name_count) + ",1")
    name_data = name_cursor.fetchone()
    family_name = str(name_data[1])
    last_name = str(name_data[2])
    reverse_bool = str(name_data[3])
    if short_name:
        if str(reverse_bool) == str('100') or str(reverse_bool) == str('101'):
            name = str(family_name)
        else:
            name = str(last_name)
    else:
        if str(reverse_bool) == str('1') or str(reverse_bool) == str('101'):
            name = str(last_name + '·' + family_name)
        elif str(reverse_bool) == str('2'):
            name = str(last_name)
        else:
            name = str(family_name + last_name)
    name_cursor.close()
    #挑出范围内的任何一个物品
    item_cursor = db.cursor()
    random_item_count = int(random.randint(0,int(item_number) - 1))
    item_data_cursor = item_cursor.execute("select * from ITEM limit " + str(random_item_count) + ",1")
    item_data = item_cursor.fetchone()
    item = str(item_data[0])
    item_cursor.close()
    #合并输出
    final_name = (name + '的' + item)
    return final_name
while True:
    for i in range(1,21):
        print(generate_name())
    time.sleep(10)

