class Solution:
	def fizzBuzz(self, n: int) -> list[str]:
		def find(num):
			if num % 3 == 0 and num % 5 == 0:
				return "FizzBuzz"
			elif num % 3 == 0:
				return "Fizz"
			elif num % 5 == 0:
				return "Buzz"
			else:
				return f"{num}"
		
		answer = []
		for num in range(1, n + 1):
			answer.append(find(num))
		return answer