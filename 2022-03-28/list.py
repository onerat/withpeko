# 공백을 둔 문자열 숫자들이 주어진다.
# 문자열의 모든 숫자의 합계를 구하여라
# hint*  split()는 문자열 메소드이다. 인수 값을 기준으로 문자열 배열을 생성시켜준다. 


string = input()
str_list = string.split()
s = 0
for i in str_list:
    s += int(i)
print(s)

