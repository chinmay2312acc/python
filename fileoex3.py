fin = open("num_calc_2.txt")
count = 0 
runningtotal = 0
for line in fin :
    line = line.strip()
    if(line.isdigit()) :
        runningtotal = runningtotal + int(line)
        count = count + 1

print("total sum of numbers are ", runningtotal)

mean = runningtotal/count
print("mean of numbers = ",mean) 
