tmpStr = input('请输入字符串：')
alphaNum=0
numbers=0
spaceNum=0
otherNum=0
for i in tmpStr:
    if i.isalpha():
        alphaNum +=1
    elif i.isnumeric():
        numbers +=1
    elif i.isspace():
        spaceNum +=1
    else:
        otherNum +=1
print('字母=%d'%alphaNum)
print('数字=%d'%numbers)
print('空格=%d'%spaceNum)
print('其他=%d'%otherNum)
