# [Codeforces 1400] Chipmunk Theo and Equality - 2231C

[문제 링크](https://codeforces.com/problemset/problem/2231/C)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`implementation`, `sortings`

## 제출 일자

2026년 6월 10일 07:45:10

## 문제 설명

While exploring the depths of the Internet, Theodore the chipmunk found a very interesting sequence of positive integers and decided to play with it.

In one operation, he chooses an element of the sequence and performs the following action:

If the chosen element is even, he divides it by 2.
If the chosen element is odd, he increases it by 1.
Theo really loves equality, so he wants to make all numbers in the sequence equal (otherwise, some numbers might feel offended). Since he needs to plan his lunch time, help him determine the minimum number of operations required to make all numbers equal.

## 입력

Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤10^4). 
The description of the test cases follows.
The first line of each test case contains a single integer n (1≤n≤10^5) — the length of the sequence.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤109) — the elements of the sequence.

It is guaranteed that the sum of n over all test cases does not exceed 105.

## 출력

For each test case, output a single integer — the minimum number of operations Theo needs to make all numbers in the sequence equal.
