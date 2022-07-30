from random import randint
import time

player = randint(0,1)
if player:
    print('вы начинаете')
else:
    print('начинает бот')

time.sleep(2)

def my_step(candy):
    if candy % 29:
        return candy % 29
    else:
        return 28

def bot_step(candy):
    return randint(0, 28)


candy = 2021
    
while candy > 0:
        
    if player:
        step = my_step(candy)
    else:
        step = bot_step(candy)
        
    candy -= step
    
    
    if player:
        print('вы делаете ход на {}, конфет останется {}'.format(step, candy))
    else:
        print('бот делает ход на {}, конфет останется {}'.format(step, candy))
    
    if candy <= 0:
        if player:
            print('вы выиграли')
        else:
            print('выиграл бот')
            
        
    if player:
        player = 0
    else:
        player = 1



















        
    