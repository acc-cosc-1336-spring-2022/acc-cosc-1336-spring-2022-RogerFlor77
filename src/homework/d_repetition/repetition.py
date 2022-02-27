def get_factorial(n):
	result = 1
	for i in range(1,n+1):
		result = result*i
	return result

n = int(input('Enter a number: '))
result = get_factorial(n)
print(result)

n = 20
total_numbers = n

Odd = int(input("Enter the input"))
total = 0
for number in range(1, Odd+1):
    if(number % 2!=0):
        print(number)
        total = total + number
print("The sum of odd numbers", total)