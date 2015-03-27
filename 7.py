N=7**6;sorted(reduce((lambda r,x:r-set(range(x**2,N,x))if(x in r)else r),range(2,N),set(range(2,N))))[10000]
