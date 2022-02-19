import numpy as np
import math
import random
mazeMap = [0]*5

agentLoc = np.random.randint(5,size = 1)
print('Initial Vaccum Location: Cell ', agentLoc )
#Initializing Dirt
i = 0
mazeMap = np.random.randint(2, size=5)
print ('Initial Room condition:',mazeMap)
while mazeMap.any():
#for i in range(25):
    print ('Room condition:',mazeMap)
    print('Vaccum Location: Cell ', agentLoc )
    # toss = np.random.randint(2, size = 1)
    i+= 1
    if mazeMap[agentLoc] == 1:
        mazeMap[agentLoc] = 0
        print('Sucking Dirt')   
    if ( agentLoc != 4 and (mazeMap[agentLoc + 1] == 1 or mazeMap[4] == 1)) or agentLoc == 0:
        agentLoc += 1
        print('Moving Right')
    else:
        agentLoc -= 1
        print('Moving Left')
print('Room condition:',mazeMap)
print('Vaccum Location: Cell ', agentLoc )
print('Number of Iterations', i)        