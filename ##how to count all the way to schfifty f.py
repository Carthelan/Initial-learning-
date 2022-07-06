nterms = int(input("How many terms?"))
n1, n2 = 0, 1
total_n = 0
end_term = nterms - total_n
if nterms > 15:
    print("bro that's too much")
else: 
    print("fibonacci sequence:")
    while n1 < 10000000 and end_term >= 0:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth 
        total_n =+ 1
       