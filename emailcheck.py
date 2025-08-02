def validate_email():
    email = input("Enter email: ")
    
    if "@" in email and "." in email.split("@")[1]:
        print("✅ Valid email")
    
    else:
        print("❌ Invalid email")

# Run the function
validate_email()