def solution(s, n):
    answer = ""
    for alp in s:
        if alp == " ":
            answer += alp
        elif ord(alp) + n > 122:
            answer += chr(ord(alp) + n - 26)
        elif ord(alp) > 96:
            answer += chr(ord(alp) + n)
        elif ord(alp) + n > 90:
            answer += chr(ord(alp) + n - 26)
        elif ord(alp) > 64:
            answer += chr(ord(alp) + n)
    return answer