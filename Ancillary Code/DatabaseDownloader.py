import requests
import csv
from bs4 import BeautifulSoup

global SequenceData
global MassData

def getPeptideData(protein_name):
    #proxies = {'http': 'http://10.10.78.62:3128'}
    payload = {'protein':protein_name,'mandatory':'','reagents':'nothing (in reduced form)','mplus':'m','masses':'monoisotopic','enzyme':'Trypsin','MC':'2','minmass':'500','maxmass':'unlimited','order':'mass'}
    r = requests.post("http://web.expasy.org/cgi-bin/peptide_mass/peptide-mass.pl", data=payload)#, proxies = proxies)
    return r

def extract_table(r):
    soup = BeautifulSoup(r.text, "html.parser")
    #HTMLData = soup.find("table", attrs={"class":"proteomics2"})
    raw_table = []
    for row in soup.find_all('tr'):
        raw_table.append([td.text.strip() for td in row.find_all('td')])
        if raw_table[-1] == []:
            del(raw_table[-1])
    #del(raw_table[0])
    return raw_table

def transpose(table):
    table_t = [[],[]]
    for row in table:
        table_t[0].append(row[0])
        table_t[1].append(row[3])
    return table_t

def writetocsv(DataTable, filename):
    file = open(filename,'a')
    writer = csv.writer(file)
    writer.writerows(DataTable)
    file.close()

def protein_list():
    protein = []
    file = open('Protein_List_2.csv','r')
    reader = csv.reader(file)
    i = 0
    for row in reader:
        protein.append(row)
        i = i + 1
        """if i>2999:
            break"""
    file.close()
    return protein

def getTheoraticalData(protein_list):
    for protein in protein_list:
        r = getPeptideData(protein[0])
        raw_table = extract_table(r)
        raw_table = transpose(raw_table)
        SequenceData.append(raw_table[1])
        MassData.append(raw_table[0])
        print (protein[0],end=',')


SequenceData = []
MassData = []
protein2 = protein_list()[::2]

getTheoraticalData(protein2)
"""
writetocsv(SequenceData, 'SequenceData.csv')
writetocsv(MassData, 'MassData.csv')
"""
