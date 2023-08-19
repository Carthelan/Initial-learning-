def hotel_Cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  if city == "Tampa":
    return 220
  if city == "Pittsburgh":
    return 222
  if city == "Los Angeles":
    return 475

  def rental_car_cost(days):
    if days >= 7:
       - 50
    elif days >= 3:
       - 20
input("nights", "city", "days")