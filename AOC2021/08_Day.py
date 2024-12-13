from pathlib import Path
lines = [[l.split(" ") for l in line.replace(" | ", "|").split("|")] for line in Path(__file__).with_name('08_Input.txt').open('r').read().strip().split("\n")]

# I dont think this is the right way to do this. I think the set interserctions do work but its better to do something
# like this: https://imgur.com/a/LIS2zZr

part1 = 0
for line in lines:
    for s in line[1]:
        if len(s) in (2, 3, 4, 7):
            part1 += 1
print(f"Part 1: {part1}")

display = {0: {'a', 'b', 'c', 'e', 'f', 'g'}, 
            1: {'c','f'},
            2: {'a', 'c', 'd', 'e', 'g'}, 
            3: {'a', 'c', 'd', 'f', 'g'}, 
            4: {'b', 'c', 'd', 'f'}, 
            5: {'a', 'b', 'd', 'f', 'g'}, 
            6: {'a', 'b', 'd', 'e', 'f', 'g'},
            7: {'a', 'c', 'f'}, 
            8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}, 
            9: {'a', 'b', 'c', 'd', 'f', 'g'}}

""" wire_assignments = {'a': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'b': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'c': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'd': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'f': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'g': {'a', 'b', 'c', 'd', 'e', 'f', 'g'}} """
    

# Number of Segments : Possible Number Representations
# For example, 6: {0, 6, 9} means that if you have 6 segments, you can make the digits 0, 6, and 9
number_segments = {2: {1}, 3: {7}, 4: {4}, 5: {2, 3, 5}, 6: {0, 6, 9}, 7: {8}}

for line in lines:
    to_intersect = []
    
    # What we currently know about each wire
    # For example, 'c' : {'a', 'b'} means that wire 'c' in the actual display can be either 'a' or 'b' in
    # the encoded string. In the end each set should be of length 1, so for example 'c' : {'a'} means that
    # if we see an 'a' in the encoded string, then the 'c' segment is lit up
    # At the start, any wire can be oter wire. In other words, we have no information.
    current_assignments = {'a': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'b': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'c': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'd': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'f': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'g': {'a', 'b', 'c', 'd', 'e', 'f', 'g'}}
    for encoded in line[0]:
        # Loop over possible numbers that we can represent with this many segments
        for possible_number in number_segments[len(encoded)]:
            # Loop over the wires that make up each possible number
            for wire in encoded:
                # Loop over what each wire that makes up that number could possible given the information we have
                current_assignments[wire] = current_assignments[wire].intersection(set([l for l in encoded]))


    print(current_assignments)

         

"""     for encoded in line[0]:
        current_wires = {'a': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'b': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'c': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'd': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'f': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                        'g': {'a', 'b', 'c', 'd', 'e', 'f', 'g'}}
        possible_nums = set(filter(lambda x: len(display[x]) == len(encoded), display.keys()))
        for num in possible_nums:
            for wire in display[num]:
                # Make each set that we are going to add a letter to empty so that the intersection isn't empty
                current_wires[wire] = set()
                for letter in encoded:
                    current_wires[wire].add(letter)
        to_intersect.append(current_wires)
        print(encoded)
        print("Current Wires")
        for w in current_wires:
            print(f"{w}: {current_wires[w]}")
        print()
        print("Wire Assignments")

        print("||||||\n")

        ans = to_intersect[0]
        for i in range(1, len(to_intersect)):
            print(to_intersect[i])
            print()
            for letter in "abcdefg":
                ans[letter] = ans[letter].intersection(to_intersect[i][letter])
        print(ans)
    print("--------------") """