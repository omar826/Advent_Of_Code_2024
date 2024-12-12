file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc12.txt"
file = open(file_path, 'r')
map = []
for line in file:
    line = line.strip()
    li = []
    for i in line:
        li.append(i)
    map.append(li)
file.close()
map2 =[]
for i in map:
    map2.append(i.copy())
def find():
    for i in range(len(map)):
        for j in range(len(map[i])):
            #check if map[i][j] is uppercase
            if map[i][j].isupper():
                return (i,j)
    return None
def scout1(pos):
    v = map2[pos[0]][pos[1]]
    vs = v.lower()
    map2[pos[0]][pos[1]] = vs
    ar = 1
    peri = 0
    #left
    if pos[0] == 0:
        peri += 1
    elif map2[pos[0]-1][pos[1]] not in [v, vs]:
        peri += 1
    elif map2[pos[0]-1][pos[1]] == v:
        r = scout1((pos[0]-1,pos[1]))
        ar += r[0]
        peri += r[1]
    #right
    if pos[0] == len(map2)-1:
        peri += 1
    elif map2[pos[0]+1][pos[1]] not in [v, vs]:
        peri += 1
    elif map2[pos[0]+1][pos[1]] == v:
        r = scout1((pos[0]+1,pos[1]))
        ar += r[0]
        peri += r[1]
    #up
    if pos[1] == 0:
        peri += 1
    elif map2[pos[0]][pos[1]-1] not in [v, vs]:
        peri += 1
    elif map2[pos[0]][pos[1]-1] == v:
        r = scout1((pos[0],pos[1]-1))
        ar += r[0]
        peri += r[1]
    #down
    if pos[1] == len(map2[0])-1:
        peri += 1
    elif map2[pos[0]][pos[1]+1] not in [v, vs]:
        peri += 1
    elif map2[pos[0]][pos[1]+1] == v:
        r = scout1((pos[0],pos[1]+1))
        ar += r[0]
        peri += r[1]
    return (ar, peri)





