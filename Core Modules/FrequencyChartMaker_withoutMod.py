import time
import csv

file = open('MassData.csv')
reader = csv.reader(file)
MassArray = list(reader)
file.close()
MassArray = MassArray[::2]          #formatting requirement
del(MassArray[13500])               #added for database consistency

MassData = []
for element1 in MassArray:      #or loop to create float based storage type
    MassData.append([])
    for element2 in element1:
        MassData[-1].append(float(element2))

file2 = open('sortedMassData.csv')
reader2 = csv.reader(file2)
sortedMassData_temp = list(reader2)
file2.close()
sortedMassData_temp = sortedMassData_temp[::2]
sortedMassData = []
for element in sortedMassData_temp:      #loop to create float based storage type
    sortedMassData.append([float(element[0]), float(element[1]), float(element[2])])

file = open('frequencychart_withoutMod.csv')
reader = csv.reader(file)
chart = list(reader)
chart = chart[::2]
file.close()

frequencychart = []

def binarySearchinSorted(item):
    alist = sortedMassData
    first = 0
    last = len(alist)-1
    frequency = 0
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if abs(alist[midpoint][0] - item) <= 0.01:#modiications not accounted for
            frequency+=1
            i = midpoint + 1
            while i < 2338350 and abs(alist[i][0] - item) <= 0.01:
                frequency+=1
                i+=1
            i = midpoint - 1
            while i >= 0 and abs(alist[i][0] - item) <= 0.01:
                frequency+=1
                i-=1
            found = True
        else:
            if item > alist[midpoint][0]:
                last = midpoint-1
            else:
                first = midpoint+1
    return frequency

def main():
    frequency = 0
    for protein in MassData[0:]:
        frequencychart.append([])
        time1 = time.time()
        for peptide in protein:
            frequency = binarySearchinSorted(peptide)
            frequencychart[-1].append(frequency)
        time2 = time.time()
        if len(frequencychart)%1000 == 0:
            print (len(frequencychart),", ",end = '')

main()
"""
file = open('frequencychart.csv', 'a')
writer = csv.writer(file)
writer.writerows(frequencychart)
file.close()
"""
