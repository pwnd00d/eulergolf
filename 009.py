132 chars:
p=lambda a,b:(a**2+b**2)**.5;a=[(a,b)for a,b in itertools.combinations(range(3,500),2)if a+b+p(a,b)==1000][0];a[0]*a[1]*p(a[0],a[1])

131 chars:
p=lambda a,b:(a**2+b**2)**.5;a=[(a,b,p(a,b))for a,b in itertools.combinations(range(3,500),2)if a+b+p(a,b)==1000][0];a[0]*a[1]*a[2]

121 chars:
a=[(a,b)for a,b in itertools.combinations(range(3,500),2)if a+b+(a**2+b**2)**.5==1000][0];a[0]*a[1]*(a[0]**2+a[1]**2)**.5
