# This is a guess the number game.
import random
secretNumber = random.randint(1,20)
print('I am thinking of nmuber between 1 and 20')

for guessesTaken in range(1,7):
    print('请输入：')
    guess =  int(input())

    if guess < secretNumber:
        print(' 小了')
    elif  guess > secretNumber :
        print('大了')
    else:
        break

if guess == secretNumber:
    print('good job ' +  str(guessesTaken) + ' guesses!')
else :
    print('七次机会用完了，下次再来 ')
