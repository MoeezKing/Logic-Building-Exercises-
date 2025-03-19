# list of 10 cities and reverse list ,and 1st and last in lower
ls = ['lahore', 'karachi', 'islamabad', 'quetta', 'peshawar','murree','jarawala', 'faisalabad', 'attock', 'multan']
nl = []
print(ls)
for i in ls:
    nl.insert(0, i)

print(nl)
ls.clear()

for i in nl:
    n = i[0:1].upper()+i[1:-1].lower()+i[-1:].upper()
    ls.append(n)

print(ls)
