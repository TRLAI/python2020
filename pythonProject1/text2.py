#第二题
i = float(input('请输入利润:'))
lr = (100000,200000,400000,600000,1000000)
tc = (0.1,0.075,0.05,0.03,0.015,0.01)
sum = 0
if i >= lr[4]:
    sum += (i - lr[4]) * tc[5]
    i = lr[4]
if lr[3] < i <= lr[4]:
    sum += (i - lr[3]) * tc[4]
    i = lr[3]
if lr[2] < i <= lr[3]:
    sum += (i - lr[2]) * tc[3]
    i = lr[2]
if lr[1] < i <= lr[2]:
    sum += (i - lr[1]) * tc[2]
    i = lr[1]
if lr[0] < i <= lr[1]:
    sum += (i - lr[0]) * tc[1]
    i = lr[0]
if i <= lr[0]:
    sum += i*tc[0]
print('应发奖金为:%.2f' %sum)