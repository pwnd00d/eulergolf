import math
sum([i for i in range(3,1000000) if sum([math.factorial(int(x)) for x in str(i)])==i])
