# -*-coding:utf-8-*-
'''
字符串找出所有整数并输出
'''
import re
def str_find_int():
    f = re.findall('(\d+)',s)
    print(f)

#把列表的数据合并成一个字符串，从小到大输出
def list_to_int():
    list = ['1244', '3565']
    str = ''.join(list)
    sort = sorted(str,key = lambda x:int(x))
    print(sort)


if __name__ == '__main__':
    s='sfsfa1244dfsd3565dfsfs'
    list_to_int()

