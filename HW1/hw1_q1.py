x = int(input()) 
p1 = int(input()) 
p2 = int(input())

'''after_booth_1 = x - p1
after_booth_2 = after_booth_1 - p2

if after_booth_1 >= 0 and after_booth_2 >= 0 :
	print(after_booth_2)
elif after_booth_1 >= 0 and after_booth_2 < 0 :
	print(after_booth_1)
elif after_booth_1 < 0 and after_booth_2 >= 0 :
	print()
else :
	print(x)'''

if (x-p1) >= 0 :
	if (x-p1-p2) >= 0 :
		print(x-p1-p2)
	else :
		print(x-p1)
else :
	if (x-p2) >= 0 :
		print(x-p2)
	else :
		print(x)