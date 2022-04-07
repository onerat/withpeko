# 한 변수에 숫자를 입력을 받는다.
# 그 수만큼 삼각형 탑을 만들어라
# 
# input 
# 3
# output
# *
# **
# ***
# 
# input
# 5
# output
# *
# **
# ***
# ****
# *****

n = int(input())

for j in range(n):
    for i in range(j+1):
        print("*", end="")
    print()