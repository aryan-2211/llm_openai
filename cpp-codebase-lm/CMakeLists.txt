project(cpp-codebase-lm)

set(CMAKE_CXX_STANDARD 11)

include_directories(src)

file(GLOB SOURCES
    src/*.cpp
)

add_executable(cpp-codebase-lm ${SOURCES})