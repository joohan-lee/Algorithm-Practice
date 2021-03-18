#백준 9019번. DSLR

#D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
#S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
#L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
#R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.

#프로그램 입력은 T 개의 테스트 케이스로 구성된다. 테스트 케이스 개수 T 는 입력의 첫 줄에 주어진다. 각 테스트 케이스로는 두 개의 정수 A와 B(A ≠ B)가 공백으로 분리되어 차례로 주어지는데 A는 레지스터의 초기 값을 나타내고 B는 최종 값을 나타낸다. A 와 B는 모두 0 이상 10,000 미만이다.

############################################################
import sys
import collections
input = lambda : sys.stdin.readline().strip()

def D(n):
  return (2*n) % 10000

def S(n):
  return ((n-1) + 10000) % 10000

def L(n):
  s = str(n).zfill(4)
  s = s[1:] + s[0]
  return int(s)

def R(n):
  s = str(n).zfill(4)
  s = s[3] + s[0:3]
  return int(s)

t = int(input())
cmd = ['D','S','L','R']
answer = 0 

for i in range(t):
  A, target = map(int, input().split(' '))
  #print(D(A))
  #print(S(A))
  #print(L(A))
  #print(R(A))
  
  #dq = collections.deque([A, ""]]) 이렇게 초기화 시 deque에 A값, ""가 deque원소로 각각 들어가므로 주의. 
  dq = collections.deque()
  dq.append([A,""])
  visited = [0] * 10000
  while dq:
    curNum, answer = dq.popleft()
    visited[curNum] = 1 #방문표시

    temp = D(curNum)
    if temp == target:
      print(answer + 'D')
      break
    elif visited[temp] == 0:
      visited[temp] = 1
      dq.append([temp, answer + 'D'])
    
    temp = S(curNum)
    if temp == target:
      print(answer + 'S')
      break
    elif visited[temp] == 0:
      visited[temp] = 1
      dq.append([temp, answer + 'S'])
    
    temp = L(curNum)
    if temp == target:
      print(answer + 'L')
      break
    elif visited[temp] == 0:
      visited[temp] = 1
      dq.append([temp, answer + 'L'])
    
    temp = R(curNum)
    if temp == target:
      print(answer + 'R')
      break
    elif visited[temp] == 0:
      visited[temp] = 1
      dq.append([temp, answer + 'R'])
    
  
