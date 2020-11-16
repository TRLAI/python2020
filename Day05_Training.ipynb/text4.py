#第四题
import copy
a = [1,2,3,4,5]
b = copy.deepcopy(a)
a[0] = 10
print(a)
print(b)