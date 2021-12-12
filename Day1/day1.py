import os
# part1
prev = None
counter = 0
print(os.getcwd())
with open('input.txt') as input:
    for line in input:
        if prev is not None and prev < int(line):
            counter += 1
        
        prev = int(line)

print(counter)


# part2
prev = None
result = 0
line_conter = 0
sum = 0
with open('input.txt') as input:
    for line in input:
        sum += int(line)
        if line_conter >= 2:    
            delta_counter = line_conter - 3
            with open('input.txt') as delta_input:
                delta_sum = 0
                for delta_line in delta_input:
                    if delta_counter >= 0:
                        delta_sum += int(delta_line)
                        delta_counter -= 1
                    else: break

                window = sum - delta_sum
                if prev is not None and prev < window:
                    result += 1
                prev = window
        line_conter += 1

print(result)