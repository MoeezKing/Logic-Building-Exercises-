total_students = int(input('How many students? '))

students = dict()

for i in range(1,total_students+1):
    name = input(f'Enter name of student {i}: ')
    marks = input(f'Enter marks for {name} (comma-separated):').split(',')
    marks = tuple([int(x) for x in marks])
    students[name] = marks

above_90 = set()
print('--- Student Averages ---')
for item in students:
    avg = (students[item][0]+students[item][1]+students[item][2])/3
    print(f'{item}: {round(avg, 2)}')
    if students[item][0]>90 or students[item][1]>90 or students[item][2]>90:
        above_90.add(item)

print('--- Students scoring above 90 in any subject ---')
for x in above_90:
    print(x)

print('--- Sorted student names ---')
alpha_name = [x for x in students]
alpha_name.sort()
print(alpha_name)
