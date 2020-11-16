#第七题
a = input('请输入字符串:')
zimu = 0
shuzi = 0
kongge = 0
qita = 0
for i in a:
    if i >='a' and i <= 'z' or i >= 'A' and i <= 'Z':
        zimu += 1
    elif i in '0123456789':
        shuzi += 1
    elif i ==' ':
        kongge += 1
    else:
        qita += 1
        print("字母个数%d " %zimu)
        print("数字个数%d " %shuzi)
        print("空格个数%d " %kongge)
        print("其他个数%d " %qita)