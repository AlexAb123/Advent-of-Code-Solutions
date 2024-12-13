from pathlib import Path
from collections import Counter
lines = Path(__file__).with_name('03_Input.txt').open('r').read().strip().split("\n")

def getOnesAndZeroes(lines):
    columns = ["".join([line[i] for line in lines]) for i in range(len(lines[0]))]
    zeroes = []
    ones = []
    for column in columns:
        counter = Counter(column)
        zeroes.append(counter["0"])
        ones.append(counter["1"])
    return ones, zeroes

ones, zeroes = getOnesAndZeroes(lines)
gamma = ""
epsilon = ""
for i in range(len(zeroes)):
    gamma += "0" if zeroes[i] > ones[i] else "1"
    epsilon += "0" if zeroes[i] < ones[i] else "1"

gamma, epsilon = int(gamma, 2), int(epsilon, 2)
print(f"Part 1: {gamma*epsilon}")

oxygen = lines.copy()
for col in range(len(lines[0])):
    if len(oxygen) == 1:
        break
    new = []
    ones, zeroes = getOnesAndZeroes(oxygen)
    most = "0" if zeroes[col] > ones[col] else "1"
    for o in oxygen:
        if o[col] == most:
            new.append(o)
    oxygen = new

co2 = lines.copy()
for col in range(len(lines[0])):
    if len(co2) == 1:
        break
    new = []
    ones, zeroes = getOnesAndZeroes(co2)
    least = "1" if zeroes[col] > ones[col] else "0"
    for c in co2:
        if c[col] == least:
            new.append(c)
    co2 = new
print(f"Part 2: {int(oxygen[0], 2)*int(co2[0], 2)}")