# [Gold II] Visits - 24977 

[문제 링크](https://www.acmicpc.net/problem/24977) 

### 성능 요약

메모리: 120248 KB, 시간: 208 ms

### 분류

깊이 우선 탐색, 그래프 이론, 그래프 탐색, 최소 스패닝 트리

### 제출 일자

2024년 8월 20일 06:14:13

### 문제 설명

<p>Each of Bessie’s $N$ ($2\le N\le 10^5$) bovine buddies (conveniently labeled $1\ldots N$) owns her own farm. For each $1\le i\le N$, buddy $i$ wants to visit buddy $a_i$ ($a_i\neq i$).</p>

<p>Given a permutation $(p_1,p_2,\ldots, p_N)$ of $1\ldots N$, the visits occur as follows.</p>

<p>For each $i$ from $1$ up to $N$:</p>

<ul>
	<li>If buddy $a_{p_i}$ has already departed her farm, then buddy $p_i$ remains at her own farm.</li>
	<li>Otherwise, buddy $p_i$ departs her farm to visit buddy $a_{p_i}$’s farm. This visit results in a joyful "moo" being uttered $v_{p_i}$ times ($0\le v_{p_i}\le 10^9$).</li>
</ul>

<p>Compute the maximum possible number of moos after all visits, over all possible permutations $p$.</p>

### 입력 

 <p>The first line contains $N$.</p>

<p>For each $1\le i\le N$, the $i+1$-st line contains two space-separated integers $a_i$ and $v_i$.</p>

### 출력 

 <p>A single integer denoting the answer.</p>

<p><strong>Note that the large size of integers involved in this problem may require the use of 64-bit integer data types (e.g., a "long long" in C/C++).</strong></p>

