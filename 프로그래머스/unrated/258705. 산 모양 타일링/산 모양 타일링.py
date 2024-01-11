def solution(n, tops):
    full_mountain_triangle = [1]
    one_missing_mountain = [1]
    before = 0
    for top in tops:
        if top == 1:
            full_mountain_triangle.append((3 * full_mountain_triangle[before] + one_missing_mountain[before]) % 10007)
            one_missing_mountain.append((2 * full_mountain_triangle[before] + one_missing_mountain[before]) % 10007)
        else:
            full_mountain_triangle.append((2 * full_mountain_triangle[before] + one_missing_mountain[before]) % 10007)
            one_missing_mountain.append((full_mountain_triangle[before] + one_missing_mountain[before]) % 10007)
        before += 1
    return full_mountain_triangle[-1] % 10007