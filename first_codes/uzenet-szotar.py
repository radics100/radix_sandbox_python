uzenet = 'Egy egy fontos üzenet számodra, olvasd el kérlek!'
count = {}

for character in uzenet.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)


    
