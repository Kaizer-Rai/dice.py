#dice project, updates necessary // dice.py
import random
while True:
    roll = input('please select a dice to roll; d4, d6, d8, d10, d12, d20, d100 or quit ')
    if roll == 'd4':
        d4 = random.randint(1,4)
        print(d4)
    elif roll == "d6":
        d6 = random.randint(1,6)
        print(d6)
    elif roll == "d8":
        d8 = random.randint(1,8)
        print(d8)
    elif roll == "d10":
        d10 = random.randint(0,9)
        print(d10)
    elif roll == "d12":
        d12 = random.randint(1,12)
        print(d12)
    elif roll == "d20":
        d20 = random.randint(1,20)
        print(d20)
        if d20 == 1:
                print('crit fail!')
        elif d20 == 20:
                print('crit!')
    elif roll == 'd100':
        d10 = random.randint(0,9)
        d100 = random.randrange(0, 100, 10)
        if d100 == 0:
            print('00', d10)
        else:
            print(d100, d10)
    elif roll == "quit":
        print("come again!")
        quit()
    else:
        print('input not recognized, try again!')
