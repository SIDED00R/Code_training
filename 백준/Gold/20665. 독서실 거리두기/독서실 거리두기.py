Max_time=60*12
MAX_NUM=10**9

def time_converter(state):
    hour=int(state[:2])
    minute=int(state[2:])
    converted_time=(hour-9)*60+minute
    return converted_time

def add_schedule(start,end):
    if start==720:
        return
    if sum(arr[start]) == 0:
        idx=0
    else:
        pos_arr=[]
        for i in range(N):
            if arr[start][i]!=0:
                pos_arr.append(i)
        idx=0
        mscore = 0
        for i in range(N):
            score = MAX_NUM
            for j in pos_arr:
                score=min(abs(i-j),score)
            if score==0:
                continue
            if score>mscore:
                mscore=score
                idx=i
    for i in range(start,end):
        arr[i][idx]=1

N,T,P=map(int,input().split())
arr = [[0 for i in range(N)] for _ in range(Max_time)]

time_arr = [list(map(time_converter,input().split())) for i in range(T)]
time_arr.sort()
for i in range(T):
    add_schedule(*time_arr[i])
cnt=0
for i in range(Max_time):
    cnt+=arr[i][P-1]
print(Max_time-cnt)