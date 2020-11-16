#第八题
a = 100
b = 1
sum = 0
while  b <= 10:
       sum += a + a/2
       a = a/2
       b += 1
print("总共经过%d米" %sum)
print("第十次反弹%d米" %a)