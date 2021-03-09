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
  
#1개 테스트 틀린이유는 하기와 같이 추정.
#=> lost : [1,2,3,3] / reserve : [3,4] 같이 학생에 중복된 넘버가 있으면 처리를 못함.
  
  ###################################################
    
#풀이2. - 210309
#통과(100/100)

def solution(n, lost, reserve):
    answer = 0
    set_lost = set(lost) - set(reserve) #여벌있고 도난당한 사람 제거
    set_reserve = set(reserve) - set(lost) #여벌있고 도난당한 사람 제거
    
    for person_num in set_reserve: #빌려줄 수 있는 사람 모두 검사
        if person_num - 1 in set_lost: #빌려줄 수 있는 사람 번호보다 1 작으면 빌려줌
            set_lost.remove(person_num-1)
        elif person_num + 1 in set_lost: #빌려줄 수 있는 사람 번호보다 1 크면 빌려줌
            set_lost.remove(person_num + 1)
    
    answer = n - len(set_lost)
    
    return answer
 
