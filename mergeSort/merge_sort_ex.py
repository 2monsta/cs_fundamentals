import numpy
import numpy.random as r

def merge_and_sort(first_array, second_array):
	newArr = [];
	while(len(first_array) !=0  and len(second_array) !=0):
		if(first_array[0] > second_array[0]):
			newArr.append(second_array.pop(0));
		elif(first_array[0] < second_array[0]):
			newArr.append(first_array.pop(0));
		if(len(first_array)==0):
			newArr = newArr + second_array
		elif(len(second_array)==0):
			newArr = newArr + first_array
	return newArr;

a = [1, 3, 5]
b = [2, 4, 6]

# print merge_and_sort(a, b);




def merge_sort(a):
	if len(a) == 1:
		return a
	else:
		mid = len(a)/2
		firstHalf = a[:mid]
		secondHalf = a[mid:]
		return merge_and_sort(merge_sort(firstHalf),merge_sort(secondHalf))




random_array = r.random_integers(0, 100, 10).tolist()
# print random_array

sorted_array = merge_sort(random_array)
# print sorted_array



# square all the numberss in a sorted aray, maintain the sory


