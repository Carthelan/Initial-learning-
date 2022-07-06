#perfect square(print)
import math
df = open("C:\\Users\\Klill\\Documents\\Python\\Python Lists\\perfectsquares.txt", "w")
square_list = []
n = int(input('Which range to test?: '))

for i in range(n+1):
    if math.sqrt(i).is_integer():
                print (i, "is a perfect square")
                if True: 
                        square_list.append(i)
                        df.write(str(i))
                        df.write('\n')
                continue
    else:
            print(i, "is not a perfect square")
            continue
df.close()
print ("done")
print (len(square_list) , "perfect squares")
