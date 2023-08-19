Num = 0
factors = []
primes = []
while True:
    Num = Num + 1
    if Num <= 1:
        print(f"{Num} is not a prime number")
    else:
        for factor in range(2, Num):
            if Num % factor == 0:
                factors.append(factor)
        if len(factors) == 0:
            primes.append(Num)
            print(primes)
            factors.clear
