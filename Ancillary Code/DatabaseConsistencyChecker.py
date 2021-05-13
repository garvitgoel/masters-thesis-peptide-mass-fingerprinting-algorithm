Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Bioseparation\AppData\Local\Programs\Python\Python36-32\FrequencyMass.py 
>>> len(Protien_List)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    len(Protien_List)
NameError: name 'Protien_List' is not defined
>>> len(Protein_List)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    len(Protein_List)
NameError: name 'Protein_List' is not defined
>>> len(ProteinList)
23884
>>> len(MassArray)
23884
>>> len(SequenceArray)
23884
>>> ProteinList[0]
['G3HIK4']
>>> for element in MassArray:
	if element == []:
		print ("found")

		
found
>>> for index in range(len(MassArray)):
	if MassArray[index] == []:
		print (index)

		
13500
>>> for index in range(len(SequenceArray)):
	if SequenceArray[index] == []:
		print (index)

		
13500
>>> for index in range(len(ProteinList)):
	if ProteinList[index] == []:
		print (index)

		
>>> MassArray[13500]
[]
>>> ProteinList[13500]
['G3GWR3']
>>> a =[1,2,3]
>>> del(a[0])
>>> a
[2, 3]
>>> del(MassArray[13500])
>>> for index in range(len(MassArray)):
	if MassArray[index] == []:
		print (index)

		
>>> del(SequenceArray[13500])
>>> for index in range(len(SequenceArray)):
	if SequenceArray[index] == []:
		print (index)

		
>>> del(ProteinList[13500])
>>> ProteinList[13500]
['G3H251']
>>> ProteinList[14500]
['G3HQF2']
>>> MassArray[14500]
['7237.6938', '6773.4766', '6574.3809', '6446.2859', '5298.7640', '4971.5733', '3513.6316', '3456.6691', '2652.1059', '2650.2807', '2522.1858', '2284.1310', '2093.0236', '2018.8817', '1981.9565', '1963.8507', '1956.9404', '1853.8616', '1815.9267', '1807.7496', '1762.7282', '1736.8482', '1710.8635', '1677.7805', '1620.8181', '1611.8369', '1492.7232', '1455.7358', '1424.6994', '1309.6891', '1246.6153', '1191.5844', '1181.5941', '1118.5204', '1102.5156', '1063.4894', '1009.4564', '1004.5614', '946.4145', '918.3719', '907.3883', '862.3668', '821.4031', '808.4443', '745.4195', '729.3994', '719.4177', '686.3347', '662.3976', '652.3432', '600.3568', '589.3184', '572.3507', '558.3602', '506.2965']
>>> 
