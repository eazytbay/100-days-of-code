#accept the age from the user
age = input()
#subtract the inputed age from 90 assuming that 90 is the benchmark
years = 90 - int(age)
#multiply it by 52 to convert it to weeks
week = years * 52
#display the remaining age in weeks
print(f"You have {week} weeks left.")
