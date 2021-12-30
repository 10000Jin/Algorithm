# 배낭 채우기 문제


# ---------- 분할 정복기법 ----------
def knapSack_dc(W, wt, val, n):
    if n == 0 or W == 0:                                            
        return 0

    if (wt[n-1] > W):                                              
        return knapSack_dc(W, wt, val, n-1)                         
    else:                                                          
        valWithout = knapSack_dc(W, wt, val, n-1)                  
        valWith = val[n-1] + knapSack_dc(W-wt[n-1], wt, val, n-1)
        return max(valWith, valWithout)


# ---------- 동적 계획법(테이블) ----------
def knapSack_table(W, wt, val, n):
    A = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w-wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)

    return A[n][w]


# ---------- 동적 계획법(메모이제이션) ----------
def knapSack_mem(W, wt, val, n):
    if (mem[n][W] == None):                                             # 해당 인덱스의 항목이 없다면 아직 풀리지 않은 것이므로 풀고 저장
        if n == 0 or W == 0:                                            # 기반 상황 : 물건이 없거나 용량이 0이면 당연히 최대가치 0
            mem[n][W] = 0
            return mem[n][W]

        if (wt[n-1] > W):                                               # 현재 물건의 용량이 총용량보다 크다면 못넣음
            mem[n][W] = knapSack_mem(W, wt, val, n-1)                   # 이때의 최대가치는 그 전에 넣은 것까지의 최대가치
            return mem[n][W]
        else:                                                           # 현재 물건의 용량이 총용량보다 작거나 같다면 넣던지 안넣던지 두가지 선택
            valWith = val[n-1] + knapSack_mem(W-wt[n-1], wt, val, n-1)  # 넣는다면 최대가치는 넣은 항목의 가치와 그 항목을 제외한 그 전에 넣은 항목까지의 최대가치
            valWithout = knapSack_mem(W, wt, val, n-1)                  # 안넣는다면 용량은 변함없고 고려할 물건수는 하나 줄음
            mem[n][W] = max(valWith, valWithout)                        # 두가지 상황에서 최대가치를 저장
            return mem[n][W]

    return mem[n][W]                                                    # 해당 인덱스의 항목이 있다면 이미 풀었던 문제임으로 재사용(memoization)


val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
"""
val = [26, 20, 14, 40, 50]
wt = [3, 2, 1, 4, 5]
W = 6
"""
n = len(val)
print("0-1 배낭문제(분할 정복) : ", knapSack_dc(W, wt, val, n))
print("0-1 배낭문제(분할 정복 table) : ", knapSack_table(W, wt, val, n))

mem = [[None for x in range(W+1)] for x in range(n+1)]
print("0-1 배낭문제(분할 정복 memoization) : ", knapSack_mem(W, wt, val, n))