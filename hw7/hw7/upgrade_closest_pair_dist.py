
import math
import time
import random

def strip_closest2(P, d):
    n = len(P)
    d_min = d                                           # d보다 크면 의미가 없으므로 d_min은 d로 초기화
    P.sort(key = lambda point: point[1])                # y좌표를 기준으로 정렬

    for i in range(n):
        j = i + 1                                       # 띠영역 안에서 한점과 그 다음점을 비교해    
        while j < n and (P[j][1] - P[i][1]) < d_min:    # 다음 점이 띠영역을 벗어나지 않고 y좌표의 차이가 d_min보다 작으면 반복
            dij = distance(P[i], P[j])                  # 두 점을 비교해 거리를 dij에 저장
            if dij < d_min:                             # dij가 d_min보다 작으면
                d_min = dij                             # d_min을 dij로 갱신(영역을 좁힘)
            j += 1                                      # 그 다음점으로 이동
    return d_min                                        # 최종적인 최단거리 d_min반환


def closest_pair_dist(P, n):
    if n < 3:                                           # 점이 3개 이하라면
        return closest_pair(P)                           # 억지기법으로 해결

    mid = n // 2                                        # 중앙값을 mid에 저장  
    mid_x = P[mid][0]                                   # 중앙값의 x좌표

    dl = closest_pair_dist(P[:mid], mid)                # 왼쪽 그룹에서 최근접 쌍의 거리
    dr = closest_pair_dist(P[mid:], n - mid)            # 오른쪽 그룹에서 최근접 쌍의 거리
    d = min(dl, dr)                                     # 둘중 더 짧은 거리 d에 저장
     
    Pm = []                                             # x좌표가 -d~d인 점들의 집합(띠영역)
    for i in range(n):                                  
        if abs(P[i][0] - mid_x) < d:                    # 점의 x좌표에서 중앙값의 x좌표를 뺀 절댓값이
            Pm.append(P[i])                             # d보다 작으면 Pm(띠영역)에 추가

    ds = strip_closest2(Pm, d)                           # Pm내에서 d보다 작은 최근접쌍의 거리 찾기
    return min(d, ds)                                   # 둘중 더 짧은 것은 반환








def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)   # 거리 계산 공식


def closest_pair(p):
    n = len(p)
    mindist = float("inf")                                  # 최단 거리 무한대로 초기화
    for i in range(n-1):                                    # 모든 점들의 쌍에 대해 
        for j in range(i+1, n):
            dist = distance(p[i], p[j])                     # 거리를 dist에 저장
            if dist < mindist:                              # 두점 사이의 거리가 최단거리보다 작다면
                mindist = dist                              # 두점 사이의 거리를 최단거리로 갱신
    return mindist


def strip_closest(P, d):
    n = len(P)
    d_min = d                                               # d보다 크면 의미가 없으므로 d_min은 d로 초기화

    for i in range(n):
        j = i + 1                                           # 띠영역 안에서 한점과 그 다음점을 비교해    
        while j < n and (P[j][1] - P[i][1]) < d_min:        # 다음 점이 띠영역을 벗어나지 않고 y좌표의 차이가 d_min보다 작으면 반복
            dij = distance(P[i], P[j])                      # 두 점을 비교해 거리를 dij에 저장
            if dij < d_min:                                 # dij가 d_min보다 작으면
                d_min = dij                                 # d_min을 dij로 갱신(영역을 좁힘)
            j += 1                                          # 그 다음점으로 이동
    return d_min                                            # 최종적인 최단거리 d_min반환


