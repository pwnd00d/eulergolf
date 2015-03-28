sum(filter(lambda x:not sum([i for i in range(2,int(x**.5)+1) if x%i == 0]),range(2,2000000)))
