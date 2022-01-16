#N = int(input())
#arr = list(map(int, input().split()))
#M = int(input())
#qst = list(map(int, input().split()))

N = 5
arr = "2 52 23 55 100"
M = 4
qst = ['5', '2', '55', '99']

for x in range(len(qst)):
    if arr.find(qst[x]) != -1:
        print(1, end=" ")
    else:
        print(0, end=" ")
