salary = int(input("Enter your salary: "))
years = int(input("Enter your years of service: "))
if(years>5):
    bonus = 0.05*salary
    salary = salary + bonus
    print("As you have worked for more than 5 years, your bonus amount is",bonus)
    print("Your salary is now",salary)
else:
    print("As you worked for less than 5 years, there is no bonus for you and salary remains",salary)
