# [LeetCode Medium] Product of Array Except Self - product-of-array-except-self

[문제 링크](https://leetcode.com/problems/product-of-array-except-self/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Prefix Sum`

## 제출 일자

2026년 10월 6일 07:29:58

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
- 시간복잡도: 시간: O(N), 공간: O(N) (prefix_product, suffix_product 두 개의 보조 배열 사용)
- 더 나은 알고리즘: 이 문제의 정석 최적해는 O(1) 추가 공간(출력 배열 제외)으로 푸는 것입니다. 1) answer 배열을 prefix product로 채우고(answer[i] = nums[0..i-1]의 곱), 2) 오른쪽에서 왼쪽으로 순회하며 suffix를 스칼라 변수 하나로 누적해 answer[i]에 곱해주는 방식입니다. 이렇게 하면 별도의 prefix_product/suffix_product 리스트가 필요 없어 공간 복잡도가 O(N)에서 O(1)로 줄어듭니다 (출력 배열은 공간 복잡도 계산에서 제외).

### 잘한 점

- division을 사용하지 않고 O(N) 시간에 정확한 정답을 도출함
- 0이 포함된 경우를 포함해 모든 엣지케이스를 추가 분기 없이 자연스럽게 처리함
- 변수명(prefix, suffix, front, back)이 역할을 직관적으로 드러냄

### 개선할 점

- Follow-up으로 제시된 O(1) 추가 공간 최적화를 적용하지 않고 O(N) 크기의 보조 리스트 두 개를 사용함
- prefix_product/suffix_product 배열에 더미 값(1)을 앞에 추가하고 음수 인덱스로 접근하는 방식이 직관적이지 않아 유지보수성이 떨어짐
- 리스트 두 개를 순회 후 다시 한 번 순회하며 answer를 만드는 구조라, 단일 패스로 answer를 직접 채우는 더 간결한 구현이 가능함에도 불필요하게 복잡함

### 상세 피드백

코드는 division 없이 O(N) 시간으로 정확하게 동작하며, 0이 포함된 입력에서도 문제없이 처리됩니다. 로직을 직접 추적해보면 answer 값이 모두 올바르게 계산되는 것을 확인할 수 있습니다. 다만 이 문제의 핵심 포인트 중 하나인 '공간 최적화'(Follow-up: O(1) extra space)를 적용하지 않고 prefix_product, suffix_product라는 두 개의 추가 리스트(길이 n+1)를 만들어 O(N)의 추가 공간을 사용하고 있습니다. 이는 Medium 난이도 문제에서 자주 요구되는 최적화 포인트이므로, 면접이나 실전에서는 출력 배열 하나만 사용하고 suffix 곱을 스칼라 변수로 누적하는 방식으로 개선하는 것이 좋습니다. 또한 prefix_product와 suffix_product의 인덱싱 방식이 1칸씩 쉬프트되어 있고 음수 인덱스(-idx-1, -idx-2)를 혼용하고 있어 가독성이 다소 떨어지고, 코드를 읽는 사람이 off-by-one 오류를 의심하게 만듭니다. 변수명 자체(prefix, suffix, front, back)는 의미가 명확해서 좋았습니다.
