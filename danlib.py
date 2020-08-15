# 这是一个lib，下次更新删除主代码含有弹幕爬取的部分并用lib代替

# getdanmuku(cid_input)只允许输入cid数字
# 它会爬取弹幕文件并返回一个弹幕文件完整路径，且在目录生成文件
# 默认是以cid命名的csv文件

# list(file_path, user_count)需要指定文件路径/文件名和想查询的列数
# 这个能查询单个弹幕的信息，它会把原始弹幕行处理后返回一个列表，原文件不受影响
# 如果遇到未知类型弹幕，则会返回原始信息，原始信息不会处理发送时间，时间戳，颜色等数值
# 但是，如果要做监视，最好用上时间戳，所以这种情况请自行修改代码，使其不处理时间戳
# 可以嵌套getdanmuku()，但是重复查询则不推荐

# listall(file_path)只需要指定文件路径
# 这个会以元组的形式返回所有弹幕消息，这些消息同样被处理，key为序号
# 同样，如果遇到未知类型弹幕，则会返回原始信息，也建议做监视的同学改原始代码
# 可以嵌套getdanmuku()，但是重复查询则不推荐

import csv
import os
import requests
import time
from bs4 import BeautifulSoup


class DanmukuError(Exception):
    pass


def getdanmuku(cid_input):
    try:
        if str(cid_input).isdigit():
            url = str('http://comment.bilibili.com/' + str(cid_input) + '.xml')
            file_name = str(str(cid_input) + '.csv')
        else:
            raise DanmukuError('你只能输入cid')

        if os.path.exists(file_name):
            user_input = input(str(os.path.abspath(file_name)) + '已经存在，更新它吗？[y/n]:')
            while True:
                user_input = user_input.lower()
                if user_input == 'yes' or user_input == 'y':
                    bvIndex = url.find('BV')
                    id = url[bvIndex:]
                    rr = requests.get(url=url)
                    rr.encoding = 'uft-8'
                    soup = BeautifulSoup(rr.text, 'lxml')
                    danmu_info = soup.find_all('d')
                    all_info = []
                    all_text = []

                    for i in danmu_info:
                        all_info.append(i['p'])
                        all_text.append(i)
                    f = open('danmu_info.csv', 'w', encoding='utf-8')
                    csv_writer = csv.writer(f)

                    for i in all_info:
                        i = str(i).split(',')
                        csv_writer.writerow(i)
                    f.close()

                    f = open('danmu_text.csv', 'w', encoding='utf-8')
                    csv_writer = csv.writer(f)

                    for i in all_text:
                        csv_writer.writerow(i)
                    f.close()

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
                    file_final = open(file_name, 'w', encoding='utf-8')

                    for line in file1.readlines():
                        danmuku = str(line)[0:int(len(line)) - 1]
                        danmuku_list.append(str(danmuku))

                    count = 0

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

                    if int(os.path.getsize(file_name)) == 0:
                        os.remove(file_name)
                        raise DanmukuError('cid错误，检查cid是否正确')
                    else:
                        if os.path.exists(file_name):
                            print(os.path.abspath(file_name))
                            return os.path.abspath(file_name)
                        else:
                            raise DanmukuError('弹幕文件在生成期间被删除或者程序出错')
                    break
                elif user_input == 'no' or user_input == 'n':
                    return os.path.abspath(file_name)
                    break
                else:
                    user_input = input(str(os.path.abspath(file_name)) + '已经存在，更新它吗？[y/n]:')
        else:
            bvIndex = url.find('BV')
            id = url[bvIndex:]
            rr = requests.get(url=url)
            rr.encoding = 'uft-8'
            soup = BeautifulSoup(rr.text, 'lxml')
            danmu_info = soup.find_all('d')
            all_info = []
            all_text = []

            for i in danmu_info:
                all_info.append(i['p'])
                all_text.append(i)
            f = open('danmu_info.csv', 'w', encoding='utf-8')
            csv_writer = csv.writer(f)

            for i in all_info:
                i = str(i).split(',')
                csv_writer.writerow(i)
            f.close()

            f = open('danmu_text.csv', 'w', encoding='utf-8')
            csv_writer = csv.writer(f)

            for i in all_text:
                csv_writer.writerow(i)
            f.close()

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
            file_final = open(file_name, 'w', encoding='utf-8')

            for line in file1.readlines():
                danmuku = str(line)[0:int(len(line)) - 1]
                danmuku_list.append(str(danmuku))

            count = 0

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

            if int(os.path.getsize(file_name)) == 0:
                os.remove(file_name)
                raise DanmukuError('cid错误，检查cid是否正确')
            else:
                if os.path.exists(file_name):
                    print(os.path.abspath(file_name))
                    return os.path.abspath(file_name)
                else:
                    raise DanmukuError('弹幕文件在生成期间被删除或者程序出错')


    except Exception as e:
        print(e)


