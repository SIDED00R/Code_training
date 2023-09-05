def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = sum(days[ : a - 1 ])
    day = month + b
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    return week[day % 7]