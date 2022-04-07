# 스택에 대한 기능이 `지속적`으로 입력된다.
# 기능을 종료시키고 싶을때는 `END`라는 값을 입력을 하면 입력이 종료된다.
# 예시

# PUSH 숫자 <- Stack에 숫자를 Push한다.
# POP <- Stack에 pop을 한다.
# END <- 입력을 종료한다.

# input
# PUSH 4
# PUSH 3
# POP
# PUSH 1
# PUSH 5
# PUSH 3
# POP
# POP
# END

# output
# [4,1]


stack = []
while True:
    string = input().split()
    if string[0] == "END":
        break
    elif string[0] == "PUSH":
        stack.append(string[1])
    elif string[0] == "POP":
        stack.pop()
print(stack)
