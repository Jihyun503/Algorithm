from collections import Counter

def solution(participant, completion):
    t = set(participant) - set(completion)
    if len(t) :
        return list(t)[0]

    p = Counter(participant)
    c = Counter(completion)
    for key, value in p.items():
        if value != c[key]:
            return key
