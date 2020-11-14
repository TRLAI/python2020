for i in range(100,1000):
    bai=i//10
    shi=(i-bai*100)//10
    ge=i%10
    if pow(bai,3)+pow(shi,3)+pow(ge,3)==i:
        print(i)
