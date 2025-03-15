# [Gold III] Cutting Banknotes - 21386 

[문제 링크](https://www.acmicpc.net/problem/21386) 

### 성능 요약

메모리: 32412 KB, 시간: 480 ms

### 분류

수학, 정수론

### 제출 일자

2025년 3월 16일 08:55:46

### 문제 설명

<p>Philip is often faced with a big problem: after going out for dinner or having a few beers, he owes money to his friends or the other way around. These are often small amounts, but because Philip hates coins, his wallet contains only banknotes. Therefore he usually can’t pay the amount exactly. Since he hates coins, he also doesn’t allow his friends to return them as change. He does allow for banknotes as change though.</p>

<p>To accomodate for this problem, he and his friends came up with the following idea: let’s pay with pieces of banknotes. To make the cutting easy, they only cut banknotes in two equally-sized pieces, cut those pieces in two pieces, and so on. This yields a much larger range of amounts that can be paid. Philip wonders which ones exactly.</p>

### 입력 

 <p>On the first line an integer t (1 ≤ t ≤ 100): the number of test cases. Then for each test case:</p>

<ul>
	<li>One line with a number x (0.01 ≤ x ≤ 10 000.00): the amount Philip has to pay. This is formatted with two decimal digits and a period as decimal separator.</li>
	<li>One line with a positive integer n (1 ≤ n ≤ 1 000): the number of different banknotes.</li>
	<li>n lines, each with an integer b<sub>i</sub> (1 ≤ b<sub>i</sub> ≤ 10 000): the values of the banknotes.</li>
</ul>

### 출력 

 <p>For each test case:</p>

<ul>
	<li>One line with “<code>yes</code>” if the amount can be paid exactly and “<code>no</code>” otherwise.</li>
</ul>