def list(file_path, user_count):
    if os.path.exists(file_path):
        pass
    else:
        raise DanmukuError('弹幕文件不存在')

    file_path = open(str(file_path), 'r', encoding='utf-8')

    blank_count = 0
    user_count = int(user_count)

    try:
        for line in file_path.readlines():
            if blank_count != user_count:
                blank_count += 1
            else:
                raw_mode = False
                def_list = []

                line = line.split(',')

                # 整理发送时间
                send_time_left = int(str(line[0]).split('.')[0])
                send_time_right = int(str(line[0]).split('.')[1])

                hour = send_time_left // 3600
                temp_1 = send_time_left % 3600
                minu = temp_1 // 60
                sec = temp_1 % 60
                if len(str(hour)) == 1:
                    hour = str('0') + str(hour)
                else:
                    pass
                if len(str(minu)) == 1:
                    minu = str('0') + str(minu)
                else:
                    pass
                if len(str(sec)) == 1:
                    sec = str('0') + str(sec)
                else:
                    pass
                send_time_video = str(('%s:%s:%s.%s') % (hour, minu, sec, send_time_right))
                def_list.append(send_time_video)

                # 整理弹幕类型
                if int(line[1]) == 1:
                    danmuku_type = ('滚动弹幕')
                elif int(line[1]) == 4:
                    danmuku_type = ('底部弹幕')
                elif int(line[1]) == 5:
                    danmuku_type = ('顶部弹幕')
                elif int(line[1]) == 6:
                    danmuku_type = ('逆向弹幕')
                elif int(line[1]) == 7 and int(line[5]) == 0:
                    danmuku_type = ('特殊弹幕')
                elif int(line[1]) == 7 and int(line[5]) == 1:
                    danmuku_type = ('精确弹幕')
                elif int(line[1]) == 9 and int(line[5]) == 2:
                    danmuku_type = ('BAS弹幕')
                else:
                    raw_mode = True

                if raw_mode:
                    pass
                else:
                    def_list.append(danmuku_type)

                # 字号不需要整理
                def_list.append(str(line[2]))

                # 整理颜色
                color = str(hex(int(line[3])))[2:]
                def_list.append(color)

                # 转换时间戳
                timestamp = int(line[4])
                time_send = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timestamp)))
                def_list.append(time_send)

                # 整理弹幕池
                if int(line[5]) == 0:
                    danmuku_pool = '普通弹幕池'
                elif int(line[5]) == 1 or int(line[5]) == 2:
                    danmuku_pool = '特殊弹幕池'
                else:
                    raw_mode = True

                if raw_mode:
                    pass
                else:
                    def_list.append(danmuku_pool)

                # 用户ID和rowID不用整理
                def_list.append(str(line[6]))
                def_list.append(str(line[7]))

                # 调整发送内容
                send_what = str(line[8])
                def_list.append(send_what[0:len(send_what) - 1])

                if raw_mode:
                    return line
                else:
                    return def_list
                break

    except Exception as e:
        print(e)

    finally:
        file_path.close()


def listall(file_path):
    if os.path.exists(file_path):
        pass
    else:
        raise DanmukuError('弹幕文件不存在')

    file_path = open(str(file_path), 'r', encoding='utf-8')

    blank_count = 0

    try:
        return_thing = {}
        for line in file_path.readlines():
            raw_mode = False
            def_list = []

            line = line.split(',')

            # 整理发送时间
            send_time_left = int(str(line[0]).split('.')[0])
            send_time_right = int(str(line[0]).split('.')[1])

            hour = send_time_left // 3600
            temp_1 = send_time_left % 3600
            minu = temp_1 // 60
            sec = temp_1 % 60
            if len(str(hour)) == 1:
                hour = str('0') + str(hour)
            else:
                pass
            if len(str(minu)) == 1:
                minu = str('0') + str(minu)
            else:
                pass
            if len(str(sec)) == 1:
                sec = str('0') + str(sec)
            else:
                pass
            send_time_video = str(('%s:%s:%s.%s') % (hour, minu, sec, send_time_right))
            def_list.append(send_time_video)

            # 整理弹幕类型
            if int(line[1]) == 1:
                danmuku_type = ('滚动弹幕')
            elif int(line[1]) == 4:
                danmuku_type = ('底部弹幕')
            elif int(line[1]) == 5:
                danmuku_type = ('顶部弹幕')
            elif int(line[1]) == 6:
                danmuku_type = ('逆向弹幕')
            elif int(line[1]) == 7 and int(line[5]) == 0:
                danmuku_type = ('特殊弹幕')
            elif int(line[1]) == 7 and int(line[5]) == 1:
                danmuku_type = ('精确弹幕')
            else:
                raw_mode = True

            if raw_mode:
                pass
            else:
                def_list.append(danmuku_type)

            # 字号不需要整理
            def_list.append(str(line[2]))

            # 整理颜色
            color = str(hex(int(line[3])))[2:]
            def_list.append(color)

            # 转换时间戳
            timestamp = int(line[4])
            time_send = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timestamp)))
            def_list.append(time_send)

            # 整理弹幕池
            if int(line[5]) == 0:
                danmuku_pool = '普通弹幕池'
            elif int(line[5]) == 1 or int(line[5]) == 2:
                danmuku_pool = '特殊弹幕池'
            else:
                raw_mode = True

            if raw_mode:
                pass
            else:
                def_list.append(danmuku_pool)

            # 用户ID和rowID不用整理
            def_list.append(str(line[6]))
            def_list.append(str(line[7]))

            # 调整发送内容
            send_what = str(line[8])
            def_list.append(send_what[0:len(send_what) - 1])

            if raw_mode:
                return_thing[str(blank_count)] = line
            else:
                return_thing[str(blank_count)] = def_list
                def_list = []

            blank_count += 1

    except Exception as e:
        print(e)

    finally:
        file_path.close()
        return return_thing


def count(file_path):
    try:

        if os.path.exists(file_path):
            pass
        else:
            no_file = True
            raise DanmukuError('弹幕文件不存在')

        file_path = open(str(file_path), 'r', encoding='utf-8')

        blank_count = 0

        for line in file_path.readlines():
            blank_count += 1
        file_path.close()
        return blank_count

    except Exception as e:
        print(e)
