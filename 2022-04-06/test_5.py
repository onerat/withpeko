# N번만큼 카페의 메뉴와 가격값을 입력을 받는다.
# 이때 메뉴와 가격을 예쁘게 출력 시켜라. 출력시 메뉴 단어 순서대로 출력 시켜라. (한줄에 메뉴 3개씩 출력)
# 입력값중 메뉴가 중복 되었을 경우 제일 과거의 가격을 출력 시킨다.
# 
# input
# 5
# 아이스아메리카노 1500
# 바닐라라때 2000
# 달고나라때 3500
# 딸기스무디 4000
# 아이스아메리카노 2000


# 달고나라때:3500원      
# 딸기스무디: 4000원     
# 바닐라라때: 2000원     
# 아이스아메리카노: 1500원     

n = int(input())
menu = dict()
for i in range(n):
    menu_name, menu_price = input().split()
    if not (menu_name in menu):
      menu[menu_name] = menu_price

keys = sorted(menu.keys())

for key in keys:  
  print(f"{key}:{menu[key]}원     ")