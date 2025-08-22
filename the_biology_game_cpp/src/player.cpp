#include <iostream>
#include <string>
#include "player.h"

Player::Player(const std::string& name) : name(name) {}

void Player::greet() {
	std::cout << "Welcome, " << name << "!" << std::endl;
}

