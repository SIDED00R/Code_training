# [LeetCode Medium] Two Sum II - Input Array Is Sorted - two-sum-ii-input-array-is-sorted

[문제 링크](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Two Pointers`, `Binary Search`

## 제출 일자

2026년 10월 4일 07:27:25

## 문제 설명

1-인덱스 정수 배열 numbers가 주어지며, 이 배열은 이미 비내림차순으로 정렬되어 있습니다.

합이 특정 target 숫자가 되는 두 숫자를 찾으세요. 이 두 숫자를 numbers[index1]와 numbers[index2]라고 하며, 여기서 1 <= index1 < index2 <= numbers.length입니다.

두 숫자의 인덱스 index1과 index2를 길이 2인 정수 배열 [index1, index2]로 반환하세요.

테스트는 정확히 하나의 해답이 존재하도록 생성됩니다. 같은 요소를 두 번 사용할 수는 없습니다.

풀이는 상수만큼의 추가 공간만 사용해야 합니다.

 

예제 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: 2와 7의 합은 9입니다. 따라서 index1 = 1, index2 = 2입니다. [1, 2]를 반환합니다.

예제 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: 2와 4의 합은 6입니다. 따라서 index1 = 1, index2 = 3입니다. [1, 3]을 반환합니다.

예제 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: -1과 0의 합은 -1입니다. 따라서 index1 = 1, index2 = 2입니다. [1, 2]를 반환합니다.

 

제약 조건:

2 <= numbers.length <= 3 * 10^4

-1000 <= numbers[i] <= 1000

numbers는 비내림차순으로 정렬되어 있습니다.

-1000 <= target <= 1000

테스트는 정확히 하나의 해답이 존재하도록 생성됩니다.

## 코드 리뷰

- 효율성: 보통
- 시간복잡도: O(N log N) 시간, O(1) 공간
- 더 나은 알고리즘: Two Pointers 기법을 사용하면 O(N) 시간, O(1) 공간으로 해결 가능합니다. 배열이 이미 정렬되어 있으므로 left=0, right=len(numbers)-1로 시작해서 합이 target보다 크면 right를 감소시키고, 작으면 left를 증가시키는 방식으로 한 번의 순회로 답을 찾을 수 있습니다. 이 문제의 알고리즘 태그에도 'Two Pointers'가 명시되어 있어 이 방법이 의도된 풀이입니다.

### 잘한 점

- 이분탐색의 경계 조건(start <= end, mid-1/mid+1)을 정확하게 구현하여 off-by-one 오류가 없음
- 변수명이 비교적 명확하여 코드의 의도를 파악하기 쉬움

### 개선할 점

- 정렬된 배열이라는 특성을 완전히 활용하지 못해 O(N) Two Pointers 대신 O(N log N) 풀이를 사용함
- 해를 찾지 못하는 경우에 대한 명시적 처리(예외 발생 또는 명확한 return)가 없어 암묵적으로 None을 반환함
- 각 외부 루프 반복마다 내부에서 전체 이분탐색을 다시 수행하므로 불필요한 중복 비교가 발생함

### 상세 피드백

주어진 코드는 각 인덱스에 대해 나머지 구간에서 이분탐색을 수행하는 방식으로, 정답은 찾지만 전체 시간복잡도가 O(N log N)이 되어 이 문제에서 기대하는 O(N) Two Pointers 풀이보다 비효율적입니다. 배열이 정렬되어 있다는 성질을 완전히 활용하지 못하고 있습니다. Two Pointers를 사용하면 바깥쪽 for 루프 자체가 필요 없어지고, 각 포인터가 한 번씩만 이동하므로 전체 N번의 비교로 끝낼 수 있습니다. 또한 코드에 함수가 정답을 못 찾았을 때 명시적인 return 문이 없어 None을 반환하게 되는데, 문제 제약조건상 항상 해가 존재한다고 보장되어 있어 실제로는 문제가 되지 않지만, 방어적 코딩 관점에서는 바람직하지 않습니다. 변수명(now_num, start, end)은 대체로 명확하고 이해하기 쉽습니다. 이분탐색 경계 처리(start <= end, mid-1/mid+1)는 정확하게 구현되어 있어 버그 없이 동작합니다.
