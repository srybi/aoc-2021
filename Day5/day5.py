def get_max_size():
    with open("input.txt") as input:
        lines = input.readlines()
        return int(max(sum([num.rstrip("\n").replace(" -> ", ",").split(",") for num in lines], [])))

def create_field(max):
    return [[0 for i in range(max+1)] for j in range(max+1)]

def get_cords():
    #[[x1, y1, x2, y2] ...]
    with open("input.txt") as input:
        lines = input.readlines()
        return [num.rstrip("\n").replace(" -> ", ",").split(",") for num in lines]

def mark_field(field, cords):
    x1, y1, x2, y2 = [int(num) for num in cords]
    # vertical move
    if x1 == x2:
        # down
        if (y1 - y2) < 0:
            for i in range(abs(y1-y2) + 1):
                field[x1][y1 + i] += 1
        # up
        if (y1 - y2) > 0:
            for i in range(y1-y2 + 1):
                field[x1][y1 - i] += 1
    # horizontal move
    if y1 == y2:
        #right
        if (x1 - x2) < 0:
            for i in range(abs(x1-x2) + 1):
                field[x1 + i][y1] += 1
        #left
        if (x1 - x2) > 0:
            for i in range(abs(x1-x2) + 1):
                field[x1 - i][y1] += 1

def check_field(field):
    counter = 0
    for r in range(len(field)):
        for c in range(len(field)):
            if field[r][c] > 1:
                counter += 1
    return counter

    

def main():
    max = get_max_size()
    field = create_field(max)
    cords = get_cords()
    print(max)
    for cord in cords:
        print(cord)
        mark_field(field, cord)

    print(check_field(field))

if __name__ == "__main__": 
    main()