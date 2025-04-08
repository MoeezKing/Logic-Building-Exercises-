import json as j

total = int(input('How many expenses: '))
tracker = dict()
expences = dict()
for x in range(total):
    date = input('Enter date: ')
    category = input('Enter category: ')
    amount = int(input('Enter amount: '))
    expences[date] = (category, amount)

tracker['expences'] = expences

#getiing maximum spend
most_spending = max(expences.items(), key=lambda x:x[1][1])
tracker['highest_spend'] = most_spending

# calculating total spend
total_spend = [x[1] for x in expences.values()]
total_spend = sum(total_spend)
tracker['total_spend'] = total_spend

# spendings catagory wise
category = {x[0] for x in expences.values()}
category_wise = dict()
for i in category:
    amounts = [x[1] for x in  expences.values() if x[0]==i]
    total_amount = sum(amounts)
    category_wise[i] = total_amount

tracker['category_wise'] = category_wise

with open('new.json','w') as f:
    j.dump(tracker,f,indent=4)

with open('new.json','r') as f:
    data = j.load(f)

print('--- Expense Summary ---')
print(f'Total spend: ${data['total_spend']}')

print('Spending by category:')
for x in data['category_wise']:
    print(f'{x}: ${data['category_wise'][x]}')

print('Highest expense:')
print(f'{data['highest_spend'][1][0]} -${data['highest_spend'][1][1]} on {data['highest_spend'][0]}')
