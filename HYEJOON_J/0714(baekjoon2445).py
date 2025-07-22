N = int(input())

for i in range(1,N+1):
    print(i*'*' + ((2*N)-(i*2))*' ' + i*'*')

for j in range(N-1, 0, -1):
    print(j*'*' + ((2*N)-(j*2))*' ' + j*'*')
