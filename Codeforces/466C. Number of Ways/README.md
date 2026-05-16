# [Codeforces 1700] Number of Ways - 466C

[문제 링크](https://codeforces.com/problemset/problem/466/C)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`binary search`, `brute force`, `data structures`, `dp`, `two pointers`

## 제출 일자

2026년 5월 17일 08:47:48

## 문제 설명

배열 $a[1], a[2], \ldots, a[n]$가 $n$개의 정수로 구성되어 있습니다. 배열의 모든 요소를 세 개의 연속적인 부분으로 나누는 방법의 수를 세세요. 각 부분의 합이 같아야 합니다. 보다 공식적으로, 다음과 같은 인덱스 쌍 $i, j$ ( $2 \leq i \leq j \leq n - 1$ )의 수를 찾아야 합니다.

## 입력

첫 번째 줄에는 정수 $n$ $(1 \le n \le 5 \cdot 10^5)$이 포함되어 있으며, 이는 배열에 몇 개의 숫자가 있는지를 나타냅니다. 두 번째 줄에는 $n$개의 정수 $a[1], a[2], \ldots, a[n]$ $(|a[i]| \le 10^9)$가 포함되어 있습니다. 이는 배열 $a$의 요소들입니다.

## 출력

배열을 같은 합을 가진 세 부분으로 나누는 방법의 수를 나타내는 정수를 하나 출력하시오.
