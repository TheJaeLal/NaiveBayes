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

	pYes = dict()
	pNo = dict()

	for c in Yes:
		if c!='total':
			pYes[c] = Yes[c]/Yes['total']

	for c in No:
		if c!='total':
			pNo[c] = No[c]/No['total']

	print('*********************************')
	print_table(Yes,No,pYes,pNo,Columns[i],classes)



