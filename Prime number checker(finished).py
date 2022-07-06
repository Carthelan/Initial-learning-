"""prime number checker"""
num = int(input("Up to which number?: "))

print("All primes from 0 to ", num, "are: ")

for num in range(0, num + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, "is prime")
