#write a python program to find the average of test score for each student in the class. there are 16 student in the class
number_of_students = 16
test_score = 4
for students in range(number_of_students+1):
    total_score = 0
    for items in range (test_score):
        test = int(input(f"enter the score each in the test{items}\n"))
        total_score+=test
        average = total_score/test
    print(average)
print("all students fall within the excellent average score")


