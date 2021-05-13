import csv

file = open('MassData.csv')
reader = csv.reader(file)
MassArray = list(reader)
file.close()
MassArray = MassArray[::2]          #formatting requirement
del(MassArray[13500])               #added for database consistency

file = open('SequenceData.csv')
reader = csv.reader(file)
SequenceArray = list(reader)
file.close()
SequenceArray = SequenceArray[::2]  #formatting requirement
del(SequenceArray[13500])

MassData = []
for element1 in MassArray:      #or loop to create float based storage type
    MassData.append([])
    for element2 in element1:
        if float(element2) <= 3200:
            MassData[-1].append(float(element2))

SequenceData = []
for index1 in range(len(SequenceArray)):
    SequenceData.append([])
    for index2 in range(len(SequenceArray[index1])):
        if float(MassArray[index1][index2]) < 3200:
            SequenceData[-1].append(SequenceArray[index1][index2].replace(" ", ""))

file = open('TestInput.csv')
reader = csv.reader(file)
peak_temp = list(reader)
peaks = []
for element in peak_temp:     #this for loop is for formating, each element of peak has to be converted to float 52.34 from an string array ['52.34']
    if float(element[0]) < 3200:
        peaks.append(float(element[0]))

file2 = open('Protein_List.csv')
reader2 = csv.reader(file2)
ProteinList = list(reader2)
file2.close()
del(ProteinList[13500])             #added for database consistency

"""file2 = open('frequencychart.csv')
reader2 = csv.reader(file2)
frequencychart = list(reader2)
file2.close()
frequencychart = frequencychart[::2]
del(frequencychart[13500])"""

file2 = open('sortedMassDatatrunc.csv')
reader2 = csv.reader(file2)
sortedMassData_temp = list(reader2)
file2.close()
sortedMassData_temp = sortedMassData_temp[::2]

sortedMassData = []
for element in sortedMassData_temp:      #loop to create float based storage type
    sortedMassData.append([float(element[0]), int(element[1]), int(element[2])])

file = open('CHO_Proteome.csv')
reader = csv.reader(file)
Proteome_temp = list(reader)
file.close()

Proteome = []
for protein in ProteinList:
    for element in Proteome_temp:
        if element[0] == protein[0]:
            Proteome.append(element[1])
            break
N = len(ProteinList)
for i in reversed(range(N)):
    if MassData[i] == []:
        del(ProteinList[i])
        del(MassData[i])
        del(SequenceData[i])
        del(Proteome[i])

print ("CSV Data Ready")
