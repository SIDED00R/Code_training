# [LeetCode Medium] Top K Frequent Elements - top-k-frequent-elements

[문제 링크](https://leetcode.com/problems/top-k-frequent-elements/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Hash Table`, `Divide and Conquer`, `Sorting`, `Heap (Priority Queue)`, `Bucket Sort`, `Counting`, `Quickselect`

## 제출 일자

2026년 10월 23일 10:53:58

## 문제 설명

정수 배열 nums와 정수 k가 주어졌을 때, k개의 가장 빈도가 높은 원소를 반환하세요. 답은 어떤 순서로든 반환할 수 있습니다.

 

예제 1:

입력: nums = [1,1,1,2,2,3], k = 2

출력: [1,2]

예제 2:

입력: nums = [1], k = 1

출력: [1]

예제 3:

입력: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

출력: [1,2]

 

제약 조건:

1 <= nums.length <= 10^5

-10^4 <= nums[i] <= 10^4

k는 [1, 배열 내 고유한 원소의 개수] 범위에 있습니다.

정답은 유일함이 보장됩니다.

 

후속 질문: 알고리즘의 시간 복잡도는 O(n log n)보다 더 나아야 합니다. 여기서 n은 배열의 크기입니다.

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: O(N log K) 시간, O(N) 공간 (N은 nums 길이, K는 반환할 개수)
- 더 나은 알고리즘: Bucket Sort(계수 정렬) 방식을 사용하면 O(N)에 해결 가능합니다. Counter로 빈도를 구한 뒤, 빈도값을 인덱스로 하는 버킷 배열(크기는 len(nums)+1)을 만들어 각 숫자를 해당 빈도 버킷에 담고, 버킷을 빈도가 높은 쪽부터 순회하며 k개를 채우면 힙 연산 없이도 선형 시간에 풀 수 있습니다. 또는 heapq.nlargest(k, dic.items(), key=lambda x: x[1])를 사용하면 같은 O(N log K)이지만 코드가 훨씬 간결해집니다.

### 잘한 점

- 힙을 K 크기로 유지하여 O(N log K)의 효율적인 시간복잡도를 달성함
- Counter를 활용해 빈도 계산을 간결하고 명확하게 처리함
- 불필요한 전체 정렬 없이 top-K만 추출하는 핵심 아이디어를 정확히 구현함

### 개선할 점

- 힙에 [value, key] 리스트 대신 튜플을 사용하면 비교 연산 성능과 메모리 효율이 더 좋음
- heapq.nlargest 같은 표준 라이브러리 함수를 쓰면 더 간결하게 동일한 복잡도를 구현할 수 있음
- O(N)에 해결 가능한 Bucket Sort 방식을 고려하지 않아 최적해에는 도달하지 못함
- 변수명(dic, now_case)이 다소 비직관적이어서 가독성이 떨어짐

### 상세 피드백

전체적으로 min-heap을 이용해 상위 K개 빈도 요소를 추적하는 정석적인 접근입니다. Counter로 빈도를 계산한 뒤 크기 K짜리 힙을 유지하면서 더 큰 빈도가 들어오면 가장 작은 값을 pop하는 로직이 정확하게 구현되어 있고, 시간복잡도는 O(N log K)로 문제의 follow-up 조건(O(N log N)보다 빠를 것)을 만족합니다. 다만 최적해인 O(N) Bucket Sort에는 미치지 못하며, 힙에 [value, key] 리스트를 넣는 방식은 튜플보다 비교 연산이 약간 느리고 메모리도 더 씁니다. 또한 Python 표준 라이브러리의 heapq.nlargest를 활용하면 직접 구현한 힙 로직보다 코드량을 크게 줄이면서 가독성을 높일 수 있습니다. k=1이나 모든 원소가 유니크한 경우 등 엣지케이스는 Counter와 힙의 일반적 동작으로 잘 처리되지만, 입력이 비어있는 경우(제약상 발생하지 않음)에 대한 고려는 없습니다. 변수명 dic, now_case 등은 다소 모호하여 freq_map, item처럼 더 명확한 이름을 쓰면 좋겠습니다.
