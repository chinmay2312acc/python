date = int(input("enter the date today : " ))
year = int(input("what year are we in : " ))
mm = int(input("how many months have passed by in year : "))
y = int(input("enter the last 2 digits of the year : "))
c = int(input("enter the first 2 digits of the year : "))

w = date + [[13*[mm+1]]/5] + y + [y/4]+[c/4] - [2*c]
print(w)








