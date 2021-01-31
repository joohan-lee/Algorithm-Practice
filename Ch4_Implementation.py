##########################################
#Note
#1.코딩테스트에서 '구현'이란 머릿속의 알고리즘을 소스코드로 바꾸는 과정.
#2.일반적 코딩테스트 파이썬 환경은 1백만개 데이터를 O(NlogN) 시간복잡도로 계산시,
#  1초가 소요됨. (1백만개의 O(NlogN)복잡도 데이터 연산 => 2천만번 연산)

###########################################
#예제4-1 : 상하좌우 (시뮬레이션 유형)
def upDownLeftRight():
  n = int(input())
  plan = input().split()

  x, y = 1, 1

  for c in plan:
    if c == 'L' and y > 1:
      y -= 1
    elif c == 'R' and y < n:
      y += 1
    elif c == 'U' and x > 1:
      x -= 1
    elif c == 'D' and x < n:
      x += 1

  print(x, y)

###########################################
#예제4-2 : 시각 *
def timeCount3():
  n = int(input())

  cnt = 0
  
  for i in range(n+1):
    for j in range(60):
      for k in range(60):
        #if str(i).find("3") or str(j).find("3") or str(k).find("3"): #find는 위치를 존재 위치를 반환, 없으면 -1 반환. 0 : false / 그 외 : true
        if '3' in str(i) + str(j) + str(k):
          cnt += 1
  
  return cnt



###########################################
#실전문제1. 왕실의 나이트
def knight():
  loc = input()
  col = int(ord(loc[0])) - int(ord('a')) + 1
  row = int(loc[1])

  steps = [(-1,-2), (1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1)]

  cnt = 0
  
  for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row > 0 and next_row <= 8 and next_col > 0 and next_col <=8:
      cnt += 1
    
  return cnt

#############################################
#실전문제2. 게임 개발
def gameDevelop():
  #n,m 입력받기
  n, m = map(int, input().split())
  
  #리스트 내포(List Comperehension))
  #[표현식 for 항목1 in 반복가능객체1 if 조건문1
  #for 항목2 in 반복가능객체2 if 조건문2
  #...
  #for 항목n in 반복가능객체n if 조건문n]
  
  #방문한 배열 초기화
  d = [[0] * m for _ in range(n)]

  #x,y, direction (현재위치, 바라보는 방향)
  x, y, direction = map(int, input().split())
  d[x][y] = 1 #현재 위치는 방문 처리

  #맵 정보 입력
  array = []
  for k in range(n):
    array.append(list(map(int, input().split())))

  
  #북,동,남,서 이동 정의
  dx = [-1,0,1,0]  #방향 0:북, 1:동, 2:남, 3: 서
  dy = [0,1,0,-1]

  #시뮬레이션 시작
  count = 1 
  turn_time = 0

  while True:
    #왼쪽 회전
    direction -= 1
    if direction == -1:
      direction = 3
    
    #방향대로 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    #이동한 곳이 가보지 않고 육지라면 이동.
    if d[nx][ny] == 0 and array[nx][ny] == 0:
      d[nx][ny] = 1
      x = nx
      y = ny
      count += 1
      turn_time = 0

      continue

    else:
      turn_time += 1
    
    #네 방향 모두 가지 못하는 경우
    if turn_time == 4:
      #뒤로한칸
      nx = x - dx[direction]
      ny = y - dy[direction]

      if array[nx][ny] == 0:
        x = nx
        y = ny
      else:
        break

      turn_time = 0

  print(count)
      



#Main
#upDownLeftRight()
#print(timeCount3())
#print(knight())

gameDevelop()
