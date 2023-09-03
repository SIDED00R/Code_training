def solution(strArr):
    return [s.lower() if idx % 2 == 0 else s.upper() for idx, s in enumerate(strArr)]