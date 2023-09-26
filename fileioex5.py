fin = open("ex5.txt", "w")

count = 0
runningtotal = 0 
for i in range(10):
    user_input = input("enter your number")
    fin.write(user_input+'\n')
fin.close()
#print()

fin = open("ex5.txt", "r")
for line in fin :
    line = line.strip()
   # print(line)
    if(line.isdigit()) :
        runningtotal = runningtotal + int(line)
        count = count + 1 
           
       
            

print(runningtotal)
print(runningtotal/count)
            
        

    