n = int(input())
if n > 100:
    print(f"{n}이 100 보다 큽니다")
elif n < 0:
    print(f"{n}이 0 보다 작습니다")
else:        
    if n % 2 == 0:
        print("짝수")
    else:
        print("홀수")