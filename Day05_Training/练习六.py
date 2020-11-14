for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            s1 = x*100+y*10+z
            s2 = pow(x,3)+pow(y,3)+pow(z,3)
            if s1 == s2:
                print(s1)
