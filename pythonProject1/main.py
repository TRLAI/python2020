# 第一题
num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k):
                print(i,j,k,sep='')
                num += 1
print('总计有%s个' % num)

