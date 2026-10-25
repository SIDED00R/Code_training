# [LeetCode Medium] Course Schedule - course-schedule

[문제 링크](https://leetcode.com/problems/course-schedule/)

## 성능 요약

메모리: - KB, 시간: - ms

## 분류

`Depth-First Search`, `Breadth-First Search`, `Graph Theory`, `Topological Sort`, `Directed Acyclic Graph`

## 제출 일자

2026년 10월 25일 09:53:56

## 문제 설명

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 

Constraints:

1 <= numCourses <= 2000

0 <= prerequisites.length <= 5000

prerequisites[i].length == 2

0 <= ai, bi < numCourses

All the pairs prerequisites[i] are unique.

## 코드 리뷰

- 효율성: 효율적
- 시간복잡도: O(V + E) 시간, O(V + E) 공간 (V = numCourses, E = len(prerequisites))

### 잘한 점

- O(V+E)의 최적 시간복잡도로 Kahn's 알고리즘을 올바르게 구현함
- defaultdict를 활용해 그래프와 차수 배열을 간결하게 초기화함
- 사이클 탐지의 핵심 로직(스택에 차수 0인 노드를 넣고 처리)이 정확하게 동작함

### 개선할 점

- 그래프를 구성할 때 next_node와 count의 방향이 실제 선수과목 의존관계(prerequisite -> course)와 반대로 되어 있어 코드 가독성과 유지보수성이 떨어짐 (우연히 사이클 존재 여부는 역방향에서도 동일하기 때문에 정답은 맞지만 혼란을 줄 수 있음)
- 마지막에 count.items()를 순회해 전부 0인지 확인하는 방식 대신, 처리된 노드 개수를 세어 numCourses와 비교하는 방식이 더 명확하고 일반적인 Kahn's 알고리즘 패턴에 부합함
- 변수명(out, n_n)이 다소 축약되어 가독성이 떨어지며, 어떤 의미인지 파악하기 어려움

### 상세 피드백

이 풀이는 Kahn's 알고리즘(BFS 기반 위상 정렬)을 이용한 전형적인 O(V+E) 풀이로, Course Schedule 문제의 최적 해법 중 하나입니다. DFS 기반 사이클 탐지와 시간복잡도는 동일하지만 재귀 깊이 제한 문제를 피할 수 있다는 장점이 있습니다.

다만 코드에서 그래프를 구성하는 방향이 직관과 반대입니다. prerequisites[i] = [a, b]는 'b를 먼저 들어야 a를 들을 수 있다'는 의미(b -> a 간선)인데, 코드는 `next_node[front=a].append(back=b)`로 a -> b 간선을 만들고 `count[b]`를 증가시킵니다. 즉 원래 그래프의 역방향 그래프에 대해 in-degree를 계산하는 셈입니다. 다행히 방향 그래프를 전부 뒤집어도 사이클 존재 여부는 변하지 않기 때문에(원그래프가 DAG ⟺ 역그래프가 DAG) 사이클 탐지 자체는 정확하게 동작하지만, 변수명(next_node, count)이 실제 의미(선수과목 그래프의 역방향)와 일치하지 않아 코드를 읽는 사람이 혼란을 느끼기 쉽습니다. 주석이나 변수명을 'reverse_graph', 'out_degree' 등으로 명확히 하면 가독성이 크게 개선될 것입니다.

또한 마지막에 `count.items()`를 순회하며 0이 아닌 값이 있는지 확인하는 대신, 처리된 노드 수를 카운트해서 `processed == numCourses`인지 비교하는 방식이 더 명확하고 Kahn's 알고리즘의 전형적인 구현 패턴에 가깝습니다. defaultdict를 사용해 count[i]가 없을 때 자동으로 0이 되는 점을 활용한 것은 좋지만, 명시적으로 모든 노드의 in-degree를 0으로 초기화한 뒤 계산하는 편이 더 안전하고 읽기 쉽습니다.
