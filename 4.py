from itertools import combinations
max([i[0]*i[1]for i in combinations(range(100,1000),2)if str(i[0]*i[1])==str(i[0]*i[1])[::-1]])
