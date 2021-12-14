
length = 0
with open("input.txt") as input:
    for line in input:
        length = len(line.rstrip("\n"))
        break


#part1
def get_bits(most_common):
    result = ''
    for i in range(length):
        zero_counter = 0
        one_counter = 0
        with open("input.txt") as input:
            for line in input:
                if line[i] == '0': 
                    zero_counter += 1
                else:
                    one_counter += 1
        if (most_common and zero_counter < one_counter) or (not most_common and zero_counter > one_counter) or (zero_counter == one_counter):
            result += '1'
        elif (most_common and zero_counter > one_counter) or (not most_common and zero_counter < one_counter):
            result += '0'

    return result
    
gamma_rate = int(get_bits(True), 2)
epsilon_rate = int(get_bits(False), 2)



print(gamma_rate * epsilon_rate)

#part2
most_common = get_bits(True)
least_common = get_bits(False)

def get_perfect_str(perfect):
    with open('input.txt') as input:
        lines = list(set(input.read().splitlines()))
        for index in range(length):
            for line in lines:
                if len(lines) == 1:
                    return lines[0]
                if line[index] != perfect[index]:
                    lines.remove(line)

#THERE WERE DUPLICATES IN THE INPUT FILE 
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


oxygen_generator_rating = int(get_perfect_str(most_common), 2)
C02_srubber_rating = int(get_perfect_str(least_common), 2)

print(oxygen_generator_rating * C02_srubber_rating)
