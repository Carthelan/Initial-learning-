year = 2005

def leap_year(year):
    if (year % 100) != 0:
         print("It's not a Leap Year")
    else: 
        (year % 4) == 0 and (year % 400) == 0 
        print("It's a Leap Year")
leap_year(year) 