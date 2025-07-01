# Project Documentation

## Overview

This project is a C++ codebase that provides utility functions for mathematical operations and string manipulations. It is designed to demonstrate the usage of these utility functions in a simple application.

## Directory Structure

```
cpp-codebase-lm
├── src
│   ├── main.cpp
│   ├── math_utils.cpp
│   ├── math_utils.h
│   ├── string_utils.cpp
│   └── string_utils.h
├── docs
│   └── documentation.md
├── CMakeLists.txt
└── README.md
```

## Utility Functions

### Math Utilities

The `math_utils` module provides basic mathematical operations. The following functions are available:

1. **add**
   - **Signature:** `double add(double a, double b)`
   - **Description:** Returns the sum of two numbers.
   - **Example:**
     ```cpp
     double result = add(5.0, 3.0); // result is 8.0
     ```

2. **subtract**
   - **Signature:** `double subtract(double a, double b)`
   - **Description:** Returns the difference between two numbers.
   - **Example:**
     ```cpp
     double result = subtract(5.0, 3.0); // result is 2.0
     ```

3. **multiply**
   - **Signature:** `double multiply(double a, double b)`
   - **Description:** Returns the product of two numbers.
   - **Example:**
     ```cpp
     double result = multiply(5.0, 3.0); // result is 15.0
     ```

4. **divide**
   - **Signature:** `double divide(double a, double b)`
   - **Description:** Returns the quotient of two numbers. Throws an error if the divisor is zero.
   - **Example:**
     ```cpp
     double result = divide(6.0, 3.0); // result is 2.0
     ```

### String Utilities

The `string_utils` module provides functions for string manipulation. The following functions are available:

1. **concatenate**
   - **Signature:** `std::string concatenate(const std::string& str1, const std::string& str2)`
   - **Description:** Concatenates two strings and returns the result.
   - **Example:**
     ```cpp
     std::string result = concatenate("Hello, ", "World!"); // result is "Hello, World!"
     ```

2. **split**
   - **Signature:** `std::vector<std::string> split(const std::string& str, char delimiter)`
   - **Description:** Splits a string into a vector of substrings based on the specified delimiter.
   - **Example:**
     ```cpp
     std::vector<std::string> result = split("a,b,c", ','); // result is {"a", "b", "c"}
     ```

## Usage

To use the utility functions, include the respective header files in your source files. For example, to use the math utilities in `main.cpp`, include `math_utils.h`:

```cpp
#include "math_utils.h"
```

## Building the Project

To build the project, use CMake. Navigate to the project directory and run the following commands:

```bash
mkdir build
cd build
cmake ..
make
```

## Conclusion

This documentation provides an overview of the utility functions available in the project, along with examples of how to use them. For further details, refer to the source code in the `src` directory.