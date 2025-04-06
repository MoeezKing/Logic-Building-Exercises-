
total = int(input('how may contacts: '))
dic = dict()
for i in range(1,total+1):
    name = input('Enter name: ')
    ph_n = input('Enter phone: ')
    email = input('Enter email: ')
    dic[name] = (ph_n,email)

search =input('Search for a contact: ')

print('--- All Contacts (Sorted) ---')
l = [(n,p) for n,p in dic.items()]
l.sort(key= lambda x: x[0], reverse=False)
for n,p in l:
    print(f'{n}: {p[0]}, {p[1]}')

print('--- Contact Search ---')
print(f'{search}: {dic[search][0]}, {dic[search][1]}')

print('--- Unique Email Domains ---')
unique = {'@'+x.split('@')[1] for p,x in dic.values()}
print(unique)
