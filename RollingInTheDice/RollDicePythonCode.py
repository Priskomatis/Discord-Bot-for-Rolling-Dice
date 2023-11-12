import random

d6 = [1,2,3,4,5,6]
d10 = [1,2,3,4,5,6,7,8,9,10]
d20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


def roll(dice, noOfDice):
    sum = 0
    if dice == 'd6':
        for y in range(noOfDice):
            randomRoll = random.choice(d6)
            sum = sum + randomRoll
            roll=sum
            print('Roll #',y,' :',randomRoll)
            
        print('Your roll is: ',roll)
    elif dice =='d10':
        for y in range(noOfDice):
            randomRoll = random.choice(d10)
            sum = sum + randomRoll
            roll=sum
            print('Roll #',y,' :',randomRoll)
            
        print('Your roll is: ',roll)
    elif dice =='d20':
        for y in range(noOfDice):
            randomRoll = random.choice(d20)
            sum = sum + randomRoll
            roll=sum
            print('Roll #',y,' :',randomRoll)
            
        print('Your roll is: ',roll)
        
        

UserRoll = input("Enter the dice you want to roll: ")
userRollNo = int(input("enter how many of these dice you want: "))


roll(UserRoll, userRollNo)









