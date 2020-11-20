a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))
if a > b > c:
    print(c,b,a)
elif a > c > b:
    print(b,c,a)
elif b > a > c:
    print(c,a,b)
elif b > c > a:
    print(a,c,b)
elif c > a > b:
    print(b,a,c)
else:
    print(a,b,c)