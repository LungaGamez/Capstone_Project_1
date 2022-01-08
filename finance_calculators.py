#Compulsroy Task

import math #To be able to use Math functions in the code

investment_cal = input('''Choose either 'investment' or 'bond' from the menu below to proceed:  

investment \t- to calculate the amount of interest you'll earn on interest
bond       \t- to calculate the amount you'll have to pay on a home loan \n\n''')

#Investment Calculator


if investment_cal == "investment":
    
    P    = float(input("Enter the amount of money you would like to deposit ?\n"))
    r    = float(input("Enter the number of an interest rate ?\n")) / 100 / 12
                        #calculated by dividing the annual interest rate by 12.
    t    = float(input("Enter the number of years you planning to invest?\n"))

    interest = input("Choose one type of interest you would like between 'simple' or 'compound'?\n")

    if interest == "simple":

            A = P*(1 + r * t)
            print("The amount you will get after the given period at the interest rate is R",math.trunc(A),)
    
    elif interest == "compound":
    
        A = P* math.pow((1+r),t)
        print("The amount you will get after the given period at the interest rate is R",math.trunc(A),)
                                #added math.trunc function to cut off the decimal part of the float.

    else:
            if interest != "simple" or interest != "compound": # a call for when the user enters incorrect words from the two options.
                print("Error! You entered an incorrect word, re-enter correct word from the choices above:")
            
    
#Home Loan Calculator

if investment_cal == "bond":
    
    P = float(input("Enter the current value of your house ?\n"))
    i = float(input("Enter the number of an interest rate ?\n")) / 100 / 12
    n = float(input("Enter the number of months you planning to repay the bond?\n"))
    
#Formula to calculate bond  
    repayment = P* ((i * ((1+i) ** n)) / ((1+i) ** n - 1)) 

    print("The amount of money you will have to repay each month is",math.trunc(repayment),)

if investment_cal != "investment" and investment_cal != "bond" : #a call for when the user enters the expected main words incorrect.
                    print("Error! You entered an incorrect word, re-enter correct word from the choices above:")





        
