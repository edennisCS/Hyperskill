import random


listset = ["1. Create an account","2. Log into account","0. Exit"]

x = 0
while x == 0:
    for i in listset:
        print(i)
    x =1

    entry = int(input())

    if entry == 1:
        
        number = "400000"

        for i in range(10):
            number += str(random.randint(0, 9))
        

        pin = str(random.randint(0, 9)) 
        for i in range(3):
            pin += str(random.randint(0, 9))
        

        print("Your card has been created")
        print("Your card number:")
        print(number)
        print("Your card PIN:")
        print(pin)
        x = 0


        
    elif entry == 2:
        print("Enter your card number:")
        numberentry = int(input())
        print("Enter your PIN:")
        pinentry = int(input())

        if numberentry == int(number) and pinentry == int(pin):
            print("You have successfully logged in!")

            listset = ["1. Balance","2. Log out","0. Exit"]

            for i in listset:
                print(i)
                
            entry = int(input())
            
            if entry == 1:
                print("Balance: 0")

            elif entry == 2:
                print("You have successfully logged out!")
                x = 0
            else:
                print("Bye!")
                exit()
        else:
            print("Wrong card number or PIN!")
            x = 0

    else:
        print("Bye!")
        exit()
