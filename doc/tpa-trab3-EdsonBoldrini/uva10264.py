# Problem: UVA 10264 - The Most Potent Corner
# Author(s): Edson Boldrini


def solve(numberOfDimensions, weights):
    potencies = {}
    for w in weights:
        acc = 0
        for i in range(len(w)):
            if (w[i] == '0'):
                neighbour = w[:i] + '1' + w[i + 1:]
            elif(w[i] == '1'):
                neighbour = w[:i] + '0' + w[i + 1:]
            acc += weights[neighbour]
        potencies[w] = acc
    maxPotency = 0
    for p in potencies:
        for i in range(len(p)):
            if (p[i] == '0'):
                neighbour = p[:i] + '1' + p[i + 1:]
            elif(p[i] == '1'):
                neighbour = p[:i] + '0' + p[i + 1:]
            neighbouringPotency = potencies[p] + potencies[neighbour]
            if(neighbouringPotency > maxPotency):
                maxPotency = neighbouringPotency
    print(maxPotency)


def main():
    try:
        line = input()
        numberOfDimensions = int(line)
        while(line != ""):
            try:
                weights = {}
                for i in range(2**numberOfDimensions):
                    try:
                        line = input()
                        weights[(bin(i).replace('0b', '')).rjust(
                            numberOfDimensions, '0')] = int(line)
                    except EOFError:
                        break
                solve(numberOfDimensions, weights)
                line = input()
                numberOfDimensions = int(line)
            except EOFError:
                break
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
