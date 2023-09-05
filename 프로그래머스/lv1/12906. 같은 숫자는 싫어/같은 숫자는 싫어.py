def solution(arr):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return [arr[0]] + [i for idx, i in enumerate(arr) if i != arr[max(idx - 1, 0)]]