file = open('letrehozott-file.txt', 'w')
file.write('ez kerül a létrehozott fájlba, ha minden igaz')
file.close()
file = open('letrehozott-file.txt', 'r')
print(file.read())

print('Name of the file: ', file.name)
print('Close or not: ', file.closed)
print('Opening mode: ', file.mode)

file.close()
