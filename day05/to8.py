far = []
high = 100
for i in range(1,11):
    if i == 1:
        far.append(high)
    else:
        far.append(high * 2)
    high = high / 2

print("经过的总距离为：",sum(far))
print("第十次反弹的高度为：",high)