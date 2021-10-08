a = int(input("Введите целевую систему счисления(2 или 8): "))

if a == 2:
	n = int(input("Введите десятичное число, которое хотите перевести: "))
	b = ''
	while n > 0:
		b = str(n % 2) + b
		n = n // 2
	print(b)
elif a == 8:
	m = int(input("Введите десятичное число , которое хотите перевести: ")) 
	result = ''
	while m > 0:
		result = str(m % 8) + result
		m = m // 8
	print(result)
else:
	print("Не найдена такая система счисления!")