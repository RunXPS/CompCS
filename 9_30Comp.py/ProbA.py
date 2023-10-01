# 1) split input
# 2) take in teams till limit is reached
# 3) add additional until all are taken
import re


# input
def test():
    # 0 - total teams
    # 1 - total taking
    # 2 - total taking from single team
    usrInput : str = "10 7 3\n3 9\n1 9\n4 9\n5 9\n9 7\n2 7\n6 7\n7 7\n8 5\n10 5\n"
    regex = re.compile("[ \\n]")
    splitInput = regex.split(usrInput)
    schools = []
    numberFrom = []
    output = ""
    overflow = 0
    totalTaken = 0
    i = 0
    # until all teams are taken
    while (totalTaken < int(splitInput[1])):
        # find if school has already been taken
        location = schools.index(splitInput[4+i*2])
        if (location != -1):
            # if school max has not been reached or total max have been reached,
            if (numberFrom[location] != splitInput[2] + overflow):
                numberFrom += 1
                output += splitInput[3+i*2] + "\n"
                # remove added elements
                splitInput.pop(3+i*2)
                splitInput.pop(3+i*2)
                totalTaken += 1
        else:
            schools.append(splitInput[4+i*2])
            numberFrom.append(1)
            output += splitInput[3+i*2] + "\n"
            splitInput.pop(3+i*2)
            splitInput.pop(3+i*2)
            totalTaken += 1
        i += 1