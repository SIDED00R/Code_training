#include <iostream>
int main() {
	int a, b;
	std::cin >> a >> b ;
	b = b - 45;
	if (b < 0) {
		b = b + 60;
		a = a - 1;
	}
	if (a < 0) {
		a = a + 24;
	}
	std::cout << a << " " << b;
}