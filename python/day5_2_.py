# High score
student_scores = input("Input a list of student scores").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

#For loop with range:
for  number in range(1, 11, 3): #if we give the range to 11 then it gives the result upto 10, if we add number by using comma then it steps how large steps you want to be.
    print(number)

#For loop with high range:

total = 0
for number in range(0, 101):
    total += number    #By using this code, we can find the sum of the range whatever the range will be.
print(total)
