def linear_search(a, num):
	
	for i in range(len(a)):
		if num == a[i]:
			num = i
			break;
	return num;

# a = [5,4,3,2,1]

# print linear_search(a, 1);
a = range(0,20,2);
print a;
def binary_search(a , b):
	start = 0
	end = len(a) -1
	
	while start < end:
		mid = (start + end )/2
		if(a[mid] == b):
			return mid
		elif b > a[mid]:
			start = mid +1
		elif b< a[mid]:
			end = mid -1
		print start, end

print binary_search(a, 17);