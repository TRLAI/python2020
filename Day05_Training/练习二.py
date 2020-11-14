arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
while(1):
    i = int(input('请输入当月利润：'))
    if i == 0:
        break
    result = 0
    for idx in range(0,6):
        if i > arr[idx]:
            result += (i-arr[idx])*rat[idx]
            i = arr[idx]
    print("应发放奖金为：",result)
