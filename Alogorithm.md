# 알고리즘

문제 풀 때 라이브러리 사용하지 않는다.

- ##### max(), min(), indexof(), sort(), slicing 등

- ##### 대신, append, len 같은 건 써도 됨.

- #### 시간 복잡도(Time Complexity)

  - ![image](https://user-images.githubusercontent.com/52814897/65399002-4ff9ae80-ddf5-11e9-9bb6-6453fc9905c9.png)

  - ##### 알고리즘의 작업량을 표현

  - ##### 실제 걸리는 시간과 실행되는 명령문 개수를 계산

  - #### 빅-오(O) 표기법(Big-Oh Notation)

    - ##### 최고차 항의 차수만으로 비교.

    - ##### 최악의 경우

      - ##### n 번 모두 확인해야하는 법 -> 유한하므로 시간 복잡도 계산하기에 적합

  - ##### 오메가 표기법

    - ##### 최선의 경우

      - ##### 한 번에 찾아낼 경우

  - ##### 세타 표기법

    - ##### 최악=최선일 경우

- ##### 이진탐색

  - ##### List가 정렬되어 있어야 함.

  - ##### 중간 값을 비교한 후에, 중간 값을 기준으로 필요 없는 한 쪽은 버린다.

  - ##### 100만 개는 10<sup>20</sup> 이고, 원하는 값은 20번만에 찾을 수 있다.



## 정렬

- #### 버블 정렬(Bubble Sort)

  - ##### 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

    ```python
    # Bubble sort
    arr = [55, 7, 78, 12, 42]
    n = len(arr)
    # 2. n-1 부터 1까지 전체 반복
    for j in range(n - 1, 0, -1):
    	# 1. 처음부터 끝까지 1회 비교
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    ```

- #### 선택 정렬(Selection Sort)

  - ##### 최소값을 찾아 맨 앞으로 옮김

    ```python
    arr = [55, 7, 78, 12, 42]
    # 1. 처음 수로 초기 설정
    MIN = 0
    
    # 3. 2번을 idx:[0]~[n-2]까지 반복 (마지막[n-1]은 자동)
    for j in range(len(arr) - 1):
        MIN = j
        # 2. 처음부터 끝까지 보면서 가장 작은 수 맨 앞으로.
        for i in range(1, len(arr)):
            if arr[i] < arr[MIN]:
        		MIN = i
                
        arr[j], arr[MIN] = arr[MIN], arr[j]
    ```

    

- #### 카운팅 정렬(Counting Sort)??

  - ##### 각 항목의 개수를 세서 정렬

  - ##### 누적 빈도수를 이용??

    ```python
    data = [0, 3, 1, 3, 1, 2, 4, 1]
    counts = [0] * 5 
    
    for val in data:
        counts[val] += 1
        
    sorted = []
    for i in range(len(counts)):
        for j in range(counts[i]):
            sorted.append(i)
            ???
    ```

    

## 배열 연습 문제

- #### Gravity

  <img src = "https://user-images.githubusercontent.com/52814897/62027223-1dc63900-b218-11e9-899c-d9c942abcc71.png" style="zoom:60%" />

  <img src = "https://user-images.githubusercontent.com/52814897/62027242-2585dd80-b218-11e9-9cbd-7e1a7bd8a4d8.png" style="zoom:60%" />

  

  

  ```python
  # Gravity
  ```

  

- #### Baby-gin Game

<img src = "https://user-images.githubusercontent.com/52814897/62027556-edcb6580-b218-11e9-8f85-d3b9cb2184f0.png" style = "zoom:60%" />

<img src="https://user-images.githubusercontent.com/52814897/62027569-f4f27380-b218-11e9-9980-bec0bc251100.png" style="zoom:60%" />

```python
data = 'ABC'

n = len(data)
for i in range(n):
    for j in range(n):
        if i == j: continue
        for k in range(n):
            if i == k or j == k: continue
            print(data[i], data[j], data[k])
```



- #### 최적화 문제 -> 완전 검색

  - ##### 최대 혹은 최소가 되는 경우를 찾는 문제
  
  - ##### 모든 가능한 경우를 조사한다. 
  
  - ##### 모든 후보해를 조사한다.
  
  - ##### 모든 가능한 경우들이 조합과 관련이 깊다.
  
    - ##### 순열, 부분집합, 조합, n!, 2^n
  
- #### 완전 검색을 좀 더 효율적으로 하는 방법

  1. ##### 백트래킹(가지치기)

  2. ##### 동적 계획법(메모이제이션)



## 배열 2

### 부분집합

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr) # n: 원소의 개수

