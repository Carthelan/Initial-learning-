## Goldbach's Conjecture
## everything is a sum of two primes

## calculate primes up to a certain point 
## function to test what two numbers can add up to that 
## iterate through list. First number + first, 2nd, 3rd -> last entry
    ## 2nd + 2nd, 3rd, 4th -> last entry

factors = []
Primes = []
max_len = 3

Number = 1

x = 0
y = x + 1
        

def pos_1(x):
    Prime_Nums[x]

def pos_2(y):
    Prime_Nums[y]

def print_factors(Number):
    for i in range(1, Number):
        if Number % i == 0:
            factors.append(i)
while True:
    print_factors(Number)
    if len(factors) <= 1:
        Primes.append(Number)
        factors.clear()
    else:  
        factors.clear()
    if len(Primes) == max_len:
        print(Primes)
        break
    Number = Number + 1
Prime_Nums = map(int, Primes)
print(Prime_Nums[0])