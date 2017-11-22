def sumOfMultiple(n):
	sum =0;
	for i in range(0, n):
		if i % 3 == 0 or i%5==0:
			sum+=i;
	print sum;

sumOfMultiple(1000);

# num3 = range(0, 10, 3)
# num5 = range(0,10,5)
# num15 = range(0,10, 3*5)

# def sumOfMultipleBetter(number, max):
# 	sum =0
# 	for i in range(0, max , number):
# 		sum +=i
# 	return sum

# MAX = 1000

# sum = sumOfMultipleBetter(3, MAX) + sumOfMultipleBetter(5, MAX) - sumOfMultipleBetter(15, MAX);

	
