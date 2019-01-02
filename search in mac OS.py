import urllib.request
import re
import time
import os

#获取座位信息
url = "http://bslc.lib.swjtu.edu.cn/uas/gethtml_zuowei.jsp?callback=?"
response = urllib.request.urlopen(url)
response = str(response.read())

#爬取指定位置
def search_count(response, area):
    a = response.find(area)
    b = response.find("UsableCount", a)
    c = response.find("Name", b)
    if c == -1:
        c = None
    usablecount = re.search(r'[0-9]\d*', response[b:c])
    return usablecount.group()


#输出
print('全部区域：2B1,2B2,3A1,3A2,3A3,3B1,3B2,4A1,4B1,4B3,4C,5A1,5B1,5B2')
print('输入想要查询的楼层名称，以空格隔开')
inint = input()
b = inint.split()
seats = []
print(time.strftime('%H:%M:%S',time.localtime(time.time())))
for i in range(len(b)):
    a = b[i]
    area = a[0] + '-' + a[1:]
    seatcount = int(search_count(response, area))
    seats.append(seatcount)
    print("{}楼{}区的座位情况：{}".format(a[0],a[1:],seatcount))

print("是否进入抢座模式，是1/否0")
a = int(input())
if a == 1:
    while a == 1:
        response = urllib.request.urlopen(url)
        response = str(response.read())
        seats = []
        for i in range(len(b)):
            aa = b[i]
            area = aa[0] + '-' + aa[1:]
            seatcount = int(search_count(response, area))
            seats.append(seatcount)
        print(time.strftime('%H:%M:%S',time.localtime(time.time())))
        for i in range(len(seats)):
            if seats[i] >= 1:
                os.system("say {}".format(b[i]))
                print("{}区有座位".format(b[i]))
                a = 0
        time.sleep(1)
if a == 0:
    print("end")
