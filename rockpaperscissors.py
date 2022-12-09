with open('rockpapsci.txt') as f:
    lines = f.read().splitlines()


def is_draw(yo,elf):
    if elf== "A" and yo=="X":
        return True
    elif elf=="B" and yo== "Y":
        return True
    elif elf== "C" and yo=="Z":
        return True
    else:
        return False

def is_win(yo,elf):
    if elf == "A" and yo == "Y":
        return True
    elif elf== "B" and yo == "Z":
        return True
    elif elf=="C" and yo== "X":
        return True
    else:
        return False


def calculate_tool_score(tool):
    if tool=="X":
        return 1
    elif tool== "Y":
        return 2
    elif tool =="Z":
        return 3
score=0
for game in lines:

    elf,yo = game.split(" ")
    if is_draw(yo,elf):
        score+=3
    elif is_win(yo, elf):
        score+=6
    score= score + calculate_tool_score(yo)

print(score)


