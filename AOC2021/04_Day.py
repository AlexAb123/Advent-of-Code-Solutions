from pathlib import Path
lines = Path(__file__).with_name('04_Input.txt').open('r').read().strip().split("\n")

winners = [int(num) for num in lines[0].split(",")]
boards = []
temp = []
for line in lines[2:]:
    if line == "":
        boards.append(temp)
        temp = []
    else:
        temp.append(list(map(int, (filter(lambda x: x != "", line.split(" "))))))
boards.append(temp)


def isWon(board, called):
    for r in board:
        if all(v in called for v in r):
            return True
    for c in range(len(board[0])):
        col = []
        for r in range(len(board)):
            col.append(board[r][c])
        if all(v in called for v in col):
            return True
    return False

def getUncalled(board, called):
    uncalled = []
    for r in board:
        for num in r:
            if num not in called:
                uncalled.append(num)
    return uncalled

called = set()
done = False
for num in winners:
    if done:
        break
    called.add(num)
    for board in boards:
        if isWon(board, called):
            print(f"Part 1: {num*sum(getUncalled(board, called))}")
            done = True
            break
finalNum = 0
called = []
finalBoard = None
done = False
for num in winners:
    if done:
        break
    called.append(num)
    for board in boards:
        if isWon(board, called):
            boards.remove(board)
        if len(boards) == 1:
            finalBoard = boards[0]
        elif len(boards) == 0:
            done = True
            finalNum = num
            break
print(f"Part 2: {finalNum*sum(getUncalled(finalBoard, called))}")