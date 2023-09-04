def solution(polynomial):
    polynomial = polynomial.split()
    x = []
    num = []
    xnum = 0
    number = 0
    for op in polynomial:
        if "x" in op:
            x.append(op)
        elif op == "+":
            continue
        else:
            num.append(op)
    for n in num:
        number += int(n)
    for numx in x:
        if numx == "x":
            xnum += 1
        else:
            constant = numx.replace("x", "")
            xnum += int(constant)   
            
    if number != 0 and xnum != 0:
        return f"{xnum}x + {number}" if xnum > 1 else f"x + {number}"
    elif number != 0:
        return f"{number}"
    return f"{xnum}x" if xnum > 1 else f"x"
