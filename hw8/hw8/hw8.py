
from queue import Queue

BUCKETS = 256
DIGHTS = 9                                      # 최대 긴 단어 길이

def radix_sort(A):

    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())                  # 버킷만큼의 공백 큐 생성

    n = len(A)
    
    pos = DIGHTS - 1
    while pos >= 0:
        for i in range(n):                      # 모든 단어들에 대해
            b = BUCKETS - 1                     # 일단 맨 뒤의 버캣을 설정(짧은 단어)
            if len(A[i]) > pos:                 # 긴 단어: 해당 pos에 알파벳이 있으면
                b = ord(A[i][pos])              # 버캣의 위치 계산
            queues[b].put(A[i])                 # 버캣에 삽입
        
        j = 0
        for b in range(BUCKETS):                # 버캣에서 꺼내 원래의 리스트로
            while not queues[b].empty():        # b번째 큐가 공백이 아닌 동안
                A[j] = queues[b].get()          # 원소를 꺼내 리스트에 저장
                j += 1
           
        pos -= 1




infile = open("D:\\@@@@@@과제 모음@@@@@@\\3학년 1학기\\알고리즘\\hw8\\aa.txt", "r")
words = infile.read().split()
infile.close()
print("정렬전 ; ", words)
print()

radix_sort(words)

print("정렬후 : ", words)