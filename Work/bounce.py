# bounce.py
#
# Exercise 1.5

#!/usr/bin/env python3

height = 100
count = 0

for i in range(10):
    
    height *= 0.6
    count += 1

    print(count, round(height, 4))

