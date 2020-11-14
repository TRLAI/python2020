h=100
time=10
height=[]
for i in range(2,time+1):
    h/=2
    height.append(h)
print(sum(height)*2+100)
print(min(height)/2)

