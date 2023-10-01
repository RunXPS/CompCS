# len and max speed
details = input().split(" ")
# possible problems
problems = []
for i in range(int(details[0])):
    problems.append(int(input()))
problems.sort()
total = int(details[1]) * 5
counter = 0
while (total >= 0 and counter < int(details[0])):
    total -= problems[counter]
    counter += 1
print(str(counter - 1))