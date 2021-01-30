import numpy as np 
'''
计算欧氏距离【也就是空间中两个点之间的距离】
'''

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# 算出对应点的差的平方之和，对这个和求算数平方根。
op1 = np.sqrt(np.sum(np.square(vector1-vector2)))
# 直接调用numpy的方法。
op2 = np.linalg.norm(vector1-vector2)

print(op1, op2)

from collections import namedtuple
from math import sqrt
Point = namedtuple('Point', ['x', 'y', 'z'])


class Vector(Point):
    def __init__(self, p1, p2, p3):
        super(Vector).__init__() # 等价于 super().__init__(p1, p2, p3)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    # 魔术方法
    # ，当日常执行a-b时，实际调用了sub方法：
    # ，a.__sub__(b)，这里重写了作为减法时的方法
    # 。这里相当于定义了这样一个类，当：两个类的实例发生减法运算时，执行下列方法。
    def __sub__(self, other):
        tmp = (self.p1 - other.p1)**2 + (self.p2 - other.p2)**2 + (self.p3 - other.p3)**2
        return sqrt(tmp)
    
p1 = Vector(8, 2, 3)
p2 = Vector(4, 5, 6)

print(p1 - p2)