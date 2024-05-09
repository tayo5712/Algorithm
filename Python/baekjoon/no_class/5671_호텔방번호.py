while True:
	try:
		res = 0
		a, b = input().split()
		for i in range(int(a), int(b) + 1):
			if len(set(str(i))) == len(str(i)):
				res += 1
		print(res)
	except:
		break
