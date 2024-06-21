import random
import json
import os


launchArray = []


def randomPrice():
    return random.randrange(500, 1000)
    
def randomDestination():
    return random.choices(['Nibiru', 'New Tijuana', 'Venus', 'Europa', 'Mars'])

def travelDistance():
    return random.randrange(100000000, 1000000000)

def randomBoolean():
    return random.choice(['true', 'false'])

def randomSeats():
    return random.randrange(1, 150)

def randomPassengers():
    return random.randrange(1, 150)

def randomTime():
    year = '2038'
    month = random.randrange(1, 12)
    day = random.randrange(1, 28)
    hour = random.randrange(1, 12)
    minute = random.randrange(0, 60)
    second = random.randrange(0, 60)
    timeString = f'2038-{month}-{day} {hour}:{minute}:{second}'
    return timeString

def randomCompany():
    return random.choice(["Cosmic Wanderlust Ventures", "StarVoyage Enterprises", "Celestial Journeys Co.", "GalaxyBound Expeditions", "Interstellar Odyssey Group"])

def randomForeignId():
    return random.randrange(1, 150)

def createData():
    for i in range(10):
        seatArray = []
        passengerIdArray = []
        baseObject = {"id": i, 
              "destination": randomDestination(), 
              "distance_from_earth": travelDistance(), 
              'is_available': randomBoolean(),
              'date_time': randomTime(),
              'seller_company': randomCompany(),
              }
        for j in range(10):
            seatArray.append(j)
            passengerIdArray.append(j)
        launchArray.append(baseObject)

createData()

with open('launch_seed.txt', 'w') as file:
    file.write(str(launchArray))

