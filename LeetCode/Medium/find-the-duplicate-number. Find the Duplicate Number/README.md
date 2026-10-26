# [LeetCode Medium] Find the Duplicate Number - find-the-duplicate-number

[문제 링크](https://leetcode.com/problems/find-the-duplicate-number/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Two Pointers`, `Binary Search`, `Bit Manipulation`, `Pigeonhole Principle`, `Floyd's Cycle Finding Algorithm`

## 제출 일자

2026년 10월 27일 07:47:57

## 문제 설명

각 정수가 [1, n] 범위에 포함되는 n + 1개의 정수를 담고 있는 배열 nums가 주어집니다.

nums에는 오직 하나의 중복된 숫자만 존재합니다. 이 중복된 숫자를 반환하세요.

배열 nums를 수정하지 않고, 오직 일정한(constant) 추가 공간만 사용하여 문제를 해결해야 합니다.

 

예제 1:

입력: nums = [1,3,4,2,2]
출력: 2

예제 2:

입력: nums = [3,1,3,4,2]
출력: 3

예제 3:

입력: nums = [3,3,3,3,3]
출력: 3

 

제약 조건:

1 <= n <= 10^5

nums.length == n + 1

1 <= nums[i] <= n

nums에 있는 모든 정수는 정확히 한 번 나타나며, 단 하나의 정수만 두 번 이상 나타납니다.

 

후속 질문:

nums에 중복된 숫자가 적어도 하나 존재해야 함을 어떻게 증명할 수 있을까요?

선형 시간 복잡도로 문제를 해결할 수 있나요?

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: 시간복잡도: O(N), 공간복잡도: O(1)

### 잘한 점

- Floyd's Cycle Detection Algorithm을 정확히 구현하여 시간 O(N), 공간 O(1)의 최적 복잡도를 달성함
- 배열을 수정하지 않고(read-only) 문제의 제약조건을 완벽하게 만족시킴
- slow/fast 두 변수만으로 cycle 탐지와 시작점 탐색을 모두 처리하여 코드가 매우 간결함

### 개선할 점

- 사용하지 않는 `from collections import Counter` import가 남아있어 코드 정리가 필요함
- Floyd's algorithm의 두 단계(cycle 탐지, cycle 시작점 찾기)에 대한 설명 주석이 없어 처음 보는 사람이 로직을 이해하기 어려움

### 상세 피드백

이 풀이는 Floyd's Cycle Finding Algorithm(토끼와 거북이 알고리즘)을 정확하게 구현한 최적 풀이입니다.

문제의 핵심 제약조건인 '배열 수정 금지'와 '상수 공간 사용'을 모두 만족시키면서 O(N) 시간복잡도를 달성했습니다. nums[i]를 포인터로 취급하여 cycle을 찾고, 두 번째 phase에서 cycle의 시작점(= 중복된 숫자)을 찾아내는 방식이 교과서적으로 잘 적용되었습니다.

다만 코드 상단의 `from collections import Counter` import가 실제로는 사용되지 않고 있습니다. 이는 아마 이전에 Counter를 이용한 O(N) 시간 O(N) 공간 풀이를 시도했다가 Floyd's algorithm으로 전환하면서 삭제를 빼먹은 것으로 보입니다. 불필요한 import는 제거하는 것이 좋습니다.

또한 코드에 Floyd's algorithm을 사용했다는 주석이 없어서, 처음 보는 사람은 slow/fast 변수가 왜 nums[idx] 형태로 움직이는지 이해하기 어려울 수 있습니다. 간단한 주석(예: '# phase 1: cycle 찾기', '# phase 2: cycle 시작점 찾기')을 추가하면 가독성이 크게 향상될 것입니다.

알고리즘 선택과 정확성 측면에서는 이미 최적의 풀이이며, n=1 같은 경계 케이스에서도 정상 동작함을 확인했습니다.
