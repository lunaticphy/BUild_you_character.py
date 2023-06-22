# desighn character
hat = [' -/----\- ', '____-----', '         ']
head = ['[ * < * ]', '{ 0 ^ 0 }', '| - _ - |']
neck = "|  |"
shirt = ['|_|~~~~|_|', '|______|', ' || {_______} ||']
torso = "|    |"
pants = ['|| ||', 'II II', '!! !!']
shoes = ['< <', 'U U', '(_ (_']

def pick_your_character():

    print(hat)
    user_hat = input("Pick a Hat: ")
    if user_hat == '0':
        to = hat[0]
        print(to)
    elif user_hat == '1':
        to = hat[1]
        print(to)
    elif user_hat == '2':
        to = hat[2]
        print(to)
    else:
        print("Pick from 0-2")

    print(head)
    user_pick_h = input("pick a Head from list: ")
    if user_pick_h == '0':
        us = head[0]
        print(us)
    elif user_pick_h == '1':
        us = head[1]
        print(us)
    elif user_pick_h == '2':
        us = head[2]
        print(us)
    else:
        print("Pick from 0-2")

    print(shirt)
    user_for_shirt = input("Pick a shirt ")
    if user_for_shirt == '0':
        do = shirt[0]
        print(do)
    elif user_for_shirt == '1':
        do = shirt[1]
        print(do)
    elif user_for_shirt == '2':
        do = shirt[2]
        print(do)
    else:
        print("Pick from 0-2")

    print(pants)
    user_for_pants = input("Pick some pants ")
    if user_for_pants == '0':
        wo = pants[0]
        print(wo)
    elif user_for_pants == '1':
        wo = pants[1]
        print(wo)
    elif user_for_pants == '2':
        wo = pants[2]
        print(wo)
    else:
        print("Pick from 0-2")

    print(shoes)
    user_for_shoes = input("Pick some shoes ")
    if user_for_shoes == '0':
        io = shoes[0]
        print(io)
    elif user_for_shoes == '1':
        io = shoes[1]
        print(io)
    elif user_for_shoes == '2':
        io = shoes[2]
        print(io)
    else:
        print("Pick from 0-2")

    print("Your Character")
    print('   ', to)# hat
    print('   ', us) # head
    print('     ', neck)
    print(" u", do, "u") # shirt
    print('    ', torso)
    print('   ', wo)
    print('   ', io)
pick_your_character()
