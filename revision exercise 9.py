#year = input("Enter the current year")
#age = int(input("What age will you be at the end of this year?")) #  Note the int() cast on the input
#print("You were born in", year-age)
#TypeError: unsupported operand type(s) for -: 'str' and 'int'

## amended code
year = int(input("Enter the current year"))
age = int(input("what age will you be at the end of this year"))
year_of_birth = year - age
print("you were born in", year_of_birth)

#3.Which of the follow two code snippets will give an error and why?
#a)print("2000"+18)
#b)print("2000"+str(18))

print("2000"+18)# THIS WOULD GIVE AN ERROR AS WE ARE TRYING TO ADD AN INTEGER AND A STRING

print("2000"+str(18))


