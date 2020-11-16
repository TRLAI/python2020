#第三题
x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))
z = int(input("Enter 3rd Number: "))

MAX = max(x,y,z)
MIN = min(x,y,z)
MID = 0
if MIN < x <MAX:
    MID = x
elif MIN < y <MAX:
    MID = y
elif MIN < z <MAX:
    MID = z
print(MIN,MID,MAX)
