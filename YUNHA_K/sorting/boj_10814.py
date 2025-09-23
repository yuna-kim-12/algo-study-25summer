import sys
input = sys.stdin.readline

N = int(input())
people = []
for _ in range(N):
    age, name = input().split()
    people.append((int(age), name))

people.sort(key=lambda person: person[0])
for person in people:
    print(*person)