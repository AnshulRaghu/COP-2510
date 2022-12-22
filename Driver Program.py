from Trivia import get_questions

playerScores = [0, 0]
turn = 0
questions = get_questions()

for obj in questions:
    if turn == 0:
        print('Question for the first player:')
    else:
        print('Question for the second player:')
    print(str(obj))
    choice = int(input('Enter your solution (a number between 1 and 4): '))

    if choice == obj.correctAnswer:
        print('This is the correct answer.\n')
        playerScores[turn] += 1
    else:
        print(f'That is incorrect. The correct answer is {obj.correctAnswer}.\n')


    if turn == 1:
        turn = 0
    else:
        turn = 1

print(f'The first player earned {playerScores[0]} points.')
print(f'The second player earned {playerScores[1]} points.')

if playerScores[0] > playerScores[1]:
    print(f'The first player wins the game.')
elif playerScores[0] < playerScores[1]:
    print(f'The second player wins the game.')
else:
    print(f'The game was a tie.')