from itertools import combinations
max([i for i in map(lambda x:x[0]*x[1],combinations([j for j in range(100,1000)],2))if str(i)==str(i)[::-1]])
