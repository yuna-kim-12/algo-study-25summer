from collections import defaultdict

def solution(genres, plays):
    answer = []
    best_plays = defaultdict(list)
    for i in range(len(genres)):
        best_plays[genres[i]].append([plays[i], i])

    #장르 내 재생수 정렬(많이 재생된 음악, 같은 재생 수일 경우 낮은 고유번호)
    for value in best_plays.values():
        value.sort(key=lambda x: (-x[0], x[1]))

    total = {}
    for k, v in best_plays.items():
        # s = sum(x[0] for x in v)
        s = 0
        for x in v:
            s += x[0]
        total[k] = s
    # 장르 재생 수 합 정렬
    # total_plays = dict(sorted(total.items(), key=lambda x:x[1], reverse=True))
    total_plays = sorted(total, key=lambda x: total[x], reverse=True)

    # 문제 보면 palys길이는 1일수도 있음.
    for genre in total_plays:
        for play_info in best_plays[genre][:2]:
            answer.append(play_info[1])
    print(best_plays)
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))