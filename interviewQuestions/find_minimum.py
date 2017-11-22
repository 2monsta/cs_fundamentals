def find_minimum(a):
	lowest = 0;
	for i in range(1, len(a)):
		if a[i]<a[i-1]:
			lowest = a[i]
	return lowest;

a = [12,3,5,-3,20]
print find_minimum(a)