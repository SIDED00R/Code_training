def solution(myStr):
    answer = []
    ans = myStr.replace("b","a").replace("c","a")
    ans = ans.split("a")
    ans = " ".join(ans).split()
    if ans == []:
        return ["EMPTY"]
    return ans