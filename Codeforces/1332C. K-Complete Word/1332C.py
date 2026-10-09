from collections import defaultdict
t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	word = input()
	
	split_word = []
	for start_idx in range(0, n, k):
		split_word.append(word[start_idx:start_idx + k])
	
	answer = 0
	for idx in range(k // 2):
		dic = defaultdict(int)
		for now_word in split_word:
			front_letter = now_word[idx]
			back_letter = now_word[-idx - 1]
			dic[front_letter] += 1
			dic[back_letter] += 1
		answer += (2 * len(split_word)) - max(dic.values())
	if k % 2 == 1:
		dic = defaultdict(int)
		for now_word in split_word:
			letter = now_word[k // 2]
			dic[letter] += 1
		answer += (len(split_word)) - max(dic.values())
	print(answer)