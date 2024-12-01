from pathlib import Path
positions = list(map(int, Path(__file__).with_name('07_Input.txt').open('r').read().strip().split(",")))

fuelCosts = []
for i in range(max(positions)+1):
    fuelCosts.append(sum([abs(x-i) for x in positions]))
print(f"Part 1: {min(fuelCosts)}")
fuelCosts = []
for i in range(max(positions)+1):
    fuelCosts.append(sum([abs(sum(range(1,abs(x-i)+1))) for x in positions]))
print(f"Part 2: {min(fuelCosts)}")