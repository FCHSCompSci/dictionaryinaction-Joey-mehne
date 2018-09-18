import random

a_difficulty = input("What difficulty would you like the alien to be?(easy, medium, or hard): ")
alien_0 = {
    'difficulty': a_difficulty,
    'health': 12,
    }
print("The alien is coming for you!")

game_stats = {
    'state': True,
    }

dice_list = [0,1,2,3,4,5,6,7,8,9,10,11,12]

while True:
    dice_roll = random.choice(dice_list)
    dice = input("Press r to roll the dice! Roll high enough and you'll get the alien!: ")
    if dice_roll == 12:
        alien_0['health'] = alien_0['health'] - dice_roll
        print("Your rolled a 12! The alien is defeated!")
        break
    elif dice_roll >= 7 and dice_roll <= 11:
        alien_0['health'] = alien_0['health'] - dice_roll
        print("You rolled a %s, great shot! He should be dead soon!" % dice_roll)
    elif dice_roll >= 1 and dice_roll <= 6:
        alien_0['health'] = alien_0['health'] - dice_roll
        print("You rolled a %s. Not bad, but the alien isn't finished quite yet!" % dice_roll)
    else:
        print("You rolled a 0 and missed your shot!")

    if game_stats['state'] == False:
        break






#change speed to heatlh
#loop code
#lets test some shiznet
