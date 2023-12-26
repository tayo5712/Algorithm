def solution(genres, plays):
    answer = []
    total_dict = {}
    sing_dict = {}
    
    for i in range(len(genres)):
        if genres[i] not in total_dict:
            total_dict[genres[i]] = 0
            sing_dict[genres[i]] = []
        total_dict[genres[i]] += plays[i]
        sing_dict[genres[i]].append(i)
    
    genre_rank = sorted(total_dict, key = lambda x : total_dict[x], reverse = True)      
    
    for k, v in sing_dict.items():
        sing_dict[k] = sorted(sing_dict[k], key = lambda x : plays[x], reverse = True)
    
    for genre in genre_rank:
        if len(sing_dict[genre]) > 1:
            answer.append(sing_dict[genre][0])
            answer.append(sing_dict[genre][1])
        else:
            answer.append(sing_dict[genre][0])
    
    return answer
