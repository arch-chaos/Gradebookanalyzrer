# Student Gradebook Analyzer
# Author: [Your Name Here]
# Date: November 5, 2025

print("Welcome to Gradebook Analyzer")
print()

# Empty dictionary to store student marks
marks = {}

# Ask how many students
num_students = int(input("How many students are in the class? "))

# Get data for each student
for i in range(num_students):
    print("Student", i+1)
    name = input("Name: ")
    mark = float(input("Marks: "))
    marks[name] = mark

print("Data entry complete")
print()

# Main program loop
while True:
    print("MENU")
    print("1. Show Statistics")
    print("2. Show Grades")
    print("3. Show Pass/Fail")
    print("4. Show Results Table")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    # Option 1: Statistics
    if choice == "1":
        print()
        print("STATISTICS")
        
        # Calculate average
        total = 0
        for mark in marks.values():
            total = total + mark
        average = total / len(marks)
        
        # Calculate median
        marks_list = []
        for mark in marks.values():
            marks_list.append(mark)
        marks_list.sort()
        
        n = len(marks_list)
        if n % 2 == 0:
            median = (marks_list[n//2 - 1] + marks_list[n//2]) / 2
        else:
            median = marks_list[n//2]
        
        # Find max
        max_mark = 0
        max_student = ""
        for name, mark in marks.items():
            if mark > max_mark:
                max_mark = mark
                max_student = name
        
        # Find min
        min_mark = 100
        min_student = ""
        for name, mark in marks.items():
            if mark < min_mark:
                min_mark = mark
                min_student = name
        
        # Display results
        print("Total Students:", len(marks))
        print("Average:", average)
        print("Median:", median)
        print("Highest:", max_mark, "-", max_student)
        print("Lowest:", min_mark, "-", min_student)
        print()
    
    # Option 2: Grades
    elif choice == "2":
        print()
        print("GRADE DISTRIBUTION")
        
        # Assign grades
        grades = {}
        for name, mark in marks.items():
            if mark >= 90:
                grades[name] = "A"
            elif mark >= 80:
                grades[name] = "B"
            elif mark >= 70:
                grades[name] = "C"
            elif mark >= 60:
                grades[name] = "D"
            else:
                grades[name] = "F"
        
        # Count grades
        count_A = 0
        count_B = 0
        count_C = 0
        count_D = 0
        count_F = 0
        
        for grade in grades.values():
            if grade == "A":
                count_A = count_A + 1
            elif grade == "B":
                count_B = count_B + 1
            elif grade == "C":
                count_C = count_C + 1
            elif grade == "D":
                count_D = count_D + 1
            elif grade == "F":
                count_F = count_F + 1
        
        print("Grade A:", count_A)
        print("Grade B:", count_B)
        print("Grade C:", count_C)
        print("Grade D:", count_D)
        print("Grade F:", count_F)
        print()
    
    # Option 3: Pass/Fail
    elif choice == "3":
        print()
        print("PASS/FAIL SUMMARY")
        
        # List comprehension
        passed = [name for name, mark in marks.items() if mark >= 40]
        failed = [name for name, mark in marks.items() if mark < 40]
        
        print("Total Students:", len(marks))
        print("Passed:", len(passed))
        print("Failed:", len(failed))
        
        print("Passed Students:")
        for name in passed:
            print(name)
        
        print("Failed Students:")
        for name in failed:
            print(name)
        print()
    
    # Option 4: Results Table
    elif choice == "4":
        print()
        print("RESULTS TABLE")
        print("Name       Marks     Grade")
        
        for name, mark in marks.items():
            # Calculate grade
            if mark >= 90:
                grade = "A"
            elif mark >= 80:
                grade = "B"
            elif mark >= 70:
                grade = "C"
            elif mark >= 60:
                grade = "D"
            else:
                grade = "F"
            
            print(name, "    ", mark, "    ", grade)
        print()
    
    # Option 5: Exit
    elif choice == "5":
        print("Thank you for using Gradebook Analyzer")
        break
    
    else:
        print("Invalid choice")
        print()