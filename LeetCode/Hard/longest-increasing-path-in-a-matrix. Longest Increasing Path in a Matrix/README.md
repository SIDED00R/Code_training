# [LeetCode Hard] Longest Increasing Path in a Matrix - longest-increasing-path-in-a-matrix

[문제 링크](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Dynamic Programming`, `Depth-First Search`, `Breadth-First Search`, `Graph Theory`, `Topological Sort`, `Memoization`, `Matrix`, `Directed Acyclic Graph`

## 제출 일자

2026년 10월 24일 08:04:18

## 문제 설명

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

 

Constraints:

m == matrix.length

n == matrix[i].length

1 <= m, n <= 200

0 <= matrix[i][j] <= 2^31 - 1

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: 시간복잡도 O(m*n), 공간복잡도 O(m*n) (dp 테이블) + 최악의 경우 O(m*n) 재귀 스택
- 더 나은 알고리즘: DFS+메모이제이션은 이미 이 문제의 최적 해법 중 하나입니다. 다만 재귀 깊이 문제를 피하려면 Kahn's algorithm 기반 위상 정렬(BFS)로 구현하는 것이 더 안전합니다. 각 셀의 in-degree(자신보다 큰 인접 셀 개수)를 계산한 뒤, in-degree가 0인 셀부터 BFS로 레벨을 늘려가며 처리하면 동일한 O(m*n) 시간에 재귀 스택 오버플로우 위험 없이 풀 수 있습니다.

### 잘한 점

- DFS + 메모이제이션을 통해 O(m*n) 시간복잡도로 문제를 최적에 가깝게 해결함
- 방향 배열(di, dj)과 dp 테이블을 활용해 코드가 간결하고 로직이 명확하게 드러남
- 각 셀을 한 번만 계산하도록 dp[i][j] != 0 체크로 중복 연산을 효과적으로 차단함

### 개선할 점

- 재귀 기반 DFS이므로 입력 크기가 커질 경우(최대 40000칸) RecursionError 위험이 있으며 sys.setrecursionlimit 설정이 누락됨
- 반복문 기반 DFS나 위상 정렬(BFS) 방식으로 구현했다면 재귀 깊이 문제 없이 더 안정적인 해법이 되었을 것임

### 상세 피드백

이 풀이는 DFS와 메모이제이션(dp 배열)을 결합하여 각 셀을 단 한 번만 완전히 계산하도록 만든, 이 문제에 대한 정석적이고 최적에 가까운 접근입니다. 시간복잡도는 O(m*n)으로, 각 셀에서 4방향 탐색을 O(1)회 수행하고 메모이제이션으로 중복 계산을 제거했습니다. 코드 구조도 깔끔하고 di/dj 방향 배열, dp 테이블 초기화, 전체 순회 후 최댓값 갱신 로직이 명확하게 작성되어 가독성이 좋습니다.

다만 주의할 점은 재귀 기반 DFS이기 때문에, 행렬이 200x200(최대 40000칸)이고 모든 값이 엄격히 증가하는 지그재그 형태로 배열된 최악의 경우 재귀 깊이가 수만 단계까지 깊어질 수 있어 Python의 기본 재귀 제한(1000)을 초과해 RecursionError가 발생할 위험이 있습니다. sys.setrecursionlimit()을 호출해 안전마진을 두거나, 재귀 대신 반복문 기반 DFS(스택 명시적 관리) 혹은 위상 정렬(BFS) 방식으로 구현하면 이런 위험을 원천적으로 제거할 수 있습니다. 또한 matrix가 비어있는 극단적 입력에 대한 방어 코드가 없지만, 문제 제약조건상 m, n >= 1이 보장되므로 실용적으로는 문제가 되지 않습니다.
