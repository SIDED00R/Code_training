# [LeetCode Medium] Product of Array Except Self - product-of-array-except-self

[문제 링크](https://leetcode.com/problems/product-of-array-except-self/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Prefix Sum`

## 제출 일자

2026년 10월 6일 23:36:43

## 문제 설명

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

2 <= nums.length <= 10^5

-30 <= nums[i] <= 30

The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

## 코드 리뷰

- 효율성: 보통
- 시간복잡도: O(N) 시간, O(N) 추가 공간 (prefix_product, suffix_product 배열 때문)
- 더 나은 알고리즘: 후속 질문(O(1) 추가 공간)까지 고려하면, 별도의 prefix/suffix 배열을 만들지 않고 answer 배열 자체를 prefix 곱으로 채운 뒤, 뒤에서부터 suffix 변수 하나만 유지하며 answer[i] *= suffix; suffix *= nums[i] 형태로 한 번 더 순회하면 추가 배열 없이 O(N) 시간, O(1) 추가 공간으로 풀 수 있습니다.

### 잘한 점

- 나눗셈을 사용하지 않아 0이 포함된 입력에서도 안전하게 동작함
- O(N) 시간복잡도로 문제의 필수 요구사항을 만족함
- prefix/suffix 곱을 활용하는 핵심 아이디어를 올바르게 구현함

### 개선할 점

- prefix_product, suffix_product 두 개의 보조 배열을 사용해 O(N) 추가 공간이 들어가며, Follow-up에서 요구하는 O(1) 추가 공간을 만족하지 못함
- 음수 인덱싱(-idx-1, -idx-2)을 반복적으로 사용해 코드의 의도를 파악하기 어렵고 오프바이원 오류 위험이 있음
- answer 배열을 바로 활용해 in-place로 prefix/suffix 곱을 누적하는 더 간결한 구현이 가능함에도 별도 리스트를 만들어 메모리와 가독성 측면에서 비효율적임

### 상세 피드백

이 풀이는 나눗셈을 사용하지 않고 prefix_product와 suffix_product 두 배열을 미리 계산한 뒤 곱해서 정답을 구하는 전형적인 접두사/접미사 곱 방식입니다. 로직 자체는 정확하며 0이 포함된 입력(Example 2)도 나눗셈을 쓰지 않으므로 문제없이 처리됩니다. 시간복잡도는 O(N)으로 문제에서 요구하는 조건을 만족하지만, 공간복잡도는 두 개의 길이 N+1 배열을 추가로 사용하므로 O(N) 추가 공간이 필요합니다. 문제의 Follow-up(O(1) 추가 공간)을 만족하지 못하는 점이 아쉽습니다. 또한 '-idx-1', '-idx-2' 같은 음수 인덱싱을 두 군데에서 사용해 로직을 따라가기가 다소 어렵고, prefix_product[idx]는 '왜 idx인가', suffix_product[-idx-2]는 '왜 그 위치인가'를 바로 이해하기 힘들어 가독성이 떨어집니다. append로 점진적으로 리스트를 채우는 대신 길이를 미리 알고 있으므로 answer 배열에 바로 쓰는 방식(2-pass, O(1) 추가 공간)으로 바꾸면 효율성과 가독성을 모두 개선할 수 있습니다.
