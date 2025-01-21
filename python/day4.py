#RANDOM NUMBER GENERATOR:
import random #Now we r able to use this random module in python.

random_integer = random.randint(1, 10) #if we run, the result will be random '1-10'
print(random_integer)

random_float = random.random() #it always give us result we the random is btwn 0 and 1 or empty.
print(random_float) #result always will be 0.000000-0.9999999......

random_float = random.random() * 5 #here the result will be btwn 1-4 by using "*5" but the result will not incluude 5. 
print(random_float)

love_score = random.randint(1, 100)
print(f"your love score is {love_score}")

#COIN TOSS:
random_side = random.randint(0, 1)
if random_side == 1:
    print("heads")
else:
    print("tails")

#PYTHON LISTS:
states_of_india = ["Bihar", "Gujrat", "Maharastra", "Rajasthan", "Uttraprasedh"]
#we can write the name of anything in the place of state and as much as u want, thats totally up on u.

states_of_india[4] = "Uttarpradesh" #this statement is used for correction in items.

states_of_india.append("Kashmir") #this statement is used to add one item in the end.

states_of_india.extend(["Assam", "Delhi", "Punjab"]) #this statement is to add bunch of items in the end.

states_of_india.remove("Punjab",) #this staement is used remove any one of the item.

print(states_of_india[-1]) #if we write any numerical digit in '[]', the result will give us the name of the item which is in the position of '[_]'. remember, it always starts from '0' and if we write negative numbers than it will start counting item from bottom. 

#WHO WILL PAY THE BILL:
names_string = input("Give me everybody's name, seperated by a comma.")
names = names_string.split(",")
# # get the total number of items in a list.
# num_items = len(names)
# #generate random numbers btwn. 0 anmd the last index.
# random_choice = random.randint(0, num_items - 1) #this'-1' is written bcz the computer counts the items from 0.
# person_who_will_pay = names[random_choice]
#OR
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today")

#mixing of two seperated items:
fruits = ["Apple", "Guava", "Grapes", "Pineapple", "Orange"]
vegetables = ["Tomato", "potato", "Ladyfinger", "Brinjal"]

dirty_dozen = [fruits, vegetables] #"dirty_dozen" is used to combine two groups of items.

print(dirty_dozen)

#Treasure map:
row1 = ["🔲", "🔲", "🔲"]
row2 = ["🔲", "🔲", "🔲"]
row3 = ["🔲", "🔲", "🔲"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the tresure?")
#23
horizonal = int(position[0]) #2 
vertical = int(position[1]) #3

selected_row = map[vertical - 1] #because it starts counting from "0", so we'll substracted by 1.
selected_row[horizonal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

