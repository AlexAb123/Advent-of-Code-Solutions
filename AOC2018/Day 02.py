from pathlib import Path
from collections import Counter
lines = Path(__file__).with_name('Day 02 Input.txt').open('r').read().strip().split("\n")

def get_all_combos_remove_one_char(str):
    combos = set()
    for i in range(len(str)):
        combos.add(str[0:i] + str[i+1:])
    return combos

twos = 0
threes = 0
done = False
for i in range(len(lines)):
    counter = Counter(lines[i])
    two_counted = False
    three_counted = False
    for key in counter:
        if not two_counted and counter[key] == 2:
            twos += 1
            two_counted = True
        if not three_counted and counter[key] == 3:
            threes += 1
            three_counted = True
    for j in range(i+1, len(lines)):
        combos1 = get_all_combos_remove_one_char(lines[i])
        combos2 = get_all_combos_remove_one_char(lines[j])
        if len(combos1.intersection(combos2)) > 0:
            part2 = list(combos1.intersection(combos2))[0]
            done = True
            break

print(f"Part 1: {twos*threes}")
print(f"Part 2: {part2}")