def upgrade_closest_pair_dist(P, n):
    if n <= 3:                                              # 점이 3개 이하라면
        return closest_pair(P)                              # 억지기법으로 해결

    mid = n // 2                                            # 중앙값을 mid에 저장  
    mid_x = P[mid][0]                                       # 중앙값의 x좌표

    dl = upgrade_closest_pair_dist(P[:mid], mid)                    # 왼쪽 그룹에서 최근접 쌍의 거리
    dr = upgrade_closest_pair_dist(P[mid:], n - mid)                # 오른쪽 그룹에서 최근접 쌍의 거리
    d = min(dl, dr)                                         # 둘중 더 짧은 거리 d에 저장
     
    Pm = []                                                 # x좌표가 -d~d인 점들의 집합(띠영역)
    i = 0                                                   # 왼쪽 부분 리스트의 시작 인덱스
    j = mid + 1                                             # 오른쪽 부분 리스트의 시작 인덱스
    while i <= mid and j <= n-1:                            # 인덱스를 넘지 않는 선에서 반복
        if P[i][0] > mid_x - d or P[j][0] < mid_x + d:      # 각 부분리스트의 점의 x좌표가 띠영역 안에 들어온다면
            if P[i][1] <= P[j][1]:                          # 왼쪽 부분리스트의 점이 같거나 더 작다면
                Pm.append(P[i])                             # Pm에 추가
                i = i+1                                     # 왼쪽 부분 리스트의 인덱스 1증가
            else:                                           # 오른쪽 부분리스트의 점이 같거나 더 작다면
                Pm.append(P[j])                             # Pm에 추가
                j = j+1                                     # 오른쪽 부분리스트의 인덱스 1증가
        
        else:                                               # 띠영역에 들어오는 점이 없다면
            if P[i][0] <= mid_x - d and P[j][0] >= mid_x + d:   # 두 부분리스트의 점이 다 띠영역 밖에 있다면
                i += 1                                  
                j += 1                                      # 양쪽 부분리스트의 인덱스 1증가
            elif P[i][0] <= mid_x - d:                      # 왼쪽 부분리스트의 점이 띠영역 밖에 있다면
                i += 1                                      # 왼쪽 부분리스트의 인덱스 1증가
            elif P[j][0] >= mid_x + d:                      # 오른쪽 부분리스트의 점이 띠영역 밖에 있다면
                j += 1                                      # 오른쪽 부분리스트의 인덱스 1증가

    ds = strip_closest(Pm, d)                               # Pm내에서 d보다 작은 최근접쌍의 거리 찾기
    return min(d, ds)                                       # 둘중 더 짧은 것은 반환


#p = [(2, 3), (12, 30), (40, 50)]
#p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
#p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4), (4, 3), (37, 41), (24, 41)]
#p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4), (4, 3), (37, 41), (24, 41), (52, 3), (11, 63), (22, 12)]
#p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4), (4, 3), (37, 41), (24, 41), (52, 3), (11, 63), (22, 12), (4, 6), (11, 44), (6, 1)]
#p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4), (4, 3), (37, 41), (24, 41), (52, 3), (11, 63), (22, 12), (4, 6), (11, 44), (6, 1), (14, 71), (52, 22), (33, 51)]


p = []
for i in range(200):
    x = random.randrange(1, 100)
    y = random.randrange(1, 100)
    p.append((x, y))


print("################억지기법################")
print("n = ", len(p))
print("가장 가까운 두 점의 거리", closest_pair(p))

#start = time.time()
#for i in range(10000):
#    closest_pair(p)
#end = time.time()
#print("실행시간(만회 반복) : %f초" % (end-start))




p.sort(key = lambda point:point[0])
print("\n\n################ 분할 정복 기법 ################")
print("n = ", len(p))
print("가장 가까운 두 점의 거리", closest_pair_dist(p,len(p)))

start2 = time.time()
for i in range(10000):
    closest_pair_dist(p,len(p))
end2 = time.time()
print("실행시간(만회 반복) : %f초" % (end2-start2))





#p.sort(key = lambda point:point[0])
print("\n\n################ 개선된 분할 정복 기법 ################")
print("n = ", len(p))
print("가장 가까운 두 점의 거리", upgrade_closest_pair_dist(p,len(p)))

start3 = time.time()
for i in range(10000):
    upgrade_closest_pair_dist(p,len(p))
end3 = time.time()
print("실행시간(만회 반복) : %f초" % (end3-start3))
