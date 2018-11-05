#-*- coding -*-
poem = '''\
	programming is fun
	when the work is done
	if you wanne make your work also fun
	use Python'''

#python 2 f = file('poem.txt','a')
#python 3 f = open('poem.txt','a')
#w:write a:append
f = open('poem.txt','a')
f.write(poem)
f.close()

#default r:read
f = open('poem.txt')
while True:
	line = f.readline()
	if len(line)==0:
		break
	print (line)
f.close()	

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
dict['haha'] = 123
print(dict)