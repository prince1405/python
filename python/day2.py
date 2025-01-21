#Info:- to convert a statement into  comment, we have to press "ctrl+/"




#data Types


#String


print("Hello"[0])

print("123" + "345") #answer wiil be (123345)

#Integer
print(123+345) #It will give us a right answer.

#Float
3.14159

#Boolean
True
False

#The "len" tag is not applicable for integers. eg.
#object of type integer has no len.
num_char = len(input("Near C & D appartment"))
new_num_char = str(num_char) #we can't measure the length without this statement because it converts number into strings.
print("Your name has " + new_num_char + "characters.")
#Some examples:-
a = float(123)
print(type(a))

print(70 + float("100.5")) #result- 170.5 {bcz it is in integer form}
print(str(70) + str(100)) #result- 70100 {bcz it is in the form of string by using "str" tag}

#Calculator.
two_digit_number = input("Type a two digit number")
print(type(two_digit_number)) #it is in the form of string.
#converting string form into integer form:
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
#let the two digit number be 87.
print(first_digit)
print(second_digit)

result = first_digit + second_digit #the result will be 8+7=87, bcz it is in the form of string
print(result)

result = int(first_digit) + int(second_digit) #it will give the correct answer bcz it is in the form of integer.
print(result)

#Boolean
result = second_digit < first_digit #for true and false, we must have to use  "reslt".
print(result)

#Mathematical Operations
#1. addition
print(3+5) 
print(type(3+5)) #it will describe the type bcz of the "type" tag i.e. "int", means it is in the form of integer.

#2. substraction
print(5-3)
print(type(5-3)) #type= "int", means it is in the form of integer.

#3. Multiplication
print(5*3) # we will use '*' key as a multiplication.
print(type(5*3)) #type= "int", means it is in the form of integer.

#4. Division
print(6/3)
print(type(6/3)) #type= "float", means it is in the form of float.

#5. Power
print(2 ** 3) #this "**" key act as a power.
print(type(2 ** 3)) #type= "int", means it is in the form of integer.

#BODMAS {left to right}
print(2+2/2) #output will be '3' as per the rule of BODMAS.

# *********************************

#BMI Calculator
height = input("enter your height in m; ")
weight = input("enter your weight in kg; ")
bmi = float(height)  / int(weight) 
bmi_as_int = float(bmi)
print(bmi_as_int)

#Value of data types:-

#the result will be in decimal/float.
print(8 / 3) 

#When we use "//" then the result will be in integer,means the number which comes after the decimal will be replaced.
print(int(8 / 3)) #or
print((8 // 3))

#the result will be in round figure.
print(round(8 / 3)) 

#here third place is the number of digit we want after the decimal, eg.:-
print(round(8 / 3, 4)) 
print(round(2.66666666, 2)) #the result will be 2.67.

#Calculations with result:
result = 4 / 2 #the result will be 2, but if we have to divide the result by 2:- 
result /= 2 #the answer will be 0 {4/2=2 and 2/2=0}
print(result)

#Manipulate a value with a previous value:

#example:
score = 0
#user score as a point
score += 1 #if we want to do add/subs./mult./div. with score.
print(score) 


#f-string
#example:-
score = 0
height = 2.1
isWinning = True
#all of these different data types combine into string by using an "f" and then using these curly brackets to place a variables into the string.
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#life in a days, weeks and years:
age = input("What is your current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(years_remaining)
print(months_remaining)
print(weeks_remaining)
print(days_remaining)
#f-string:
print(f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months, {years_remaining} years.")

#Tip Calculator:
print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
# bill_with_tip = tip / 100 * bill + bill #Or {bill * (1 + tip / 100), the result will be the same
# print(bill_with_tip)
#in percentage:
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
#divide the bill by the no. of people:
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}; ")