#실전문제 2. 떡볶이 떡 만들기
#Binary search , Parametric search


def parametric_search(array, target, start, end):

  while start <= end:
    mid = (start+end) // 2
    
    total = 0
    for elem in arr:
      elem = elem - mid
      if elem >= 0: #길이가 음수일 때는 더하지 않도록 주의!!!!
        total = total + elem 
      

    if total == target: #자른 떡 길이 합이 M이면 
      return mid
    elif total > target: #자른 떡 길이의 합이 더 크면
      start = mid + 1
      continue
    else: #자른 떡 길이 합이 M보다 작으면
      end = mid - 1
      continue
  
  return -1


n, m = map(int, input().split())

arr = list(map(int,input().split()))

max_leng = max(arr) #떡 중 제일 긴 떡

print(parametric_search(arr, m, 0, max_leng))



