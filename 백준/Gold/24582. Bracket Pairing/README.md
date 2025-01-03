# [Gold I] Bracket Pairing - 24582 

[문제 링크](https://www.acmicpc.net/problem/24582) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

다이나믹 프로그래밍, 문자열

### 제출 일자

2025년 1월 3일 14:01:07

### 문제 설명

<p>There are four types of brackets: round <code>()</code>, square <code>[]</code>, curly <code>{}</code>, and angle <code><></code>. A bracket sequence is defined to be valid as follows:</p>

<ul>
	<li>An empty sequence is valid.</li>
	<li>If X is a valid bracket sequence, then pXq is a valid bracket sequence, where p is an open bracket, q is a close bracket, and p, q are of the same type.</li>
	<li>If X and Y are valid bracket sequences, then the concatenation of X and Y , Z = XY , is a valid bracket sequence.</li>
</ul>

<p>You have a bracket sequence in which some brackets are given, but the others are unknown and represented by question marks (‘<code>?</code>’). You shall fill in each unknown bracket using the four types of brackets described above and obtain a valid bracket sequence. How many different valid bracket sequences can you obtain?</p>

### 입력 

 <p>The input has a single line giving a non-empty bracket sequence. The length of the sequence is even and no larger than 20. All sequence characters are either one of the four types of open or close brackets, or a question mark denoting an unknown bracket. There is at least one question mark in the sequence.</p>

### 출력 

 <p>Output the number of different valid bracket sequences you can obtain.</p>

