# [LeetCode Easy] Best Time to Buy and Sell Stock - best-time-to-buy-and-sell-stock

[문제 링크](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Dynamic Programming`

## 제출 일자

2026년 9월 25일 19:14:41

## 문제 설명

You are given an array prices where prices[i] is the price of a given stock on the i^th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

 

Constraints:

1 <= prices.length <= 10^5

0 <= prices[i] <= 10^4

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: O(N)

### 잘한 점

- O(N)의 시간복잡도로 배열을 한 번만 순회하여 효율적으로 문제를 해결했습니다.
- 변수 now_min을 사용하여 추가적인 공간 복잡도 없이 O(1) 공간으로 구현했습니다.

### 개선할 점

- 초기 최솟값으로 1e10이라는 임의의 큰 상수를 사용하여, 가격 범위가 커질 경우 잠재적 오류의 여지가 있습니다.
- range(len(prices))를 사용하여 인덱스로 접근하는 방식은 파이썬의 이터레이터 활용 관점에서 가독성이 다소 떨어집니다.

### 상세 피드백

제출된 코드는 주식 가격 배열을 단 한 번만 순회하면서(O(N) 시간복잡도) 지금까지의 최저가와 현재가에서의 최대 이익을 동시에 갱신하는 매우 효율적이고 우수한 접근법을 사용했습니다. 별도의 추가 메모리를 사용하지 않아 O(1) 공간복잡도를 달성한 점도 훌륭합니다. 다만, 초기 최솟값으로 임의의 큰 수인 1e10을 사용하는 대신 float('inf')를 사용하거나 첫 번째 원소를 초기값으로 설정하는 것이 더 파이썬스럽고 안전합니다. 또한 range(len(prices)) 대신 for price in prices:와 같이 리스트의 원소를 직접 순회하면 가독성이 더욱 향상될 것입니다. 전체적으로 LeetCode Easy 난이도에 알맞은 최적의 해법을 보여주었습니다.
