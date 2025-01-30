# [Gold V] Logic Puzzle - 16073 

[문제 링크](https://www.acmicpc.net/problem/16073) 

### 성능 요약

메모리: 32412 KB, 시간: 88 ms

### 분류

구현

### 제출 일자

2025년 1월 30일 10:39:26

### 문제 설명

<p>While browsing a kiosk at a recent trip, you bought a magazine filled with various kinds of logic puzzles. After a while of solving, however, you start to get a bit bored of the puzzles. Still wanting to complete all the puzzles in the magazine, you start wondering about ways to solve some of them algorithmically.</p>

<p>The puzzle you are currently trying to solve is called Mosaic, and it is quite similar to the classic Minesweeper video game:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6765c456-ce04-4d09-83de-69c9ca3b4e05/-/preview/" style="width: 396px; height: 163px;"></p>

<p style="text-align: center;">Figure L.1: Illustration of the first sample</p>

<p>You are given a two-dimensional grid of cells, initially all white, and you have to color some of the cells in black. You are also given a grid of clue numbers, which extends beyond the borders of the puzzle grid by one cell in each direction. The number in a cell indicates (exactly) how many cells in the 3 × 3 block centered at this cell need to be colored in black. You may not color any cells outside of the original grid.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with two integers h, w (1 ≤ h, w ≤ 100), the height and width of the puzzle;</li>
	<li>h + 2 lines, each with w + 2 integers c<sub>1</sub>, . . . , c<sub>w+2</sub> (0 ≤ c<sub>i</sub> ≤ 9), the clue numbers.</li>
</ul>

### 출력 

 <p>If the given clue numbers are inconsistent, output impossible. Otherwise, output h lines with w characters each, the solution to the puzzle. Use X for black cells and . for white cells. If there are multiple solutions, any of them will be accepted.</p>

