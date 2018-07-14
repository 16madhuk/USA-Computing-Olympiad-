#!/usr/bin/python

file = open("snowboots.in", 'r')
f = open("snowboots.out", 'w')

firstLine = file.readline()
nums = firstLine.split(' ')
N = int(nums[0])
second = nums[1].split('\n')
B = int(second[0])

tilesnowDepth = [] #snow depth corresponding to tile with index i
secondLine = file.readline()
nums2 = secondLine.split(' ')
for n in nums2:
    tilesnowDepth.append(int(n))

bootSnowDepth = []
bootDistance = []

for line in file:
    bootVals = line.split(' ')
    bootSnowDepth.append(int(bootVals[0]))
    temp = bootVals[1].split('\n')
    dist = temp[0]
    bootDistance.append(int(dist))

bootSnowDepth = list(reversed(bootSnowDepth))
#print "reversed!!!", bootSnowDepth
bootDistance = list(reversed(bootDistance))
#print "reversed....", bootDistance
leastSwaps = 0
currentLoc = 0

curBootDepth = bootSnowDepth.pop()
curBootDist = bootDistance.pop()

#while u r not at the end of the path
while (currentLoc+curBootDist < N-1):
    #if this boot works, step
    success = False
    if tilesnowDepth[currentLoc+curBootDist] <= curBootDepth:
        currentLoc += curBootDist
        success = True
    else:     #take max num of steps with current boot
        for i in range(curBootDist-1, 0, -1):
            if tilesnowDepth[currentLoc+i] <= curBootDepth:
                currentLoc+= i
                success = True
                break
    if success == False:
        curBootDepth = bootSnowDepth.pop()
        curBootDist = bootDistance.pop()
        leastSwaps += 1
        while (tilesnowDepth[currentLoc] > curBootDepth):
            curBootDepth = bootSnowDepth.pop()
            curBootDist = bootDistance.pop()
            leastSwaps += 1

print leastSwaps
discars = str(leastSwaps)
f.write(discars)