def scout(pos, sides):
    v = map[pos[0]][pos[1]]
    vs = v.lower()
    map[pos[0]][pos[1]] = vs
    ar = 1
    peri = 0
    #left
    if (pos[0]!= 0) and (map[pos[0]-1][pos[1]] in [v, vs]):
        pass
    elif (pos[1] != 0 and pos[1] != len(map[0])-1) and ((pos[0],pos[1]-1) in sides and (pos[0],pos[1]+1) in sides) and ('l' in sides[(pos[0],pos[1]-1)]) and ('l' in sides[(pos[0],pos[1]+1)]):
            peri -= 1
            if pos not in sides:
                sides[pos] = ['l']
            else:
                sides[pos].append('l')
            pass
    elif (pos[1] != 0) and ((pos[0],pos[1]-1) in sides) and ('l' in sides[(pos[0],pos[1]-1)]):
            if pos not in sides:
                sides[pos] = ['l']
            else:
                sides[pos].append('l')
            pass
    elif (pos[1] != len(map[0])-1) and ((pos[0],pos[1]+1) in sides) and ('l' in sides[(pos[0],pos[1]+1)]):
            if pos not in sides:
                sides[pos] = ['l']
            else:
                sides[pos].append('l')
            pass
    else:
        if pos[0] == 0:
            peri += 1
            if pos not in sides:
                sides[pos] = ['l']
            else:
                sides[pos].append('l')
        elif map[pos[0]-1][pos[1]] not in [v, vs]:
            peri += 1
            if pos not in sides:
                sides[pos] = ['l']
            else:
                sides[pos].append('l')
    
            
    
    #right
    if (pos[0]!= len(map)-1) and (map[pos[0]+1][pos[1]] in [v, vs]):
        pass
    elif (pos[1] != 0 and pos[1] != len(map[0])-1) and ((pos[0],pos[1]-1) in sides and (pos[0],pos[1]+1) in sides) and ('r' in sides[(pos[0],pos[1]-1)]) and ('r' in sides[(pos[0],pos[1]+1)]):
            peri -= 1
            if pos not in sides:
                sides[pos] = ['r']
            else:
                sides[pos].append('r')
            pass
    elif (pos[1] != len(map[0])-1) and ((pos[0],pos[1]+1) in sides) and ('r' in sides[(pos[0],pos[1]+1)]):
            if pos not in sides:
                sides[pos] = ['r']
            else:
                sides[pos].append('r')
            pass
    elif (pos[1] != 0) and ((pos[0],pos[1]-1) in sides) and ('r' in sides[(pos[0],pos[1]-1)]):
            if pos not in sides:
                sides[pos] = ['r']
            else:
                sides[pos].append('r')
            pass
    else:
        if pos[0] == len(map)-1:
            peri += 1
            if pos not in sides:
                sides[pos] = ['r']
            else:
                sides[pos].append('r')
        elif map[pos[0]+1][pos[1]] not in [v, vs]:
            peri += 1
            if pos not in sides:
                sides[pos] = ['r']
            else:
                sides[pos].append('r')


    #up
    if (pos[1]!= 0) and (map[pos[0]][pos[1]-1] in [v, vs]):
        pass
    elif (pos[0] != 0 and pos[0] != len(map)-1) and ((pos[0]-1,pos[1]) in sides and (pos[0]+1,pos[1]) in sides) and ('u' in sides[(pos[0]-1,pos[1])]) and ('u' in sides[(pos[0]+1,pos[1])]):
            peri -= 1
            if pos not in sides:
                sides[pos] = ['u']
            else:
                sides[pos].append('u')
            pass
    elif (pos[0] != 0) and ((pos[0]-1,pos[1]) in sides) and ('u' in sides[(pos[0]-1,pos[1])]):
            if pos not in sides:
                sides[pos] = ['u']
            else:
                sides[pos].append('u')
            pass
    elif (pos[0] != len(map)-1) and ((pos[0]+1,pos[1]) in sides) and ('u' in sides[(pos[0]+1,pos[1])]):
            if pos not in sides:
                sides[pos] = ['u']
            else:
                sides[pos].append('u')
            pass
    else:
        if pos[1] == 0:
            peri += 1
            if pos not in sides:
                sides[pos] = ['u']
            else:
                sides[pos].append('u')
        elif map[pos[0]][pos[1]-1] not in [v, vs]:
            peri += 1
            if pos not in sides:
                sides[pos] = ['u']
            else:
                sides[pos].append('u')


    #down
    if (pos[1]!= len(map[0])-1) and (map[pos[0]][pos[1]+1] in [v, vs]):
        pass
    elif (pos[0] != 0 and pos[0] != len(map)-1) and ((pos[0]-1,pos[1]) in sides and (pos[0]+1,pos[1]) in sides) and ('d' in sides[(pos[0]-1,pos[1])] and ('d' in sides[(pos[0]+1,pos[1])])):
            peri -= 1
            if pos not in sides:
                sides[pos] = ['d']
            else:
                sides[pos].append('d')
            pass
    elif (pos[0] != len(map)-1) and ((pos[0]+1,pos[1]) in sides) and ('d' in sides[(pos[0]+1,pos[1])]):
            if pos not in sides:
                sides[pos] = ['d']
            else:
                sides[pos].append('d')
            pass
    elif (pos[0] != 0) and ((pos[0]-1,pos[1]) in sides) and ('d' in sides[(pos[0]-1,pos[1])]):
            if pos not in sides:
                sides[pos] = ['d']
            else:
                sides[pos].append('d')
            pass
    else:
        if pos[1] == len(map[0])-1:
            peri += 1
            if pos not in sides:
                sides[pos] = ['d']
            else:
                sides[pos].append('d')
        elif map[pos[0]][pos[1]+1] not in [v, vs]:
            peri += 1
            if pos not in sides:
                sides[pos] = ['d']
            else:
                sides[pos].append('d')
    if (pos[1] + 1 != len(map[0])) and map[pos[0]][pos[1]+1] == v:
        r = scout((pos[0],pos[1]+1), sides)
        ar += r[0]
        peri += r[1]
    if (pos[1] != 0) and map[pos[0]][pos[1]-1] == v:
        r = scout((pos[0],pos[1]-1), sides)
        ar += r[0]
        peri += r[1]
    if (pos[0] != 0) and map[pos[0]-1][pos[1]] == v:
        r = scout((pos[0]-1,pos[1]), sides)
        ar += r[0]
        peri += r[1]
    if (pos[0]+1 != len(map)) and map[pos[0]+1][pos[1]] == v:
        r = scout((pos[0]+1,pos[1]), sides)
        ar += r[0]
        peri += r[1]

    return (ar, peri)
pos = find()
total =0
total0 = 0
while pos != None:
    sides = {}
    r = scout(pos, sides)
    r0 = scout1(pos)
    total += r[0]*r[1]
    total0 += r0[0]*r0[1]
    pos = find()
print(total0)
print(total)




