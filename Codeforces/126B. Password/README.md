# [Codeforces 1700] Password - 126B

[문제 링크](https://codeforces.com/problemset/problem/126/B)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`binary search`, `dp`, `hashing`, `string suffix structures`, `strings`

## 제출 일자

2026년 8월 19일 00:59:32

## 문제 설명

Asterix, Obelix and their temporary buddies Suffix and Prefix has finally found the Harmony temple. However, its doors were firmly locked and even Obelix had no luck opening them. A little later they found a string $s$, carved on a rock below the temple's gates. Asterix supposed that that's the password that opens the temple and read the string aloud. However, nothing happened. Then Asterix supposed that a password is some substring $t$ of the string $s$. Prefix supposed that the substring $t$ is the beginning of the string $s$; Suffix supposed that the substring $t$ should be the end of the string $s$; and Obelix supposed that $t$ should be located somewhere inside the string $s$, that is, $t$ is neither its beginning, nor its end. Asterix chose the substring $t$ so as to please all his companions. Besides, from all acceptable variants Asterix chose the longest one (as Asterix loves long strings). When Asterix read the substring $t$ aloud, the temple doors opened.  You know the string $s$. Find the substring $t$ or determine that such substring does not exist and all that's been written above is just a nice legend.

## 입력

You are given the string $s$ whose length can vary from $1$ to $10^{6}$ (inclusive), consisting of small Latin letters.

## 출력

Print the string $t$. If a suitable $t$ string does not exist, then print " Just a legend " without the quotes.

## 코드 리뷰

- 효율성: 비효율적
- 시간복잡도: O(N²)
- 더 나은 알고리즘: KMP 알고리즘의 pi 배열(prefix function)을 활용하면 O(N) 시간에 문제를 해결할 수 있습니다.

### 잘한 점

- 문제의 조건을 정확히 이해하고 올바른 로직(접두사이자 접미사이면서 내부에 존재하는 가장 긴 문자열 찾기)을 구현함
- 입력 처리 시 `sys.stdin.readline`과 `rstrip()`을 사용하여 빠른 입력을 유도함

### 개선할 점

- 슬라이싱과 `in` 연산자를 반복문 내에서 사용하여 시간 복잡도가 $O(N^2)$으로 매우 비효율적임
- 최대 길이 $10^6$의 입력에 대해 시간 초과 및 메모리 초과 위험이 존재함
- 가능한 모든 후보를 리스트에 담고 역순으로 탐색하는 방식은 불필요한 메모리 낭비를 초래함

### 상세 피드백

제출하신 코드는 모든 접두사이자 접미사인 문자열을 구한 뒤, 그것이 문자열의 내부(양 끝을 제외한 부분)에 존재하는지 `in` 연산자를 통해 확인하고 있습니다. 이 방식은 파이썬의 슬라이싱과 `in` 연산자의 특성 때문에 최악의 경우 $O(N^2)$의 시간 복잡도를 가집니다. 문제의 입력 크기가 $10^6$이므로, 이 풀이는 시간 초과(Time Limit Exceeded) 또는 메모리 초과를 유발하게 됩니다. KMP 알고리즘의 $\pi$ 배열을 활용하면 접두사와 접미사이면서 동시에 내부에도 존재하는 가장 긴 문자열을 단 $O(N)$ 시간에 찾을 수 있습니다. 문자열 매칭 및 패턴 문제에서는 슬라이싱을 이용한 완전탐색을 지양하고 KMP나 Z-algorithm 등의 선형 시간 알고리즘을 떠올리는 연습이 필요합니다.
