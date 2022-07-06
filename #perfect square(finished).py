#perfect square
import math
square_list = []
n = int(input('Which range to test?: '))

for i in range(n+1):
    if math.sqrt(i).is_integer():
                print (i, "is a perfect square")
                square_list.append(i)
                continue
    else:
            print(i, "is not a perfect square")
            continue
print ("done")
print (square_list)