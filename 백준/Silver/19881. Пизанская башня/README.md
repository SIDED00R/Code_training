# [Silver I] Пизанская башня - 19881 

[문제 링크](https://www.acmicpc.net/problem/19881) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

다이나믹 프로그래밍, 재귀

### 제출 일자

2024년 8월 22일 07:46:06

### 문제 설명

<p>Многим из вас, наверное, известна легенда про Ханойскую башню. Легенда гласит, что в одном далеком монастыре находится бронзовый диск, на котором закреплены три алмазных стержня. Давным-давно, в самом начале времен, монахи этого монастыря провинились перед богами. Разгневанные боги положили <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> дисков на один из стержней, все диски имели разные радиусы и были расположены по убыванию радиуса --- самый большой диск лежал снизу, на нем диск поменьше, \dots, самый маленький диск располагался сверху. Монахи должны перекладывать диски между стержнями, причем каждый раз должны класть диск либо на пустой стержень, либо поверх большего диска. Как только все <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> дисков будут переложены со стержня, на который боги сложили их, на другой стержень, башня вместе с храмом обратятся в пыль и под громовые раскаты погибнет мир.</p>

<p>Однако недавно Петя прочитал новую версию легенды. Согласно этой легенде, в Пизанской башне есть аналогичная головоломка, но второй стержень у нее наклонен. Со второго стержня можно снимать сразу несколько дисков, лежащих сверху, и перекладывать их вместе, не меняя порядка, на другой стержень. При этом группу дисков также можно перекладывать либо на пустой стержень, либо на диск, который больше нижнего из перекладываемых дисков.</p>

<p>По легенде, когда все диски будут перенесены с первого стержня на третий, Пизанская башня перестанет наклоняться и начнет стоять ровно.</p>

<p>Петю заинтересовало, за какое минимальное число действий можно перенести все диски с первого стержня Пизанской головоломки на третий.  Помогите ему выяснить это.</p>

### 입력 

 <p>Во входном файле задано единственное натуральное число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>40</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 40$</span></mjx-container>) --- количество дисков.</p>

### 출력 

 <p>Выведите единственное число --- минимальное число перекладываний, необходимое для того, чтобы все диски оказались на третьем стержне.</p>

