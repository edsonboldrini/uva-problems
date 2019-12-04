# Problem: UVA 10920 - Spiral Tap
# Author(s): Edson Boldrini

import math


def solve(numbers):
    borderSize = int(numbers[0])
    numberToFind = int(numbers[1])

    center = (borderSize//2)+1

    if(numberToFind == 1):
        print("Line = %d, column = %d." % (center, center))
    else:
        i = 3
        while(numberToFind > i*i):
            i += 2
        lb = (i-2)*(i-2)
        pad = (borderSize-i)/2

        column = center
        line = center

        if(numberToFind <= lb + i-1):
            column = lb+i-numberToFind+pad
            line = borderSize-pad
        elif(lb + i-1 < numberToFind and numberToFind <= lb + 2*(i-1)):
            column = pad+1
            line = lb+(i-1)*2+1-numberToFind+pad
        elif(lb + 2*(i-1) < numberToFind and numberToFind <= lb + 3*(i-1)):
            column = numberToFind-(lb+2*(i-1))+pad+1
            line = pad+1
        else:
            column = borderSize-pad
            line = numberToFind-(lb+3*(i-1))+pad+1

        print("Line = %d, column = %d." % (line, column))


def main():
    try:
        line = input()
        while line:
            numbers = line.split(' ')
            if(numbers[0] == '0' and numbers[1] == '0'):
                break
            solve(numbers)
            try:
                line = input()
            except EOFError:
                break
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
