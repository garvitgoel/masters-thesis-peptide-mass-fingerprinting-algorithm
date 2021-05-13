import CSVData

SequenceData = CSVData.SequenceData
MassData = CSVData.MassData
peaks = CSVData.peaks
ProteinList = CSVData.ProteinList
sortedMassData = CSVData.sortedMassData
Proteome = CSVData.Proteome

def findPeptideHits(item):
#for the item peptide, returns all the matching elements in sortedMassData
    peptideHits = []
    alist = sortedMassData
    first = 0
    last = len(alist)-1
    frequency = 0
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if abs(alist[midpoint][0] - item) <= 0.01:#modiications not accounted for
            frequency+=1
            peptideHits.append(alist[midpoint])
            i = midpoint + 1
            while i < 2338350 and abs(alist[i][0] - item) <= 0.01:
                frequency+=1
                peptideHits.append(alist[i])
                i+=1
            i = midpoint - 1
            while i >= 0 and abs(alist[i][0] - item) <= 0.01:
                frequency+=1
                peptideHits.append(alist[i])
                i-=1
            found = True
        else:
            if item > alist[midpoint][0]:
                last = midpoint-1
            else:
                first = midpoint+1
    return peptideHits

def applyModifications(peak):
    possibleMasses = [peak,peak-57.02146,peak-15.99491,peak-(57.02146+15.99491)]
    return possibleMasses

MassMap = []
def createMapping():
    for peak in peaks:
        MassMap.append([])
        possibleMasses = applyModifications(peak)
        for mass in possibleMasses:
            MassMap[-1].append(findPeptideHits(mass))

def SimpleSearch(item):
    frequency = 0
    for protein in MassData:
        for peptide in protein:
            if abs(peptide - item) <=0.01:
                frequency+=1
    print (frequency)

Unique = []
def FindUnique():
    for element1 in MassMap:
        Tlen = len(element1[0]) + len(element1[1]) + len(element1[2]) + len(element1[3])
        if Tlen == 1:
            if len(element1[0]) == 1:
                Unique.append([MassMap.index(element1), element1, ProteinList[element1[0][0][1]]])
            if len(element1[1]) == 1:
                Unique.append([MassMap.index(element1), element1, ProteinList[element1[1][0][1]]])
            if len(element1[2]) == 1:
                Unique.append([MassMap.index(element1), element1, ProteinList[element1[2][0][1]]])
            if len(element1[3]) == 1:
                Unique.append([MassMap.index(element1), element1, ProteinList[element1[3][0][1]]])

def ListMappedProteins():
    MappedProteins = []
    for element1 in MassMap:
        for element2 in element1:
            for element3 in element2:
                if ProteinList[element3[1]] not in MappedProteins:
                    MappedProteins.append(ProteinList[element3[1]])
    return MappedProteins

createMapping()
#MappedProteins = ListMappedProteins()
FindUnique()
for element in Unique:
	print (element)
    
