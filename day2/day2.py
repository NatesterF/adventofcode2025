import math
import re
f=open("input.txt",'r')
ranges_string = f.read()
ranges=ranges_string[:-1].split(",")
print(ranges)
output = 0
for range_string in ranges:
    extremes=range_string.split("-")
    print(extremes)
    start=int(extremes[0]) 
    end=int(extremes[1]) 
    for i in range(start,end+1):
        num_string=str(i)
        n=len(num_string) 
        if re.match(r'^(.+?)\1+$',num_string):
            print(num_string)
            output += i


            


print(output)
