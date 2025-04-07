import random as r

total = int(input('How mamy participants are there: '))
name = list()
for x in range(1,total+1):
    nam = input(f'Enter the name of participant {x}: ')
    name.append(nam)

name = set(name)
name = list(name)

shfffled =name[:]
while True:
    r.shuffle(shfffled)
    if all(shfffled[i] != name[i] for i in range(len(name))):
        break

santa_matcher = dict()
giver = shfffled[0]
for i in range(1,len(shfffled)):
    receiver = shfffled[i]
    santa_matcher[giver] = receiver
    giver = receiver

santa_matcher[giver] = shfffled[0]

for x in santa_matcher:
    print(f'{x} -> {santa_matcher[x]}')
