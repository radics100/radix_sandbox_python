x = ['körte', 'bogyó', 'zöldség', 'szőlő']
y = ['könnyű', 'nehéz','gyors', 'lassú']
a = 0
b = 0
for i in x:
	for j in y:
		print(x[0], y[2])
		b += 1
	a += 1
	b =0

x = 50
total = 0
for number in range(1, x+1):
	total = total + number
	print('Sum of 1 until %d: %d' % (x, total))

counter = 0
while (counter < 10):
	print('The count is:' , counter)
	counter = counter + 1
print('Done!')


