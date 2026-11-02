# [LeetCode Medium] Range Sum Query 2D - Immutable - range-sum-query-2d-immutable

[문제 링크](https://leetcode.com/problems/range-sum-query-2d-immutable/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Array`, `Design`, `Matrix`, `Prefix Sum`

## 제출 일자

2026년 11월 3일 08:12:13

## 문제 설명

2D 행렬 matrix가 주어졌을 때, 다음 유형의 여러 쿼리를 처리하세요:

왼쪽 위 모서리 (row1, col1)와 오른쪽 아래 모서리 (row2, col2)로 정의된 사각형 영역 내에 있는 matrix의 원소들의 합을 계산하세요.

NumMatrix 클래스를 구현하세요:

NumMatrix(int[][] matrix) 정수 행렬 matrix로 객체를 초기화합니다.

int sumRegion(int row1, int col1, int row2, int col2) 왼쪽 위 모서리 (row1, col1)와 오른쪽 아래 모서리 (row2, col2)로 정의된 사각형 영역 내에 있는 matrix의 원소들의 합을 반환합니다.

sumRegion이 O(1) 시간 복잡도로 동작하는 알고리즘을 설계해야 합니다.

 

예제 1:

입력
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
출력
[null, 8, 11, 12]

설명
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // 8을 반환 (즉, 빨간색 사각형의 합)
numMatrix.sumRegion(1, 1, 2, 2); // 11을 반환 (즉, 초록색 사각형의 합)
numMatrix.sumRegion(1, 2, 2, 4); // 12를 반환 (즉, 파란색 사각형의 합)

 

제약 조건:

m == matrix.length

n == matrix[i].length

1 <= m, n <= 200

-10^4 <= matrix[i][j] <= 10^4

0 <= row1 <= row2 < m

0 <= col1 <= col2 < n

최대 10^4번의 sumRegion 호출이 이루어집니다.

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: 생성자 O(M*N), sumRegion 호출당 O(1), 전체 O(M*N + Q) (Q는 쿼리 수)
- 더 나은 알고리즘: 현재 풀이의 시간복잡도 자체는 이미 최적(O(1) 쿼리)이라 알고리즘을 바꿀 필요는 없습니다. 다만 구현 방식을 (M+1) x (N+1) 크기의 패딩된 2D prefix sum 배열로 바꾸면, row1==0 또는 col1==0인 경계 케이스를 if-elif-elif로 분기 처리할 필요가 없어집니다. P[i][j] = matrix[0..i-1][0..j-1]의 합으로 정의하고 P[0][*] = P[*][0] = 0으로 두면, sumRegion은 항상 'P[row2+1][col2+1] - P[row1][col2+1] - P[row2+1][col1] + P[row1][col1]' 한 줄로 통일되게 계산할 수 있어 코드가 훨씬 간결해지고 버그 가능성도 줄어듭니다.

### 잘한 점

- 시간복잡도 측면에서 생성자 O(M*N), 쿼리당 O(1)로 문제의 요구사항을 정확히 만족시키는 최적의 접근을 선택함
- 포함-배제 원리를 활용한 2D prefix sum 공식을 정확하게 구현하여 모든 테스트 케이스에서 올바른 결과를 반환함

### 개선할 점

- row1/col1이 0인 경우를 처리하기 위해 4가지 분기(if/elif/elif/else)를 사용하는데, prefix sum 배열을 (M+1)x(N+1)로 패딩하면 분기 없이 하나의 수식으로 통일할 수 있어 코드가 더 간결하고 안전해짐
- 생성자에서 행 방향 합을 먼저 구한 뒤 열 방향으로 다시 누적하는 2단계 로직이라 가독성이 다소 떨어지며, 2중 for문으로 한 번에 2D prefix sum을 구축하는 표준 패턴을 사용하면 더 직관적임

### 상세 피드백

이 풀이는 2D prefix sum(누적합)을 정확히 구현했고, 생성자에서 O(M*N)에 전처리를 끝내고 sumRegion을 O(1)에 처리하므로 'sumRegion은 O(1)이어야 한다'는 문제 요구사항을 충분히 만족합니다. 포함-배제(inclusion-exclusion) 공식도 정확하게 적용되어 정답을 반환합니다.

다만 구현 세부사항에서 개선할 점이 있습니다. row1==0, col1==0 조합에 따라 if/elif/elif로 4가지 경우를 나누어 처리하고 있는데, 이는 2D prefix sum 배열을 (M+1) x (N+1) 크기로 패딩(1번째 행/열을 0으로 채움)하면 전부 하나의 공식으로 통합할 수 있습니다. 현재처럼 경계 조건마다 분기를 두면 코드가 길어지고, 새로운 경계 버그가 생길 여지도 커집니다. 또한 생성자에서 행 방향 prefix sum을 만든 뒤 다시 열 방향으로 누적하는 2단계 순회 방식은 동작은 올바르지만, 처음부터 2중 for문 하나로 2D prefix sum을 만드는 표준 방식에 비해 약간 가독성이 떨어집니다. 전반적으로 복잡도는 최적이지만 코드 스타일을 다듬으면 더 깔끔하고 유지보수하기 쉬운 코드가 될 것입니다.
