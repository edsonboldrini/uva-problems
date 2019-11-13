def solve(acc):
    acc.sort()
    median = 0
    if(len(acc)%2 == 1):
        median = int(acc[(len(acc)//2)])
    else:
        median = (int(acc[(len(acc)//2)-1]) + int(acc[len(acc)//2]))//2
    print(median)

def main(): 
    try:
        line = input()
        acc = []
        while line:
            acc.append(int(line))
            solve(acc)                        
            try:
                line = input()
            except EOFError:
                break
    except EOFError:
        print("No lines")   

if __name__ == "__main__":
    main()