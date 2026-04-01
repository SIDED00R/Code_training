#include <iostream>
int main() {
	int a, b;
	std::cin >> a >> b ;
	if (a > 0 && b > 0)
		std::cout << "1";
	else if (a > 0 && b < 0)
		std::cout << "4";
	else if (a < 0 && b > 0)
		std::cout << "2";
	else
		std::cout << "3";
}