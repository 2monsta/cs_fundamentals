def inserstion_sort(a):
	for i in range(len(a)):
		temp = a[i]
		j = i
		while j > 0 and a[j-1]>temp:
			a[j] = a[j-1]
			j-=1
		a[j] = temp
	return a;

a= [5, 4, 3, 2, 1]

print inserstion_sort(a);