def solution(myString, pat):
    return 1 if pat.replace("A","c").replace("B","A").replace("c","B") in myString else 0