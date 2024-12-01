from pathlib import Path

def solve():
    from collections import Counter
    l1, l2 = map(sorted, map(list, zip(*[map(int, line.split()) for line in Path(__file__).with_name('Day 01 Input.txt').open('r').read().strip().split("\n")])))
    part1 = 0
    part2 = 0
    counter = Counter(l2)
    for left, right in zip(l1, l2):
        part1 += abs(left - right)
        part2 += left * counter[left]
    return part1, part2

if __name__ == "__main__":
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")