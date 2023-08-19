# Write your function below!
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count

item = (["fizz","cat","fizz"])
fizz_total = fizz_count(item)
print (fizz_total)