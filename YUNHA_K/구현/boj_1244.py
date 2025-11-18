import sys

def chagne_switch(switch_num):
    if switches[switch_num - 1] == 1:
        switches[switch_num - 1] = 0
    else:
        switches[switch_num - 1] = 1

def male_stu(switch_num):
    for i in range(1, N // switch_num + 1):
        chagne_switch(switch_num * i)

def female_stu(switch_num):
    center_idx = switch_num - 1
    chagne_switch(switch_num)

    k = 1
    while True:
        left_idx = center_idx - k
        right_idx = center_idx + k

        if 0 <= left_idx < N and 0 <= right_idx < N and \
                switches[left_idx] == switches[right_idx]:
            chagne_switch(left_idx + 1)
            chagne_switch(right_idx + 1)
            k += 1
        else:
            break


N = int(sys.stdin.readline())
switches = list(map(int, sys.stdin.readline().split()))
num_students = int(sys.stdin.readline())

for _ in range(num_students):
    sex, switch_num = map(int, sys.stdin.readline().split())
    if sex == 1:
        male_stu(switch_num)
    else:
        female_stu(switch_num)

for i in range(0, len(switches), 20):
    print(' '.join(map(str, switches[i:i + 20])))