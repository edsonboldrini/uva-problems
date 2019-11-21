def solve(A, B):
    print(A)
    print(B)

def main():
    try:
        line = input()
        while(line != "0"):
            try:
                A = int(line)
                B = []
                line = input()
                while(line != "0"):
                    try:
                        B.append([int(i) for i in line.split(" ")])
                        line = input()
                    except EOFError:
                        break
                solve(A, B)
                print("")
                line = input()
            except EOFError:
                break
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
