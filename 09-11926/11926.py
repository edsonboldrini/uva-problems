def solve(oneTimeTasks, repeatingTasks):
    for rt in repeatingTasks:
        start = int(rt.split(" ")[0])
        end = int(rt.split(" ")[1])
        repeat = int(rt.split(" ")[2])
        i = 0
        while(i + start + repeat <= 1000000 + repeat):
            oneTimeTasks.append(str(start + i) + " " + str(end + i))
            i += repeat

    conflict = False
    tasksDone = []
    for ott in oneTimeTasks:
        start = int(ott.split(" ")[0])
        end = int(ott.split(" ")[1])
        for td in tasksDone:
            if((start < td[0] and end > td[1]) or (start >= td[0] and end <= td[1]) or (start > td[0] and start < td[1]) or (end > td[0] and end < td[1])):
                conflict = True
                break
        if (not conflict):
            tasksDone.append((start, end))
        else:
            break        

    if(conflict):
        print("CONFLICT")
    else:
        print("NO CONFLICT")


def main():
    try:
        line = input()
        while(line != "0 0"):
            try:
                oneTimeTasksCount = int(line.split(" ")[0])
                repeatingTasksCount = int(line.split(" ")[1])
                oneTimeTasks = []
                repeatingTasks = []
                for i in range(oneTimeTasksCount):
                    line = input()
                    oneTimeTasks.append(line)
                for j in range(repeatingTasksCount):
                    line = input()
                    repeatingTasks.append(line)
                solve(oneTimeTasks, repeatingTasks)
                line = input()
            except EOFError:
                break
    except EOFError:
        print("No lines")


if __name__ == "__main__":
    main()