# 모든 경우를 선택할 수 있는 selection
# 0001, 0010, 0011, 0100...이런식으로
# 배열의 모든 자리 선택가능
for selection in range(1 << n): 
    for pick in range(n):
        # selection의 각 자리를 확인하면서
        # (1, 10, 100, 1000 이런식으로..) 
        # selection비트의 1인 부분을 출력
        if selection & (1 << pick): 
            print(arr[j], end=", ")
        print()
    print()
```




## 문자열

### 문자열

- ASCII: 문자 인코딩 표준

- `print(ord('A'))` 로 A에 대한 ASCII 코드 값을 알 수 있다.

- `print(chr(65))`로 65에 ASCII 코드 값에 해당하는 문자를 알 수 있다.

- ![image](https://user-images.githubusercontent.com/52814897/62843619-275e9f00-bcf6-11e9-9eb0-149e322f9e31.png)

- 유니코드(UTF): 다국어 처리를 위한 표준

- 문자열 뒤집기

  - ```python
    ## 문자열 뒤집기
    # 1. Slicing 사용
    arr = 'algorithm'
    print(arr[::-1])
    # 2. 교환 방식
    arr = list(arr)
    n = len(arr)
    for i in range(n//2):
        #arr[i] <-> arr[n- 1 - i]
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    print(''.join(arr))
    ```

- 문자열 숫자를 정수형으로 변환

  - ```python
    ## 문자열 숫자를 정수로 변환
    # 1. ASCII 활용
    arr = '12345'
    val = 0
    for i in arr:
        val = val * 10 + ord(i) - ord('0')
    # 2. 내장함수
    int(arr)
    ```

### 패턴 매칭

- 고지식한 알고리즘(Brute Foce)
- KMP 알고리즘
- 보이어-무어 알고리즘
  - 텍스트의 용량이 클 때 좋음.

### 문자열 암호화

### 문자열 압축

### 실습 1, 2



------

## 스택

### 스택1

- 기본 구조

```python
S = []
def push(item): # full 상태 체크
    S.append(item)
def pop():
    if len(S) == 0: # empty 상태 체크
        return print('empty')
    return S.pop()
for i in range(3):
    push(i)
for i in range(4):
    pop()
```

- 덱: deque()  사용
  - stack과 queue 둘 다 사용 가능

```python
from collections import deque
S = deque()

while S:
    S.popleft() # 비어있으면 false가 나옴

for i in range(N):
    S.append(i)
while S:
    S.pop()
```

### 재귀호출

- 문제를 재귀적으로 푼다.
- 재귀적 정의를 구현할 때 재귀호출이 좋다.
- 재귀적 정의 --> 좀 더 작은 문제의 답을 사용해서 더 큰 문제의 답을 구하는 방법.
- 팩토리얼 구하는 문제
- 반드시 재귀 호출이 끝나는 `Base Case` 구조가 있어야 함.

### Memoization

- Memoization으로 재귀함수의 시간복잡도를 줄일 수 있음.

- 일반적인 피보나치

  ```python
  def fibonacci(n): # n 번째 피보나치 수를 반환
      if n == 1 or n == 0:
          return n
      else:
          return fibonacci(n - 1) + fibonacci(n - 2)
  print(fibonacci(10))
  ```

- Memoization을 적용한 피보나치

  ```python
  memo = [-1] * 100
  def fibonacci(n): # n번째 피보나치 수를 반환
      if n == 1 or n == 0:
          return n
      # 이미 답을 구했는지 확인
      if memo[n] != -1:
          return memo[n]
      memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
      return memo[n]
  ```

- for 문을 이용한 Memoization

  ```python
  memo = [-1] * 100
  def fibonacci(n): # n번째 피보나치 수를 반환
   	
      memo[0], memo[1] = 0, 1
      for i in range(2, n + 1): # i ==> 문제를 나타내는 값
          memo[i] = memo[i - 1] + memo[i - 2]
      return memo[n]
  ```

- 



### DP(동적계획법)

- Dynamic Programming
- 중복 계산이 필요한 부분을 함수로 만들어 계산(예, 재귀함수)
- 느리고 복잡
- Bottom-up 방식. 하위 문제를 풀고 그 해를 기반으로 다음 단계를 해결한다.(피보나치 수열)

### DFS(깊이우선 탐색)

- Depth-First Search

- 가장 짧은 길을 찾지는 않는다.

- 한 방향으로 가다가 막히면 다시 마지막 갈림길 간선이 있는 정점으로 back

- 모든 정점을 방문하는 순회방법

- 연습문제 3??? 기본 틀?

  ```python
  import sys; sys.stdin = open('DFS_input.txt', 'r')
  V, E = map(int, input().split())    # 정점수, 간선수
  G = [[] for _ in range(V + 1)]      # 정점 번호 1 ~ V
  
  for _ in range(E):
      u, v = map(int, input().split())
      G[u].append(v)
      G[v].append(u)
  
  for i in range(1, V + 1):
      print(i, '-->', G[i])
  ```

- 기본 DFS 방법인가?

  ```python
  def DFS(v): # v: 시작점
      S = []
      visit = [False] * (V + 1)
      visit[v] = True # 시작점 방문
      S.append(v)		# 시작점을 스택에 push
      while S: 		# 빈 스택이 아닌 동안
      	# v의 방문하지 않은 인접정점을 찾는다. ==> w
          for w in G[v]:
              if not visit[w]: # 방만하지 않은 곳부터 찾기
                  visit[w] = True # w 방문하고
                  S.append(v)		# v 를 스택에 push
                  v = w			# w를 현재 방문하는 정점하는 설정
                  break
              else:				# 이전에 방문한 정점으로 되돌아 간다.
                  v = S.pop()
                  
  ```

- 재귀호출 DFS

  - ```python
    def DFS(v):
        visit[v] = True; print(v, end=' ')
        for w in G[v]:
            if not visit[w]:
                DFS(w)
    ```
  
  - ```python
    # 주변 탐색 시계방향으로
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    
    ######## dfs_recursion 함수 #######
    def dfs_recursion(y, x):
        global N_matrix, N
        N_matrix[y][x] = 0 # 확인한 곳은 0으로
        for i in range(8): # 8방향 확인하면서
            check_y = y + dy[i]
            check_x = x + dx[i]
            # 경계조건 및 방문한 곳인지 확인
            if check_x >= 0 and check_y >= 0 and check_x < N and check_y < N and N_matrix[check_y][check_x] != 0: 
                dfs_recursion(check_y, check_x) 
        return None
    ########################### main #####
    for y in range(N):
        for x in range(N):
            if N_matrix[y][x] != 0: # 매트릭스 element index로 하나씩 확인
                dfs_recursion(y, x)
    ```
  

### 위상 정렬(DAG)

### 백트래킹(Back-Tracking)

- `깊이우선탐색`은 모든 후보, 경로를 검사

- 반면, `백트래킹`은 불필요한 경로를 조기에 차단.(가지치기: pruning)
  
  - 따라서, 깊이 우선 탐색을 하기에는 경우의 수가 너무 많은 경우(N!의 경우)에 사용
  
- 상태 공간 트리
  
  - 시작점을 `root`, 분기되는 갈래를 `node`, 끝단의 단말 node는 `leaf`라고 부름
  
- 부분집합 구하기
  - 멱집합(powerset): 공집합과 자기자신을 포함한 모든 부분집합
  
  - 부분집합의 개수는 2^n^개
  
  - ```python
    def backtrack(a, k, input):
        global MAXCANDIDATES
        c = [0] * MAXCANDIDATES
        
        if k == input:
            process_solution(a, k)
        else:
            k += 1
            ncandidates = construct_candidates(a, k, input, c)
            for i in range(ncandidates):
                a[k] = c[i]
                backtrack(a, k , input)
    
    def construct_candidates(a, k, input, c):
        c[0] = True
        c[1] = False
        return 2
    
    def process_solution(a, k):
        sum_check = 0
        empty_string = ''
        empty_string += '( '
        for i in range(k+1):
            if a[i]:
                sum_check += i
                empty_string += str(i) + ' '
        empty_string += ')'
    
        if sum_check == 10:
            print(empty_string)
    
    MAXCANDIDATES = 100
    NMAX = 100
    a = [0] * NMAX
    
    backtrack(a, 0, 10)
    ```
  
- 순열 구하기

  - ```python
    # 순열 라이브러리
    from itertools import permutations
    for p in permutations(range(3)): # [0, 1, 2] [0, 2, 1] [1, 0, 2] ...
    ```
  - ```python
    # 직접 만들기
    
    ```

  - ```python
    def backtrack(a, k, input):
        global MAXCANDIDATES
        c = [0] * MAXCANDIDATES
    	
        # Base Case
        if k == input:
            for i in range(1, k+1):
                print(a[i], end=' ')
            print()
        
        else:
            k += 1
            ncandidates = construct_candidates(a, k, input, c)
            for i in range(ncandidates):
                a[k] = c[i]
                backtrack(a, k, input)
    
    def construct_candidates(a, k, input, c):
        in_perm = [False] * NMAX
    
        for i in range(1, k):
            in_perm[a[i]] = True
        
        ncandidates = 0
        for i in range(1, input+1):
            if in_perm[i] == False:
                c[ncandidates] = i
                ncandidates += 1
        return ncandidates
    ```

- 분할 정복 알고리즘

  - 주어진 문제의 입력을 다루기 쉽게 부분으로 분할하여 문제를 해결(정복)하는 방식의 알고리즘

  - 문제를 더 이상 나눌 수 없을 때까지 나누고 이렇게 나누어진 문제들을 각각 풂으로써 전체 문제의 답을 얻는 알고리즘

  - 문제를 두 단계(1. 분할, 2. 정복)로 나누어 해결하는 것

  - 대표적인 예: 합병 정렬, 퀵 정렬, 이진 탐색, 거듭제곱 연산(a^b)등

    - 거듭제곱 연산

      - ```python
        # 거듭제곱 연산 O(n)
        def Power(Base, Exponenet):
            if Base == 0:
                return 1
            result = 1 # Base^0은 1이므로
            for i in range(Exponent):
                result *= Base
            return result
        
        # 거듭제곱 연산 O(n)의 분할 정복 O(log2n)
        def Power(Base, Exponenet):
            
            # Base Case(기저사례, 멈추는 구간)
            if Exponenet == 0 or Base == 0:
                return 1
            
            if Exponent % 2 == 0:
                NewBase = Power(Base, Exponent/2)
                return NewBase * NewBase
            else:
                NewBase = Power(Base, (Exponent - 1) / 2)
                return (NewBase * NewBase) * Base
        ```

    - 퀵 정렬

      - 전체 데이터에 대해 정렬을 수행하지 않고, `기준키(피벗)`를 중심으로 왼쪽 부분(작은부분)과 오른쪽 부분(큰 부분) 리스트로 분할
      
      - `순환 호출`을 이용하기 때문에 `스택`이 필요
      
      - ```python
        def quickSort(a, begin, end):
            if begin < end:
                p = partition(a, begin, end)
                quickSort(a, begin, p-1)
                quickSort(a, p+1, end)
        
        def partition(a, begin, end):
            pivot = (begin + end) //2
            L = begin
            R = end
            while L < R:
                while(a[L] < a[pivot] and L < R):
                    L += 1
                while(a[R] >= a[pivot] and L < R):
                    R -= 1 
        
                if L < R:
                    if L == pivot:
                        pivot = R
                    a[L], a[R] = a[R], a[L]
            
            a[pivot], a[R] = a[R], a[pivot]
            return R
            
        
        a = [54, 88, 77, 26, 93, 7, 49]
        print('정렬 전 {}'.format(a))
        quickSort(a, 0, len(a)-1)
        print('정렬 후 {}'.format(a))
        
        
        ```
      

------

## 큐(Queue)

### 큐

- 선입선출구조(FIFO: First In First Out)

- ![image](https://user-images.githubusercontent.com/52814897/63818995-84a55200-c97e-11e9-856a-fe7308e9732e.png)

- 큐 구현

  - ```python
    class Queue:
        def __init__(self):
            self.queue = []
    
        def enqueue(self, ele):
            self.queue.append(ele)
            return None
    
        def dequeue(self):
            if len(self.queue) < 1:
                print("Empty")
                return False
            else:
                return self.queue.pop(0)
    ```

  - 

- 라이브러리 모듈

  - ```python
    import queue
    q = queue.Queue()
    q.put('A')
    q.put('B')
    q.get()
    ```

- 선형 큐

  - 장점: 삽입, 삭제의 처리속도 빠름
  - 단점: 포화상태로 잘못 인식할 경우 메모리 낭비 발생

- 원형 큐

  - ```python
    def isEmpty():
        return front == ResourceWarning
    
    def isFull():
        return (rear+1) % len(cQ) == front
    
    def enQueue(item):
        global rear
        if isFull():
            print('Queue_Full')
        else:
            rear = (rear + 1) % len(cQ)
            cQ[rear] = item
        
    def deQueue():
        global front
        if isEmpty():
            print('Queue_Empty')
        else:
            front = (front + 1) % len(cQ)
            return cQ[front]
    
    cQ_SIZE = 3
    cQ = [0]*cQ_SIZE
    
    front = rear = 0
    
    enQueue('A')
    enQueue('B')
    # Size는 3이지만 1개는 Full을 검사하는 용도로 사용
    # 실제 사용가능 메모리는 2개이다.
    enQueue('C')
    
    ```

- 열결 큐

  - 메모리 동적 활용으로 절약 가능

### 우선순위 큐

- 삽입, 삭제시 원소의 재배치가 발생하여 시간과 메모리 낭비가 큼

### 큐의 활용 : 버퍼(Buffer)

- 버퍼
  - 데이터를 한 곳에서 다른 곳으로 전송할 때 일시적으로 그 데이터를 보관하는 메모리 영역
  - 버퍼링: 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작
  - FIFO 방식의 자료구조인 큐가 활용

### 너비우선탐색 (BFS)

- 연습문제3

- ```python
  # 정점이 1~7로 7개이지만 편의상 인덱스 번호와 맞추기 위해 * 8 을 해주어
  # 인덱스가 0~8까지 생기게 한다
visited = [0] * 8
  
  
  
  ```
  

### 최단경로

## 리스트

### 순차리스트

### 연결리스트

- ```python
  class Node:
      def __init__(self, data, link):
          self.data = data
          self.link = link
          
  def addtoFirst(data): # 첫 노드에 데이터 삽입
          global Head
          Head = Node(data, Head) # 새로운 노드 생성
          
  def add(pre, data): # pre 다음에 데이터 삽입
      if pre == None:
          print('error')
      else:
          pre.link = Node(data, pre.link)
          
  def addtoLast(data): # 마지막에 데이터 삽입
      global Head
      if Head == None: # 빈 리스트이면
          Head = Node(data, None)
      else:
          p = Head
          while p.link != None: # 마지막 노드 찾을때까지
              p = p.link
          p.link = Node(data, None)
  
  def delete(pre): # pre 다음 노드 삭제
      if pre == None or pre.link == None:
          print('error')
      else:
          pre.link = pre.linke.link
          
  def deleteFist(): # 처음 노드 삭제
      global Head
      if pre == None:
          print('error')
      else:
          Head = Head.link
          
  data = [1, 2, 3, 4]
  Head = None
  
  # 내림차.
  for i in range(len(data)):
      addtoFirst(data[i])
  # 오름차
  for i in range(len(data)):
      addtoLast(data[i])
      
  add(Head, 8) # 데이터 삽입하기
      
  while Head.link != None:
      print(Head.data, end='->')
      Head = Head.link
  print(Head.data)
  ```

- 이중 연결 리스트

  - 양쪽 방향으로 순회할 수 있도록 연결한 리스트

### 삽입정렬

- ```python
  def insertion_sort(a):
      for i in range(1, len(a)):
          for j in range(i, 0, -1):
              if a[j-1] > a[j]:
                  a[j], a[j-1] = a[j-1], a[j]
                  
  a = [50, 80, 70, 20, 90]
  
  print('정렬 전: ', end='')
  print(a)
  insertion_sort(a)
  
  print('정렬 후: ', end='')
  print(a)
  ```

### 병합정렬

- 분할 과정

  - ```python
    def merge_sort(m):
        if len(m) <= 1: # 사이즈가 0이거나 1인 경우, 바로 리턴
            return m
        
        # 1. DIVIDE 부분
        mid = len(m) // 2
        left = m[:mid]
        right = m[mid:]
        
        # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
        left = merge_sort(left)
        right = merge_sort(right)
        
        # 2. CONQUER부분 : 분할된 리스트를 병합
        return merge(left, right)
    ```

- 병합 과정

  - ```python
    def merge(left, right):
        result = [] # 두 개의 분할된 리스트를 병합하여 result를 만듦
        
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
                
        if len(left) > 0:
            result.extend(left)
        if len(right) > 0:
            result.extend(right)
        return result
    ```

- 리스트를 이용한 스택의 구현

  - Push/Pop

  - ```python
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.link = link
    
    def push(i):
        global top
        top = Node(i, top)
        
    def pop():
        global top
        
        if top == None:
            print("error")
        else:
            data = top.data
            top = top.link
            return data
            
    top = None
    push(3)
    push(4)
    push(5)
    push(6)
    pop()
    
    while top.link != None:
        print(top.data, end='->')
        top = top.link
    
    print(top.data)
    ```

## 완전 검색 & 그리디

### 반복(iteration)과 재귀(Recursion)

- `for`와 `while`의 차이

  - 반복 횟수를 알 경우와 그렇지 않을 경우

- `재귀`는 반복에 비해 간결하고 이해하기 쉬우나, 함수 호출이기 때문에 반복적인 스택의 사용과 메모리 및 속도에서 `성능 저하` 발생

- 재귀를 이용한 최솟값 구하기

  - ```python
    arr = [9, 2, 3, 7, 5, 6, 8, 1, 4, 10]
    def getMin(start, end):
        if start == end:
            return arr[start]
        else:
            result = getMin(start, end - 1)
            return min(result, arr[end])
    print(getMin(0, len(arr) - 1))
    ```

### 완전 검색 기법

- 고지식한 방법(Brute-force)
  - 모든 경우를 확인해본다.

### 순열과 조합

- 정점이 n개 있을 경우 간선의 개수: n * (n-1) / 2

- 순열과 조합![image](https://user-images.githubusercontent.com/52814897/64932826-9c387200-d87c-11e9-8403-1a68cc6ecf51.png)

  - ``` python
    # 순열
    arr = 'ABCDE'
    N = len(arr)
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                print(arr[i], arr[j], arr[k])
    
    # 조합
    arr = 'ABCDE'
    N = len(arr)
    
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                print(arr[i], arr[j], arr[k])
    
    # 조합(재귀)
    arr = 'ABCDE'
    N, R = len(arr), 3
    choose = []
    def comb(k, s):
        if k == R:
            print(choose)
        else:
            for i in range(s, N):
                choose.append(arr[i])
                comb(k + 1, i + 1)
                choose.pop()
    
    comb(0, 0)
    
    # 조합2(재귀 + 인자전달)
    def combination(com_arr, start):
        if len(com_arr) == R:
            print(com_arr)
        else:
            for i in range(start, N):
                combination(com_arr + [N_arr[i]], i + 1)
                
    N = 5
    R = 3
    N_arr = [i for i in range(N)]
    combination([], 0)
    ```

- 중복 순열 ![image](https://user-images.githubusercontent.com/52814897/64934766-073b7600-d888-11e9-8119-f21f134b8f4c.png)

- 중복 조합 ![image](https://user-images.githubusercontent.com/52814897/64935029-75cd0380-d889-11e9-9e09-fe3090aa787e.png)

### 탐욕 알고리즘

- Top-down 방식. 하위 문제를 풀기 전에 선택이 먼저 이루어진다.
- 빠르고 간결
- 대부분의 최적화 문제는 탐욕으로 풀 수 없는 경우가 많다.
- DP와 비교

------

## 분할 정복 & 백트래킹

### 분할정복

- 기본적으로 2분할(양팔저울로 진짜 금화 찾기 문제)
- 병합정렬, 퀵정렬

#### 병합정렬

- 코드는 복잡하지만 N*logN으로 N^2^ 보다 빠르다.

```python
def mergeSort(lo, hi):  # 매개변수 --> 문제의 크기
    if lo == hi: return

    # 분할
    mid = (lo + hi) >> 1
    mergeSort(lo, mid)  # 왼쪽
    mergeSort(mid + 1, hi)  # 오른쪽
    # 왼쪽과 오른쪽을 병합
    i, j, k = lo, mid + 1, lo
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1
    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= hi:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1
    for i in range(lo, hi + 1):
        arr[i] = tmp[i]


arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)
print(arr)
mergeSort(0, len(arr) - 1)
print(arr)
```

#### 퀵정렬

- 퀵정렬은 병합정렬과 달리 중심 2분할이 아닌, `pivot`을 중심으로 분할한다.

```python
# Hoare-Partition 알고리즘
arr = [69, 10, 30, 2, 16, 8, 31, 22]
def quickSort(lo, hi):
    if lo >= hi: return

    # partition
    i, j, pivot = lo, hi, arr[lo]
    while i < j:
        while i <= hi and pivot >= arr[i]: i += 1
        while pivot < arr[j]: j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]

    quickSort(lo, j - 1)
    quickSort(j + 1, hi)
    
