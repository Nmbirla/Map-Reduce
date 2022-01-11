import sys

def sortAndtrunk(lst):
    lst = sorted(lst, key=lambda x: (-1 * x[1], x[0]))
    top10 = lst[0:min(len(lst), 10)]
    return [rec[0] for rec in top10]


keys = []
kv = []
# Lines = MapOut.readlines() # comment this
# for line in Lines: # comment this
for line in sys.stdin:  # uncomment this
    line = line.strip().split('\t')
    key = (int(line[0]), int(line[1]))
    keys.append(key)
    kv.append([key, int(line[2])])
ukeys = list(set(keys))
R1_out = []
for key in ukeys:
    MutualFriends = 0
    isFriend = 0
    for i in range(len(kv)):
        if kv[i][0] == key:
            MutualFriends += kv[i][1]
            if kv[i][1] == 0:
                isFriend = 1
    R1_out.append([key[0], key[1], MutualFriends, isFriend])

person = {}
for row in R1_out:
    p1, p2 = row[0:2]
    if p1 not in person.keys():
        person[p1] = []
    if p2 not in person.keys():
        person[p2] = []
    if row[3] != 1:
        person[p1].append(row[1:3])
        person[p2].append([row[0], row[2]])

for x in person:
    print(x, ':', sortAndtrunk(person[x]))