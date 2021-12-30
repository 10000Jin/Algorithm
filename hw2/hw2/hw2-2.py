import time
str = "ACBDCCDBADCBBC"

print("\n## 억지기법을 활용 ##")
def count_substr(str, A, B):                            # 억지기법
    start = time.time()
    n = len(str)                                        # 문자열의 크기 n에 저장
    count = 0                                           # 부분 문자열 개수 변수 초기화
    
    for i in range(n):                                  # 문자열의 0번지부터 마지막까지
        if str[i] == A:                                 # 해당 번지의 값이 A라면
            for j in range(i+1, n):                     # 다음 번지부터 마지막까지 확인하면서
                if str[j] == B:                         # B가 나온다면
                    count = count + 1                   # count를 1증가

    return count                                        # count 반환


start = time.time()
for i in range(1000000):
    count_substr(str, "A", "B")
end = time.time()
print(str, " ==> ", count_substr(str, "A", "B"))
print("실행시간 : ", end-start)



print("\n## 더 효율적인 알고리즘 ##")
def count_substr_v2(str, A, B):                         # 더 효율적인 알고리즘
    n = len(str)                                        # 문자열의 크기 n에 저장
    count = 0                                           # 부분 문자열 개수 변수 초기화
    list_A = []                                         # A의 번지수를 저장할 리스트
    list_B = []                                         # B의 번지수를 저장할 리스트

    for i in range(n):                                  # 문자열의 0번지부터 마지막까지
        if str[i] == A:                                 # 해당 번지의 값이 A라면
            list_A.append(i)                            # 해당 번지수를 list_A에 저장
        elif str[i] == B:                               # 해당 번지의 값이 B라면
            list_B.append(i)                            # 해당 번지수를 list_B에 저장

    for i in range(len(list_A)):                        # 문자열에서 A와 B가 있는 번지수를 비교하여
        for j in range(len(list_B)):                        
            if list_A[i] < list_B[j]:                   # A번지수가 B번지수보다 작으면 A가 앞에 존재하는
                count = count + 1                       # 것이므로 count 1증가

    return count                                        # count 반환


start2 = time.time()
for i in range(1000000):
    count_substr_v2(str, "A", "B")
end2 = time.time()
print(str, " ==> ", count_substr_v2(str, "A", "B"))
print("실행시간 : ", end2-start2)