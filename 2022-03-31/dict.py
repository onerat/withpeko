n = int(input())
pokemon = {}

for i in range(n):
    while True:
        count = input().split()
        count[1] = int(count[1])
        if count[0] == '없음':
            break
        if count[0] in pokemon:
            pokemon[count[0]] += count[1]
        else:
            pokemon[count[0]] = count[1]

keys = list(pokemon.keys())
keys.sort()     
for key in keys:
    print(f"{key}: {pokemon[key]}")

