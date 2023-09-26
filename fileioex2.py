count = 0 
fin = open("daffodils.txt")
for line in fin :
    line = line.strip
    count = count + 1

print(count)
