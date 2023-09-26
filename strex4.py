first_name = input (" enter your first name : ")
length = len(first_name)
 
if length < 5 :
    sur_name = input("ente your surname : ")
    full_name =  first_name  + sur_name
    full_name = full_name.upper()
    print(full_name)
else :
    if first_name.islower() == true :
        print(first_name)
    else :
        
        first_name = first_name.lower()
        print(first_name)
        
        
        