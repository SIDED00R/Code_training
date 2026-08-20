# [Codeforces 1700] Password - 126B

[문제 링크](https://codeforces.com/problemset/problem/126/B)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`binary search`, `dp`, `hashing`, `string suffix structures`, `strings`

## 제출 일자

2026년 8월 20일 17:05:35

## 문제 설명

Asterix, Obelix and their temporary buddies Suffix and Prefix has finally found the Harmony temple. However, its doors were firmly locked and even Obelix had no luck opening them. A little later they found a string $s$, carved on a rock below the temple's gates. Asterix supposed that that's the password that opens the temple and read the string aloud. However, nothing happened. Then Asterix supposed that a password is some substring $t$ of the string $s$. Prefix supposed that the substring $t$ is the beginning of the string $s$; Suffix supposed that the substring $t$ should be the end of the string $s$; and Obelix supposed that $t$ should be located somewhere inside the string $s$, that is, $t$ is neither its beginning, nor its end. Asterix chose the substring $t$ so as to please all his companions. Besides, from all acceptable variants Asterix chose the longest one (as Asterix loves long strings). When Asterix read the substring $t$ aloud, the temple doors opened.  You know the string $s$. Find the substring $t$ or determine that such substring does not exist and all that's been written above is just a nice legend.

## 입력

You are given the string $s$ whose length can vary from $1$ to $10^{6}$ (inclusive), consisting of small Latin letters.

## 출력

Print the string $t$. If a suitable $t$ string does not exist, then print " Just a legend " without the quotes.

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: O(N)

### 잘한 점

- KMP 알고리즘의 pi 배열을 정확하고 효율적으로 구현함
- 시간복잡도 O(N)으로 최적의 성능을 달성함
- 짧은 문자열 등의 엣지케이스를 적절히 처리함

### 개선할 점

- 파이썬의 input() 사용 시 매우 긴 입력(N=10^6)에서 I/O 성능 병목이 발생할 수 있음
- 변수명이 다소 짧아(s, n, pi, k, m, ans) 가독성을 조금 더 높일 여지가 있음

### 상세 피드백

이 풀이는 KMP 알고리즘의 실패 함수(pi 배열)를 활용하여 매우 효율적으로 문제를 해결했습니다. 문자열의 길이를 $N$이라 할 때, pi 배열을 구하는 과정은 O(N)의 시간복잡도를 가집니다. 이후 조건을 만족하는 가장 긴 접두사/접미사 겸 내부 문자열을 찾는 로직도 pi 배열을 거슬러 올라가는 방식으로 O(N)에 수행됩니다. 전체 시간복잡도 O(N)과 공간복잡도 O(N)은 이 문제를 해결하기 위한 최적의 성능입니다. 다만 파이썬에서 입출력 속도나 문자열 슬라이싱 등에 주의해야 하며, 엣지케이스 처리도 깔끔하게 잘 작성되었습니다.
