file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc8.txt"

list1 = []
antenna = {}
with open(file_path, "r") as file:
    i=0
    for line in file:
        l = line.strip()
        for j, a in enumerate(l):
            if a != ".":
                if a in antenna:
                    antenna[a].append((i,j))
                else:
                    antenna[a] = [(i,j)]
        list1.append(l)
        i+=1
w = len(list1[0])
h = len(list1)
count =set([])
for a in antenna:
    for i, at1 in enumerate(antenna[a]):
        for at2 in antenna[a][i+1:]:
            n0 = at2[0] - at1[0]
            n1 = at2[1] - at1[1]
            if at2[0]+n0 in range(h) and at2[1]+n1 in range(w):
                count.add((at2[0]+n0, at2[1]+n1))
            if at1[0]-n0 in range(h) and at1[1]-n1 in range(w):
                count.add((at1[0]-n0, at1[1]-n1))
print(len(count))
count =set([])
for a in antenna:
    for i, at1 in enumerate(antenna[a]):
        for at2 in antenna[a][i+1:]:
            n0 = at2[0] - at1[0]
            n1 = at2[1] - at1[1]
            k=0
            while True:
                if at2[0]+k*n0 in range(h) and at2[1]+k*n1 in range(w):
                    count.add((at2[0]+k*n0, at2[1]+k*n1))
                else:
                    break
                k+=1
            k=0
            while True:
                if at1[0]-k*n0 in range(h) and at1[1]-k*n1 in range(w):
                    count.add((at1[0]-k*n0, at1[1]-k*n1))
                else:
                    break
                k+=1
print(len(count))

    



