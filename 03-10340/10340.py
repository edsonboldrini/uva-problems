def solve(charactersCost, charactersList):
    price = 0.0
    for c in charactersList:
        if(c in charactersCost.keys()):
            price += charactersCost[c]
    finalCost = str(round(price, 2)).split('.')
    if(len(finalCost[1]) == 1):
        completeZero = finalCost[1].ljust(2, '0')        
        finalCost.pop(1)
        finalCost.append('.') 
        finalCost.append(completeZero) 
        finalCost = ''.join(finalCost)
        print(finalCost+'$')
    else:
        print(str(round(price, 2))+'$')

def main():    
    try:
        line = input()
        numberOfTests = int(line)
        # print(numberOfTests)
        for i in range(numberOfTests):            
            try:
                line = input()
                numberOfPaidCharacters = int(line)
                # print(numberOfPaidCharacters)
                charactersCost = {}
                for j in range(numberOfPaidCharacters):
                    try:
                        line = input()
                        data = line.split(' ')
                        charactersCost[data[0]] = float(data[1])/100
                    except EOFError:
                        break
                # print(charactersCost)
                try:
                    line = input()
                    numberOfTextLines = int(line)
                    charactersList = []
                    for k in range(numberOfTextLines):
                        try:
                            line = input()
                            data = [char for char in line]
                            for c in data:
                                charactersList.append(c)
                        except EOFError:
                            break
                    # print(charactersList)
                    solve(charactersCost, charactersList)
                except EOFError:
                    break
            except EOFError:
                break            
    except EOFError:
        print("No lines")  

if __name__ == "__main__":
    main()