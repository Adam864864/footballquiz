import streamlit as st




questions = ('who won the ballon dor in 2003:',
             'who is the most player scored goals in the world:',
             'who is the goat:',
             'how many ballon dors did beckenbauer have:',
             'how many champion leagues did ac milan have:',
             'who won the world cup 2014',
             'who won the super ballon dor',
             'the first world cup played in ........')

options = (('A.Ronaldinho','B.Rivaldo','C.Nedved'),
           ('A.Messi','B.Pele','C.Ronaldo'),
           ('ronaldo','B.Messi','C.both'),
           ('A.3','B.4','C.2'),
           ('A.5','B.7','C.6'),
           ('A.germany','B.spain','C.argentina'),
           ('A.Platini','B.de stefano','C.vanpasten'),
           ('A.USA','B.Uruguay','C.Brasil'))

answers = ('C','C','B','C','c','a','b','b')
guesses = []
score = 0
question_num = 0

for question in questions :
    print('----------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('enter (A,B,C):').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('correct')
    else:
        print('incorrect')
        print(f'{answers[question_num]} is the correct answer')


    question_num += 1


