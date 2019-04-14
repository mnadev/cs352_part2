file = open("copy.txt", "w") 

for i in range(0,1024):
    file.write(i*str(i))

file.close()