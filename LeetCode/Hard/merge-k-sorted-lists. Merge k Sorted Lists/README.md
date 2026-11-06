# [LeetCode Hard] Merge k Sorted Lists - merge-k-sorted-lists

[문제 링크](https://leetcode.com/problems/merge-k-sorted-lists/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Linked List`, `Divide and Conquer`, `Heap (Priority Queue)`, `Merge Sort`, `Tournament Sort`

## 제출 일자

2026년 11월 7일 08:13:53

## 문제 설명

k개의 연결 리스트 lists가 배열로 주어지며, 각 연결 리스트는 오름차순으로 정렬되어 있습니다.

모든 연결 리스트를 하나의 정렬된 연결 리스트로 합쳐서 반환하세요.

 

예제 1:

입력: lists = [[1,4,5],[1,3,4],[2,6]]
출력: [1,1,2,3,4,4,5,6]
설명: 연결 리스트는 다음과 같습니다:
[
  1->4->5,
  1->3->4,
  2->6
]
이들을 하나의 정렬된 연결 리스트로 합치면:
1->1->2->3->4->4->5->6

예제 2:

입력: lists = []
출력: []

예제 3:

입력: lists = [[]]
출력: []

 

제약 조건:

k == lists.length

0 <= k <= 10^4

0 <= lists[i].length <= 500

-10^4 <= lists[i][j] <= 10^4

lists[i]는 오름차순으로 정렬되어 있습니다.

lists[i].length의 합은 10^4을 초과하지 않습니다.

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: 시간복잡도 O(N log k), 공간복잡도 O(k + N) (N은 전체 노드 수, k는 리스트 개수) - 힙에 최대 k개의 원소를 유지하며 N번의 push/pop을 수행하므로 O(N log k)

### 잘한 점

- min-heap을 사용해 O(N log k)의 최적 시간복잡도를 달성함
- ListNode 비교 불가 문제를 [value, idx] 쌍으로 우회하여 올바르게 해결함
- 빈 리스트(lists[i]가 None) 및 빈 입력(lists=[])에 대한 엣지케이스를 자연스럽게 처리함
- dummy head(answer) 패턴을 사용해 결과 리스트 구성을 간결하게 처리함

### 개선할 점

- 이미 있는 노드를 재사용하지 않고 ListNode(value)로 매번 새 노드를 생성해 불필요한 메모리 할당이 발생함
- 원본 입력 리스트 lists 배열 자체를 직접 수정하는 side-effect가 있어 좋은 설계 습관이 아님
- 변수명 now_node는 current_node 등으로 바꾸면 가독성이 더 좋아질 수 있음
- 힙에 저장하는 원소를 list([value, idx])가 아닌 tuple로 쓰면 약간의 성능/메모리 이점이 있음

### 상세 피드백

min-heap을 이용한 k-way merge는 이 문제에 대해 이론적으로 최적에 가까운 접근입니다 (Divide and Conquer 방식도 동일하게 O(N log k)이며 서로 우열을 가리기 어려운 대안입니다). ListNode 객체는 기본적으로 비교 연산자가 없기 때문에 [value, idx] 형태로 튜플/리스트를 만들어 인덱스로 tie-break을 처리한 점은 적절한 해결책입니다. 다만 이미 존재하는 노드의 값을 그대로 쓸 수 있음에도 ListNode(value)로 매번 새 노드를 생성해서 복사하는 부분은 불필요한 메모리 할당입니다. 원본 노드(now_node = lists[idx]처럼)를 직접 연결하면 추가 공간을 절약할 수 있습니다. 또한 lists[idx] = lists[idx].next 로 원본 입력 배열을 변경하는 side-effect가 있는데, 별도의 포인터 배열(current)을 쓰는 것이 더 안전한 설계입니다. 빈 리스트와 빈 배열(k=0) 모두 올바르게 처리되는 점은 좋습니다.
