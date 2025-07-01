#include "string_utils.h"
#include <sstream>

std::string concatenate(const std::string& str1, const std::string& str2) {
    return str1 + str2;
}

std::vector<std::string> split(const std::string& str, char delimiter) {
    std::vector<std::string> tokens;
    std::stringstream ss(str);
    std::string token;

    while (std::getline(ss, token, delimiter)) {
        tokens.push_back(token);
    }

    return tokens;
}