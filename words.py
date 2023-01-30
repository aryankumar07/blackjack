from os import system,name
import random

def clear():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')

def check(flag2):
    if(flag2=='y'):
        return True
    elif(flag2=='n'):
        return False

def result(player,comp):
    print(f"your final hands : {player}")
    print(f"computer final hands : {comp}")

    if(sum(player)>sum(comp)):
        print("player wins")
    elif(sum(player)<sum(comp)):
        print("computer wins")
    else:
        print("tie")

num=[1,2,3,4,5,6,7,8,9,10,10,10,10]
player=[]
comp=[]

flag1=input("type 'y' to play and 'n' to dont : ")
flag1=check(flag1)
clear()

if(flag1):
    player=random.sample(num,2)
    comp=random.sample(num,2)
    print(f"your cards rea : {player}")
    print(f"computer first card : {comp[0]}")
    flag2=input("type 'y' to get another card and 'n' to skip : ")
    flag2=check(flag2)
    while flag2:
        player.append(random.choice(num))
        comp.append(random.choice(num))
        if(sum(player)>21):
            print(f"your final hands : {player}")
            print(f"computer final hands : {comp}")
            print("computer win")
            break
        elif(sum(comp)>21):
            print(f"your final hands : {player}")
            print(f"computer final hands : {comp}")
            print("player wins")
            break
        print(f"your cards are : {player}")
        flag2=input("type 'y' to get another card and 'n' to skip : ")
        flag2=check(flag2)


    if not flag2:
        result(player,comp)
