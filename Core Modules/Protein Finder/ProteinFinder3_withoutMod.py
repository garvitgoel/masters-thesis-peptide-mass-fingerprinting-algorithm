
import CSVData
import random

SequenceData = CSVData.SequenceData
MassData = CSVData.MassData
#peaks = CSVData.peaks
ProteinList = CSVData.ProteinList
sortedMassData = CSVData.sortedMassData
Proteome = CSVData.Proteome
truncationCoverage = CSVData.sequenceCoverage

MassError = 0.001
peaks = []; ran_index = [];GTProteins = []
SequenceFractionMapped = [];

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

def FractionofTruncSequenceMatched(proteinName):    #code need to account for modiications as well; need to account for G3HAC6 as well
    protein = MassData[ProteinList.index(proteinName)]
    PeptideSequences = SequenceData[ProteinList.index(proteinName)]
    CompleteSequence = Proteome[ProteinList.index(proteinName)]
    Mark = [0]*len(CompleteSequence)
    for index in range(len(protein)):
        for peak in peaks:
            if (abs(protein[index] - peak) <= MassError ):  #modifications not accounted for
                startingindex = CompleteSequence.index(PeptideSequences[index])
                for index2 in range(startingindex, startingindex + len(PeptideSequences[index])):
                    Mark[index2] = 1 
    Marked = 0.0
    for element in Mark:
        if element ==1 :
            Marked+=1
    return (Marked/len(Mark))/sequenceCoverage[ProteinList.index(proteinName)]

def printSequenceRanking():
    insertionSort(SequenceFractionMatched)
    for i in range(len(SequenceFractionMatched)):
        if [SequenceFractionMatched[i][0]] in GTProteins:
            print (SequenceFractionMatched[i][0], i)

def create_SequenceFractionMapped():
   for i in range(len(ProteinList)):
      if ProteinList[i] != ['G3HAC6']:
         SequenceFractionMapped.append(FractionSequenceMapped(ProteinList[i][0])/truncationCoverage[i])
      elif ProteinList[i] == ['G3HAC6']:
         SequenceFractionMatched.append(0.0)
   printSequenceRanking()
