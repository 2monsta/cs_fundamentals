def selection_sort(a):
	for i in range(len(a)):
		minIndex = i
		for j in range(i, len(a)):
			if a[j] < a[minIndex]:
				minIndex = j
		a[i], a[minIndex] = a[minIndex], a[i]
	return a

a = [3,5,6,1,3,4]
print selection_sort(a);