#백준 5430번. AC
#구현, 자료구조, 문자열, 덱

#R은 숫자를 역순으로, D는 가장 앞 숫자를 버리되 배열이 비어있으면 error를 출력.

#첫째줄에 테스트 케이스 개수 T,
#각 테스트 케이스 첫째줄에 명령어(EX.RDD),
#둘째줄에 배열에 들어있는 숫자 수,
#셋째줄에 배열 입력(ex. [1,2,3]))

##################################################################
#풀이 1. 시간초과
''''
from collections import deque

t = int(input())

func = []
n_arr = []
list = []
dq = deque()

for i in range(t):
  func.append(input()) #수행할 함수 (문자열)
  n_arr.append(int(input()))  #배열 숫자 개수
  arrStr = input() #배열형태로 받은 문자열
  arrStr = arrStr.replace("[","")
  arrStr = arrStr.replace("]","")
  if len(arrStr) > 0:
    dq = deque(map(int,arrStr.split(",")))
  else:
    dq = deque()
  list.append(dq)

#print(list)

for i in range(t):
  
  for ch in func[i]:
    #print("func[i]",i,func[i])
    #print("ch", ch)
    
    if list[i] == "R":
      list[i].reverse()
    elif ch == "D":
      if len(list[i]) > 0:
        list[i].popleft()
      else:
        list[i] = "error"
        break

for i in range(len(list)):
  if list[i] != "error":
    print("[",end="")
    for j in range(len(list[i])):
      print(list[i].popleft(),end="")
      if len(list[i]) > 0:
        print(",", end="")

    print("]")
  else:
    print(list[i])

'''

########################################################
#풀이2. 틀렸습니다.
''''
from collections import deque

t = int(input())

func = []
n_arr = []
arr = []
list = []


for i in range(t):
  func.append(input()) #수행할 함수 (문자열)
  n_arr.append(int(input()))  #배열 숫자 개수
  arrStr = input() #배열형태로 받은 문자열
  arrStr = arrStr.replace("[","")
  arrStr = arrStr.replace("]","")
  if n_arr[i] > 0:
    list.append(arrStr.split(","))
  else:
    list.append([])

  

#print(list)

for i in range(t):
  r = 0
  d = 0  
  for ch in func[i]:
    #print("func[i]",i,func[i])
    #print("ch", ch)
    
    if ch == "R":
      r += 1
    elif ch == "D":
      d += 1
  
  #print("len :",len(list[i]))
  if r%2 != 0:
    list[i].reverse()
  
  if d > len(list[i]):
    print("error")
  else:
    print("[" + ','.join(list[i][d:]) +"]")

  


for i in range(len(list)):
  if list[i] != "error":
    print("[",end="")
    for j in range(len(list[i])):
      print(list[i].popleft(),end="")
      if len(list[i]) > 0:
        print(",", end="")

    print("]")
  else:
    print(list[i])

'''

########################################################
#풀이3. 

import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())

for i in range(t):
  p = input()
  n = int(input())
  de = input()[1:-1].split(',')
  p = p.replace('RR','')

  r = 0
  f, b = 0,0

  for i in p:
    if i == 'R':
      r += 1
    elif i == 'D':
      if r%2 == 0:
        f += 1 #앞에서부터 지울 개수
      else:
        b += 1 #뒤에서부터 지울 개수

  if f+b <= n:
    de = de[f:n-b]
    
    if r%2 == 1:
      print("[" + ','.join(de[::-1])+"]") #역순으로 출력
    else:
      print("[" + ','.join(de) + "]")
  else:
    print("error")
