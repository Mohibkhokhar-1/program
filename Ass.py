def calculate_grade():
    # Take input for marks of 3 subjects
    print("Enter marks obtained (out of 100) in 3 subjects:")
    subject1 = float(input("Subject 1: "))
    subject2 = float(input("Subject 2: "))
    subject3 = float(input("Subject 3: "))

    # Calculate total and percentage
    total = subject1 + subject2 + subject3
    percentage = (total / 300) * 100

    
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Display results
    print(f"\nResults:")
    print(f"Total Marks: {total}/300")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

# Call the function
calculate_grade()