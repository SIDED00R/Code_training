# [Gold IV] Party Invitations - 5856 

[문제 링크](https://www.acmicpc.net/problem/5856) 

### 성능 요약

메모리: 122552 KB, 시간: 176 ms

### 분류

자료 구조, 구현, 큐, 트리를 사용한 집합과 맵

### 제출 일자

2025년 1월 5일 08:28:11

### 문제 설명

<p>Farmer John is throwing a party and wants to invite some of his cows to show them how much he cares about his herd.  However, he also wants to invite the smallest possible number of cows, remembering all too well the disaster that resulted the last time he invited too many cows to a party.</p><p>Among FJ's cows, there are certain groups of friends that are hard to separate.  For any such group (say, of size k), if FJ invites at least k-1 of the cows in the group to the party, then he must invite the final cow as well, thereby including the entire group.  Groups can be of any size and may even overlap with each-other, although no two groups contain exactly the same set of members.  The sum of all group sizes is at most 250,000.</p><p>Given the groups among FJ's cows, please determine the minimum number of cows FJ can invite to his party, if he decides that he must definitely start by inviting cow #1 (his cows are conveniently numbered 1..N, with N at most 1,000,000).</p>

### 입력 

 <ul><li>Line 1: Two space-separated integers: N (the number of cows), and G (the number of groups).</li><li>Lines 2..1+G: Each line describes a group of cows.  It starts with an integer giving the size S of the group, followed by the S cows in the group (each an integer in the range 1..N).</li></ul>

### 출력 

 <ul><li>Line 1: The minimum number of cows FJ can invite to his party.</li></ul>

