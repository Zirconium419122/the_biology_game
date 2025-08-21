cmake_minimum_required(VERSION 3.10)

# Set the project name and version
project(the_biology_game_cpp VERSION 0.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add all .cpp files in the src directory
file(GLOB_RECURSE SOURCES "src/*.cpp")

# Define the executable
add_executable(the_biology_game_cpp ${SOURCES})

