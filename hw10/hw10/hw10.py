
# 편집 거리 문제

def edit_distance_mem(S, T, m, n, mem):
    if m == 0:                                                      # S가 공백이면 T의 모든 문자 S에 삽입
        mem[m][n] = n                                               # 연산 횟수 mem에 저장
        return n
    if n == 0:                                                      # T가 공백이면 S의 모든 문자 삭제
        mem[m][n] = m
        return m

    if mem[m][n] == None:                                           # 계산되지 않은 문제라면 계산
        if S[m-1] == T[n-1]:                                        # 마지막 문자가 같으면
            mem[m][n] = edit_distance_mem(S, T, m-1, n-1, mem)      # 다음 문자로 이동

        else:                                                       # 같지 않다면 대체, 삽입, 삭제중 하나 수행
            mem[m][n] = 1 + \
                min(edit_distance_mem(S, T, m, n-1, mem), edit_distance_mem(S, T, m-1, n, mem), edit_distance_mem(S, T, m-1, n-1, mem))
                                                                    # 3가지 연산중 가장 적은 편집거리를 가진 연산을 사용 연산을 수행했음으로 1더함
        print("mem[%d][%d] = " % (m, n), mem[m][n])                 # 중간 결과 출력

    return mem[m][n]                                                # 이미 계산한 것이라면 바로 사용


def edit_distance_mem_trace(m, n, mem):
    for i in range(m+1):
        for j in range(n+1):
            if str(type(mem[i][j])) == "<class 'NoneType'>":        # 비교를 위해 None인 항목이 있으면 inf(무한)으로 변경
                mem[i][j] = float("inf")

    while not(m == 0 or n == 0):                                    # m과 n중에 하나가 0이 될때까지 반복
        num = min(mem[m-1][n-1], mem[m-1][n], mem[m][n-1])          # 왼쪽 위, 위, 왼쪽 중 가장 작은수 num저장
        
        if num == mem[m][n]:                                        # 지금 편집거리가 num과 같다면
            print("서로 같습니다.")                                 # 두 비교대상 같음
            m -= 1
            n -= 1
        elif num == mem[m-1][n-1]:                                  # num이 왼쪽 위라면
            print("%s를 %s로 대체합니다." % (S[m-1], T[n-1]))       # 대체
            m -= 1
            n -= 1
        elif num == mem[m][n-1]:                                    # num이 왼쪽이라면
            print("%s를 삽입합니다." % T[n-1])                      # 삽입
            n -= 1
        elif num == mem[m-1][n]:                                    # num이 위쪽이라면
            print("%s를 삭제합니다." % S[m-1])                      # 삭제
            m -= 1

    if m == 0:                                                      # m이 0이라면 삽입 연산만 남음
        while not n == 0:                                           # n이 0이 될때까지 삽입연산 반복
            print("%s를 삽입합니다." % T[n-1])                      # 삽입
            n -= 1
    elif n == 0:                                                    # n이 0이라면 삭제연산만 남음
        while not m == 0:                                           # m이 0이 될때까지 반복
            print("%s를 삭제합니다." % S[m-1])                      # 삭제
            m -= 1


S = "hotdognym"
T = "dog"
m = len(S)
n = len(T)
print("문자열: ", S, T)

mem = [[None for _ in range(n+1)] for _ in range(m+1)]
edit_distance_mem(S, T, m, n, mem)
print("편집거리(메모이제이션) = ", edit_distance_mem(S, T, m, n, mem))
print("\n----연산 과정 출력----")
edit_distance_mem_trace(m, n, mem)