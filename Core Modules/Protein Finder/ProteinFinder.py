sortedMassData = []
for element in sortedMassData_temp:      #loop to create float based storage type
    sortedMassData.append([float(element[0]), float(element[1]), float(element[2])])

def binarySearchInPeaks(item, item_index):
    alist = peaks
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if abs(alist[midpoint] - item) <= 0.001:
            found = True
        elif (abs(item + 57.02146 - alist[midpoint]) < 0.001 and 'C' in SequenceArray[item_index[0]][item_index[1]]):
            found = True
        elif (abs(item + 15.99491 - alist[midpoint]) < 0.001 and 'M' in SequenceArray[item_index[0]][item_index[1]]):
            found = True
        else:
            if item > alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def binarySearchinSorted(item):
    alist = sortedMassData
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if abs(alist[midpoint][0] - item) <= 0.001:
            found = True
            position = midpoint
        else:
            if item > alist[midpoint][0]:
                last = midpoint-1
            else:
                first = midpoint+1
    return [found, position]

set1 = []

def SimpleSearchinPeaks(item, item_index):  #returns if a particular peptide is there in the peaks
    found = False
    for peak in peaks:
        if abs(peak - item) <= 0.001:
            found = True
        elif abs(item + 57.02146 - peak) < 0.001 and 'C' in SequenceArray[item_index[0]][item_index[1]]:
            found = True
        elif abs(item + 15.99491 - peak) < 0.001 and 'M' in SequenceArray[item_index[0]][item_index[1]]:
            found = True
    return found

def main():
    for index1 in range(len(MassData)):
        print (index1, ", ", end = '')
        for index2 in range(len(MassData[index1])):
            if SimpleSearchinPeaks(MassData[index1][index2], [index1, index2]) == True:
                if MassData[index1] not in set1:
                    set1.append([ProteinList[index1], SequenceArray[index1][index2], MassArray[index1][index2]])
                """else:
                    set1[set1.index(MassData[index1])].append(SequenceArray[index1][index2], MassArray[index1][index2])"""
