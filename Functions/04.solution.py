import math

def circle(r):
    area = math.pi * r * r
    circumference = 2 * math.pi * r
    return area, circumference

a, c = circle(2)
print("area:", a, "circumference:", c)
