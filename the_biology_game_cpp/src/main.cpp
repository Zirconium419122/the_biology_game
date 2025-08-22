#include <iostream>
#include <string>
#include "player.h"

int main()
{
	std::string name;
	std::cout << "Adventurer, please enter your name: " << std::endl;
	std::cin >> name;

	Player player(name);

	return 0;
}
