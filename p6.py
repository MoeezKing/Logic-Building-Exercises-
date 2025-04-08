import json as j
import random as r

total = int(input('How many flashcards? '))

questions = []
for i in range(1,total+1):
    question = input(f'Enter question {i}: ')
    answer = input('Enter its answer: ')
    questions.append({answer:question})

with open('new.json','w') as f:
    j.dump(questions,f,indent=4)

print('Flashcards saved to flashcards.json ✅')


shuffled = questions[:]

while True:
    r.shuffle(shuffled)
    if all(shuffled[i].items() != questions[i].items() for i in range(len(questions))):
        break

print('--- Quiz Time ---')
score = 0
for x in shuffled:
    question = list(x.items())[0][1]
    answer = list(x.items())[0][0]

    print(f'Q: {question} ?')
    user_answer = input('Your answer: ')

    if(user_answer == answer):
        print('✅ Correct!')
        score+=1
    else:
        print(f'❌ Wrong! Correct answer: {answer}')

print('--- Results ---')
print(f'Correct: {score}/{len(shuffled)}')
