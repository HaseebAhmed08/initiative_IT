name : str = 'Haseeb Ahmed'
clas : str = 'Ten'
rollnumber : int = 4
section : str = 'B'
math_Marks : int = 1
urdu_Marks : int = 16
english_Marks : int = 20
sindhi_Marks : int = 8
islamiyat_Marks : int = 9

student_Total_Marks = math_Marks+urdu_Marks+english_Marks+sindhi_Marks+islamiyat_Marks

student_Percentage = (student_Total_Marks/500)*100

if student_Percentage>80 and student_Percentage<100:
    print("Grade A")
elif student_Percentage >=70 and student_Percentage < 80:
    print ("Grade B")
elif student_Percentage>=60 and student_Percentage<70:
    print("Grade C")
elif student_Percentage >=50 and student_Percentage <60:
    print(f"{name} is pass")
else :
    print(f"{name} is fail his percentage is {student_Percentage} ")








    