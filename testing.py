import math


f = open("test.txt", "r")
print(f.readline())
for line in f:
    print("dentro del if")
    print(line)