#include <iostream> 

int fibonacci(int n){
    // Base case
    if (n <= 1)
        return n;
    return fibonacci(n-1) + fibonacci(n-2);
}
    
