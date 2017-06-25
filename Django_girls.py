print ('Hello, Django girls')

if 3>2:
	print('It works')

if 5>2:
	print('5 is indeed greater than 2')
else:
	print('5 is not greater than 2')

name ='Tatiana'
if name =='Tatiana':
	print('Hi Tatiana')
elif name =='Aga':
	print('Hi Aga')
else:
	print('Hi somebody')


def hi ():
	print('Hi there')
	print('how are you doing')

hi()

def love():
	print('LOOOVE')
	print('really?')

love()

def hi(name):
	if name == 'Tatiana':
		print ('Hi Tatiana')
	elif name == 'Michal':
		print ('Hi Michal')
	else:
		print ('Hi there')

hi('Aga')

def hi(name):
	print('Hi ' + name + '!')
girls = ['Tatiana', 'Lena', 'Wanda']
for name in girls:
	hi(name)
	print('Next member')


for i in range (1,10):
	print (i)
