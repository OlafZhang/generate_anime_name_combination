#确保安装bs4,requests,csv,lxml
#只会先写入到文件，然后需要手动运行数据库写入工具
#违规词汇系统仍然在开发
#这个只是套件的一部分，必须配合danmuku_main.py使用
import os,time
import danlib

#这个不是b站播放页面的URL
#使用浏览器的F12开发者工具，查找pagelist?bvid=av号或bv号...格式的文件,其中就有cid
#如果是番剧，查找data?r=loader&cid=，也有cid
#都是xhr，方式为GET
#如果有多分p，注意每个分p的cid都是不同的
#也可以直接去相关网站使用BV号查cid号

cid = 21270514

file_name = danlib.getdanmuku(cid)

file_final = open(file_name, 'r', encoding='utf-8')
name_file = open('name.txt', 'a', encoding='utf-8')
item_file = open('item.txt', 'a', encoding='utf-8')
log_file = open('log.txt', 'a', encoding='utf-8')

timestamp_reading = open('timestamp_bili', 'r', encoding='utf-8')
for line in timestamp_reading.readlines():
    timestamp_old = int(line)
timestamp_reading.close()

name_count = 0
item_count = 0

for line in file_final.readlines():

    new_string = ''
    line = line.split(',')
    user_id = str(line[6])
    timestamp = int(line[4])
    time_send = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timestamp)))
    if int(timestamp) > int(timestamp_old):
        timestamp_old = timestamp
        raw_text = str((line[8])[0:len(str(line[8])) - 1])
        if str(raw_text)[0:2] == '人物':
            if raw_text[2] == ":":
                raw_text = raw_text.split(':')[1]
            elif raw_text[2] == "：":
                raw_text = raw_text.split('：',)[1]
            else:
                pass

            for i in raw_text:
                if i == ':':
                    new_string += ','
                elif i == '：':
                    new_string += ','
                else:
                    new_string += i
            new_string = str(('%s\n')%(new_string))
            name_count += 1
            log = str(("[%s-人物]用户'%s'发送弹幕'%s'\n") % (time_send, user_id, raw_text))
            log_file.write(log)
            name_file.write(str(new_string))

        elif str(raw_text)[0:2] == '物品':
            if raw_text[2] == ":":
                raw_text = raw_text.split(':')[1]
            elif raw_text[2] == "：":
                raw_text = raw_text.split('：',)[1]
            else:
                pass
            new_string = raw_text
            new_string = str(('%s\n')%(new_string))
            item_count += 1
            log = str(("[%s-物品]用户'%s'发送弹幕'%s'\n") % (time_send, user_id, raw_text))
            log_file.write(log)
            item_file.write(str(new_string))
        else:
            continue
    else:
        pass

timestamp_file = open('timestamp_bili', 'w', encoding='utf-8')
timestamp_file.write(str(timestamp))
timestamp_file.close()

if int(name_count) + int(item_count) == 0:
    print(str("[%s-总结]无人发送") % (time_send))
else:
    log = str(("[%s-总结]当前阶段写入%s个人物，%s个物品\n") % (time_send, str(name_count), str(item_count)))
    print(log)
    log_file.write(log)

name_file.close()
item_file.close()
file_final.close()
log_file.close()
os.remove(file_name)

