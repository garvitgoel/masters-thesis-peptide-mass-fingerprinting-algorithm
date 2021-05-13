import CSVData
import random

SequenceData = CSVData.SequenceData
MassData = CSVData.MassData
#peaks = CSVData.peaks
ProteinList = CSVData.ProteinList
"""sortedMassData = CSVData.sortedMassData"""   #sortedMassData was not required
Proteome = CSVData.Proteome
truncationCoverage = CSVData.sequenceCoverage

MassError = 0.001
peaks = [];index = [];GTProteins = []
SequenceFractionMatched = [];MassFractionMatched = []

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

def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and float(alist[position-1][1]) < float(currentvalue[1]):
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue

def FractionMassMatch(proteinName):
    protein = MassData[ProteinList.index([proteinName])]
    NumberOfMatches = 0
    for peptide in protein:
        found = False
        for peak in peaks:
            if abs(peptide - peak) <= MassError :
                found = True
            """elif abs(peptide + 57.02146 - peak) <= 0.01 :
                found = True
            elif abs(peptide + 15.99491 - peak) <= 0.01 :
                found = True"""
        if found == True:
            NumberOfMatches += 1
    return NumberOfMatches/len(protein)

def FractionSequenceMatch(proteinName):
    protein = MassData[ProteinList.index([proteinName])]
    PeptideSequences = SequenceData[ProteinList.index([proteinName])]
    CompleteSequence = Proteome[ProteinList.index([proteinName])]
    Mark = [0]*len(CompleteSequence)
    for index in range(len(protein)):
        for peak in peaks:
            if (abs(protein[index] - peak) <= MassError ):
                startingindex = CompleteSequence.index(PeptideSequences[index])
                for index2 in range(startingindex, startingindex + len(PeptideSequences[index])):
                    Mark[index2] = 1 
    Marked = 0.0
    for element in Mark:
        if element ==1 :
            Marked+=1
    return Marked/len(Mark)

def printSequenceRanking():
    insertionSort(SequenceFractionMatched)
    for i in range(len(SequenceFractionMatched)):
        if [SequenceFractionMatched[i][0]] in GTProteins:
            print (SequenceFractionMatched[i][0], i)

def printMassRanking():
    insertionSort(MassFractionMatched)
    for i in range(len(MassFractionMatched)):
        if [MassFractionMatched[i][0]] in GTProteins:
            print (MassFractionMatched[i][0], i)

def main():
   global peaks;global index;global GTProteins;global SequenceFractionMatched;global MassFractionMatched

   peaks = [];index = [];GTProteins = []

   SequenceFractionMatched = [];MassFractionMatched = []

   GenerateExpData()
   for i in range(len(ProteinList)):
      if ProteinList[i] != ['G3HAC6']:
         SequenceFractionMatched.append([ProteinList[i][0],FractionSequenceMatch(ProteinList[i][0])/truncationCoverage[i]])
         MassFractionMatched.append([ProteinList[i][0],FractionMassMatch(ProteinList[i][0])/truncationCoverage[i]])
      elif ProteinList[i] == ['G3HAC6']:
         SequenceFractionMatched.append([ProteinList[i][0],0.0])
         MassFractionMatched.append([ProteinList[i][0],0.0])
   printSequenceRanking()
   printMassRanking()

   
