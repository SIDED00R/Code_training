# [Gold II] Broken Cipher Generator - 22430 

[문제 링크](https://www.acmicpc.net/problem/22430) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

자료 구조, 그리디 알고리즘, 구현, 파싱, 재귀, 스택, 문자열

### 제출 일자

2025년 1월 25일 07:25:12

### 문제 설명

<p>JAG (Japanese Alumni Group) は多くのプログラマで構成される謎の組織であり，この組織の本部がある建物に入るためには毎回ある機械によって生成される暗号文を解かなくてはならない． この暗号文は，'<samp>+</samp>'，'<samp>-</samp>'，'<samp>[</samp>'，'<samp>]</samp>' の記号と大文字のアルファベットからなっており，以下の BNF で定義される <Cipher> によって表される．</p>

<pre><Cipher> ::= <String> | <Cipher><String>
<String> ::= <Letter> | '['<Cipher>']'
<Letter> ::= '+'<Letter> | '-'<Letter> |
             'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' |
             'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'</pre>

<p>ここでそれぞれの記号は以下のような意味を表す．</p>

<ul>
	<li>+(文字) : その文字の次のアルファベットを表す (ただし '<samp>Z</samp>' の次のアルファベットは '<samp>A</samp>' であるとする)</li>
	<li>-(文字) : その文字の前のアルファベットを表す (ただし '<samp>A</samp>' の前のアルファベットは '<samp>Z</samp>' であるとする)</li>
	<li>[(文字列)] : その文字列を左右反転した文字列を表す</li>
</ul>

<p>しかしこの暗号文を生成する機械には現在故障が発生しており，暗号文のうちアルファベットの箇所が数文字壊れて読めなくなっている場合がある．読めない文字は仮に '<samp>?</samp>' と表されている． 調査の結果，壊れた文字の埋め方は，復号後の文字列が，復号後の文字列としてありえる文字列の中で辞書順最小になるようなものであることがわかった． あなたの仕事はこの暗号文を正しく復号することである．</p>

### 입력 

 <p>入力は複数のデータセットから構成される． 各データセットは，上記の BNF で定義された暗号文において，一部の大文字のアルファベットが ‘?’ に置き換えられた文字列を含む 1 行からなる． 各文字列の長さは <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$80$</span></mjx-container> 以下であると仮定してよい． また各データセットに含まれる '<samp>?</samp>' の数は <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> 以上 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container> 以下であると仮定してよい．</p>

<p>入力の終了は '<samp>.</samp>' の1文字だけを含む行で表される．</p>

### 출력 

 <p>各データセットに対して，復号後の文字列が辞書順最小になるように暗号文を復号したときの，復号後の文字列を出力せよ．</p>

