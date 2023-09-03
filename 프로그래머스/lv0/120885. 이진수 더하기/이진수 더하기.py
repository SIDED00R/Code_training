def solution(bin1, bin2):
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    answer = bin1 + bin2
    return bin(answer).replace("0b","")