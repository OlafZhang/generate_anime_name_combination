#确保安装bs4,requests,csv,lxml
#只会先写入到文件，然后需要手动运行数据库写入工具
#违规词汇系统仍然在开发
#这个只是套件的一部分，必须配合danmuku_main.py使用
import requests,os,csv,time
from bs4 import BeautifulSoup

#这个不是b站播放页面的URL
#在网上找工具转换一个视频的cid再来替换下面的url的数字
#或者使用使用F12，查找pagelist?bvid=av号或bv号...格式的文件,其中就有cid
#如果有多分p，注意每个分p的cid都是不同的

url = 'http://comment.bilibili.com/1145141919810.xml'

def get_csv(urll):   #请求的方式得到数据jason文件
    bvIndex = url.find('BV')
    id = url[bvIndex:]
    rr=requests.get(url=urll)
    rr.encoding='uft-8'
    soup=BeautifulSoup(rr.text,'lxml')
    danmu_info=soup.find_all('d')
    all_info=[]
    all_text=[]
    for i in danmu_info:
        all_info.append(i['p'])
        all_text.append(i)
    f = open('danmu_info.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(f)
    for i in all_info:
        i=str(i).split(',') #把弹幕信息分隔好
        csv_writer.writerow(i)
    f.close()
    f = open('danmu_text.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["内容"])
    for i in all_text:
        csv_writer.writerow(i)
    f.close()
if __name__=='__main__':
    get_csv(url)


file1 = open('danmu_text.csv', 'r', encoding='utf-8')
file2 = open('danmu_text_output.csv', 'w', encoding='utf-8')
for line in file1.readlines():
    if line == '\n':
        line = line.strip("\n")
    file2.write(line)
file1.close()
file2.close()


file1 = open('danmu_info.csv', 'r', encoding='utf-8')
file2 = open('danmu_info_output.csv', 'w', encoding='utf-8')
for line in file1.readlines():
    if line == '\n':
        line = line.strip("\n")
    file2.write(line)
file1.close()
file2.close()


danmuku_list = []
file1 = open('danmu_text_output.csv', 'r', encoding='utf-8')
file2 = open('danmu_info_output.csv', 'r', encoding='utf-8')
file_final = open('danmuku_final.csv', 'w', encoding='utf-8')
for line in file1.readlines():
    danmuku = str(line)[0:int(len(line)) - 1]
    danmuku_list.append(str(danmuku))
count = 0
danmuku_all_list = []
for line in file2.readlines():
    info = str(line)[0:int(len(line)) - 1]
    final_text = str(info + "," + danmuku_list[count] + "\n")
    file_final.write(final_text)
    count += 1
file1.close()
file2.close()
file_final.close()

os.remove("danmu_info.csv")
os.remove("danmu_text.csv")
os.remove("danmu_info_output.csv")
os.remove("danmu_text_output.csv")

file_final = open('danmuku_final.csv', 'r', encoding='utf-8')
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
os.remove('danmuku_final.csv')

