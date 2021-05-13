import csv
import copy

global FrequencyChart
global SequenceArray

file = open('SequenceData.csv')
reader = csv.reader(file)
SequenceArray = list(reader)
file.close()
SequenceArray = SequenceArray[::2]

FrequencyChart = copy.deepcopy(SequenceArray)
for row in FrequencyChart:
    for index in range(len(row)):
        row[index] = 0

def counter(peptide):
    count = 0
    for index1 in range(len(SequenceArray)):
        for index2 in range(len(SequenceArray[index1])):
            if SequenceArray[index1][index2] == peptide:
                count+=1
    return count
"""
for index1 in range(len(SequenceArray)):
        for index2 in range(len(SequenceArray[index1])):
            FrequencyChart[index1][index2] = counter(SequenceArray[index1][index2])
            print (index1, index2)
            
"""
