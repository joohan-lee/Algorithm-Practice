#프로그래머스 DFS/BFS - 타겟 넘버 문제.
#BFS 풀이1.
def solution(numbers, target):
    superNode = [0]
    for i in numbers:
        subNode = []
        for j in superNode:
            subNode.append(j+i)
            subNode.append(j-i)
        superNode = subNode
        
    return superNode.count(target)
  #출처 : https://train-validation-test.tistory.com/entry/Programmers-level-2-%ED%83%80%EA%B2%9F-%EB%84%98%EB%B2%84-python

#BFS풀이2.
'''
import collections

def solution(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum+number, num_idx + 1))
            stack.append((current_sum-number, num_idx + 1))

    return answer
'''
  #출처 : https://eda-ai-lab.tistory.com/475

