#HW1 Q1 Product purchasing problem: 
#HW1 Q1 商品購買問題: 

#Question:
# There is a person who loves to eat scallion pancakes and drink grapefruit green tea the most. Tonight, he takes out x dollars from his wallet and goes to the Gongguan Night Market. He plans to pass by a stall selling scallion pancakes for p1 dollars and a beverage shop selling grapefruit green tea for p2 dollars in order. He will try to buy a scallion pancake first, and if he doesn't have enough money, he will skip it. Whether or not he buys the scallion pancake, he will then try to buy a cup of grapefruit green tea, and if he doesn't have enough money, he will skip it. After visiting both stalls, he will return home.
# For example, if he brings 100 dollars out and a scallion pancake costs 40 dollars, he will buy one; then a cup of grapefruit green tea costs 35 dollars, he will buy one; finally, he will return home with 25 dollars. If he brings 100 dollars out and a scallion pancake costs 40 dollars, he will buy one; then a cup of grapefruit green tea costs 95 dollars, he will skip it; finally, he will return home with 60 dollars.

# Please write a program to input the above information and calculate the amount of money he has left after returning home.

#題目：
# 有一個人，最喜歡吃蔥抓餅跟喝葡萄柚綠茶。今晚他從錢包拿出 x 元，走向公館夜市，準備依 序經過了一張蔥抓餅賣 p1 元的攤子，以及一杯葡萄柚綠茶賣 p2 元的飲料店。他會先試著買一張蔥抓餅，此時錢不夠他就跳過;不論是否買了蔥抓餅，他會接著試著買一杯葡萄柚綠茶，此時錢不夠他就跳過。逛完兩攤之後他就回家。
# 舉例來說，如果他帶 100 元出門，蔥抓餅一張 40 元，他就會買一張;接著葡萄柚綠茶一杯 35 元， 他就會買一杯;最後他帶著 25 元回家。如果他帶 100 元出門，蔥抓餅一張 40 元，他就會買一張;接 著葡萄柚綠茶一杯 95 元，他就會跳過不買;最後他帶著 60 元回家。

# 請寫一個程式，讀入上述資訊，並計算出他回家後剩餘的金額。

# My Code
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
