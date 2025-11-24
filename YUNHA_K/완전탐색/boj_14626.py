ISBN = input()
total = 0

for i in range(13):
    weight = 1 if i % 2 == 0 else 3

    if ISBN[i] == '*':
        star_weight = weight
    else:
        total += int(ISBN[i]) * weight

for num in range(10):
    if (total + (num * star_weight)) % 10 == 0:
        print(num)
        break