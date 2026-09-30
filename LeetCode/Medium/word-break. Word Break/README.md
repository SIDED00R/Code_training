# [LeetCode Medium] Word Break - word-break

[문제 링크](https://leetcode.com/problems/word-break/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Hash Table`, `String`, `Dynamic Programming`, `Trie`, `Memoization`, `Brute-Force Search`

## 제출 일자

2026년 9월 30일 10:59:42

## 문제 설명

문자열 s와 문자열 사전 wordDict가 주어질 때, s를 하나 이상의 사전 단어로 이루어진 공백으로 구분된 시퀀스로 나눌 수 있으면 true를 반환하세요.

참고로 사전에 있는 같은 단어를 분할 과정에서 여러 번 재사용할 수 있습니다.

 

예제 1:

입력: s = "leetcode", wordDict = ["leet","code"]
출력: true
설명: "leetcode"는 "leet code"로 분할할 수 있으므로 true를 반환합니다.

예제 2:

입력: s = "applepenapple", wordDict = ["apple","pen"]
출력: true
설명: "applepenapple"은 "apple pen apple"로 분할할 수 있으므로 true를 반환합니다.
사전 단어를 재사용할 수 있다는 점에 유의하세요.

예제 3:

입력: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
출력: false

 

제약 조건:

1 <= s.length <= 300

1 <= wordDict.length <= 1000

1 <= wordDict[i].length <= 20

s와 wordDict[i]는 소문자 영어 알파벳으로만 이루어져 있습니다.

wordDict의 모든 문자열은 서로 다릅니다.

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: O(N * M * K) (N은 문자열 s의 길이, M은 wordDict의 단어 개수, K는 단어의 최대 길이)
- 더 나은 알고리즘: 해시셋(HashSet)을 활용하여 단어 존재 여부 O(1) 조회 및 딕셔너리 단어 길이별 순회로 최적화 가능

### 잘한 점

- 중복 연산을 방지하는 전형적이고 안정적인 DP 테이블(dp 배열) 활용
- 단어를 찾은 즉시 break 문을 통해 불필요한 내부 반복을 줄여 성능 최적화
- 변수명이 직관적이고 코드의 흐름이 한눈에 파악됨

### 개선할 점

- wordDict의 단어 개수가 많을 때 매번 모든 단어를 순회하여 약간의 비효율성 존재
- 파이썬의 불리언(boolean) 타입 대신 숫자(1, 0)를 사용하여 가독성이 다소 떨어짐

### 상세 피드백

제출하신 코드는 동적 계획법(Dynamic Programming)을 활용하여 문제를 매우 올바르고 효율적으로 해결하였습니다. dp 배열의 크기를 s의 길이 + 1로 설정하고, 0번째 인덱스를 True(1)로 초기화한 점은 전형적이면서도 정확한 접근법입니다. 각 위치 i에서 wordDict의 모든 단어와 비교하여 이전 상태가 가능하고 현재 슬라이싱한 문자열이 단어와 일치하는지 확인하는 로직은 O(N * M * K)의 시간복잡도로 LeetCode Medium 난이도를 통과하기에 충분히 훌륭합니다. 다만, wordDict를 매번 탐색하는 것보다 wordDict를 집합(set)으로 변환하고 문자열 s의 가능한 단어 길이를 이용해 순회하면 더 최적화할 수 있습니다. 전반적으로 코드의 가독성이 좋고 엣지 케이스 처리가 잘 되어 있습니다.
