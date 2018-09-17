import random

a_speed = input("What speed would you like the alien?(slow, medium, or fast): ")
alien_0 = {
    'x_position': 1,
    'y_position': 26,
    'speed': a_speed
    }
print("The alien is at " + str(alien_0['x_position']) + "," + str(alien_0['y_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
    y_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
    y_increment = 2
else:
    x_increment = 3
    y_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_0['y_position'] = alien_0['y_position'] + y_increment

dice_list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
dice_roll = random.choice(dice_list)

while a_speed == a_speed:
    dice = input("Press r to roll the dice! Roll high enough and you'll get the alien!: ")
    if dice_roll == 12:
        print("Your rolled a 12! The alien is defeated!")
        break
    elif dice_roll >= 7 and not dice_roll == 12:
        print("Great shot! One more hit should do it!")
        break
    elif dice_roll >= 1 and not dice_roll == 7:
        print("Not bad, but the alien isn't finished quite yet!")
        break
    else:
        print("You rolled a 0 and missed your shot! It's now at " + str(alien_0['x_position']) + "," + str(alien_0['y_position']))
        break

#change speed to heatlh
#loop code
#lets test some shiznet
