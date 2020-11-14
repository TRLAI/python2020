h = 100 
times = 10 
height = []
for i in range(2,times+1):
    h /=2
    height.append(h)
print(sum(height)*2+100)
print(min(height)/2)
