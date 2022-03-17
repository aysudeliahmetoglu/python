#The success grade of a university course is calculated with a midterm grade and a final exam grade.
# The coefficient of the visa grade is 30%, the coefficient of the final grade is 70%. 
# Write the program that finds the course average as a result of these grades that a student has 
# taken in the exam.

midterm_exam = int(input("please enter midterm exam note: "))
final_exam = int(input("please enter final exam note: "))
average = (midterm_exam * 30 / 100) + (final_exam * 70 / 100)
print("your average is ", average)

