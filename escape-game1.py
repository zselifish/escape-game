#the passwords
password = 1720
password_two = 12
#shows if the game has been beaten.
game_beat = 0
for 1 in 10:    
    while game_beat == 0:
        entered = int(input('enter the password'))
        if entered == password:
            print('well done. you may proceed')
            game_beat +=1
    else:
        print('try again')
    while game_beat == 1:
        entered = int(input('enter the password'))
        if entered == password_two:
            print('well done, you may proceed')
            game_beat +=1
        else:
            print('try again')