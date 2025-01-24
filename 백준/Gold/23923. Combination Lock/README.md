# [Gold II] Combination Lock - 23923 

[문제 링크](https://www.acmicpc.net/problem/23923) 

### 성능 요약

메모리: 225328 KB, 시간: 1444 ms

### 분류

수학, 누적 합, 슬라이딩 윈도우, 정렬

### 제출 일자

2025년 1월 24일 10:27:35

### 문제 설명

<p>A combination lock has <b>W</b> wheels, each of which has the integer values 1 through <b>N</b> on it, in ascending order.</p>

<p>At any moment, each wheel shows a specific value on it. <b>X<sub>i</sub></b> is the initial value shown on the i-th wheel.</p>

<p>You can use a single move to change a wheel from showing the value X to showing either X+1 or X-1, wrapping around between 1 and <b>N</b>. For example, if a wheel currently shows the value 1, in one move you can change its value to 2 or <b>N</b>.</p>

<p>Given all wheels' initial values, what is the minimum number of moves to get all wheels to show the same value?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow.</p>

<p>The first line of each test case contains the two integers <b>W</b> and <b>N</b>.</p>

<p>The second line contains <b>W</b> integers. The i-th integer is <b>X<sub>i</sub></b>.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the minimum number of moves to get all wheels to show the same value.</p>

