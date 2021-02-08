#실전문제 1. 부품 찾기
#이진탐색이용가능
#계수 정렬 이용 가능.
#집합 자료형 이용 가능.

def binary_search(array, elem, start, end):
  if start > end:
    return "no"

  mid = (start+end) // 2

  if array[mid] == elem:
    return "yes"

  elif elem < array[mid]: #찾고자 하는게 중간값보다 작으면 왼쪽 탐색
    if binary_search(array, elem, start, mid-1) == "yes":
      return "yes"

  else: #찾고자 하는게 중간값보다 크면 오른쪽 탐색
    if binary_search(array, elem, mid+1, end) == "yes":
      return "yes"

  

n = int(input())
array = list(map(int, input().split())) #부품 모음
array.sort()

m = int(input())
elements = list(map(int, input().split())) #찾을 부품


for j in range(m):
  print(binary_search(array, elements[j], 0, len(array)-1), end = ' ')


##########################################################################################################


#실전문제1. 부품 찾기
#계수 정렬 이용하기


n = int(input())
array = [0] * 1000001

for i in input().split():
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))


result = []
for i in range(m):
  if array[x[i]] == 1:
    #result.append("yes")
    print("yes", end = ' ')
  else:
    #result.append("no")
    print("no", end = ' ')
  
#############################################################################################################
#집합 자료형 이용하기

n = int(input())
array = list(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print("yes", end = ' ')
  else:
    print("no", end = ' ')
