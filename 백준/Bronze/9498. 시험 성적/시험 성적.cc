#include <iostream>
int main() {
	int a;
	std::cin >> a ;
	if (100 >= a && a >= 90)
		std::cout << "A";
	else if (89 >= a && a >= 80)
		std::cout << "B";
	else if (79 >= a && a >= 70)
		std::cout << "C";
	else if (69 >= a && a >= 60)
		std::cout << "D";
	else
		std::cout << "F";
}