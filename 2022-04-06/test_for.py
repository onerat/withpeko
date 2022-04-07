
n = int(input())

for j in range(n):
    for i in range(j+1):
        if i == 0: 
            print("*", end="")
        else:
            print("*", end="*")
    print()