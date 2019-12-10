# Problem: UVA 1062 - Containers
# Author(s): Edson Boldrini


def solve(containers):
    stacks = []
    for c in containers:
        pushed = False
        for j in range(len(stacks)):
            if (stacks[j][-1] >= c):
                pushed = True
                stacks[j].append(c)
                break
        if (not pushed):
            stacks.append([c])

    return len(stacks)


def main():
    try:
        i = 1
        stacks = 0
        line = input()
        while(line != "end"):
            try:
                containers = line
                stacks = solve(containers)
                print("Case %d: %d" % (i, stacks))
                i += 1
                line = input()
            except EOFError:
                break
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
