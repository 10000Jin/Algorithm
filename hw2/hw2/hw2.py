
A = [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0]
n = len(A)                                      # A의 크기 n에 저장

print("A = ", A)

for i in range(n-1, 0, -1):                     # 정렬되지 않은 부분의 크기
    bechanged = False                           # 교환됐음을 의미하는 bechanged변수 초기화
    for j in range(i):                          # 0번지부터 정렬안된 부분의 마지막 번지까지
       if A[j] > A[j+1]:                        # 만약 뒤에 수랑 비교했을때 크다면
           A[j], A[j+1] = A[j+1], A[j]          # 뒤에 수랑 자리를 바꿈
           bechanged = True                     # 교환되었음으로 bechanged에 true저장

    if not bechanged: break;                    # 정렬안된부분을 안쪽 루프로 비교하여 교환된곳이
                                                # 없다면 더이상 진행할 필요가 없으므로 반복 탈출

print("\n정렬후 A = ", A)                         # 결과 출력
