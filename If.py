

def isPrime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True


for i in range(1, 30):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
