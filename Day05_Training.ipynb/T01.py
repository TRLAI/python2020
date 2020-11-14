count=0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
                if (x!=y) and (y!=z) and (z!=x):
                    print("%d%d%d" %(x,y,z))
                    count+=1
print("1~4四个数字能组成",count,"个互不相同且无重复数字的三位数。")
