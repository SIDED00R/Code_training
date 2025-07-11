# 유니코드 완성형 한글 범위: U+AC00 ~ U+D7A3
first = 0xAC00
last = 0xD7A3

all_korean_syllables = [chr(code) for code in range(first, last + 1)]

n = int(input())
print(all_korean_syllables[n - 1])