quickSort(0, len(arr) - 1)
```

```python
# Lomuto partition 알고리즘
arr = [69, 10, 30, 2, 16, 8, 31, 22]
def quickSort(lo, hi):
    if lo >= hi: return
    i = lo - 1
    for j in range(lo, hi):
        if arr[hi] > arr[j]
        	if += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]
   
    quickSort(lo, j - 1)
    quickSort(i + 1, hi)

print(arr)
quickSort(0, len(arr) - 1)
print(arr)
```

### 백트래킹

- 백트래킹과 DFS의 차이

  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 경로를 따라가지 않고 가지치기 한다.(Prunning)
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능

- 백트래킹을 이용한 순열구하기

  ```python
  # 백트래킹을 이용한 순열구하기
  arr = 'ABC'
  N = len(arr)
  order = [0] * N		# 순서를 저장
  visit = [False] * N
  def perm(a, k, n):
      if k == n:
          print(a)
     	else:
          for i in range(n):
              if visit[i]: continue
              visit[i] = True
              a[k] = i
              perm(a, k + 1, n)
              visit[i] = False
  perm(order, 0, N)
  ```

- N-Queen 문제

  ```python
  N = 8
  cnt = 0
  visit = [0] * N
  cols = [0] * N 	# 퀀의 열값을 저장
  def Possible(k, c): # k번 퀸의 열 i가 답이 되는 선택인지 조사
      for i in range(k): # 0 ~ k-1 번 퀸과 대각에 있는지 조사
          if k - i == abs(c - cols[i]):
              return False
      return True
      
  def nQueen(k):
      if k == N:
          global cnt
          cnt += 1
      else:
          for i in range(N):
              if visit[i] or not Possible(k, i): continue
                  visit[i] = 1
                  cols[k] = i		# k번 퀸의 열값을 i로 결정
                  nQueen(k + 1)
                  visit[i] = 0
  
  nQueen(0)
  ```

  

### 트리

- 한 개 이상의 노드로 이루어진 유한 집합

- 노드(node), 간선(edge), 루트 노드(root node), 형제 노드(sibling node), 조상 노드, 서브트리, 자손노드, 리프 노드(leaf node)

- 차수(degree): 노드의 차수, 트리의 차수

- 높이: 노드의 높이, 트리의 높이

- ```python
  13
  1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
  import sys
  sys.stdin = open('input.txt', 'r')
  
  
  def preorder(T):
      if T != 0:
          print(T, end=' ')
          preorder(child[T][0])
          preorder(child[T][1])
  
  def inorder(T):
      if T != 0:
          inorder(child[T][0])
          print(T, end=' ')
          inorder(child[T][1])
  
  def postorder(T):
      if T != 0:
          postorder(child[T][0])
          postorder(child[T][1])
          print(T, end=' ')
  
  N = int(input())
  arr = list(map(int, input().split()))
  child = [[0] * 2 for i in range(N+1)]
  
  for i in range(N - 1):
      if child[arr[i*2]][0] == 0:
          child[arr[i*2]][0] = arr[i*2+1]
      else:
          child[arr[i*2]][1] = arr[i*2+1]
  
  print('전위 순회 결과: ', end=' ')
  preorder(1)
  print()
  print('중위 순회 결과: ', end=' ')
  inorder(1)
  print()
  print('후위 순회 결과: ', end=' ')
  postorder(1)
  
  ```

#### 이진 트리 - 종류

- 포화 이진 트리(Full Binary Tree)
  - 모든 레벨에 노드가 포화상태
  - 높이가 h일 때, 최대 노드 개수는 (2^h+1^ - 1)의 노드를 가진다.
- 완전 이진 트리(Complete Binary Tree)
  - 단말 노드 직전 노드까지는 포화 상태이며, 1번 부터 n 번 까지 차례대로 빈 자리가 없는 이진 트리
- 편향 이진 트리(Skewed Binary Tree)
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
    - 왼쪽 편향 이진 트리, 오른쪽 편향 이진 트리

#### 이진 트리 - 순회(traversal)

순회(traversal)란 트리의 각 노드를 중복되지 않게 전부 방문 하는 방법

- 전위 순회(preorder traversal, VLR): 루트 - 왼쪽 - 오른쪽

  ```python
  preorder_traverse (TREE T)
  	IF T is not null
      	visit(T)
          preorder_traverse(T.left)
          preorder_traverse(T.right)
  ```

- 중위 순회(inorder traversal, LVR)

  ```python
  inorder_traverse (TREE T)
  	IF T is not null
      	inorder_traverse(T.left)
          visit(T)
          inorder_traverse(T.right)
  ```

- 후위 순회(postorder traversal, LRV)



#### 트리의 표현

![image](https://user-images.githubusercontent.com/52814897/66532046-f14c6880-eb48-11e9-926d-c17ad7f6606a.png)

#### 이진 탐색 트리의 연산

- 탐색 연산
  - `x==k`: 탐색 성공, `x<k`: 왼쪽 서브 트리 탐색, `x>k`: 오른쪽 서브 트리 탐색
- 삽입 연산
- 삭제 연산
  - 단말 노드일 경우(차수 = 0): 그냥 삭제하면 된다.
  - 하나의 서브 트리만 가진 경우(차수 = 1): 삭제 후 서브 트리를 이동해줘야 한다.
  - 두 개의 서브 트리를 가진 경우(차수 = 2)
    - 자식 노드 중에 삭제한 노드의 자리에 들어올 노드를 선택해야 함.
      - 왼쪽 서브 트리의 가장 큰 킷값
      - 또는, 오른 서브 트리의 가장 작은 킷값\

- 이진 탐색 트리 - 성능
  - 탐색, 삽입, 삭제 시간은 트리의 높이만큼 시간이 걸린다.
    - O(h), h: BST의 깊이(height)
  - 평균의 경우
    - BT(Balanced Tree): 균형 잡힌 트리일 경우
    - O(log n)
  - 최악의 경우
    - 한쪽으로 치우친 편향 이진 트리의 경우
    - O(n). 순차 탐색과 시간 복잡도가 같다.

### 힙

- 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조
- 최대 힙(max heap)
  - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키 값>자식 노드의 키 값
  - 루트 노드: 키 값이 가장 큰 노드
- 최소 힙(min heap)
  - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키 값<자식 노드의 키 값
  - 루트 노드: 키 값이 가장 작은 노드

#### 힙 연산

- 삽입
  - 부모 노드와 비교하며 자리를 바꾼다.
- 삭제
  - 특정 위치의 노드 삭제후, 마지막 노드로 자리를 채운 후, 최대 또는 최소 힙의 조건을 따진 후 자리를 바꾼다.

#### 힙이 활용

- 특별한 큐의 구현(우선 순위 큐) / 정렬(힙 정렬)
- 완전 정렬보다 관리 비용이 적다.

------

## GRAPH

- 실 세계 문제를 그래프로 추상화해서 해결하는 방법
- 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현
- 정점(Vertext)들의 집합과 간선(Edge)들의 집으로 구성된 자료 구조
- V개의 정점이 가지는 그래프의 최대 간선의 개수는 V*(v-1)/2 개이다.

### 서로소 집합들(Disjoint-Sets)

- 창용마을 무리의 개수

  ```python
  # disjoint-sets
  for tc in range(1, int(input()) + 1):
      V, E = map(int, input().split())
      p = [x for x in range(V + 1)] # 정점의 번호 1 ~V
  
      def find_set(x):
          if x != p[x]:
              p[x] = find_set(p[x])
          return p[x]
  
      ans = V
      for _ in range(E):
          u, v = map(int, input().split())
          a = find_set(u); b = find_set(v)
          if a == b: continue
          p[b] = a
          ans -= 1
  ```

### 최소신장트리(MST)

- KRUSKAL 알고리즘
- PRIM 알고리즘

### 최단 경로

- Dijkstrea 알고리즘
  - 최단 경로의 최적부분 구조

------

## 기타 설명

- 객체 지향 프로그래밍
  - 객채는 함수와 변수를 하나의 단위로 묶을 수 있는 방법이다.
  - 객체는 속성(attribute)과 동작(action)을 가지고 있다.
    - 예) 자동차: 객체 / 속성: 메이커, 모델, 색상 / 동작: 주행하기, 방향전환
  - 클래스는 객체를 여러개 만들 수 있는 틀인데, 모든 객체가 같을 필요는 없다. 기본적으로 틀은 같으나, 일부 속성(색상, 모델)과 동작 등을 변경할 수 있다.

## 수식 Tip