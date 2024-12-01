from pathlib import Path
lanternFish = list(map(int, Path(__file__).with_name('06_Input.txt').open('r').read().strip().split(",")))

fish = [0,0,0,0,0,0,0,0,0]

for daysLeft in lanternFish:
    fish[daysLeft] += 1
    
for day in range(256):
    zero = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7] + zero
    fish[7] = fish[8]
    fish[8] = zero

    if day == 79:
        print(f"Part 1: {sum(fish)}")

print(f"Part 2: {sum(fish)}")
