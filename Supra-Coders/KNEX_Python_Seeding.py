import random

launchArray = []
#baseObject = {"id": identifier, 
#              "price": randomPrice, 
#              "destination": randomDestination, 
#              "distance_from_earth": travelDistance, 
#              'not_fully_booked': bookingBoolean,
#              'number_of_passengers': randomPassengers,
#              'seats': [],
#              'datetime': randomTime,
#              'seller_company': randomCompany,
#              'passenger_ids': randomForeignId
#              }

def randomPrice():
    return random.randrange(500, 1000)

def randomDestination():
    return random.choice(["Mars", "Venus", "New Tijuana", "Europa", "Nibiru"])

def travelDistance():
    return random.randrange(100000000, 1000000000)

def bookingBoolean():
    return random.choice([True, False])

def randomPassengers():
    return random.randrange(0, 150)

def randomTime():
    return 

def randomCompany():
    return random.choice(["", "", "", "", ""])

def randomForeignId():
    return random.randrange(0, 10)

#def function(): 
    