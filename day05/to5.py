import time
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
time.sleep(1)   #暂停一秒
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))