import math

def solve(numbers):
    differences = []
    if (numbers[0] == 1 or len(numbers) == 2):
        print("Jolly")
    else:
        for i in range(1, len(numbers)-1):
            candidate = abs(numbers[i]-numbers[i+1])                       
            differences.append(candidate)                                     
        allowedDifferences = [i for i in range(1,numbers[0])]        
        jolly = True
        if(0 not in differences):
            for j in allowedDifferences:                
                if (j not in differences):
                    jolly = False
                    break
            if (jolly):
                print("Jolly")
            else:
                print("Not jolly")
        else:
            print("Not jolly")
    

def main():    
    line = input()        
    while line:
        numbers = line.split(' ')  
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])                                         
        solve(numbers)
        try:
            line = input()
        except EOFError:
            break

if __name__ == "__main__":
    main()