# Problem: UVA 514 - Rails
# Author(s): Edson Boldrini


def solve(N, cars):
    stack = []

    while(len(stack) > 0):
        stack.pop()
    j = 0
    for i in range(N):
        c = cars[i]
        if(c == 0):
            break

        while(j < N and j != c):
            if(len(stack) > 0 and stack[-1] == c):
                break
            j += 1
            stack.append(j)
        if(len(stack) > 0 and stack[-1] == c):
            stack.pop()
    if(len(stack) == 0):
        print("Yes")
    else:
        print("No")


def main():
    try:
        line = input()
        while(line != "0"):
            try:
                N = int(line)
                cars = []
                line = input()
                while(line != "0"):
                    try:
                        cars = [int(i) for i in line.split(" ")]
                        solve(N, cars)
                        line = input()
                    except EOFError:
                        break
                print("")
                line = input()
            except EOFError:
                break
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
