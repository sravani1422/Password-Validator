t = int(input())
for i in range(t):
	n = input()
	digit = []
	upper = []
	lower = []
	if(len(n)>=6 and len(n)<=20):
		for i in n:
			if(i.isdigit()):
				digit.append(i)
			elif(i.isupper()):
				upper.append(i)
			elif(i.islower()):
					lower.append(i)
	if(len(digit)>=1 and len(upper)>=1 and len(lower)>=1):
		print("True")
	else:
		print("False")
