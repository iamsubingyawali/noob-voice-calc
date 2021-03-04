import time                                         #importing required functions
import functools
import operator
import math

print("Date:",time.strftime("20%y/%m/%d"))          #printing time and date
print("Time:",time.strftime("%H:%M"))
ct = int(time.strftime('%H')) 
print()

name = input("Hello ! What's your name ? ")         #who are u ?

print()

if ct< 12:                                          #greetings a/c to time
    print("Good Morning, "+name+"!")
elif 12 <= ct< 17:
    print("Good Afternoon, "+name+"!")
else:
    print("Good Evening, "+name+"!")

print("WELCOME TO SUBIN'S CALCULATOR  !")

print()

def main():             #defining the function so that u can re-run it without exiting

    print("1.Addition")                     #listing operations
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Solve Quadratic Equation")
    print("6.Find The Square Root")
    print("7.Find The Square")
    print("8.Find The Cube Root")
    print("9.Find The Cube")
    print("10.Find The Percentage")
    print("11.Calculate The Logarithm")

    print()

    while True:                     #handling exceptions
        try:
            a = int(input("Which Operation you wanna perform ? : "))
        except ValueError:
            print("Please Enter a Number, not a letter.")
            print()
            continue
        else:

            print("Ok")

            if a > 11 or a <= 0:              #being funny...for the wrong inputs..hahaha
                print("Tilganga Eye Hospital may be right choice for you. Thank You !")

                print()

                again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                if again == 'y':                    #wanna re-run ??
                    main()
                else:
                    print("Thanks For Using My Calculator ! -Subin")
                    exit(0)

            elif a == 5:                #solving quadratic equations
                print("The quadratic equation is : ax2 + bx + c = 0")
                q = int(input("Enter a: "))
                w = int(input("Enter b: "))
                t = int(input("Enter c: "))
                y = (w ** 2) - (4 * q * t)
                s1 = (-w - (y ** (1 / 2))) / (2 * q)
                s2 = (-w + (y ** (1 / 2))) / (2 * q)
                print("The solutions are", s1, "and", s2)
                print("Successfully Calculated ! ")
                print("MADE BY SUBIN")

                print()

                again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                if again == 'y':
                    main()
                else:
                    print("Thanks For Using My Calculator ! -Subin")
                    exit(0)

            elif a == 6:                           #finding square root
                s = int(input("Enter The Number : "))
                print("The Square Root of", s, "is : ", math.sqrt(s))
                print("Successfully Calculated ! ")
                print("MADE BY SUBIN")

                print()

                again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                if again == 'y':
                    main()
                else:
                    print("Thanks For Using My Calculator ! -Subin")
                    exit(0)

            elif a == 7:                           #finding square
                s = int(input("Enter The Number : "))
                print("The Sqaure of ", s, "is : ", math.pow(s, 2))
                print("Successfully Calculated ! ")
                print("MADE BY SUBIN")

                print()

                again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                if again == 'y':
                    main()
                else:
                    print("Thanks For Using My Calculator ! -Subin")
                    exit(0)

            elif a == 8:                            #finding cube root
                s = int(input("Enter The Number : "))
                print("The Cube Root of ", s, "is : ", s ** (1 / 3))
                print("Successfully Calculated ! ")
                print("MADE BY SUBIN")

                print()

                again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                if again == 'y':
                    main()
                else:
                    print("Thanks For Using My Calculator ! -Subin")
                    exit(0)

            elif a == 9:                                #finding cube
                s = int(input("Enter The Number : "))
                print("The Cube of ", s, "is : ", s ** 3)
                print("Successfully Calculated ! ")
                print("MADE BY SUBIN")

                print()

                again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                if again == 'y':
                    main()
                else:
                    print("Thanks For Using My Calculator ! -Subin")
                    exit(0)

            elif a == 10:                               #calculating percentage
                s = int(input("Enter The Principle Number: "))
                x = int(input("Enter The Percentage Rate: "))
                print(x, "% of", s, "is", (s * x) / 100)
                print("Successfully Calculated ! ")
                print("MADE BY SUBIN")

                print()

                again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                if again == 'y':
                    main()
                else:
                    print("Thanks For Using My Calculator ! -Subin")
                    exit(0)

            elif a == 11:                               #calculating log
                s = int(input("Enter The Number: "))
                x = input("Enter The base: ")
                if x == 'e':
                    print("The Logarithm of", s, "with base 'e' is", math.log(s))
                else:
                    print("The Logarithm of", s, "with base", x, "is", math.log(s, int(x)))
                print("Successfully Calculated ! ")
                print("MADE BY SUBIN")

                print()

                again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                if again == 'y':
                    main()
                else:
                    print("Thanks For Using My Calculator ! -Subin")
                    exit(0)

            list = []                 #defining list to perform addition and multiplication

            while True:               #handling exceptions
                try:                  #How many nos. ??
                    b = int(input("How many numbers u gonna use for calculation ? : "))

                except ValueError:
                    print("Please Enter a Number, not a letter.")
                    print()
                    continue

                else:

                    if b <= 1:          #being rude for wrong inputs
                        print("What are you doing here....go to 3rd Standard to study Maths well....")
                        print("There is no calculator made to perform calculation with", b, "numbers. ")
                        print("Enter a positive number.")

                        print()

                        again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                        if again == 'y':
                            main()
                        else:
                            print("Thanks For Using My Calculator ! -Subin")
                            exit(0)

                    elif a == 2:                    #performing subtraction
                        c=int(input("Enter The Number: "))
                        for i in range(b-1):
                            d=int(input("Enter The Number: "))
                            c=c-d
                        print("The Result is :",c)

                    elif a == 4:                    #performing division
                        c=int(input("Enter The Number: "))
                        for i in range(b-1):
                            d=int(input("Enter The Number: "))
                            c=c/d
                        print("The Result is :",c)
               
                        print()

                        again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                        if again == 'y':            #wanna re-run ??
                            main()
                        else:
                            print("Thanks For Using My Calculator ! -Subin")
                            exit(0)

                    elif b >= 1:                    #appending inputs to the defined list
                        for x in range(b):
                            list.append(int(input("Enter The Number: ")))

                    else:
                        print("Tilganga Eye Hospital may be right choice for you. Thank You !")

                        print()

                    if a == 1:                      #performing adddition
                        print("The Sum is :", sum(list))

                    elif a == 3:                    #performing multiplication
                        q = functools.reduce(operator.mul, list)
                        print("The Product is :", q)

                    print("Successfully Calculated ! ")

                    print("MADE BY SUBIN")    #It's me...

                    print()
                    print()

                    again = input('Do You Want To Re-Run The Calculator ? (y/n):  ')
                    if again == 'y':
                        main()
                    else:
                        print("Thanks For Using My Calculator ! -Subin")
                        exit(0)
#THANK U

main()   #calling the function to initialize the programme
