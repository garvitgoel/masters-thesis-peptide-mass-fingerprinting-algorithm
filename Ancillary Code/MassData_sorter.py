import csv
import CSVData
import time

MassData = CSVData.MassData

def insertionSort(alist):   #this sorts the individual proteins within the database
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

index2 = []
def indexcontrol():
    for element in MassData:
        index2.append(0)

"""def largestMass_old():
    largest = MassData[0][index2[0]]
    largestindex = index2[0]
    for index in range(len(MassData)):
        if largest < MassData[index][index2[index]]:
            largest = MassData[index][index2[index]]
            largestindex = index
    return [largest, largestindex]
"""
def largestMass():
    for i in range(len(MassData)):
        if MassData[i] != []:
            largest = MassData[i][0]
            largestindex = i
    for index in range(len(MassData)):
        if len(MassData[index]) > 0 and largest < MassData[index][0]:
            largest = MassData[index][0]
            largestindex = index
    return [largest, largestindex]
    
sortedMassData = []
def sortMassData():
    for counter in range(1795764):
        largest, largestindex = largestMass()
        sortedMassData.append([largest, largestindex, index2[largestindex]])
        del (MassData[largestindex][0])
        index2[largestindex]+= 1
        if (len(sortedMassData)%100000 == 0):
            print (len(sortedMassData), time.time() - timestart)

insertionSort(MassData[5])
indexcontrol()
timestart = time.time()
sortMassData()

"""file = open('sortedMassDataTrunc.csv', 'a')
writer = csv.writer(file)
writer.writerows(sortedMassData)
file.close()"""

