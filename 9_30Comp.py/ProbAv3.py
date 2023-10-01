# first line of
# n - number of teams
# k - number of teams advancing
# c - number from each team 
f = input()
m = [f]
n, k, c = [int(i) for i in f.split(" ")]
for i in range(n):
    line = input()
    m.append(line)
# nl - int list of nu,bers
nl = [[int(j) for j in k] for k in [i.split(" ") for i in m]]
n, k, c = nl[0]

d = {id:0}
mc = [0] * (len(nl) - 1)
# iterate through integer list
for i in range(1, len(nl)):
    if nl[i][1] not in d.keys():
        d[nl[i][1]] = 1
    else:
        d[nl[i][1]] += 1
    if d[nl[i][1]] <= c and sum(mc) < k:
        mc[i - 1] = 1
        #print(mc, n, k, c, sum(mc))

for i in range(len(mc)):
    if not sum(mc) == k:
        mc[i] = 1

for i in range(1, len(nl)):
    if mc[i - 1]:
        print(nl[i][0])

#print(mc)