select_Line = int(input("What line do you want to read: "))   #This stores the integer value of the line that will be read from the text file in the variable select_line.

with open("Input Output.txt", "r") as file:   
    lines = file.readlines() 

true_Line = lines[select_Line - 1].strip()
print(true_Line)

new_Line = input("What do you want to add to the file: ")

with open("Input Output.txt", "a") as file:
    file.write("\n" + new_Line) 
    print(new_Line, "has been added to the file.")