## Goldbach's Conjecture
## everything is a sum of two primes

## ~~calculate primes up to a certain point~~
## ~~function to test what two numbers can add up to that~~
## ~~iterate through list. First number + first, 2nd, 3rd -> last entry
    ## 2nd + 2nd, 3rd, 4th -> last entry~~


Primes = [1, 2]
num_list = []
goldbach_Dict = {}

def writeToDict(val, factor1, factor2):
    goldbach_Dict[val] = (f"{factor1} + {factor2}")
 
for n in range(1, 51):
    num_list.append(n)
    
for i in num_list:
    for j in range(2, i):
        if (i % j) == 0:
            break
        else: 
            Primes.append(i) 
            break

for m in num_list:
    for k in Primes:
        for l in Primes:
            if (k + l) < m:
                break
            if (k + l) == m:
                writeToDict(m, l, k)

new_line = "/n"
with open(r"C:\Users\Klill\OneDrive\Desktop\goldbach conjecture.txt", "w") as file:
    for k, v in goldbach_Dict.items():
        file.write(f"{k}: {v}  ")
print(goldbach_Dict)