#输入半径，计算圆的周长和面积

import math
'''
导入math库
'''

r = float(input("请输入半径："))

c = 2 * math.pi * r
s = math.pi * r * r
print("当半径为:%.2f时"%r)
print("圆的周长为:%.2f"%c)
print("面积为:%.2f"%s)
