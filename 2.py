def two():
	a=b=c=1
	while b<2000**2:
		a,b=b,a+b
		if b%2-1:c+=b
	return c-1
