money = int(input())
count = 0

count += money // 50000
money %= 50000
count += money // 10000
money %= 10000
count += money // 5000
money %= 5000
count += money // 1000
money %= 1000
count += money // 500
money %= 500
count += money // 100
money %= 100
count += money // 50
money %= 50

print(f"answer = {count}")
