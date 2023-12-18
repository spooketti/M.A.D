"""
n, m = input().split()
cowInit = input().split()
candyHeight = input().split()
candyHeight = list(candyHeight)
candyGroundDist = [0] * m
cowInit = list(cowInit)
for i in len(cowInit):
    for j in len(candyHeight):
            if()
            candyHeight[j] = candyHeight[j] - cowInit[i]
            
print(cowInit)
"""

n, m = input().split()
cowInit = input().split()
candyHeight = input().split()
candyHeight = list(candyHeight)
tallestCow = []
for i in range(len(n)+1):
    tallestCow.append(0)
cowInit = list(cowInit)
for i in range(len(cowInit)):
    for j in range(len(candyHeight)):
        if(int(cowInit[i]) > int(tallestCow[i]) and int(tallestCow[i]) < int(candyHeight[j])):
            tallestCow[i] = int(cowInit[i])
            cowInit[i] = int(cowInit[i]) + int(candyHeight[j]) - int(tallestCow[i])
print(cowInit)
            

"""
    
numTestCase = int(input())
plantData = []
for i in range(numTestCase):
    
    plantRow = []
    nPlant = int(input())
    plantRow.append(nPlant)
    for j in range(3):
        nPlantHeight = input().split()
        nPlantHeight = list(nPlantHeight)
        plantRow.append(nPlantHeight) 
    for j in range(nPlant):
        if(plantRow[2]
    plantData.append(plantRow)
    
print(plantData)
"""
