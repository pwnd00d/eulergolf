def two():
	a=b=c=1
	while b<2000**2:
		a,b=b,a+b
		if b%2-1:c+=b
	return c-1

sum([n for n in[int(((.5+5**.5/2)**n-(-.5-5**.5/2)**-n)/5**.5)for n in range(34)]if n%2-1])

r=.5+5**.5/2;sum([n for n in[int((r**n-(-r)**-n)/5**.5)for n in range(34)]if n%2-1])
