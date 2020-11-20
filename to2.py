num=input("请输入利润:(单位为万)\n")
num1=float(num)
if num1<=0:
    print("利润应大于零!")
elif num1<=10:
    num2 = num1 * 1.1
    print("奖金为{}万元".format(num2))
elif num1<=20:
    num2 = 10 * 1.1+(num1-10)*1.075
    print("奖金为{}万元".format(num2))
elif num1<=40:
    num2 = 10 * 1.1 + 10 * 1.075+(num1-20)*1.05
    print("奖金为{}万元".format(num2))
elif num1<=60:
    num2 = 10 * 1.1 + 10 * 1.075+ 20 * 1.05+(num1-40)*1.03
    print("奖金为{}万元".format(num2))
elif num1<=100:
    num2 = 10 * 1.1 + 10 * 1.075+ 20 * 1.05 + 20 * 1.03+(num1-60)*1.015
    print("奖金为{}万元".format(num2))
else:
    num2 = 10 * 1.1 + 10 * 1.075+ 20 * 1.05 + 20 * 1.03 + 40 * 1.015+(num1-100)*1.01
    print("奖金为{}万元".format(num2))