#!/usr/bin/python

file = open("reststops.in",'r')
f = open("reststops.out", "w")


line1 = file.readline()
nums = line1.split(' ')
N = int(nums[1])
L = int(nums[0])
rF = int(nums[2])
rB = int(nums[3])
#stops = {} #maps from tastiness to meters In
tasties = [] #list of tastiness values, sorted
meters = []
totalTastiness = 0 #final value outputted

for line in file:
    nums = line.split(' ')
    metersIn = int(nums[0])
    tastinessEs = nums[1].split('\n')
    tastiness = int(tastinessEs[0])
    #stops[tastiness] = metersIn
    tasties.append(tastiness)
    meters.append(metersIn)

stopsAt = [False]* len(meters) #which places to stop at
#print stopsAt
maxSoFar = 0
for i in range(len(tasties)-1, -1, -1):
    #print tasties[i]
    if (int(tasties[i]) > int(maxSoFar)):
        #print tasties[i], ">" ,maxSoFar
        maxSoFar = int(tasties[i])
        stopsAt[i] = True
#print stopsAt
timeStopped = 0 #totaltime stopped so far
for i in range(len(stopsAt)):
    if stopsAt[i] == True:
        timeBess = (rB* int(meters[i]))+ timeStopped
        timeJohn = int(rF* int(meters[i]))
        if timeBess < timeJohn:
            totalTastiness += (int(tasties[i])* (timeJohn-timeBess))
            timeStopped += timeJohn-timeBess
            #timeBess=timeJohn

print totalTastiness
val = str(totalTastiness) + '\n'
f.write(val)

