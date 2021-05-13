import CSVData

SequenceData = CSVData.SequenceData
MassData = CSVData.MassData
#peaks = CSVData.peaks
ProteinList = CSVData.ProteinList
sortedMassData = CSVData.sortedMassData
Proteome = CSVData.Proteome


def percentExplained(proteinName):
    protein = MassData[ProteinList.index(proteinName)]
    PeptideSequences = SequenceData[ProteinList.index(proteinName)]
    CompleteSequence = Proteome[ProteinList.index(proteinName)]
    Mark = [0]*len(CompleteSequence)
    for index in range(len(protein)):
        startingindex = CompleteSequence.index(PeptideSequences[index])
        for index2 in range(startingindex, startingindex + len(PeptideSequences[index])):
                    Mark[index2] = 1 
    Marked = 0.0
    for element in Mark:
        if element ==1 :
            Marked+=1
    return Marked/len(Mark)

variable = []
for proteinName in ProteinList:
    if proteinName != ['G3HAC6']:
        variable.append([proteinName, percentExplained(proteinName)])
