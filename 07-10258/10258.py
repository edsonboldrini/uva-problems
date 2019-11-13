from operator import itemgetter

def solve(submissions):
    contestants = {}
    # for s in submissions:        
    for s in submissions:
        result = s[3]
        contestant = s[0]
        if (result in ["C", "I"]):
            if (result == "C"):
                if(contestant not in contestants):
                    contestants[contestant] = [int(contestant), 1, int(s[2])]
                else:
                    contestants[contestant] = [int(contestant), int(contestants[contestant][1])+1, int(contestants[contestant][2])+int(s[2])]
            else:
                if(contestant not in contestants):
                    contestants[contestant] = [int(contestant), 0, 20]
                else:
                    contestants[contestant] = [int(contestant), int(contestants[contestant][1]), int(contestants[contestant][2])+20]
        else:
            if(contestant not in contestants):
                    contestants[contestant] = [int(contestant), 0, 0]

    contestants = [v for v in contestants.values()]
    contestants = sorted(contestants, key=itemgetter(0))
    contestants = sorted(contestants, key=itemgetter(2))
    contestants = sorted(contestants, key=itemgetter(1), reverse=True)
    
    for c in contestants:
        print(c[0], c[1], c[2])
    print("")

def main():
    try:
        line = input()
        numberOfTests = int(line)
        blankLine = input()
        for i in range(numberOfTests):
            submissions = []
            line = input()
            while(line != ""):
                try:                
                    submissions.append(line.split(' '))
                    line = input()
                except EOFError:
                    break
            solve(submissions)
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
