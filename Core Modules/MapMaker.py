import CSVData
import random

SequenceData = CSVData.SequenceData
MassData = CSVData.MassData
#peaks = CSVData.peaks
ProteinList = CSVData.ProteinList
sortedMassData = CSVData.sortedMassData
Proteome = CSVData.Proteome
truncationCoverage = CSVData.sequenceCoverage

MassError = 0.005
peaks = []; ran_index = [];GTProteins = [];MassMap = [];Unique = []

def insertionSort(alist):   #sorts in ascending order, general sorter in the programe, used to sort peaks
   for index in range(1,len(alist)):
       currentvalue = alist[index]
       position = index
       while position>0 and alist[position-1]>currentvalue:
           alist[position]=alist[position-1]
           position = position-1
       alist[position]=currentvalue

def GenerateExpData():
   for i in range(0,10):
      ran_index.append(random.randint(0,23000))
   for i in ran_index:
      GTProteins.append(ProteinList[i])
      for peptide in MassData[i]:
         if random.random() < 1.0:
            peaks.append(peptide + (2*MassError*random.random() - MassError))
   insertionSort(peaks)

def findPeptideHits(item):
    peptideHits = []
    alist = sortedMassData
    first = 0
    last = len(alist)-1
    frequency = 0
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if abs(alist[midpoint][0] - item) <= MassError:#modifications not accounted for
            frequency+=1
            peptideHits.append(alist[midpoint])
            i = midpoint + 1
            while i < 1795764 and abs(alist[i][0] - item) <= MassError:
                frequency+=1
                peptideHits.append(alist[i])
                i+=1
            i = midpoint - 1
            while i >= 0 and abs(alist[i][0] - item) <= MassError:
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

def createMapping():
    for peak in peaks:
        MassMap.append(findPeptideHits(peak))

def FindUnique():
    for index1 in range(len(MassMap)):
        Tlen = len(MassMap[index1])
        if Tlen == 1:
            Unique.append([index1, MassMap[index1], ProteinList[MassMap[index1][0][1]]])

def ListMappedProteins():
    MappedProteins = []
    for element1 in MassMap:
        for element2 in element1:
            for element3 in element2:
                if ProteinList[element3[1]] not in MappedProteins:
                    MappedProteins.append(ProteinList[element3[1]])
    return MappedProteins

def main1():
   global peaks;   global index;   global GTProteins;   global MassMap;   global Unique

   peaks = [];   index = [];   GTProteins = []
   GenerateExpData()
   
   MassMap = []
   createMapping()
   
   Unique = []
   FindUnique()
   
   Identified = 0;   FP = 0;   UniquelyMappedProteins = []
   
   for element in Unique:
      if element[2] not in UniquelyMappedProteins:
         UniquelyMappedProteins.append(element[2])
      
   for protein in GTProteins:
      if protein in UniquelyMappedProteins:
         Identified += 1
   for protein in UniquelyMappedProteins:
      if protein not in GTProteins:
         FP+=1
   print (Identified, FP)

def main2():
   global peaks;   global index;   global GTProteins;   global MassMap;   global Unique

   peaks = [];   index = [];   GTProteins = []
   GenerateExpData()
   
   MassMap = []
   createMapping()
      
   Identified = 0;   FP = 0;   MappedProteins = []
   
   for element in MassMap:
      for sub_element in element:
         if ProteinList[sub_element[1]] not in MappedProteins:
            MappedProteins.append(ProteinList[sub_element[1]])
   for protein in GTProteins:
      if protein in MappedProteins:
         Identified += 1
   for protein in MappedProteins:
      if protein not in GTProteins:
         FP+=1
   print (Identified, FP)

"""for j in range(0,100):
   main1()
"""
