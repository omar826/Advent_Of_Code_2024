file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc6.txt"
with open(file_path, "r") as file:
    lines1 = file.readlines()
    lines1 = [list(line.strip()) for line in lines1]
for i, line in enumerate(lines1):
    for j, l in enumerate(line):
        if l in "><^v":
            pos1 = (i, j)
            lines1[i][j] = "."
            break
lines = []
for line in lines1:
    lines.append(line.copy())#copying list of lists
pos = pos1
obs =0
curr = "^"
def up():
    global pos
    global obs
    global curr
    while pos[0] > 0 and lines[pos[0] - 1][pos[1]] != "#":
        if "u" in lines[pos[0]][pos[1]]:
            return -1
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "u"
        pos = (pos[0] - 1, pos[1])
        
    if pos[0] == 0:
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "u"
        return 1
    else:
        curr = ">"
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "u"
        return 0
def down():
    global pos
    global obs
    global curr
    while pos[0] < len(lines) - 1 and lines[pos[0] + 1][pos[1]] != "#":
        if "d" in lines[pos[0]][pos[1]]:
            return -1
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "d"
        
        pos = (pos[0] + 1, pos[1])
    if pos[0] == len(lines) - 1:
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "d"
        return 1
    else:
        curr = "<"
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "d"
        return 0
def left():
    global pos
    global obs
    global curr
    while pos[1] > 0 and lines[pos[0]][pos[1] - 1] != "#":
        if "l" in lines[pos[0]][pos[1]]:
            return -1
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "l"
        
        pos = (pos[0], pos[1] - 1)
    if pos[1] == 0:
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "l"
        return 1
    else:
        curr = "^"
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "l"
        return 0
def right():
    global pos
    global obs
    global curr
    while pos[1] < len(lines[0]) - 1 and lines[pos[0]][pos[1] + 1] != "#":
        if "r" in lines[pos[0]][pos[1]]:
            return -1
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "r"
        
        pos = (pos[0], pos[1] + 1)
    if pos[1] == len(lines[0]) - 1:
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "r"
        return 1
    else:
        curr = "v"
        lines[pos[0]][pos[1]] = lines[pos[0]][pos[1]] + "r"
        return 0
def move():
    global obs
    global curr
    global pos
    while True:
        if curr == "^":
            k = up()
            if k == -1:
                obs += 1
                break
            elif k == 1:
                break
        elif curr == "v":
            k = down()
            if k == -1:
                obs += 1
                break
            elif k == 1:
                break
        elif curr == "<":
            k = left()
            if k == -1:
                obs += 1
                break
            elif k == 1:
                break
        elif curr == ">":
            k = right()
            if k == -1:
                obs += 1
                break
            elif k == 1:
                break
        else:
            break
move()
count = 0
for line in lines:
    for l in line:
        if l not in "#.":
            count += 1
print(count)
obs = 0
for i,line in enumerate(lines1):
    for j, l in enumerate(line):
        if l != "#":
            lines1[i][j] = "#"
            pos = pos1
            curr = "^"
            lines = []
            for line in lines1:
                lines.append(line.copy())
            move()
            lines1[i][j] = "."
print(obs)
            

                
        




    




            
    


        
