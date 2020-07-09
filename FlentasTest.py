userInput = int(input())
for i in range(userInput):
    numofPersons = int(input())
    persons = list(map(int, input().split()))
    ordered = sorted(persons)
    result = 0
    while numofPersons > 3:
        op1 = ordered[0] + (2 * ordered[1]) + ordered[numofPersons - 1]
        op2 = (2 * ordered[0]) + ordered[numofPersons - 1] + ordered[numofPersons - 2]
        result = result + min(op1, op2)
        numofPersons = numofPersons - 2

    if numofPersons == 3:
        result = result + sum(ordered[0:3])
    elif numofPersons == 2:
        result = result + ordered[1]
    else:
        result = result + ordered[0]
    print(result)



