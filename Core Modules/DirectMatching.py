import CSVData

SequenceData = CSVData.SequenceData
MassData = CSVData.MassData
peaks = CSVData.peaks
ProteinList = CSVData.ProteinList
sortedMassData = CSVData.sortedMassData
Proteome = CSVData.Proteome


found = []
for protein in MassData:
    found.append([])
    for peptide in protein:
        found[-1].append(0)
        for peak in peaks:
            if abs(peptide - peak) <= 0.01:
               found[-1][-1] = 1 
