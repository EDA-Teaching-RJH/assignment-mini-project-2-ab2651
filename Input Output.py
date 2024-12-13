import re

select_Email = int(input("What line do you want to read: "))   

with open("Input Output.txt", "r") as file:   
    lines = file.readlines() 

true_Line = lines[select_Email - 1].strip()
print(true_Line)

new_Email = input("What email do you want to add to the file: ")
email = new_Email.strip()
if re.search(".+@.+", email):
    with open("Input Output.txt", "a") as file:
        file.write("\n" + new_Email) 
        print(new_Email, "has been added to the file.")
else:
    print("An invalid email was entered.")