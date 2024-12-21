import random

#Varaiables that we need
list = [1,2,3,4,5,6,7,8,9,0]
bal = 1000
#Engine

print("Welcome to this casino.")
print("The rules of this game are: there are 3 numbers. If the numbers are same i.e (4,4,4) (0,0,0) then you win. Else you lose")
dialogue = input("User: ")
print("Would you like to enter? Prompt: Yes / No")
answ1 = input("User: ")

while True:
    if answ1 == "Yes":
        if bal == 0:
            print("You finished all your money now.")
            quit()
        num1 = random.choice(list)
        num2 = random.choice(list)
        num3 = random.choice(list)
        gamb = num1, num2, num3
        print(gamb)
    if num1 == num2 == num3:
        print("CONGRATS, YOU WON $10,000.Would u like to continue? Prompt: Yes / No")
        bal = bal + 10000
        print("You have $",bal)
        answ2 = input("User:")
        if answ2 == "Yes":
            continue;()
        else:
            quit()
    else:
        print("You didnt win. Sorry for that. Would you like to try again? Prompt: Yes / No")
        bal = bal - 200
        print("You have $",bal)
        answ3 = input("User: ")
        if answ3 == "Yes":
            continue;()
    
        else:
            quit()




    

