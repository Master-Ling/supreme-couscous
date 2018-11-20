# coding=utf-8
# author Lingzi time 2018/11/19

import random
"""
示例

change函数
combi = ['otu2',3]
change后得 {'otu2': [1, 1, 1]}

deal函数
ranlist = [1,3,5]
orilist = {'b0':[1,1,1],'b1':[1,1,1,1],'b2':[1,1]}
deal后得 {'b0':[1],'b1':[1,1,1],'b2':[1,1]}

"""

# 读取数据
file = open(r'G:\SRTP\2018\数据处理\样本数.txt')


# 规范格式change函数
def change(combi):
    l1 = {}
    l2 = []
    for c in range(combi[1]):
        l2.append(1)
    l1.update({combi[0]: l2})
    return (l1)


# 删除对应随机数deal函数
def deal(orilist, ranlist):
    n = 0
    for m in orilist:
        n = n + len(orilist[m])
        for x in ranlist:
            if n >= x:
                orilist.update({m: orilist[m][1:]})
                ranlist = ranlist[1:]
            else:
                break
    return()


# 调用函数
total = file.read()  # 读取并分栏
lines = total.split('\n')

olist = random.sample(range(1,28321),8321)  # 随机数表
rlist = sorted(olist)  # 排序随机数表

orinlist={}  # orinlist为最终字典

for i in range(len(lines)-1):  # 形成orilist orinlist
    z = str(lines[i]).split('\t')
    m = []
    m.append(z[0])
    m.append(int(z[5]))
    x = change(m)
    orinlist.update(x)

deal(orinlist, rlist)

final=[]  # 计数
for m in orinlist:
    final.append(len(orinlist[m]))

print(orinlist.keys())
print(final)
