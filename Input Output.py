select_Line = int(input("What line do you want to read: "))

with open("Input Output.txt", "r") as file:
    lines = file.readlines() 

true_Line = lines[select_Line - 1].strip()
print(true_Line)

new_Line = input("What do you want to add to the file: ")

with open("Input Output.txt", "a") as file:
    file.write(new_Line) 
    print(new_Line, "has been added to the file.")