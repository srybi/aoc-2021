#part 1
x_pos = 0
depth = 0

def get_value(string):
    length = len(string)
    return int(string[length-1])

with open("input.txt") as input:
    for line in input:
        value = get_value(line.rstrip("\n"))
        if line.__contains__("forward"):
            x_pos += value
        if line.__contains__("up"):
            depth -= value
        if line.__contains__("down"):
            depth += value

print (x_pos * depth)

#part 2

x_pos = 0
depth = 0
aim = 0

with open("input.txt") as input:
    for line in input:
        value = get_value(line.rstrip("\n"))
        if line.__contains__("forward"):
            x_pos += value
            depth += (aim * value)
        if line.__contains__("up"):
            aim -= value
        if line.__contains__("down"):
            aim += value


print (x_pos * depth)