import os

length = 0
print(os.getcwd())
with open("input.txt") as input:
    for line in input:
        length = len(line.rstrip("\n"))
        break

def get_lines_as_List():
    with open('input.txt') as input:
        return input.read().splitlines()
#part1
def get_bits(most_common, input):

    result = ''
    for i in range(length):
        zero_counter = 0
        one_counter = 0

        for line in input:
            if line[i] == '1': 
                one_counter += 1
            else:
                zero_counter += 1

        bites = zero_counter < one_counter # there are more 1 than 0
        equal = zero_counter = one_counter # there are euqaly 1 and 0

        if most_common:
            if bites or equal:
                result += "1"
            else:
                result += "0"
        else:
            if bites or equal:
                result += "0"
            else:
                result += "1"


    return result

input = get_lines_as_List()
gamma_rate = int(get_bits(True, input), 2)
epsilon_rate = int(get_bits(False, input), 2)



print(gamma_rate * epsilon_rate)

#part2
def get_perfect_str(most_common):
    lines = get_lines_as_List()
    
    for index in range(length):
        perfect = get_bits(most_common, lines)
        for line in lines[:]:
            if len(lines) == 1:
                print(lines)
                return lines[0]
            if line[index] != perfect[index]:
                lines.remove(line)


oxygen_generator_rating = int(get_perfect_str(True), 2)
C02_srubber_rating = int(get_perfect_str(False), 2)

print(oxygen_generator_rating * C02_srubber_rating)
