# Problem: UVA 11988 - Broken Keyboard (a.k.a. Beiju Text)
# Author(s): Edson Boldrini


def solve(sentence):
    resultSentence = ""
    cursor = len(resultSentence)
    for c in sentence:
        if(c == "["):
            cursor = 0
        elif(c == "]"):
            cursor = len(resultSentence)
        else:
            if (cursor == 0):
                resultSentence = c + resultSentence
            elif (cursor > 0 and cursor < len(resultSentence)):
                resultSentence = resultSentence[:cursor] + \
                    c + resultSentence[cursor:]
            elif (cursor == len(resultSentence)):
                resultSentence = resultSentence + c
            cursor += 1

    print(resultSentence)


def main():
    try:
        line = input()
        while(line != ""):
            try:
                solve(line)
                line = input()
            except EOFError:
                break
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
