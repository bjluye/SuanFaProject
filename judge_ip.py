# -*-coding:utf-8-*-

# 判断IP地址是否有效IP
import re

def judge_ip_1(ip_path):
    s = '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
    compile_ip = re.compile(s)
    print(compile_ip)
    if compile_ip.match(ip_path):
        print("true")
        return True
    else:
        print("false")
        return  False

def judge_ip_2(ip_path):
    if '.' not in ip_path:
        return False
    elif ip_path.count('.') !=3:
        return False
    else:
        flag = True
        list = ip_path.split('.')
        print(list)
        for l in list:
            try:
                one_num = int(l)
                if one_num>=0 and one_num<=255:
                    pass
                else:
                    flag=False
            except:
                flag=False
        return flag




if __name__ == '__main__':
    ip_list = ['', '172.31.137.251', '100.10.0.1000', '1.1.1.1', '12.23.13', 'aa.12.1.2', '12345678', '289043jdhjkbh']
    for str in ip_list:
        if judge_ip_2(str):
            print('{} is 合法的ip'.format(str))
        else:
            print('{} not is 合法的ip'.format(str))


