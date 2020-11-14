str=input("请输入一行字符串：")
alphaNum=0
spaceNum=0
numbers=0
otherNum=0
for x in str:
    if x.isalpha():
        alphaNum+=1
    elif x.isspace():
        spaceNum+=1
    elif x.isnumeric():
        numbers+=1
    else:
        otherNum +=1
print("英文字母=%d"%alphaNum)
print("空格=%d"%spaceNum)
print("数字=%d"%numbers)
print("其他字符=%d"%otherNum)
