n,c = input().split(',')
pStr = input()
p = pStr.split(',')
qStr = input()
q = qStr.split(',')

c = int(c)
profit = -100000
max_profit = -10000000 #以防算出來最大獲利是負的
optimal_price = -10000000
optimal_quantity = -10000000

for i in range(len(p)) :
	p[i] = int(p[i])
	q[i] = int(q[i])
	profit = (p[i] - c) * q[i]

	if (profit > max_profit) :
		max_profit = profit 
		optimal_price = p[i]
		optimal_quantity = q[i]
	elif (profit == max_profit) :
		max_profit = profit 
		if (q[i] > optimal_quantity) :
			optimal_quantity = q[i]
			optimal_price = p[i]
	else :
		continue

print(str(optimal_price) + "," + str(max_profit))
