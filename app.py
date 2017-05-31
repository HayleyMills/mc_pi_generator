import math
from random import random as rand

counter_in = 0
counter_out = 0

for _ in range(1000000):
    x = rand()
    y = rand()

    a = math.sqrt((x * x) + (y * y))

    if a < 1:
        counter_in += 1
    else:
        counter_out += 1

quarter_area = float(counter_in) / (counter_out+counter_in)
circle_area = quarter_area*4

print "%.16f" % circle_area