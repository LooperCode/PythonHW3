import random
def Createlist():
    n = int(input("Число: "))
    listRnd = []
    for i in range(n):
        listRnd.append(random.randint(1, 11)) 
    return listRnd

def Maxincrement(listRnd):
    minPos = maxPos = tempMin = tempMax = 0
    minCount = maxCount = 0
    for i in range(len(listRnd)):
        index = 1
        tempMin = listRnd[i]
        while listRnd[i]+index in listRnd:
            tempMax = listRnd[i]+index
            minCount = index
            index += 1
        if minCount > maxCount:
            maxCount = minCount
            maxPos = tempMax
            minPos = tempMin
    return minPos, maxPos        

listRnd = Createlist()
print(listRnd)
listResult = []
listResult.append(Maxincrement(listRnd))
print(listResult)


    