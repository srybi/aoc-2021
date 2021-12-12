prev = None
counter = 0
with open('input.txt') as input:
    for line in input:
        if prev is not None and prev < int(line):
            counter += 1
        
        prev = int(line)

print(counter)
