import re   

select_Email = int(input("What line do you want to read: ")) #This takes an integer input of what line of the text file will be read and stores it in the variable select_email.

with open("Input Output.txt", "r") as file:   #This function opens the text file and the letter r makes the function read the file.
    lines = file.readlines()  #This function returns a list with all the lines that contains emails and stores it in the variable lines.

true_Line = lines[select_Email - 1].strip()   #This variable subtracts the lines returned by 1 as text files start from 1 not 0. It also removes whitespace.
print(true_Line)   #This prints the email from the correct line that was entered.

new_Email = input("What email do you want to add to the file: ")   #This takes an email address as an input and stores it in the variable new_email.
email = new_Email.strip()   #This removes the entered email of whitespaces and stores it in the new variable email.
if re.search(".+@.+", email):    #This function searches the entered email if it contains an @ symbol.
    with open("Input Output.txt", "a") as file:    #If an @ is detected, this function appends the text file and adds the email to the file.
        file.write("\n" + new_Email)    #This males sure the added email is stored in a new line after the last email in the file.
        print(new_Email, "has been added to the file.")
else:
    print("An invalid email was entered.")   #If an @ is not detected, then the error message will display.