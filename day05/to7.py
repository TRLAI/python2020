s = input("请输入一行字符:")
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print("英文字母数为%d,空格数为%d,数字数为%d,其他字符数为%d"%(letters,space,digit,others))