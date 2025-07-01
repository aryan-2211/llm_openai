#include <iostream>
#include "math_utils.h"
#include "string_utils.h"

int main() {
    // Demonstrate usage of math utility functions
    double a = 10.0;
    double b = 5.0;

    std::cout << "Math Utilities:" << std::endl;
    std::cout << "Add: " << add(a, b) << std::endl;
    std::cout << "Subtract: " << subtract(a, b) << std::endl;
    std::cout << "Multiply: " << multiply(a, b) << std::endl;
    std::cout << "Divide: " << divide(a, b) << std::endl;

    // Demonstrate usage of string utility functions
    std::string str1 = "Hello, ";
    std::string str2 = "World!";
    
    std::cout << "\nString Utilities:" << std::endl;
    std::cout << "Concatenate: " << concatenate(str1, str2) << std::endl;

    std::string str = "apple,banana,cherry";
    std::vector<std::string> fruits = split(str, ',');
    std::cout << "Split: ";
    for (const auto& fruit : fruits) {
        std::cout << fruit << " ";
    }
    std::cout << std::endl;

    return 0;
}