path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc10.txt"
map = []
with open(path, 'r') as file:
    for line in file:
        map.append(line.strip())
def score(pos, map):
    v = map[pos[1]][pos[0]]
    sc = 0
    if v == '9':
        map[pos[1]][pos[0]] = '12'
        return 1
    if pos[1]+1<len(map) and int(map[pos[1]+1][pos[0]]) == int(v)+1:
        sc += score((pos[0], pos[1]+1), map)
    if pos[1]-1>=0 and int(map[pos[1]-1][pos[0]]) == int(v)+1:
        sc += score((pos[0], pos[1]-1), map)
    if pos[0]+1<len(map[0]) and int(map[pos[1]][pos[0]+1]) == int(v)+1:
        sc += score((pos[0]+1, pos[1]), map)
    if pos[0]-1>=0 and int(map[pos[1]][pos[0]-1]) == int(v)+1:
        sc += score((pos[0]-1, pos[1]), map)
    return sc
def score2(pos, map):
    v = map[pos[1]][pos[0]]
    sc = 0
    if v == '9':
        return 1
    if pos[1]+1<len(map) and int(map[pos[1]+1][pos[0]]) == int(v)+1:
        sc += score2((pos[0], pos[1]+1), map)
    if pos[1]-1>=0 and int(map[pos[1]-1][pos[0]]) == int(v)+1:
        sc += score2((pos[0], pos[1]-1), map)
    if pos[0]+1<len(map[0]) and int(map[pos[1]][pos[0]+1]) == int(v)+1:
        sc += score2((pos[0]+1, pos[1]), map)
    if pos[0]-1>=0 and int(map[pos[1]][pos[0]-1]) == int(v)+1:
        sc += score2((pos[0]-1, pos[1]), map)
    return sc
total =0
total2 = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '0':
            map2 = []
            for l in map:
                lis = list(l)
                map2.append(lis)
            total2 += score2((j, i), map2)
            total += score((j, i), map2)
print(total)
print(total2)
