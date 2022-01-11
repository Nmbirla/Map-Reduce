import sys

keys = []
kv = []
# Lines = MapOut.readlines() # comment this
# for line in Lines: # comment this
for line in sys.stdin: # uncomment this
    line = line.strip().split('\t')
    key= (int(line[0]), int(line[1]))
    keys.append(key)
    kv.append([key,[int(line[2]), float(line[3]), float(line[4])]])
ukeys = list(set(keys))
for key in ukeys:
    M=[]
    N=[]
    for i in range(len(kv)):
        if kv[i][0]== key:
            if kv[i][1][0] == 0:
                M.append(kv[i][1][1:])
            else:
                N.append(kv[i][1][1:])
    tsum = 0
    for jm in M:
        for jn in N:
            if jm[0] == jn[0] :
                tsum += jm[1] * jn[1]
    print(key, tsum)

