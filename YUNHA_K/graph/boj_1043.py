import sys
input = sys.stdin.readline

# =========== 풀이 1 =====================
N,M = map(int, input().strip().split())
truth = list(map(int, input().strip().split()))
if len(truth) > 1:
    num_truth_people = truth[0]
    truth_people = truth[1:]
else:
    num_truth_people = 0
    truth_people = []

parties = []
for _ in range(M):
    party = list(map(int, input().strip().split()))
    party_people = party[1:]
    parties.append(party_people)

is_changed = True
while is_changed:
    is_changed = False
    for party in parties:
        is_truth = False
        for person in party:
            if person in truth_people:
                is_truth = True
                break
        if is_truth:
            for person in party:
                if person not in truth_people:
                    truth_people.append(person)
                    is_changed = True

answer = 0
for party in parties:
    can_lie = True
    for person in party:
        if person in truth_people:
            can_lie = False
            break
    if can_lie:
        answer += 1

print(answer)


# =========== 풀이 2 ==============


N,M = map(int, input().strip().split())
truth = list(map(int, input().strip().split()))
num_truth_people = truth[0]
truth_people = truth[1:] if num_truth_people > 0 else []

parties = []
for _ in range(M):
    party = list(map(int, input().strip().split()))
    parties.append(party[1:])

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(parent, x,y):
    a = find(x)
    b = find(y)
    if a != b:
        parent[a] = b

def get_lie_num():
    parent = [i for i in range(N + 1)]
    for party in parties:
        for i in range(len(party) -1):
            union(parent, party[i], party[i+1])

    truth_roots = set()
    for truth in truth_people:
        truth_roots.add(find(parent, truth))

    answer = 0

    for party in parties:
        can_lie = True
        for person in party:
            if find(parent, person) in truth_roots:
                can_lie = False
                break
        if can_lie:
            answer += 1

    return answer

if num_truth_people:
    print(get_lie_num())
else:
    print(M)