from pathlib import Path
from collections import defaultdict
from math import lcm
lines = Path(__file__).with_name('Day 20 Input.txt').open('r').read().strip().split("\n")

flipflops = defaultdict(list)
conjunctionsOutputs = defaultdict(list)
conjunctionsInputs = defaultdict(list)
broadcaster = []

for line in lines:
    l = line.split(" ")
    if l[0][0] == "&":
        for i in l[2:]:
            conjunctionsOutputs[l[0][1:]].append(i.split(",")[0])

for line in lines:
    l = line.split(" ")
    if l[0][0] == "%":
        for i in l[2:]:
            j = i.split(",")[0]
            if j in conjunctionsOutputs.keys():
                conjunctionsInputs[j].append([l[0][1:].split(",")[0], "low"])
            flipflops[l[0][1:]].append(j)
    elif l[0][0] == "&":
         for i in l[2:]:
            j = i.split(",")[0]
            if j in conjunctionsOutputs.keys():
                conjunctionsInputs[j].append([l[0][1:].split(",")[0], "low"])
    elif l[0] == "broadcaster":
        for i in l[2:]:
            broadcaster.append(i.split(",")[0])

for k in flipflops.keys():
    flipflops[k].insert(0, "off")

lowPulses = 0
highPulses = 0

for module, v in conjunctionsOutputs.items():
    for m in v:
        if m == "rx":
            rxInput = module

rxInputsDict = {}
for module in conjunctionsInputs[rxInput]:
    rxInputsDict[module[0]] = 0

done = False
i = 0
while not done or i < 1000:
    
    if i == 1000:
        print(f"Part 1: {lowPulses*highPulses}")

    q = [(broadcaster, "broadcaster", "low")]

    current = None

    while q:
        
        current, sender, pulse = q.pop(0)
        
        if sender in rxInputsDict and rxInputsDict[sender] == 0 and pulse == "high":
            rxInputsDict[sender] = i+1
            if all(v != 0 for v in rxInputsDict.values()):
                done = True
                break

        if pulse == "low":
            lowPulses += 1
        else:
            highPulses += 1

        if current == broadcaster:
            for module in current:
                q.append((module, "broadcaster", pulse))

        elif current in flipflops.keys():
            if pulse == "low":
                if flipflops[current][0] == "off":
                    flipflops[current][0] = "on"

                    for module in flipflops[current][1:]:
                        q.append((module, current, "high"))
                else:
                    flipflops[current][0] = "off"
                    for module in flipflops[current][1:]:
                        q.append((module, current, "low"))

        elif current in conjunctionsOutputs.keys():
            for j in range(len(conjunctionsInputs[current])):
                if conjunctionsInputs[current][j][0] == sender:
                    conjunctionsInputs[current][j][1] = pulse

            allHigh = True
            for module in conjunctionsInputs[current]:
                if module[1] == "low":
                    allHigh = False
                    break

            if allHigh:
                for module in conjunctionsOutputs[current]:
                    q.append((module, current, "low"))

            else:
                for module in conjunctionsOutputs[current]:
                    q.append((module, current, "high"))
    i += 1

print(f"Part 2: {lcm(*rxInputsDict.values())}")