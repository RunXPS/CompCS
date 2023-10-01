# take in input
#usr_input : str = "5 1 5\n1\n2\n4\n3\n"
details = input().split(" ")
usr_input = []
MIN_MET = False
MAX_MET = False
# get next lines
for i in range(int(details[0])-1):
    usr_input.append(input())
# check if min & max are present
for x in usr_input:
    if (x == details[1]):
        MIN_MET = True
    if (x == details[2]):
        MAX_MET = True
    if (int(x) > int(details[2]) or int(x) < int(details[1])):
        MIN_MET = False
        MAX_MET = False
        break
#try: 
#    usr_input.index(details[1])
#    MIN_MET = True
#except ValueError:
#    pass
#try: 
#    usr_input.index(details[2])
#    MAX_MET = True
#except ValueError:
#    pass

# for each possible case
if (not MIN_MET and not MAX_MET):
    print("-1\n")
elif (not MIN_MET):
    print(details[1])
elif (not MAX_MET):
    print(details[2])
else:
    out_str = ""
    i = int(details[1])
    while (i <= int(details[2])):
        out_str += str(i) + "\n"
        i += 1
    print(out_str)