# 주사위 게임3

def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice.sort()  # 정렬해두면 경우를 구분하기 쉬움

    # 1) 네 개가 모두 같을 때
    if dice[0] == dice[3]:
        return 1111 * dice[0]

    # 2) 세 개가 같을 때
    if dice[0] == dice[2] or dice[1] == dice[3]:
        p = dice[1]  # 세 개가 같은 수
        q = dice[0] if dice[1] != dice[0] else dice[3]  # 다른 수
        return (10 * p + q) ** 2

    # 3) 두 개씩 같을 때
    if dice[0] == dice[1] and dice[2] == dice[3]:
        return (dice[0] + dice[2]) * abs(dice[0] - dice[2])

    # 4) 두 개만 같고 나머지 두 개 다를 때
    if dice[0] == dice[1]:
        return dice[2] * dice[3]
    if dice[1] == dice[2]:
        return dice[0] * dice[3]
    if dice[2] == dice[3]:
        return dice[0] * dice[1]

    # 5) 네 개 다 다를 때
    return dice[0]