# n은 1 이상의 수를 입력 받는다
# 길이가 n인 정사각형을 출력하라

# input
# n = 2
# output
# **
# **

# n = int(input())
# if n <= 0:
#     print(f"{n} 은 0보다 작은 수입니다. ")
# else:
#     for j in range(n):
#         for i in range(n):
#             print("*", end="")
#         print()

x = int(input())
y = int(input())

if x <= 0 or y <= 0:
    print(f"{x} 또는 {y}는 0보다 작은 수입니다. ")
else:
    for j in range(y):
        for i in range(x):
            print("*", end="")
        print()        