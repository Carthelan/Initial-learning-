List = [1, 2, 4, 8, 16, 32, 64]
sortedList = sorted(List)
newList = []
for i in List:
    i = 0
    while i <= (max(List) + 1):
        if i == min(List):
            newList.append(i)
            List.remove(i)
        else:
            i += 1
        if len(List) == 0:
            break
if sortedList == newList:
    print ("();")