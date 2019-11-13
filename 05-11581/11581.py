dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def check(x, y):
    return x >= 0 and x < 3 and y >= 0 and y < 3


def solve(firstLine, secondLine, thirdLine):
    response = -1
    if(not (firstLine == "000" and secondLine == "000" and thirdLine == "000")):
        grid = []
        f = []
        s = []
        t = []
        f.append(int(firstLine[0]))
        f.append(int(firstLine[1]))
        f.append(int(firstLine[2]))
        s.append(int(secondLine[0]))
        s.append(int(secondLine[1]))
        s.append(int(secondLine[2]))
        t.append(int(thirdLine[0]))
        t.append(int(thirdLine[1]))
        t.append(int(thirdLine[2]))
        grid.append(f)
        grid.append(s)
        grid.append(t)
        newGrid = [[None, None, None], [None, None, None], [None, None, None]]
        while (True):
            allZeros = True
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if (grid[i][j] != 0):
                        allZeros = False

            if (allZeros):
                break

            count = 0
            for i in range(len(grid)):
                for j in range(len(grid)):
                    count = 0
                    for m in range(len(dy)):
                        if (check(i + dx[m], j + dy[m])):
                            count += grid[i + dx[m]][j + dy[m]]
                    newGrid[i][j] = count % 2

            response += 1
            for i in range(len(grid)):
                for j in range(len(grid)):
                    grid[i][j] = newGrid[i][j]

    print(response)


def main():
    try:
        line = input()
        numberOfTests = int(line)
        for i in range(numberOfTests):
            try:
                blankLine = input()
                firstLine = input()
                secondLine = input()
                thirdLine = input()
                solve(firstLine, secondLine, thirdLine)
            except EOFError:
                break
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
