#FizzBuzz exercise:
#The rule of the game is:
# If the number comes btwn the given range and is divisible by the given code then 
# we will replace the number which ius divisible by the given number to "Fizz" and "Buzz" and if the number comes which is divisible the 
#comes which is divisible by all of the given number then that number will be replaced by "FizzBuzz"    

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  #divisible by 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:   #divisible by 3
        print("Fizz")
    elif number % 5 == 0:    #divisible by 5
        print("Buzz")
    else:
        print(number)