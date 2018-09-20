#Joseph Mehne
#Dictionary Project

import random
import time

alien_0 = {
    'health': 25,
    }
time.sleep(3)
print("")
print("The aliens are coming for Earth! Act fast or the human race is doomed!")
print("")
time.sleep(2)
print("Seems like they're controlled by a mothership. Get the dice of power and use your training to...")
print("")
time.sleep(3.5)
print("KILL...")
print("")
time.sleep(1.25)
print("THEM...")
print("")
time.sleep(1.25)
print("ALL!...")
print("")
time.sleep(1)

game_stats = {
    'state': True,
    }

dice_list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
my_rolls = 0
alien_rolls = 0

def alien_damage():
    alien_0['health'] = alien_0['health'] - dice_roll

def new_health(alien):
    print("The alien's health has dropped to %s." % alien_damage)

while True:
    dice_roll = random.choice(dice_list)
    dice = input("Press r to roll the dice of power! Roll high enough and we'll be able to defeat the alien!: ")
    if dice_roll == 12:
        alien_damage()
        print("You rolled a 12! A critical hit if I've ever seen one!")
        print("")
    elif dice_roll >= 7 and dice_roll <= 11:
        alien_damage()
        print("You rolled a %s, great shot! He should be dead soon!" % dice_roll)
        print("")
    elif dice_roll >= 1 and dice_roll <= 6:
        alien_damage()
        print("You rolled a %s. Not bad, but the alien isn't finished quite yet!" % dice_roll)
        print("")
    else:
        print("You rolled a 0 and missed your shot! ")
        print("")

    if alien_0['health'] <= 0:
        print("*" * 196)
        print("* " * 98)
        time.sleep(1)
        print("*" * 196)
        print("* " * 98)
        time.sleep(1)
        print("*" * 196)
        print("* " * 98)
        time.sleep(1)
        print("")
        print("CONGRATS! The aliens lays bloody on the ground defeated. The human race has been saved by you, brave soldier!")
        print("You Win!")
        print("")
        print("")
        print("")
        break





#change speed to heatlh
#loop code
#lets test some shiznet
