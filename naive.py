import sys

if len(sys.argv) == 1:
	raise KeyError('Specify file Name as Command Line Argument')

CSVfile = sys.argv[1]

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
dataFile = open(CSVfile,'r')
dataset = dataFile.read().split('\n')
dataFile.close()
#Columns = ['Outlook','Temp','Humidity','Windy','PlayGolf']
Columns = dataset[-1].split(',')
#print(Columns)
dataset.pop()
pofYes = 0 
pofNo = 0
featureProbabilites = []

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

# print('\n')
# print(featureProbabilites)
############Query##############
print('******************************')
print('Enter Your Query.....',end = '\n')
query = []
for i,attribute in enumerate(Columns[:-1]):
	print('What is the value of',attribute,'?',list(featureProbabilites[i*2]),end = '\n>>> ')
	query.append(input().strip())

#print(query)

Likelihood_of_Yes = nYes
Likelihood_of_No = nNo

for i in range(len(query)):

	#print('Checking',query[i])

	if query[i] in featureProbabilites[i*2]:
		Likelihood_of_Yes *= featureProbabilites[i*2][query[i]]
		Likelihood_of_No *= featureProbabilites[(i*2)+1][query[i]]

	else:
		raise KeyError('No instance of '+query[i]+' class exists in the DataSet!')

print('Likelihood_of_Yes =',Likelihood_of_Yes)
print('Likelihood_of_No =',Likelihood_of_No)

if Likelihood_of_Yes > Likelihood_of_No:
	print('Output: Yes')
else:
	print('Output: No')
