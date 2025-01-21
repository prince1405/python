#Using of loops:
fruits = ["apple", "grapes", "pear"]
for fruit in fruits:  #by using this code, each and every items will be printed one bye one in a row.
    print(fruit)
    print(fruit + "pie")  #if u want to add item's last name.
print(fruits)  #it simply print the items as usual.

#Average height exercise:
student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights)
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1 #here we add 1 bcz computer always count the items from '0'.

average_height = round(total_height / number_of_students)
print(average_height)

