#Write the program that says 2 grades from a student's courses and 1 by entering 
# from the spoken keyboard and the success status is displayed on the screen and failed.

note1 = int(input("enter the student's first exam grade: "))
note2 = int(input("enter the student's second exam grade:"))
quiz  = int(input("enter the student's quiz grade: "))

average=(note1+note2+quiz)/3
if (average >50):
    print("Tebriks. Student passed the class.")
else:
    print("Unfortunately. The student failed the class.")    
