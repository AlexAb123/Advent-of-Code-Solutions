from pathlib import Path
num = int(Path(__file__).with_name('Day 03 Input.txt').open('r').read().strip())

def nth_odd(n):
    return 2*n+1

def area(layer):
    return nth_odd(layer)**2 

def spiral_size(layer):
   return 8*layer if layer > 0 else 1

# (Inclusive, Exclusive)
def range_in_spiral(layer):
    if layer == 0:
        return (1, 2)
    return (area(layer-1) + 1, area(layer) + 1)

def get_layer(n):
    if n <= 1:
        return n
    n -= 1
    l = int(n**0.5)
    l1 = 0
    l2 = 0
    if l % 2 == 1:
        l1 = l
        l2 = l + 2
    else:
        l1 = l - 1
        l2 = l + 1
    return int(((l2**2)-(l1**2))/8.0)

def position_in_spiral(n):
    return n - range_in_spiral(get_layer(n))[0]

def get_corners(layer):
    r = range_in_spiral(layer)
    size = spiral_size(layer)
    l = []
    for i in range(4):
        l.append(int(range_in_spiral(layer)[1]- 1 - size*i/4))
    return l



layer = get_layer(num)
dist_from_corner = min(map(lambda x: abs(num-x), get_corners(layer)))
side_length = (spiral_size(layer) + 4)//4
part1 = layer + (side_length//2) - dist_from_corner
print(f"Part 1: {part1}")