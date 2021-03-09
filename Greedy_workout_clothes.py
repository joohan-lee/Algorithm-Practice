#풀이 1. - 210307
#채점 점수 91.7/100

def solution(n, lost, reserve):
    answer = 0
    rental = 0
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] - reserve[j] <= 1 and lost[i] - reserve[j] >= -1:
                rental += 1
                reserve[j] = -99
                lost[i] = -99
                break
    answer = n - len(lost) + rental        
    return answer
  
  
  ###################################################
