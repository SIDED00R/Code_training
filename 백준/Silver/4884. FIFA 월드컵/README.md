# [Silver V] FIFA 월드컵 - 4884 

[문제 링크](https://www.acmicpc.net/problem/4884) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

수학

### 제출 일자

2025년 6월 21일 15:31:06

### 문제 설명

<p>FIFA는 월드컵의 대회 형식을 약간 수정하려고 한다. 현재, 월드컵은 32개팀이 참가하며, 2개의 라운드로 이루어져 있다. 첫 번째 라운드는 조별 리그이고, 32개팀은 8개의 조에 배정된다. 각 팀은 조에 속하는 다른 팀과 한 경기씩 치뤄 총 세 경기를 치룬다. 조별 리그가 완료된 후에, 각 조의 상위 두 팀은 다음 라운드 토너먼트로 진출하게 된다.  토너먼트의 첫 번째 라운드는 16개팀이 참가하며, 총 8경기가 열린다. 각 경기의 승자는 다음 라운드에 진출하게 된다. 토너먼트의 두 번째 라운드에서는 총 4경기가 열리며, 각 경기의 승자는 준결승전에 진출한다. 마지막으로 준결승전의 승자 두 팀은 결승전에 진출하게 되고, 결승전의 승자는 월드컵을 우승하게 된다.</p>

<p>토너먼트 전을 공정하게 진행하려면 토너먼트에 참가하는 팀의 수는 항상 2의 제곱꼴이 되어야 한다.</p>

<p>FIFA는 조별 리그에 참가하는 팀의 수를 추가하고, 조의 개수도 추가하려고 한다. 이 결과로 토너먼트에 참가하는 팀의 수가 변경될 수도 있다. 또한, FIFA는 일부 팀(이전 대회 우승, 개최국, 등등...)은 조별 리그를 거치지 않고 바로 토너먼트에 진출하게 규정을 바꾸려고 한다. 월드컵을 어떻게 바꿀지 주어졌을 때, 그렇게 월드컵이 바뀐다면 총 몇 경기가 열리게 되는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력은 여러 개의 테스트 케이스로 이루어져 있고, 각 테스트 케이스는 자연수 4개 G T A D가 주어진다.</p>

<p>G > 0는 그룹의 수, T는 각 그룹을 구성하는 팀의 수, A는 각 조에서 토너먼트로 진출하는 팀의 수, D는 조별 리그를 거치지 않고 바로 토너먼트로 진출하는 팀의 수이다. 항상 0 < A ≤ T이고, 네 숫자는 2<sup>16</sup>을 넘지 않는다.</p>

<p>만약, 토너먼트에 참가하는 팀의 수가 2의 제곱꼴이 아닐 때는, 가까운 2의 제곱으로 진출하는 팀의 수를 추가시켜야 한다.</p>

<p>입력의 마지막 줄에는 -1이 네 개 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, 다음을 출력한다.</p>

<pre>G*A/T+D=X+Y</pre>

<p>G, A, T, D는 입력으로 주어지는 수, X는 총 열리는 경기의 수, Y는 추가해야하는 팀의 수이다.</p>

