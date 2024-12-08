file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc4.txt"
with open(file_path, "r") as file:
    list1 = []
    for line in file:
        list1.append(line.strip())
count =0     
for i, line in enumerate(list1):
    for j, letter in enumerate(line):
        if letter == "X":
            for k in [-1, 1, 0]:
                for l in [-1, 1, 0]:
                    if i+3*k>=0 and i+3*k<len(list1) and j+3*l>=0 and j+3*l<len(list1[i]):
                        if list1[i+k][j+l] == "M" and list1[i+2*k][j+2*l] == "A" and list1[i+3*k][j+3*l] == "S":
                            count += 1
print(count)
count2=0
for i, line in enumerate(list1):
    for j, letter in enumerate(line):
        if letter == "A":
            if i-1>=0 and i+1<len(list1) and j-1>=0 and j+1<len(list1[i]):
                if (list1[i-1][j-1] == "M" and list1[i+1][j+1] == "S") or (list1[i-1][j-1] == "S" and list1[i+1][j+1] == "M"):
                    if (list1[i-1][j+1] == "M" and list1[i+1][j-1] == "S") or (list1[i-1][j+1] == "S" and list1[i+1][j-1] == "M"):
                        count2 += 1
print(count2)



            
    


        
