# Student info
Name = input("Type in your name: ")
Section = input("Type in your section: ")

# Grade input
print("Please type in your grades.")
Prelim = float(input("Prelim: "))
if Prelim <= 39.9 or Prelim >= 100.1:
    print("Error, try again.")
    exit()
    
Midterm = float(input("Midterm: "))
if Midterm <= 39.9 or Midterm >= 100.1:
    print("Error, try again.")
    exit()
        
Finals = float(input("Finals: "))
if Finals <= 39.9 or Finals >= 100.1:
    print("Error, try again.")
    exit()
    
FinalGrade = round((Prelim * 0.33332) + (Midterm * 0.33332) + (Finals * 0.33332))

# Grade to GPA
gpa = 0.00
if FinalGrade >= 99 and FinalGrade <= 100:
    gpa = 1.00
elif FinalGrade >= 96 and FinalGrade <= 98:
    gpa = 1.25
elif FinalGrade >= 93 and FinalGrade <= 95:
    gpa = 1.50
elif FinalGrade >= 90 and FinalGrade <= 92:
    gpa = 1.75
elif FinalGrade >= 87 and FinalGrade <= 89:
    gpa = 2.00
elif FinalGrade >= 84 and FinalGrade <= 86:
    gpa = 2.25
elif FinalGrade >= 81 and FinalGrade <= 83:
    gpa = 2.50
elif FinalGrade >= 78 and FinalGrade <= 80:
    gpa = 2.75
elif FinalGrade >= 75 and FinalGrade <= 77:
    gpa = 3.00
elif FinalGrade <= 74:
    gpa = 5.0

# Final Display
print("Hello,", Name, "from", Section, "here are the results.")
print("Preliminary Period Grade:", Prelim)
print("Midterm Period Grade:", Midterm)
print("Final Period Grade:", Finals)
print("Final Grade:", FinalGrade)
print("GPA:", gpa)
if gpa == 1.00:
    print("Excellent")
elif gpa == 1.25:
    print("Outstanding")
elif gpa == 1.50:
    print("Superior")
elif gpa == 1.75:
    print("Very Good")
elif gpa == 2.00:
    print("Good")
elif gpa == 2.25:
    print("Satisfactory")
elif gpa == 2.50:
    print("Fairly Satisfactory")
elif gpa == 2.75:
    print("Fair")
elif gpa == 3.00:
    print("Passed")
elif gpa == 5.00:
    print("Failed")