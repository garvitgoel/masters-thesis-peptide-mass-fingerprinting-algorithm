import csv
file = open('Uniprot_Database.csv')
reader = csv.reader(file)
UD = list(reader)
file.close()

protein = []

def find_between(s, first, last):
    start = s.index( first ) + len( first )
    end = s.index( last, start )
    return [s[start:end]]

for row in UD:
    if row[0][0] == '>':
        protein.append(find_between(row[0], "|","|"))

file = open('Protein_List.csv','a')
writer = csv.writer(file)
writer.writerows(protein)
file.close()

"""protein = []
file = open('Protein_List.csv','r')
reader = csv.reader(file)
i = 0
for row in reader:
    protein.append(row)
    i = i + 1
file.close()

"""
