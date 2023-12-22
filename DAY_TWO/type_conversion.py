#Calculate the length of the inputed string
num_char = len(input("What is your name?\n"))
#convert the variable num_char to string since you cannot concatenate a string and integer 
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters" )
