# [Gold II] 특별한 문자열 - 12889 

[문제 링크](https://www.acmicpc.net/problem/12889) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

문자열

### 제출 일자

2025년 6월 14일 11:20:47

### 문제 설명

<p>문자열 S가 다음과 같은 두 가지 조건을 만족하면 특별한 문자열이라고 한다.</p>

<ul>
	<li>S의 모든 글자는 '0' 또는 '1' 이다.</li>
	<li>S를 두 부분 UV로 나누었을 때, U가 V보다 사전순으로 앞서야 한다. </li>
</ul>

<p>예를 들어, S = "00101"은 특별한 문자열 이다. 이유는 "0" < "0101", "00" < "101", "001" < "01", "0010" < "1" 이기 때문이다.</p>

<p>길이가 N인 특별한 문자열 S가 주어진다. 이때, 길이가 N인 모든 특별한 문자열을 사전 순으로 정렬했을 때, S의 다음에 오는 특별한 문자열을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 특별한 문자열 S가 주어진다. S의 길이 N은 1보다 크거나 같고, 50보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>S의 사전 순으로 다음에 오는 특별한 문자열을 출력한다. 만약, S가 사전순으로 마지막으로 오는 특별한 문자열인 경우에는 -1을 출력한다.</p>

