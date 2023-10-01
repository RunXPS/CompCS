# 1) split input
# 2) take in teams till limit is reached
# 3) add additional until all are taken
import re


# input
def test():
    # 0 - total teams
    # 1 - total taking
    # 2 - total taking from single team
    usr_input : str = "10 7 3\n3 9\n1 9\n4 9\n5 9\n9 7\n2 7\n6 7\n7 7\n8 5\n10 5\n"
    regex = re.compile("[ \\n]")
    split_input = regex.split(usr_input)
    schools = []
    number_from = []
    output = ""
    overflow = 0
    total_taken = 0
    i = 0
    location = 0
    # until all teams are taken
    while (total_taken != int(split_input[1])):
        try:
            # see if school has already been added
            location = schools.index(split_input[4 + i * 2])
            if (number_from[location] < int(split_input[2]) + overflow):
                # add another
                output += split_input[3 + i * 2] + "\n"
                split_input.pop(3 + i * 2)
                split_input.pop(3 + i * 2)
                total_taken += 1
                number_from[location] += 1
            # if school is added and at max, skip to next one
            else: 
                i += 1
            break
        except ValueError:
            # if new school, add it to the 
            schools.append(split_input[4 + i * 2])
            number_from.append(1)
            output += split_input[3 + i * 2] + "\n"
            split_input.pop(3 + i * 2)
            split_input.pop(3 + i * 2)
            total_taken += 1
        # if max has not been reached
    for j in schools:
        print(j)

test()