# [Gold III] 더위 피하기 - 15938 

[문제 링크](https://www.acmicpc.net/problem/15938) 

### 성능 요약

메모리: 143448 KB, 시간: 968 ms

### 분류

다이나믹 프로그래밍, 그래프 이론

### 제출 일자

2025년 7월 12일 08:15:32

### 문제 설명

<p>“오늘 서울 낮 최고기온은 38도를 기록하겠습니다. 현재 전국에 폭염경보가 내려져 있고...”</p>

<p>성원이는 이 더운 날씨에 집에서 에어컨을 쐬며 누워있지 않고 밖에 나온 것을 후회하고 있다. 길을 잃었기 때문이다. 처음 보는 건물과 간판들로 둘러싸인 성원이는 생명의 위협을 느끼기 시작했다. 이대로 집에 도착하지 못하고 T초가 지나면 성원이는 더위를 먹어 쓰러지고 말 것이다. 역시 이불 밖은 위험해.</p>

<p>생명의 위협을 느끼고 있는 성원이는 집에 가기 위해 일단 아무 곳으로나 가고 있다. 구체적으로 성원이는 1초에 1m씩 동서남북 방향으로 걸어갈 수 있다. 이렇게 아무 방향으로 계속 가다 보면 언젠가는 집에 도착할 수도 있지 않을까?</p>

<p>길을 잃은 성원이를 집에서 지켜보고 있던 승현이는 성원이가 진짜로 더위를 먹어서 쓰러지면 구조하러 가기로 했다. 승현이는 지도와 성원이의 현재 위치를 알고 있고, 어느 곳에 건물이 있어 가지 못하는지 알고 있다. 승현이는 성원이가 무사히 집에 도착할 수 있는 경우의 수를 알고 싶어한다. 하지만 승현이는 무더운 날씨에 성원이를 구조하러 나가기 위한 만반의 준비를 해야 하기 때문에 여러분에게 계산을 부탁했다.</p>

<p>성원이의 현재 위치와 성원이가 더위를 버틸 수 있는 시간, 집의 위치, 그리고 장애물의 개수와 위치가 주어질 때, 성원이가 T초 이내에 집에 올 수 있는 경우의 수를 계산해 주자. 도착 시간이 같아도 중간에 거친 경로가 다르면 다른 경우로 센다. 성원이는 매초 방향을 바꿀 수 있으며(이 길이 아니다 싶으면 왔던 방향으로 돌아갈 수도 있다), 장애물이 있는 지점에는 가지 못한다. 그리고 성원이는 한 번 집에 도착하면 이동을 멈추고 다시는 밖에 나가지 않는다.</p>

### 입력 

 <p>첫 번째 줄에 성원이의 현재 위치 좌표 (X<sub>s</sub>, Y<sub>s</sub>)를 나타내는 정수 2개가 주어진다. 두 번째 줄에 성원이가 더위를 버틸 수 있는 시간 T(1 ≤ T ≤ 200)가 주어진다. 세 번째 줄에 집의 위치 좌표 (X<sub>h</sub>, Y<sub>h</sub>)를 나타내는 정수 2개가 주어진다.</p>

<p>네 번째 줄에 장애물의 개수 N(0 ≤ N ≤ 100,000)이 주어진다. 그 이후 N개의 줄에 걸쳐 각 줄에 장애물의 위치 좌표 (X<sub>i</sub>, Y<sub>i</sub>)를 나타내는 정수 2개가 주어진다.</p>

<p>주어지는 모든 좌표는 -100,000 이상 100,000 이하의 정수이며 미터 단위이다. 또한 주어지는 모든 좌표의 위치는 서로 다르다.</p>

### 출력 

 <p>첫 번째 줄에 성원이가 T초 이내에 집에 도착하는 경우의 수를 10<sup>9</sup>+7로 나눈 나머지를 출력한다.</p>

