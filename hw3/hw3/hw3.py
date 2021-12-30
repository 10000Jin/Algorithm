# p137 no.27

import queue

def is_bipartite_BFS(g):
    que = queue.Queue()                             # 큐 객체 생성
    colors = {"A" : 0, "B" : 0, "C" : 0, "D" : 0}   # 정점의 색을 나타낼 딕셔너리 0으로 초기화

    que.put("A")                                    # 시작 정점으로 A 삽입
    colors["A"] = 1                                 # A정점 1로 색칠 + 방문 표시
    while not que.empty() :                         # 큐안에 항목이 있다면 반복
        v = que.get()                               # 큐에서 정점을 빼서
        
        for u in g[v]:                              # 그 정점의 인접 정점들의
            if colors[u] == 0:                      # 색이 0(방문하지 않은 정점)이라면
                que.put(u)                          # 큐에 추가(방문)
                colors[u] = colors[v] * -1          # 색을 이전 정점의 -1을 곱해 다른색으로 색칠

            elif colors[v] == colors[u]:            # 정점과 인접정점의 색이 같다면
                return False                        # 이분 그래프가 아니므로 False 반환

    return True                                     # 특이사항 없이 반복문이 종료되면
                                                    # 이분 그래프이므로 True반환

gragh1 = {"A" : {"B", "D"},
          "B" : {"A", "C"},
          "C" : {"B", "D"},
          "D" : {"A", "C"}
         }
gragh2 = {"A" : {"B", "C", "D"},
          "B" : {"A", "C"},
          "C" : {"A", "B", "D"},
          "D" : {"A", "C"}
         }
print("Gragh1 : ", gragh1)
print("BFS 방식 이분 그래프 탐색 --> ", "Yes" if is_bipartite_BFS(gragh1) else "No")
print()
print("Gragh2 : ", gragh2)
print("BFS 방식 이분 그래프 탐색 --> ", "Yes" if is_bipartite_BFS(gragh2) else "No")
