# Problem: UVA 12247 - Jollo
# Author(s): Edson Boldrini

import sys


def solve(princessCards, princeCards):
    princessCards.sort(reverse=True)
    princeCards.sort(reverse=True)
    if (princessCards[0] > princeCards[0] and princessCards[1] > princeCards[1]):
        n = -1
    elif(princessCards[0] < princeCards[0] and princessCards[0] < princeCards[1]):
        n = 1
        while n in princessCards or n in princeCards:
            n += 1
    else:
        n = princessCards[1]+1
        while n in princessCards or n in princeCards:
            n += 1
        if (princessCards[0] > n and princessCards[1] > princeCards[1]):
            n = princessCards[0]+1
            while n in princessCards or n in princeCards:
                n += 1

    if (n > 52):
        n = -1

    print(n)
    # print("---")


def main():
    princess = []
    prince = []
    try:
        line = input()
        while line:
            cards = line.replace('\n', '').split(' ')
            if(cards == ['0', '0', '0', '0', '0']):
                break
            for i in range(len(cards)):
                cards[i] = int(cards[i])
            princess = cards[:3]
            prince = cards[3:]
            solve(princess, prince)
            try:
                line = input()
            except EOFError:
                break
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
