a = ['zöldség', 'gyümölcs', 'savanyúság', 'ennivaló']
b = ['menü', 'vacsora', 'ebéd', 'tízórai']
x = 0
y = 0

for i in a:
	for j in b:
		print(a[x], b[y])
		y += 1
	x += 1	
	y = 0
print('vége.')

