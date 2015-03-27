sum([i for i in range(1000) if not i%3 or not i%5])
sum(i for i in range(1000) if not(i%5 and i%3))
