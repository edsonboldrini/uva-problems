import math

def solve(numbers):
    differences = []
    if (len(differences) == 1):
        print("Jolly")
    else:
        for i in range(len(numbers)-1):
            candidate = abs(numbers[i]-numbers[i+1])
            if (len(differences) == 0 or candidate < len(numbers)):            
                differences.append(candidate)
            else:                        
                break        
        #print(differences)
        jolly = True
        if (0 not in differences):        
            for j in range(1, len(differences)-1):            
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