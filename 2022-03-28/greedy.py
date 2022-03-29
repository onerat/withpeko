# 한국에는 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1의 지폐 또는 동전이 있다.
# Peko는 통장에서 N원 만큼을 출금 하려고한다.
# Peko는 많은 지폐 동전을 들고 다니면 무겁고 관리가 까다롭기 때문에 최소한의 지폐와 동전만 가지고 싶어한다.
# 이때 최소한의 동전과 지폐 사용 값을 출력하라.
# 
# input 
# N = 23750
# 50000 = 0
# 10000 = 2
# 5000 = 0
# 1000 = 3
# 500 = 1
# 100 = 2
# 50 = 1
# output
# answer = 9

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