def solution(binomial):
    a, op, b = binomial.split()
    a, b = int(a), int(b)
    return a + b if op == "+" else a - b if op == "-" else a * b