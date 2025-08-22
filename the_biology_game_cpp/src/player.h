// my_class.hpp
#ifndef PLAYER_HPP
#define PLAYER_HPP

#include <string>
#include <iostream>


class Player {
public:
    std::string name;
    int hp = 100;
    
    // Constructor declaration
    Player(std::string& name);

    void greet();

};


#endif