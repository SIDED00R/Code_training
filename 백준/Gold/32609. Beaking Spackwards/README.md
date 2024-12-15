# [Gold III] Beaking Spackwards - 32609 

[문제 링크](https://www.acmicpc.net/problem/32609) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

해 구성하기, 그리디 알고리즘, 수학, 정수론

### 제출 일자

2024년 12월 15일 09:55:30

### 문제 설명

<p>The 42nd meeting of the Fortnightly Palindrome Convention is coming up, and for this special occasion, they want to spend a session admiring a special kind of palindrome-esque words. These words are not necessarily a palindrome by themselves, but they should contain an exact, predetermined number of palindrome substrings. As preparation for the session, your task is to generate these palindrome-esque words.</p>

<p>As an example, consider the second sample input. The output <code>abacaba</code> contains exactly $12$ palindrome substrings: the seven individual letters, two times <code>aba</code> (at the start and at the end), <code>aca</code>, <code>bacab</code>, and <code>abacaba</code>.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with an integer $s$ ($1\leq s\leq 10^9$), the number of required palindrome substrings.</li>
</ul>

### 출력 

 <p>Output a string that contains exactly $s$ palindrome substrings. This string should have length between $1$ and $10^5$ characters (inclusive) and only consists of English lowercase letters (<code>a-z</code>).</p>

<p>If there are multiple valid solutions, you may output any one of them.</p>

