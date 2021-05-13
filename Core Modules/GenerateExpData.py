import CSVData
import random

SequenceData = CSVData.SequenceData
MassData = CSVData.MassData
#peaks = CSVData.peaks
ProteinList = CSVData.ProteinList
sortedMassData = CSVData.sortedMassData
Proteome = CSVData.Proteome

MassError = 0.001
peaks = [];index = [];GTProteins = []

def insertionSortPeaks(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def GenerateExpData():
   for i in range(0,10):
      index.append(random.randint(0,23000))
   for i in index:
      GTProteins.append(ProteinList[i])
      for peptide in MassData[i]:
         if random.random() < 1.0:
            peaks.append(peptide + (2*MassError*random.random() - MassError))
   insertionSortPeaks(peaks)

