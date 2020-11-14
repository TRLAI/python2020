import re
x,y,z=re.split("[ ,.，、|\/]",input("请输入三个数字："))
x,y,z=int(x),int(y),int(z)
maxNum=max(x,y,z)
minNum=min(x,y,z)
print(minNum,x+y+z-maxNum-minNum,maxNum)
