# [Codeforces 1600] Erase and Extend (Easy Version) - 1537E1

[문제 링크](https://codeforces.com/problemset/problem/1537/E1)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`binary search`, `brute force`, `dp`, `greedy`, `hashing`, `implementation`, `string suffix structures`, `strings`, `two pointers`

## 제출 일자

2026년 8월 28일 10:29:26

## 문제 설명

This is the easy version of the problem. The only difference is the constraints on $n$ and $k$. You can make hacks only if all versions of the problem are solved. You have a string $s$, and you can do two types of operations on it:     Delete the last character of the string.   Duplicate the string: $s:=s+s$, where $+$ denotes concatenation.  You can use each operation any number of times (possibly none). Your task is to find the lexicographically smallest string of length exactly $k$ that can be obtained by doing these operations on string $s$. A string $a$ is lexicographically smaller than a string $b$ if and only if one of the following holds:    $a$ is a prefix of $b$, but $a\ne b$;   In the first position where $a$ and $b$ differ, the string $a$ has a letter that appears earlier in the alphabet than the corresponding letter in $b$.

## 입력

The first line contains two integers $n$, $k$ ($1 \leq n, k \leq 5000$) — the length of the original string $s$ and the length of the desired string. The second line contains the string $s$, consisting of $n$ lowercase English letters.

## 출력

Print the lexicographically smallest string of length $k$ that can be obtained by doing the operations on string $s$.

## 코드 리뷰

⏳ AI 리뷰 대기 중 — 앱에서 리뷰를 실행하면 이 문서가 갱신됩니다.
