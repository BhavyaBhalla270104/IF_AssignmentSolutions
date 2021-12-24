marks = int(input("Enter your marks: "))
if(marks>80):
    print("You have been awarded A grade")
elif(marks>60 and marks<=80):
    print("You have been awarded B grade")
elif(marks>50 and marks<=60):
    print("You have been awarded C grade")
elif(marks>45 and marks<=50):
    print("You have been awarded D grade")
elif(marks>25 and marks<=45):
    print("You have been awarded E grade")
else: print("You have been awarded F grade")
