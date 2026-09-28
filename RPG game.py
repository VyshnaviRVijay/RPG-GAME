import random
player=input("Enter Player Name:")

enemyhp=100
playerhp=100
def turn():
    player_attack=enemyhp.remove(random.randint(1,20))
    enemy_attack=playerhp.remove(random.randint(1,10))
    if playerhp==0:
        print("enemy wins")
    else:
        print("player wins")
turn()