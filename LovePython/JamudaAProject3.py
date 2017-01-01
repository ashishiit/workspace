'''
Created on Oct 14, 2016

@author: S528358
'''
import random
print('-------------------------')
print('Welcome to Dice Race!!!')
print('Humans vs Machine')
print('-------------------------')
round_count = 1
user = input('Who is player 1?')
user_total = 0
machine_total = 0
input('press ENTER to begin')
def Function_Chute(name):
    print('--------------BUT------------------')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print('%s just hit a Chute!'%name)
    print('%s has to go back to Start'%name)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
def Function_EndGame():
    print('GAME OVER!!')
    print('Thanks for playing!')
while user_total<50 or machine_total<50:
        print('-----------Round %d----------------'%round_count)
        print('Siri rolled the dice')
        siri_move1 = random.randrange(6)
        siri_move2 = random.randrange(6)
        print('Siri rolled a %d and a %d'%(siri_move1, siri_move2))
        machine_total = machine_total + siri_move1 + siri_move2        
        choice = input('press ENTER to continue playing with Siri(0 to quit)')
        if choice == '0':
            print('User quit early! COMPUTER WINS :-)')
            break
        else:
            print('\n')
            user_move1 = random.randrange(6)
            user_move2 = random.randrange(6)
            print('you rolled a %d and %d'%(user_move1, user_move2))
            user_total = user_total + user_move1 + user_move2
            if user_total < 50:
                print('%s you still have %d spaces to move'%(user,50-(user_total)))
            if machine_total%11 == 0:
                Function_Chute('Siri')                 
                machine_total = 0
            elif user_total%11 == 0:
                Function_Chute('You')                 
                user_total = 0
            print('%s you have moved %d spaces'%(user,user_total))
            print('Siri has moved %d spaces'%machine_total)
            if machine_total >= 50:
                print('Siri reached the finish first and has won the Game!')
                Function_EndGame()
                break
            elif user_total >= 50:
                print('%s has reached finish first and has won the Game!'%user)
                Function_EndGame()                
                break
        round_count = round_count + 1