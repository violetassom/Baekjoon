def solution(n, words):
    answer = []

    # 반복문 i len(words)
    # i%3이 범인
    # 안 틀리는 조건: 한글자 이상인지, 앞사람이 말한 단어의 맨 끝자리로 시작하는지, 이전에 등장하지 않은 단어인지 <=> 틀리는 조건: 한글자, 앞사람 단어 맨끝자리로 시작 안함, 이전에 등장한 단어
    # answer = [범인 번호=i%n, 차례=i//n]
    # 범인이 없으면 [0,0] 리턴
    words_dict = {}
    for i in range(len(words)):
        cur_word = words[i]
        if i == 0:    
            prev_word = cur_word[0]
            # print(prev_word)
        if (len(cur_word)==1) or (prev_word[-1]!=cur_word[0]) or (cur_word in words_dict):
            return [i%n+1,i//n+1]
        words_dict[cur_word]=0
        prev_word = cur_word
        
    return [0,0]