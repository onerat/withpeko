# 파이썬에서는 메소드는 아래와 같이 선언 가능하다.
def function_name():
  return
# return을 하지 않을경우에는 None값이 반환된다.
print(function_name())

# 메소드 인자는 메소드내에서 필요한 만큼 선언 할 수 있다.
def function(inja):
  return inja
print(function('hello pepe'))

# 인자가 두개 이상이면 인자의 자리를 지켜 줘야한다.
def function(inja1, inja2):
  return inja1 + inja2
print(function('world ', 'hello'))

# 인자의 기본값도 설정 가능하다.
def function(inja='hello peko'):
  return inja
print(function())
print(function('hello pepe'))

# 인자명을 알고 있다면 순서 상관없이 선언 가능하다.
def function(salary, tax):
  return salary - tax
print(function(tax=5000, salary=10000 ))

# 가변인자는 밑과 같이 만들 수 있다. 리스트 형식
def function(*args):
  return args

print(function(1,2,3,4,5,6,7,8))

# 가변인자는 밑과 같이 만들 수 있다. 딕셔너리 형식
def function(**args):
  string = ''
  for key in args.keys():
    string += f"{key}: "
    string += f"{args[key]}   "
  return string

print(function(name='peko', age='28', likes='맥주 컴퓨터 커피'))


# 문제
# 1. sum 메소드를 작성하여라
# sum 메소드는 배열을 입력으로 받았을 경우 1차배열의 합계만 계산한다.