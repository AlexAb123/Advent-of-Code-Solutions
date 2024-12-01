from pathlib import Path
from collections import Counter
lines = [["".join(line.split("-")[:-1])] + line.split("-")[-1].replace("]", "").split("[") for line in Path(__file__).with_name('Day 04 Input.txt').open('r').read().strip().split("\n")]

def shift(letter, shift):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return letters[(letters.index(letter) + shift) % len(letters)]

part1 = 0
for line in lines:
    counter = Counter(line[0])
    most_common = "".join(sorted(list(counter.keys()), key=lambda x: (-1*counter[x], x)))[0:5]
    
    if most_common == line[2]:
        part1 += int(line[1])
    name = ""
    for letter in line[0]:
        name += shift(letter, int(line[1]))
    if name == "northpoleobjectstorage":
        part2 = int(line[1])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")