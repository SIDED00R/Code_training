# [Gold V] Subway - 21959 

[문제 링크](https://www.acmicpc.net/problem/21959) 

### 성능 요약

메모리: 131296 KB, 시간: 188 ms

### 분류

조합론, 해 구성하기, 수학, 트리

### 제출 일자

2025년 6월 7일 10:33:03

### 문제 설명

<p>Given an integer number K, generate a tree with minimum number of nodes such that there are exactly K pairs of nodes (X, Y), where X is an ancestor of Y.</p>

### 입력 

 <p>The input (from the console) will contain a single integer number, K – the number of pairs with the specified property.</p>

### 출력 

 <p>The output (to the console) will contain N+1 lines, representing the generated tree, the nodes being indexed from 0.</p>

<p>The first line will contain the number N – the number of nodes in the tree.</p>

<p>The following N lines will contain each 2 numbers X and T, separated by a space, with the following meaning: node T is the direct ancestor of node X. If node X doesn’t have a direct ancestor, T will have value -1.</p>

