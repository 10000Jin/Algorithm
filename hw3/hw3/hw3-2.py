# p178 no.9

visited = set()                                     # 방문정점 저장 집합
inDeg = {}                                          # 진입차수 저장할 딕셔너리

def dfs_tsort(graph, start):                        # DFS 위상정렬
    if start not in visited:                        # 시작 정점이 방문하지 않은 정점이라면
        if inDeg[start] == 0:                       # 진입차수가 0이라면
            visited.add(start)                      # 이제 방문하였음으로 visited에 추가
        
            for u in graph[start]:                  # 인접정점들의 진입차수들을
                inDeg[u] -= 1                       # 1씩 감소
            print(start, end=" ")                   # 방문하였음으로 정점 출력
        
            for v in graph[start]:                  # 정점의 인접정점을
                dfs_tsort(graph, v)                 # dfs_tsort를 다시 호출하여 깊이 우선 탐색


def topological_sort_DFS(graph):
    for v in graph:                                 # 그래프의 각 정점의 
        inDeg[v] = 0                                # 진입차수를 0으로 초기화
    for v in graph:                                 # 그래프의 각 정점의 
        for u in graph[v]:                          # 인접정점의 진입차수를 1씩 증가
            inDeg[u] += 1

    for v in graph:                                 # 모든 정점에 대해 
        if len(graph[v]) > 0:                       # 인접정점이 있다면
            dfs_tsort(graph, v)                     # 깊이우선 탐색


mygraph = {"A" : {"C", "D"},
           "B" : {"D", "E"},
           "C" : {"D", "F"},
           "D" : {"F"},
           "E" : {"F"},
           "F" : set()
           }

mygraph2 = {"A" : {"B"},
            "B" : set(),
            "C" : set(),
            "D" : {"C"},
           }

print("\n##DFS 위상정렬##")
print("topological_sort_DFS : ")
topological_sort_DFS(mygraph)
print()