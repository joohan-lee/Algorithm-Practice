#예제
def change_coin():
  #1260원을 500, 100, 50, 10원으로 거슬러줄 때 최소 코인 개수는?
  n = 1260
  count = 0 
  
  coin_types = [500, 100, 50, 10]

  for coin in coin_types:
    count += n // coin #동전 개수(몫)
    n %= coin #남은 돈(나머지)
    
  
  return count
###################################################################
#실전문제1 : 큰수의 법칙
def big_number_law():
  #큰 수의 법칙
  n, m, k = map(int, input().split())
  data = list(map(int, input().split()))

  data.sort()
  first = data[len(data)- 1]
  second = data[len(data) - 2]

  result = 0
  
  i=0
  while i < m:
    for j in range(k):
      result += first
      i = i + 1
    result += second
    i = i + 1
  
  return result

def big_number_law2():
  #큰 수의 법칙2.abs 수열을 이용.
  n, m, k = map(int, input().split())
  data = list(map(int, input().split()))

  data.sort()
  first = data[n- 1]
  second = data[n - 2]

  result = 0
  
  result = (first*k + second) * (m // (k+1)) + (m%(k+1))*first
  
  return result
########################################################################
#실전문제2 : 숫자카드게임

def numberCardGame():
  n, m = map(int, input().split())
  
  max = 0
  for i in range(n):
    data = list(map(int, input().split())) #한줄씩 입력받는 idea
    min_data = min(data)
    if max < min_data:
      max = min_data

  return max

########################################################################
#실전문제3 : 1이 될때까지

def untilOne():
  n, k = map(int, input().split())
  
  count = 0 # 시도횟수
  while n != 1:
    if n%k == 0:
      n = n/k
    else:
      n = n-1
    count += 1

  return count

#print(change_coin())
#print(big_number_law2())
#print(numberCardGame())
print(untilOne())
