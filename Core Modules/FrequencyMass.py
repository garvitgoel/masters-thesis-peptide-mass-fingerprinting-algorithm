import csv
import copy

global FrequencyChart
global MassArray
global SequenceArray
global MSMass
global peak
global ProteinList
global fractionArray

file = open('SequenceData.csv')
reader = csv.reader(file)
SequenceArray = list(reader)
file.close()
SequenceArray = SequenceArray[::2]  #formatting requirement
del(SequenceArray[13500])           #added for database consistency

file = open('MassData.csv')
reader = csv.reader(file)
MassArray = list(reader)
file.close()
MassArray = MassArray[::2]          #formatting requirement
del(MassArray[13500])               #added for database consistency

file = open('TestInput.csv')
reader = csv.reader(file)
peak_temp = list(reader)
peak = []
for element in peak_temp:     #this for loop is for formating, each element of peak has to be converted to number '52' from an array '[52]'
    peak.append(element[0])

file2 = open('Protein_List.csv')
reader2 = csv.reader(file2)
ProteinList = list(reader2)
file2.close()
del(ProteinList[13500])             #added for database consistency

def Masscounter(peptideMass):   #return the count of proteins & the porteins' names having a peptide with same mass as the peptideMass
    count = [0,0,0,0,0,0,0,0]
    indexarray = []
    for index1 in range(len(MassArray)):
        for index2 in range(len(MassArray[index1])):
            if abs(float(MassArray[index1][index2]) - float(peptideMass)) < 0.001:
                count[0]+=1
                indexarray.append([index1,index2])
            elif (abs(float(MassArray[index1][index2]) + 160.031 - float(peptideMass)) < 0.001 and 'C' in SequenceArray[index1][index2]):
                count[1]+=1
            """if (abs(float(MassArray[index1][index2]) + 115.027 - float(peptideMass)) < 0.001 and 'N' in SequenceArray[index1][index2]):
                count[2]+=1
            if (abs(float(MassArray[index1][index2]) + 129.043 - float(peptideMass)) < 0.001 and 'Q' in SequenceArray[index1][index2]):
                count[3]+=1"""
            if (abs(float(MassArray[index1][index2]) + 202.074 - float(peptideMass)) < 0.001 and 'W' in SequenceArray[index1][index2]):
                count[4]+=1
            elif (abs(float(MassArray[index1][index2]) + 147.035 - float(peptideMass)) < 0.001 and 'M' in SequenceArray[index1][index2]):
                count[5]+=1
            """if (abs(float(MassArray[index1][index2]) - 17.0027 - float(peptideMass)) < 0.001 and 'E' in SequenceArray[index1][index2]):
                count[6]+=1
            if (abs(float(MassArray[index1][index2]) - 16.0187 - float(peptideMass)) < 0.001 and 'Q' in SequenceArray[index1][index2]):
                count[7]+=1"""
    return sum(count),indexarray

def Masscounter2(protein_index):
    count = 0
    for index1 in range(len(MassArray[protein_index])):
        for index2 in range(len(peak)):
            if abs(float(MassArray[protein_index][index1]) - float(peak[index2])) < 0.001:
                count+=1
            elif (abs(float(MassArray[protein_index][index1]) + 57.02146 - float(peak[index2])) < 0.001 and 'C' in SequenceArray[protein_index][index1]):
                count+=1
            elif (abs(float(MassArray[protein_index][index1]) + 15.99491 - float(peak[index2])) < 0.001 and 'M' in SequenceArray[protein_index][index1]):
                count+=1
            """elif (abs(float(MassArray[protein_index][index1]) + 160.031 - float(peak[index2])) < 0.001 and 'C' in SequenceArray[protein_index][index1]):
                count+=1
            elif (abs(float(MassArray[protein_index][index1]) + 202.074 - float(peak[index2])) < 0.001 and 'W' in SequenceArray[protein_index][index1]):
                count+=1
            elif (abs(float(MassArray[protein_index][index1]) + 147.035 - float(peak[index2])) < 0.001 and 'M' in SequenceArray[protein_index][index1]):
                count+=1"""
    return count

def ProteinFractionInPeak():
    fractionArray = []
    for index1 in range(len(MassArray)):
        countT = 0.0
        countF = 0.0
        countT = len(MassArray[index1])
        countF = Masscounter2(index1)
        if countT!=0 and countF!=0:
            fractionArray.append(countF/countT)
            if countF/countT > 0.1:
                print (index1, ProteinList[index1],fractionArray[-1],"-- ", end='')

def peakFcounter():
    for index in range(len(peak)):
        frequency = Masscounter(peak[index])
        if frequency[0] <=3:
            print (peak[index], frequency[0], frequency[1])

"""
def main():
    for row in MSMass:
        print (Masscounter(float(row[0])))
    
    
FrequencyChart = copy.deepcopy(MassArray)
for row in FrequencyChart:
    for index in range(len(row)):
        row[index] = 0
        
for index1 in range(len(MassArray)):
        for index2 in range(len(MassArray[index1])):
            FrequencyChart[index1][index2] = counter(MassArray[index1][index2])
            print (index1, index2)
            
def Seqcounter(peptide):
    count = 0
    for index1 in range(len(SequenceArray)):
        for index2 in range(len(SequenceArray[index1])):
            if SequenceArray[index1][index2] == peptide:
                count+=1
    return count

"""
