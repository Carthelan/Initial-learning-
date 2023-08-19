##population
##p0 = 1000. Increases 2% per year, 50 new people immigrate. Years for p(n)=1200
import math
def pop_increase():
    p = int(1000)
    year = 0
    while True:
        p = int(math.floor((p + 50) * (1.02)))
        print(p)
        if p >= 1500:
            print(year)
            break
        year = year + 1
pop_increase() 