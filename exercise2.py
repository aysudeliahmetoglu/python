#Write the program that finds out whether the student passed the course according
#  to the midterm and final grades entered.

midterm_exam=int(input("please enter midterm exam note:"))
final_exam=int(input("please enter final exam note: "))
average=midterm_exam+final_exam/2

if(average<30 and final_exam<40 ):
    print("you did not pass this course")
    print("your average is ",average)
elif(average>=30 and final_exam<40) :
    print("you did not pass this course") 
    print("your average is ",average)  
else:
    print("you passed this course")
    print("your average is ",average)