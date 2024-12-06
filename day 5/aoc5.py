#write a program to read a file with each line containing 2 numbers separated by spaces
#add first number in each line to list1 and second number to list2
file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc5.txt"
with open(file_path, "r") as file:
    list1 = {}
    update = []
    k=0
    for line in file:
        line = line.strip()
        if line == "":
            k = 1
            continue
        if k == 0:
            a = int(line.split('|')[0])
            b = int(line.split('|')[1])
            if a in list1:
                list1[a].append(b)
            else:
                list1[a] = [b]
        else:
            l = line.split(',')
            m = []
            for i in l:
                m.append(int(i))
            update.append(m)
sum = 0
incorr = []
for i in update:
    prev = []
    corr =1
    for j in i:
        prev.append(j)
        for k in list1[j]:
            if k in prev:
                corr = 0
                break
    if corr == 1:
        sum += i[len(i)//2]
    else:  
        incorr.append(i)
print(sum)
sum2 = 0
for i in incorr:
    prev = []
    j = 0
    while j < len(i):
        m = i[j]
        if m in prev:
            pass
        else:
            prev.append(m)
        for k in list1[m]:
            if k in prev:
                j_2 = prev.index(k)
                prev.remove(k)
                i = i[:j_2] + i[j_2+1:j+1] + [k] + i[j+1:]
                j = j - 2
                break
        j += 1
    sum2 += i[len(i)//2]
print(sum2)
                
        




    




            
    


        