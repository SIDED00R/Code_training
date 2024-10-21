# [Silver I] Heksadekadski Haos - 31195 

[문제 링크](https://www.acmicpc.net/problem/31195) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

구현, 문자열

### 제출 일자

2024년 10월 21일 16:02:44

### 문제 설명

<p>Nova generacija internet protokola <em>IPv6</em> definira IP adresu od $128$ bitova. Potpuni zapis IPv6 adrese sastoji se od $8$ grupa po $4$ heksadecimalne znamenke gdje su grupe odvojene znakom dvotočke ('<code>:</code>'). Na primjer:</p>

<p style="text-align: center;"><code>2001:0db8:85a3:0000:0000:8a2e:0370:7334</code></p>

<p>Kako bi se skratio zapis IPv6 adresa, dozvoljena su neka pojednostavljenja potpunog zapisa.</p>

<ul>
	<li>
	<p>Sve ili samo neke vodeće nule unutar grupe mogu se izostaviti, pa se tako gornja adresa može pojednostaviti kao:</p>

	<p style="text-align: center;"><code>2001:db8:85a3:0:00:8a2e:370:7334</code></p>
	</li>
	<li>
	<p>Dodatno, jedna ili više uzastopnih grupa jednakih nula može se zamijeniti dvostrukim znakom dvotočke ("<code>::</code>"). Gornja adresa tako postaje:</p>

	<p style="text-align: center;"><code>2001:db8:85a3::8a2e:370:7334</code></p>

	<p>Ovo pojednostavljenje moguće je učiniti samo jednom kako bi iz dobivenog zapisa bilo moguće jedinstveno odrediti adresu.</p>
	</li>
</ul>

<p>Napišite program koji će za pravilno zapisanu IPv6 adresu odrediti njen potpuni zapis.</p>

### 입력 

 <p>U prvom se redu nalazi niz od najviše $39$ znakova, pravilno zapisana IPv6 adresa. Niz se sastoji isključivo od znamenaka '<code>0</code>'-'<code>9</code>', malih slova '<code>a</code>'-'<code>f</code>' i znakova dvotočke – '<code>:</code>'.</p>

### 출력 

 <p>U prvi i jedini red potrebno je ispisati potpuni zapis zadane IPv6 adrese.</p>

