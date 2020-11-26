import math
import random

def oneDcurve(x):
    return (1 / pow( math.tan(x), 1/3 ))

box_count = 0
area_count = 0

x_min = 0.1
x_max = 1.5

y_min = 0
y_max = 2.2

box_area = (x_max - x_min) * (y_max - y_min)

steps = 5000000

while box_count < steps:
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    if y < oneDcurve(x):
        area_count += 1
    box_count += 1
    
func_area = (area_count / box_count) * box_area
    
print(func_area)