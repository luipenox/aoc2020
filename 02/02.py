import re

def get_values_from_file(file):
    values = []
    with open(file, encoding="utf-8") as f:
        for line in f:
            low, high, char, string = re.search(r'(\d*)-(\d*) (\S): (\S*)', line).groups()
            values.append((low, high, char, string))

    return values

def part_1(values):
    count = 0
    for low, high, char, string in values:
        if int(low) <= string.count(char) <= int(high):
            count += 1

    return count

def part_2(values):
    count = 0
    for low, high, char, string in values:
        low, high = int(low) - 1, int(high) - 1
        string_len = len(string)
        
        is_low = 0 <= low < string_len and char == string[low]
        is_high = 0 <= high < string_len and char == string[int(high)]
        
        if is_low != is_high:
            count += 1

    return count

values = get_values_from_file('input')
print(f'part 1: {part_1(values)}')
print(f'part 2: {part_2(values)}')
