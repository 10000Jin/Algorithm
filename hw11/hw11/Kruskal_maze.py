
from random import randrange
import os
import time

class disjoinSets:                                      # 서로소 집합
    def __init__(self, n):                              
       self.parent = [-1]*n                             # 각 노드(정점)은 모든 루트 노드로 초기화
       self.set_size = n                                # 집합의 개수는 노드의 개수 초기화
    
    def find(self, id):                                 # 정점의 id가 속한 집합의 대표번호 탐색
        while (self.parent[id] >= 0):                   # 부모번호가 나올때까지 반복
            id = self.parent[id]                        # id를 부모 id로 갱신
        return id

    def union(self, s1, s2):                            # 두 집합 병합
        self.parent[s1] = s2                            # s1을 s2에 병합
        self.set_size = self.set_size - 1               # 집합의 개수 1 감1


def Kruskal_maze(w, h):                                         # Kruskal 알고리즘으로 미로 만들기
    n = w * h                                                   # 정점의 개수 = 높이 * 너비
    dsets = disjoinSets(n)                                      # disjoinSets 객체 생성

    E = []                                                      # 두 정점과 그 사이의 가중치를 저장하는 리스트
    for i in range(h):
        for j in range(w):                                      # 각 정점에 대해
            if j != w-1:                                        # 가장 오른쪽을 제외하고
                E.append(((i, j), (i, j+1), randrange(100)))    # 한 정점과 그 오른쪽 정점 그리고 가중치를 랜덤으로 저장
            if i != h-1:                                        # 가장 아래쪽을 제외하고
                 E.append(((i, j), (i+1, j), randrange(100)))   # 한 정점과 그 아래쪽 정점 그리고 가중치를 랜덤으로 저장

    E.sort(key = lambda e : e[2])                               # 가중치를 기준으로 정렬

    ecount = 0                                                  # MST에 포함된 간선의 개수 0초기화
    for i in range(len(E)):                             
        e = E[i]                                                # MST에서 하나를 뽑아
        id_1 = 10 * e[0][0] + e[0][1]                           # 정점의 id를 만들어 줌
        id_2 = 10 * e[1][0] + e[1][1]                           # id = 10 * 높이 + 너비
        uset = dsets.find(id_1)                                 # id를 가지고 각 정점의 부모 id를 탐색
        vset = dsets.find(id_2)

        if uset != vset:                                        # 만약 두 정점의 부모 id가 다르면
            dsets.union(uset, vset)                             # 사이클이 생기지 않은 것이므로 두 집합 병합
            if e[0][0] == e[1][0]:                              # i가 같으면(오른쪽 이동)
                (x, y) = (e[1][0], e[1][1])
                ver[x][y] = "    "                              # 이동하는 부분 벽을 없앰
            if e[0][1] == e[1][1]:                              # j가 같으면(아래쪽 이동)
                (x, y) = (e[1][0], e[1][1]) 
                hor[x][y] = "+   "                              # 이동하는 부분 벽을 없앰

            os.system("cls")                                        # 이동한 것을 보여주기 위해 cmd창 초기화
            result = ""                                             # 미로를 출력할 result 공백으로 초기화
            for i in range(h+1):                                    
                (a, b) = (hor[i], ver[i])                           # 한 행의 위아래 벽과 양옆 벽을 튜플에 저장
                result += ''.join(a + ['\n'] + b + ['\n'])          # 위아래 벽과 양옆 벽 중간에 줄바꿈 문자를 넣어 순차대로 
            print(result)                                           # 나오게하고 미로 출력
            time.sleep(0.3)                                         # 미로를 출력한뒤 0.5초간 정지

            ecount += 1                                         # MST에 포함된 간선의 개수 1추가
            if ecount == n-1:                                   # 간선의 개수 = n-1 가 되었다면 
                break                                           # 반복문 탈출 및 종료




w = int(input("너비를 입력해주세요(w) : "))
h = int(input("높이를 입력해주세요(h) : "))

ver = [["|   "] * w + ['|'] for _ in range(h)] + [[]]           # 양옆의 벽
hor = [["+---"] * w + ['+'] for _ in range(h + 1)]              # 위아래의 벽

Kruskal_maze(w, h)