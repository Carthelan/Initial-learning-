prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
  print(food)
  print("Price: %s" % prices[food])
  print("Stock: %s" % stock[food])