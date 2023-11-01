def gcd(a, b):
    if a < b:
        a, b = b, a
        
    while b != 0:
        a, b = b, a % b
    return a

def solution(arrayA, arrayB):
    answer = 0
    A = True
    B = True
    A_gcd = arrayA[0]
    B_gcd = arrayB[0]
    for num1 in arrayA[1:]:
        A_gcd = gcd(A_gcd, num1)
    for num2 in arrayB[1:]:
        B_gcd = gcd(B_gcd, num2)
        
    for i in range(len(arrayA)):
        if arrayA[i] % B_gcd == 0:
            B = False
    for i in range(len(arrayB)):
        if arrayB[i] % A_gcd == 0:
            A = False
        
    if not A and not B:
        return 0
    else:
        if A and B:
            return max(A_gcd, B_gcd)
        elif A:
            return A_gcd
        else:
            return B_gcd