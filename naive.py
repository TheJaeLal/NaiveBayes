def print_table(Yes,No,pYes,pNo,AttrName,AttrClasses):
	print('{:10} {:5} {:5}'.format(AttrName,'Yes','No'))
	for c in AttrClasses:
		print('{:10}'.format(c),end = ' ')
		if c in Yes:
			print('{:5}'.format(Yes[c]),end = ' ')
		else:
			print('{:5}'.format('0'),end = ' ')
		if c in No:
			print('{:5}'.format(No[c]))
		else:
			print('{:5}'.format('0'))

	print('{:10} {:5} {:5}'.format('total',Yes['total'],No['total']))	

	print('***********Probabilities************')	

	for c in AttrClasses:
		print('{:10}'.format(c),end = ' ')
		if c in pYes:
			print('{:.2f}'.format(pYes[c]),end = ' ')
		else:
			print('{:5}'.format('0'),end = ' ')
		if c in pNo:
			print('{:.2f}'.format(pNo[c]))
		else:
			print('{:5}'.format('0'))


##########File/Data Handling###############
dataFile = open('weather.csv','r')
dataset = dataFile.read().split('\n')
dataFile.close()
Columns = ['Outlook','Temp','Humidity','Windy','PlayGolf']
pofYes = 0 
pofNo = 0
featureProbabilites = []

####################Attribute 1 outlook#######################
for i in range(len(Columns)-1):
	Yes = dict()
	No = dict()
	classes = set()
	totalYes,totalNo = 0,0
	for row in dataset:
		attributes = row.split(',')	
		Class = attributes[i]
		play = attributes[-1]
		#print(Class)
		classes.add(Class)
		if play=='yes':
			totalYes+=1
			if Class in Yes:
				Yes[Class]+=1
			else:
				Yes[Class] = 1
		else:
			#print('no')
			totalNo+=1
			if Class in No:
				No[Class]+=1
			else:
				No[Class] = 1

	Yes['total'] = totalYes
	No['total'] = totalNo

	nYes = Yes['total']
	nNo = No['total']

	pYes = dict()
	pNo = dict()

	for c in Yes:
		if c!='total':
			pYes[c] = Yes[c]/Yes['total']

	for c in No:
		if c!='total':
			pNo[c] = No[c]/No['total']

	featureProbabilites.append(pYes)
	featureProbabilites.append(pNo)

	print('*********************************')
	print_table(Yes,No,pYes,pNo,Columns[i],classes)


print('Number of Yes:',nYes)
print('Number of No:',nNo)

print('\n')
print(featureProbabilites)
############Query##############
print('******************************')
print('Enter Your Query.....')
query = input().split()

for i in range(len(query)):

	Likelihood_of_Yes = nYes
	Likelihood_of_No = nNo

	if query[i] in featureProbabilites[i*2]:
		Likelihood_of_Yes *= featureProbabilites[i*2][query[i]]
		Likelihood_of_No *= featureProbabilites[(i*2)+1][query[i]]

	else:
		raise KeyError('No instance of '+query[i]+' class exists in the DataSet!')

print('Likelihood_of_Yes =',Likelihood_of_Yes)
print('Likelihood_of_No =',Likelihood_of_No)

if Likelihood_of_Yes > Likelihood_of_No:
	print('Yes')
else:
	print('No')
