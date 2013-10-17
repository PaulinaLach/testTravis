#include <lib.hpp>
#include <iostream>

int defaultMethod()
{
    std::cout << "default method" << std::endl;
    return 0;
}

int method1(int value)
{
    if (value == 1) {
        std::cout << "method 1 branch 1" << std::endl;
        return 1;
    } else {
        std::cout << "method 1 branch 2" << std::endl;
        return 2;
    }
}

int method2()
{
    int unusedVariable = 0;
    std::cout << "method 2" << std::endl;
    return 3;
}
