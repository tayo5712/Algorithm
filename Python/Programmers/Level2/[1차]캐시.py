from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()
    for city in cities:
        if cacheSize:   # 캐시사이즈가 1 이상일 때만
            city = city.lower()     # 대소문자 구분 없이
            if city in q:
                q.remove(city)      # 기존 캐시에 있는 값이면 빼서 다시 뒤로 넣어줌
                q.append(city)
                answer += 1
            else:
                if len(q) >= cacheSize:     # 기존에 없는 값이 들어오면 가장 오래된 값 (제일 앞에 있는 값)을 제거하고 넣기
                    q.popleft()
                q.append(city)
                answer += 5
        else:
            answer += 5

    return answer

