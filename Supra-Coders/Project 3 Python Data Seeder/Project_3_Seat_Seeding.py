import random
f = open('seat_seed.txt', 'a')

seatSeedArray = []

def randomSeatClass(): 
    return random.randrange(1, 3)
    
def randomLaunchId(): 
    return random.randrange(1, 10)
    
def randomPrice(): 
    return random.randrange(500, 1500)
    
def randomNameIndex(): 
    return random.randrange(1, 11)


def createData():
    seatArray = []
    for i in range(50):
        baseObject = {"id": i, 
                "seat-class": randomSeatClass(),
                "launch": randomLaunchId(),
                "passenger": randomNameIndex(),
                "price": randomPrice()
              }
        seatArray.append(baseObject)
    seatSeedArray.append(seatArray)


createData()
f.write(str(seatSeedArray))
f.close()