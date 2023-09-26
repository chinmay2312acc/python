count = 0
running_total = 0 
for i in range(20):
    user_input = int(input("enter your number"))
    running_total = running_total + user_input

print(running_total)
print(running_total/20)