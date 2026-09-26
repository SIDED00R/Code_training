# [LeetCode Easy] Two Sum - two-sum

[문제 링크](https://leetcode.com/problems/two-sum/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Hash Table`

## 제출 일자

2026년 9월 26일 10:36:40

## 문제 설명

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

2 <= nums.length <= 10^4

-10^9 <= nums[i] <= 10^9

-10^9 <= target <= 10^9

Only one valid answer exists.

 

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: O(N)

### 잘한 점

- 해시 맵을 사용하여 시간 복잡도를 O(N)으로 최적화함
- 배열을 단 한 번만 순회(One-pass)하는 효율적인 구조
- 변수명(now_num, idx)이 직관적이고 가독성이 좋음
- 중복된 값이 존재하는 엣지 케이스를 자연스럽게 처리함

### 개선할 점

- 추가적인 해시 맵을 사용하므로 최악의 경우 O(N)의 공간 복잡도가 발생함 (문제 해결 상 불가피함)

### 상세 피드백

제출하신 코드는 이 문제에 대해 가장 이상적이고 최적화된 해법 중 하나입니다. 해시 맵(Dictionary)을 활용하여 배열을 단 한 번만 순회(One-pass)하면서 필요한 보수(target - now_num)가 이미 해시 맵에 존재하는지 확인하고, 존재하지 않는다면 현재 원소와 그 인덱스를 맵에 저장합니다. 이 방식은 O(N)의 시간복잡도와 O(N)의 공간복잡도로 문제를 해결하며, 문제의 Follow-up 요구사항인 O(N^2) 미만의 시간복잡도를 완벽하게 충족합니다. 변수명(now_num, idx)도 직관적이며 가독성이 매우 뛰어납니다. 엣지 케이스인 중복된 값(예: 예제 3의 [3, 3])에 대해서도 현재 원소를 맵에 넣기 전에 보수를 먼저 검사하므로 올바르게 동작합니다. 전반적으로 군더더기 없는 훌륭한 파이썬 코드입니다.
