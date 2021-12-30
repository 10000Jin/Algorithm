
print("##정의 사용##")
print()
def gcd_simple(a, b): 
    list_a = []                                 #a의 약수를 저장할 리스트 생성
    list_b = []                                 #b의 약수를 저장할 리스트 생성
    list_same = []                              #공약수를 저장할 리스트 생성

    for i in range(1, a):                       #1부터 a-1까지의 수로
        if a % i == 0:                          #a를 나누었을때 나머지가 0이면
            list_a.append(i)                    #a의 약수이므로 list_a에 저장
    for j in range(1, b):
        if b % j == 0:
            list_b.append(j)

    print("%d의 약수모음 : %s" % (a, list_a))    #a의 약수 출력
    print("%d의 약수모음 : %s" % (b, list_b))    #b의 약수 출력

    x = 0                                       #두 약수 리스트의 번지수 x, y를 0초기화
    y = 0
    while x<len(list_a) and y<len(list_b):      #두 리스트중 하나라도 번지수를 넘을때까지 반복
        if list_a[x] == list_b[y]:              #두 약수를 비교해서 같으면
            list_same.append(list_a[x])         #공약수 리스트에 추가
            x += 1                              #다음 약수 비교
            y += 1
        elif list_a[x] > list_b[y]:             #a의 약수가 크다면
            y += 1                              #b의 다음 약수로 이동
        else:                                   #b의 약수가 크다면
            x += 1                              #a의 다음 약수로 이동

    print("공약수 모음 : ", list_same)          #공약수 출력
    print()
    return list_same.pop()                      #공약수 리스트중 마지막 1개를 꺼내 반환

print("60과 28의 최대 공약수 = ", gcd_simple(60, 28))
print()


print("\n\n")
print("##한 수의 약수 사용##")
print()
def gcd_v2(a, b):
    list_a = []                                 #a의 약수를 저장할 리스트 생성

    for i in range(1, a):                       #1부터 a-1까지의 수로
        if a % i == 0:                         #a를 나누었을때 나머지가 0이면
            list_a.append(i)                    #a의 약수이므로 list_a에 저장
    print("60의 약수모음 : ", list_a)           #a의 약수 출력

    for j in range(len(list_a)-1, 0, -1):       #a의 약수의 마지막 번지부터
        if b % list_a[j] == 0:                  #해당하는 값으로 b를 나눴을떄 나머지가 0이면
            return list_a[j]                    #그때 번지수에 해당하는 값 반환

print("60과 28의 최대 공약수 = ", gcd_v2(60, 28))
print()


print("\n\n")
print("##유클리드 알고리즘##")
print()
def gcd(a, b): 
    if a >= b:                                  #a가 b보다 크거나 같다면
        print("gcd(%d, %d)" % (a, b))
        while b != 0:                           #b가 0이 아니면 반복
            x = a % b                           #a를 b로 나눈 나머지를 x에 대입
            a = b                               #a자리에 b를 넣고
            b = x                               #b자리에 x를 넣음
            print("gcd(%d, %d)" % (a, b))       #중간결과 출력
        return a                                #b가 0이 되어 반복종료시 a 반환
       
    elif a < b:                                 #a가 b보다 작다면
        return gcd(b, a)                        #a와 b를 바꿔 gcd(b, a)한 값을 반환

print("60과 28의 최대 공약수 = ", gcd(60, 28))
print()
print("28과 60의 최대 공약수 = ", gcd(28, 60))
print()


print("\n\n")
print("##최소 공배수##")
print()
def lcm(a, b):
    x = gcd(a, b)                               #최대 공약수를 x에 저장
    result = x * (int)(a / x) * (int)(b / x)    #x와 a와 b에서 x로 나눈 몫을 모두 곱하면 
    return result                               #최소 공배수이고 이를 반환

print("60과 28의 최소 공배수 = ", lcm(60, 28))
print()