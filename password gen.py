import random

def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return " ".join(templist)

uppercaseLetter1 = chr(random.int(65,90))
uppercaseLetter2 = chr(random.int(65,90))
uppercaseLetter3 = chr(random.int(65,90))
uppercaseLetter4 = chr(random.int(65,90))
uppercaseLetter5 = chr(random.int(65,90))
uppercaseletter6 = chr(random.int(65,90))
uppercaseletter7 = chr(random.int(65,90))
uppercaseletter8 = chr(random.int(65,90))
digit1 = random.int(0,10)
digit2 = random.int(0,10)
digit3 = random.int(0,10)
digit4 = random.int(0,10)

password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseletter6 + uppercaseletter7 + uppercaseletter8 + digit1 + digit2 + digit3 + digit4 
output = shuffle(password)
print (output)