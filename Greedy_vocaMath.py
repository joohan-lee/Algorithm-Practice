#백준 1339번. 단어 수학
# 그리디 알고리즘, 브루트포스 알고리즘

#단어가 주어졌을때 알파벳에 숫자를 부여해서 만들 수 있는 최대합은?
#(단어의 알파벳 순서를 바꾸는 것은 아님)


#1.모든 단어를 자릿수대로 나열하기
#2.중복제거하기
#3.앞에있는 단어부터 높은 숫자 부여하기
#4.해당 숫자로 단어의 합 구하기

#########################################################
#풀이 1. - 오답
# 예시 : 3, ABUG, FGD, ET 인 경우 잘못된 답이 나옴.
# 그 이유는 ABFUGEGDT 로 나열 후 중복된 값을 제거하는데, 중복값 제거시
# 같은 알파벳 두번 이상 사용될 때 중복 알파벳들이 어디에 쓰이냐에 따라
# 값이 달라질 수 있음을 반영하지 못함.

'''
n = int(input())

words = []
for i in range(n):
  words.append(list(input()))

max_word = 0
for word in words:
  if max_word < len(word):
    max_word = len(word)

#1. 모든 단어를 자릿수대로 나열하기
t_list = []
for i in range(max_word):
  for word in words:
    if len(word) >= max_word - i:
      t_list.append(word[i - (max_word - len(word))])

#print(t_list)

#2. 중복제거하기
new_list = []
for i in t_list:
  if i not in new_list:
    new_list.append(i)


#print(new_list)

#3.4 합 구하기

for word in words:
  for c in range(len(word)):
    for i in range(len(new_list)):
      if new_list[i] == word[c]:
        word[c] = 9-i

sum = 0
for word in words:
  #print(word)
  #print(''.join([str(_) for _ in word]))
  sum += int(''.join([str(_) for _ in word]))

print(sum)

'''


#################################################
#풀이2.

n = int(input())

words = []
for i in range(n):
  words.append(input())

dict = {}
for word in words:
  k = len(word) - 1
  for ch in word:
    if ch in dict:
      dict[ch] += pow(10, k)
    else:
      dict[ch] = pow(10, k)
    k -= 1

#값으로 숫자 리스트 만들기
nums = []
for value in dict.values():
  nums.append(value)
  
nums.sort(reverse=True)

result, coef = 0, 9
#coef = 9
for num in nums:
  result += coef*num
  #print("coef",coef,",num",num,",result",result)
  coef -= 1
  
print(result)


