
from random import shuffle, randrange
import os
import time

def DFS_maze(x, y):
    visited[y][x] = 1                                           # 방문했음으로 1
 
    room = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]     # 인접한 방들을 d에 저장
    shuffle(room)                                               # 무작위로 섞음

    for (next_x, next_y) in room:                               # 무작위로 선정된 인접한 방을 뽑아
        if visited[next_y][next_x]: 
            continue                                            # 만약 방문했던 곳이면 다시 뽑음
        if next_x == x:                                         # x좌표가 같다면 위나 아래로 이동 가능
            hor[max(y, next_y)][x] = "+   "                     # 기존 y좌표와 이동한 y좌표중 큰 값의 구멍을 뚫음
        if next_y == y:                                         # y좌표가 같다면 왼쪽이나 오른쪽으로 이동 가능
            ver[y][max(x, next_x)] = "    "                     # 기존 x좌표와 이동한 x좌표중 큰 값의 구멍을 뚫음
        
        os.system("cls")                                        # 이동한 것을 보여주기 위해 cmd창 초기화
        result = ""                                             # 미로를 출력할 result 공백으로 초기화
        for i in range(h+1):                                    
            (a, b) = (hor[i], ver[i])                           # 한 행의 위아래 벽과 양옆 벽을 튜플에 저장
            result += ''.join(a + ['\n'] + b + ['\n'])          # 위아래 벽과 양옆 벽 중간에 줄바꿈 문자를 넣어 순차대로 
        print(result)                                           # 나오게하고 미로 출력
        time.sleep(0.3)                                         # 미로를 출력한뒤 0.5초간 정지
        
        DFS_maze(next_x, next_y)                                    # 순환호출하여 이동한 방에서 다시 깊이 탐색
 
    


w = int(input("너비를 입력해주세요(w) : "))
h = int(input("높이를 입력해주세요(h) : "))
    
visited = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]   # 미로의 각 방은 아직 방문하지 않은 것으로 초기화
                                                                # 제일 아래쪽 벽과 오른쪽 벽은 열릴수 없는 끝이므로 1로 초기화
ver = [["|   "] * w + ['|'] for _ in range(h)] + [[]]           # 양옆의 벽
hor = [["+---"] * w + ['+'] for _ in range(h + 1)]              # 위아래의 벽



DFS_maze(randrange(w), randrange(h))