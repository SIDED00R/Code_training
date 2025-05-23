# [Gold IV] 학회원 - 3865 

[문제 링크](https://www.acmicpc.net/problem/3865) 

### 성능 요약

메모리: 32412 KB, 시간: 104 ms

### 분류

너비 우선 탐색, 자료 구조, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 해시를 사용한 집합과 맵, 파싱, 문자열, 집합과 맵

### 제출 일자

2025년 5월 6일 08:23:57

### 문제 설명

<p>상근이는 Sogang ACM-ICPC Team의 회장이다. 서강대학교 컴퓨터 학생들은 하나 또는 그 이상의 학회에 소속되어 있다. 상근이는 학생들이 어떤 학회에 소속되어 있는지 조사해보려고 한다.</p>

<p>상근이는 학회원의 정보를 다음과 같이 작성한다. 아래 예시는 sisobus와 weissblume은 icpc의 학회원이라는 뜻이다.</p>

<pre>icpc:weissblume,sisobus.</pre>

<p>콜론(:)의 앞에는 학회의 이름이 쓰여 있고, 뒤에는 학회원이 주어진다.</p>

<p>어떤 학회는 모든 회원이 다른 학회에 소속되어 있을 수도 잇다. 따라서, 학회원을 적는 곳에 학회의 이름을 적을 수도 있다.</p>

<pre>slug:sisobus,minhyeok,icpc,exupery.</pre>

<p>icpc에 소속되어 있는 사람은 slug에도 소속되어 있다는 뜻이다. 즉, slug의 학회원은 아래와 같다.</p>

<pre>slug:sisobus,minhyeok,weissblume,sisobus,exupery.</pre>

<p>이 경우에 sisobus는 두 번 등장한다. 중복되는 사람의 이름을 하나로 줄이게 되면, 아래와 같이 하나로 줄여서 작성할 수 있다.</p>

<pre>slug:sisobus,minhyeok,weissblume,exupery.</pre>

<p>학회의 회원 정보가 주어졌을 때, 각 학회의 학회원이 몇 명인지 구하는 프로그램을 작성하시오.</p>

<p>상근이가 작성하는 방법에는 학회의 이름이 중첩될 수도 있다. 아래 예시에서 one에 소속된 회원은 abckhw 한 명이다.</p>

<pre>one:another.
another:yetanother.
yetanother:abckhw.</pre>

### 입력 

 <p>입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 학회의 수 n이 주어진다. n은 100을 넘지 않는 양의 정수이다. 다음 n개 줄에는 각 학회의 학회원 정보가 문제에서 설명한 형식으로 주어진다. 콜론(:) 앞은 학회 이름이고, 그 뒤쪽은 회원의 이름이 콤마(,)로 구분되어져 있다. 각 정보의 마지막에는 마침표(.)가 하나 주어진다.</p>

<p>학회의 이름은 서로 다르다. 학회원 정보에서 주어지는 회원이 학회 이름이 아닌 경우에는 사람의 이름이다.</p>

<p>입력으로 주어지는 학회 정보에서 순환을 이루는 정보는 없다.</p>

<p>각 그룹 또는 사람의 이름은 비어있지 않은 문자열이며, 길이가 1과 15 사이이다. 또, 알파벳 소문자로만 이루어져 있다.</p>

<p>각 학회에 속한, 그룹이나 사람의 수는 1 이상 10 이하이다.</p>

<p>입력의 마지막 줄에는 0이 하나 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, 제일 처음으로 주어지는 학회에 포함되어 있는 회원의 수를 출력한다.</p>

