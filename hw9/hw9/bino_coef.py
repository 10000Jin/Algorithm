# 이항 계수 구하기


# ------------------ 분할 정복기법 ----------------
def bino_coef_dc(n, k):
    if k == 0 or k == n:
        return 1
    return bino_coef_dc(n-1, k-1) + bino_coef_dc(n-1, k)


# ------------------ 동적 계획법(테이블) ----------------
def bino_coef_table(n, k):
    C = [[-1 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]


# -------------- 동적 계획법(메모이제이션) -------------
def bino_coef_mem(n, k):
    if (mem[n][k] == None):                                             # 해당 인덱스의 항목이 없다면 문제를 아직 풀지 않은 것이므로 풀고 저장
        if k == 0 or k == n:                                            # 기반 상황 : nC0 또는 nCn은 모두 1
            mem[n][k] = 1
        else:                                                           # 다른 일반적인 상황이라면
            mem[n][k] = bino_coef_mem(n-1, k-1) + bino_coef_mem(n-1, k) # n번째 원소 뽑을 때 : n-1Ck-1 와 n번째 원소 뽑지 않을 때 : n-1Ck의 합
    return mem[n][k]                                                    # 해당 인덱스의 항목이 있다면 이미 풀린 문제이므로 재사용(memoization)



#n = 6
#k = 3
#n = 10
#k = 4
n = 15
k = 7
print("[Divide and Conquer] C(%d, %d) = " % (n, k), bino_coef_dc(n, k))
print("[Dynamic Programming(table)] C(%d, %d) = " % (n, k), bino_coef_table(n, k))

mem = [[None for _ in range(k+1)] for _ in range(n+1)]
print("[Dynamic Programming(memoization)] C(%d, %d) = " % (n, k), bino_coef_mem(n, k))