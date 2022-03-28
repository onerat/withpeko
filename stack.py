
# 숫자 N과 공백을 둔 문자열 숫자들을 입력 받음
# 이때 공백을 둔 문자열의 숫자를 배열로 만들고 그 배열에 숫자 N이 포함되어 있을 경우 N을 삭제시킨다
# 오름차순으로 정렬된 배열을 클릭하라
# hint* list.sort()를 하면 배열을 정렬할 수 있다. 
# hint* list.sort(reverse=True) 내림차순

n = input()
string = input().split()
stack = []
for i in string:
    if n != i: 
        stack.append(int(i))
stack.sort()
print(stack)