n = int(input())
peko = set()
pepe = set()

for i in range(n):
    count = input().split()
    peko.add(count[0])
    pepe.add(count[1])

answers = list(peko & pepe)
answers.sort()
for answer in answers:
    print(answer)