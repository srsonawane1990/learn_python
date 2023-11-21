# Saama emp condition
# 1. candidate must be graduate
# 2. must be 21 years old atleast

status = input("Enter the Graduation status [yes/no] ")
age=int(input("Enter the age : "))
if status.lower() == "yes" and age >= 21:
    print("Candidate meets criteia ")
else: 
    print("Candidates does not meet criteria")