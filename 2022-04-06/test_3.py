# 한 변수에 시험성적(숫자)를 입력으로 받는다.
# 시험성적은 0~100까지의 범위이다. 이 범위를 초과한다면 잘못된 성적이다.
# 잘못된 성적일때는 `성적입력이 잘못 되었습니다.`를 출력한다.
# 범위에 알맞은 성적이 입력이 되었을때에는 학점을 출력한다.
# 학점의 기준은 아래와 같다.
# A+ 100 ~ 95 
# A 94 ~ 90
# B+ 89 ~ 85
# B 84 ~ 80
# C+ 79 ~ 75
# C 74 ~ 70
# F 69 ~ 0
# 시험성적을 기준으로 학점을 `반환`받는  메소드를 작성하고 반환된 값을 출력하라.

def printScore(score):
    answer = ""
    if score > 100:
        answer = "점수가 100 초과하여 잘못된 입력값입니다."
    elif score < 0:
        answer = "점수가 음수이므로 잘못된 입력값입니다."
    elif score >= 95 and score <= 100:
        answer = "A+"
    elif score >= 90 and score <= 94:
        answer = "A"
    elif score >= 85 and score <= 89:
        answer = "B+"
    elif score >= 80 and score <= 84:
        answer = "B"
    elif score >= 75 and score <= 79:
        answer = "C+"
    elif score >= 70 and score <= 74:
        answer = "C"
    elif score >= 0 and score <= 69:
        answer = "F"
    return answer


score = printScore(8)
print(score)