#Take the height input from the user
height = input("Please enter your height in meters\n")
#Take the weight input from the user 
weight = input("please enter your weight in kg\n")
#convert the weight input from the user to an integer
weight_as_int = int(weight)
#convert the height input from the user to an integer
height_as_float = float(height)
#calculate the BMI
BMI = weight_as_int / height_as_float ** 2
#print out the BMI and convert it to a string
print("your body mass index is " + str(BMI))
