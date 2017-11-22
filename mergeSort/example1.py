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

a = [-4, -3, -2,-1,0,1,2,3,4,5]
for i in range(len(a)):
	smallest_abs_index = 0
	if(abs(a[i])< abs(a[smallest_abs_index])):
		smallest_abs_index = i;

merge_and_sort([], []);