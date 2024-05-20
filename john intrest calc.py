# -*- coding: utf-8 -*-
"""
By John Simon
Created on Sat Apr 29 19:37:02 2023
####  #   #     ####  #####   ####    ##    ####       ##   #    # #####      ####  # #    #  ####  #    # 
#    #  # #     #    # #    # #    #  #  #  #          #  #  ##   # #    #    #      # ##  ## #    # ##   # 
#####    #      #    # #    # #      #    #  ####     #    # # #  # #    #     ####  # # ## # #    # # #  # 
#    #   #      #    # #####  #      ######      #    ###### #  # # #    #         # # #    # #    # #  # # 
#    #   #      #    # #   #  #    # #    # #    #    #    # #   ## #    #    #    # # #    # #    # #   ## 
#####    #       ####  #    #  ####  #    #  ####     #    # #    # #####      ####  # #    #  ####  #    #
"""
#####################input#############################
fDeposit = 0
while fDeposit <= 0:
    try:
        fDeposit = float(input("Please enter a Deposit: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        

fInterest = 0
while fInterest <= 0:
    try:
        fInterest = float(input("Please enter a Interest Rate: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

iMonths = 0
while iMonths <= 0:
    try:
        iMonths = int(input("Please enter the number of months: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

fGoal = -1
while fGoal < 0:
    try:
        fGoal = float(input("Please enter the number for the goal (0 is OK): "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


##############calculations and loops ####################
fInterest = fInterest / 100 / 12

Accbal = fDeposit
for iCurrentMonth in range(1, iMonths + 1):
    Accbal += Accbal * fInterest
    print(f"Month: {iCurrentMonth:>5} Account Balance is: ${Accbal:12,.2f}")

# Goal Logic
Accbal = fDeposit
iCurrentMonth = 0
while Accbal < fGoal:
    Accbal += Accbal * fInterest
    iCurrentMonth += 1


print(f"It will take {iCurrentMonth} months to reach a goal of: ${fGoal:12,.2f}")


