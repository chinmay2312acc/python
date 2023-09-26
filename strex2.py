first_name = input("enter your first name in lower case : ")
sur_name = input("enter your second name in lower case : ")
full_name = first_name + sur_name

if full_name.islower() == True :
    full_name = full_name.upper()
else :
    print("error : type in lowercase")


print(full_name)
print("number of digits in full name are : ",len(full_name))