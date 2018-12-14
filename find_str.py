# -*-coding:utf-8-*-
'''
找出一个字符串内包含了几个另一个字符串
eg:abcdsfabc   包含几个abc
'''

def find_expect_str(s):

    t='abc'
    if s.find(t)>=0:
        num = s.count(t)
        return num
    else:
        return False

if __name__ == "__main__":
    find_expect_str('ababcdfggabc')