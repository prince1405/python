from cgi import print_exception
from re import M


print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
#if-else statement:-
if height >= 120: #sign of "equal to" '==' and "not equal to" '!='
     print("You can ride the rollercoaster!")

else:
     print("Sorry, you have to grow taller before you can ride.")

#Modulo Operation:
number = int(input("Which number do you want to choose"))

if number % 2 == 0: #Here "2" is a number by which choosen number is divide and quotient will be either even or odd, we can anynof the number instead of taking 2.
    print("This is a even number.")
else:
    print("This is a odd number.")

#elif statement:
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
       print("please pay $5.")        #{if condition1:
    elif age <= 18:                    # do A
       print("please pay $7. ")        #elif condition 2:
    else:                               # do B
       print("please pay $12.")         #else:
else:                                      #do C}
    print("Sorry, you have to grow taller before you can ride.")

#BMI 2.0 {using elif}
Height = float(input("enter your height in m: "))
Weight = float(input("enter your weight in kg: "))

bmi = round(Weight / Height ** 2)
if bmi < 18.5:
   print(f"your bmi is {bmi}, you are under weight.")
elif bmi < 25:
   print(f"your bmi is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi}, you are clinically obese.")

#BMI 3.0 {Leap year}
year = int(input("Which year do you want to check? "))

if year % 4 == 0: #means, if the year which we will choosen is divisible by 4 and the reminder will be 0, then its a leap year.
    if year % 100 == 0: #means, if the year which we will choose is divisible by 100 and the reminder will be 0, then its a leap year. 
        if year % 400 == 0: #means, if the year which we will choosen is divisible by 400 and the reminder will be 0, then its a leap year.
            print("Leap year")
            #if the year which we have choosen is not divisible by 4,100,400 then the is not a leap year: 
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

    #Multiple "if" conditions:
    bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
       bill = 5
       print("child pay $5.")        #{if condition1:
    elif age <= 18:                    # do A
       bill = 7
       print("youth pay $7. ")        #elif condition 2:
    elif age >= 45 and age <= 55:       #do B
        print("Everything is going to be ok. Have a free ride on us!")
    else:                              #else:
       bill = 12                        #do C}
       print("adult pay $12.")         
                                         
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "y":
      bill += 3     #bill=bill+3
    
    print(f"your final bill is ${bill}")
else:                                      
    print("Sorry, you have to grow taller before you can ride.")

#Pizza order :
bill = 0
print("Welcome to python pizza deliveries!")
size = input("what size pizza do you want? S, M, L")
if size == "S":
    bill += 15
    print("please pay $15")
elif size == "M":
    bill += 20
    print("please pay $20")
else:
    bill += 25
    print("please pay $25")

add_pepperoni = input("Do tou want pepperoni? Y or NO")
if add_pepperoni == "y":
    if size == "S":
      bill += 2
    else:
      bill += 3
extra_cheese = input("Do you want extra cheese? Y or NO")
if extra_cheese == "y":
    if size == "S":
      bill += 2
    else:
        bill += 3
    
print(f"your final bill is ${bill}")

#Love calculator:

print("Welcome to the love calculatoer!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r= lower_case_string.count("r")
u= lower_case_string.count("u")
e= lower_case_string.count("e")

true = t + r + u + e

l= lower_case_string.count("l")
o= lower_case_string.count("o")
v= lower_case_string.count("v")
e= lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
  print(f"your love score is {love_score}, you go together like coke and mentos.")

elif (love_score >= 40) and (love_score <= 50):
    print(f"your score is {love_score}, you are alright together")  
else:
    print(f"your score is {love_score}")    
 



