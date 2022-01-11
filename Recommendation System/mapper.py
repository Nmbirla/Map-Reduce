import itertools
import sys

op_mapper = []
fri_comb =[]
# Lines = input_data.readlines() # comment this
# for line in Lines: # comment this
for line in sys.stdin: # uncomment this
    fall =[]
    line = line.strip().split('\t')
    user = int(line[0])
    if line[1]:
        friends = list(sorted(map(int,line[1].split(','))))
    fall = friends
    fall.append(user)

    for fpair in itertools.combinations(fall,2):
        pair = list(sorted(map(int,fpair)))
        notAfriend = 1
        if (pair[0] == user) or (pair[1] == user):
            notAfriend = 0
        # print(pair[0],'\t',pair[1],'\t',notAfriend)
        print("{0}\t{1}\t{2}".format(pair[0], pair[1], notAfriend))