import sys

# Lines = inputmat.readlines() # comment this
#     for line in Lines: # comment this
for line in sys.stdin: # uncomment this
    line = line.strip().split('\t')
    max_rowM = int(line[0])
    max_colN=int(line[1])
    if float(line[2]) == 0: # Check if matrix is M
        M=line[2]
        i=int(line[3])
        j=int(line[4])
        Mij=line[5]
        for itr in range(max_colN):
            print("{0}\t{1}\t{2}\t{3}\t{4}".format(i, itr, M, j, Mij))
    else:
        N=line[2]
        j=int(line[3])
        k=int(line[4])
        Njk=line[5]
        for itr in range(max_rowM):
            print("{0}\t{1}\t{2}\t{3}\t{4}".format(itr, k, N, j, Njk))

