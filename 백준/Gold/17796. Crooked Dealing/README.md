# [Gold II] Crooked Dealing - 17796 

[문제 링크](https://www.acmicpc.net/problem/17796) 

### 성능 요약

메모리: 36668 KB, 시간: 84 ms

### 분류

자료 구조, 그리디 알고리즘, 우선순위 큐

### 제출 일자

2025년 3월 3일 08:33:05

### 문제 설명

<p>This week you started a flashy new job in Leeds as a poker dealer. Your task will be to hand out the cards for games. The base pay is not particularly good, but you found out that you can earn a lot from tips if you deal the cards well.</p>

<p>The most generous customers prefer that their opponents at the table don’t receive any pairs of cards with the same number; so to keep them happy you will make sure this never happens.</p>

<p>You already know the numbers on every card in the pile , and the number of cards any player must have in their hand. Find how many hands you can make at once without introducing a pair.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/f88d9e92-772c-4b42-b9c0-fa225337ea07/-/preview/" style="width: 623px; height: 290px;"></p>

<p style="text-align: center;">Figure C.1: Illustration of a solution to Sample Input 2.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>A line with two integers n and h (1 ≤ h ≤ n ≤ 10<sup>6</sup>), the number of cards in the pile, and the number of cards in a hand.</li>
	<li>A line with n integers v<sub>1</sub>, . . . , v<sub>n</sub> (1 ≤ v<sub>i</sub> ≤ 10<sup>6</sup> for all i), the numbers on the cards in no particular order.</li>
</ul>

### 출력 

 <p>If it is not possible to make any hands at all without introducing a pair, output impossible.</p>

<p>Otherwise, output k lines (where k is the maximum possible number of players) each containing h numbers from the input. You may not use any number any more times than it appears in v.</p>

<p>If there are multiple answers with a maximum value of k, you may output any one of them.</p>

