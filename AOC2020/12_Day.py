from pathlib import Path
lines = Path(__file__).with_name('12_Input.txt').open('r').read().strip().split("\n")

directions = {"N": (-1,0), "S": (1,0), "E": (0,1), "W": (0,-1)}
rotate = [(-1,0), (0,1), (1,0), (0,-1)]
facing = (0,1)
position = (0,0)
for line in lines:
    if line[0] == "R":
        for i in range(int(line[1:])//90):
            facing = rotate[(rotate.index(facing)+1)%4]
    elif line[0] == "L":
        for i in range(int(line[1:])//90):
            facing = rotate[(rotate.index(facing)-1)%4]
    elif line[0] == "F":
        position = (position[0] + int(line[1:])*facing[0], position[1] + int(line[1:])*facing[1])
    else:
        position = (position[0] + int(line[1:])*directions[line[0]][0], position[1] + int(line[1:])*directions[line[0]][1])
print(f"Part 1: {abs(position[0])+abs(position[1])}")



facing = (0,1)
position = (0,0)
waypoint = (-1, 10)
toWaypoint = ()
for line in lines:
    if waypoint[0] - position[0] < 0:
    elif waypoint[0] - position[0] > 0:
    elif waypoint[1] - position[1] < 0:

    elif waypoint[1] - position[1] > 0:
    

    if line[0] == "R":
        for i in range(int(line[1:])//90):
            facing = rotate[(rotate.index(facing)+1)%4]
    elif line[0] == "L":
        for i in range(int(line[1:])//90):
            facing = rotate[(rotate.index(facing)-1)%4]
    elif line[0] == "F":
        position = (position[0] + int(line[1:])*facing[0], position[1] + int(line[1:])*facing[1])
    else:
        waypoint = (waypoint[0] + int(line[1:])*directions[line[0]][0], waypoint[1] + int(line[1:])*directions[line[0]][1])
        position = (position[0] + int(line[1:])*directions[line[0]][0], position[1] + int(line[1:])*directions[line[0]][1])

print(f"Part 1: {abs(position[0])+abs(position[1])}")