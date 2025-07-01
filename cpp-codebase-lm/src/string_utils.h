#ifndef STRING_UTILS_H
#define STRING_UTILS_H

#include <string>
#include <vector>

std::string concatenate(const std::string& str1, const std::string& str2);
std::vector<std::string> split(const std::string& str, char delimiter);

#endif // STRING_UTILS_H