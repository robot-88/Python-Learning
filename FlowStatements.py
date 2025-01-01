grade = int(input("Please ennter the score of a Student"))

if grade>=90:
    print("This student's score of " + str(grade) + " is a A.")
else:
    if grade>=80:
         print("This student's score of " + str(grade) + " is a B.")
    else: 
        if grade>=70:
             print("This student's score of " + str(grade) + " is a C.")
        else:
            if grade>=60:
                 print("This student's score of " + str(grade) + " is a D.")  
            else:
                print("The score is F")         
            