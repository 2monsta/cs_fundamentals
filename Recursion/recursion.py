def add(array, currentIndex, sum):
	sum+= array[currentIndex]
	if currentIndex == len(array)-1:
		return sum
	else:
		return add(array, currentIndex+1, sum)
	

a = [10, 15, 12, 13]

# print add(a, 0 , 0)



def countDown(number):
	if(number == -1): 
		return
	else:
		print number
		countDown(number-1)



# print countDown(10);


def factorial(n):
	if n <= 0:
		return 1
	else:
		return n * factorial(n-1)
	
print factorial(5)