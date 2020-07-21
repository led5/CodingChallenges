# include <iostream>

// Brute force solution for FizzBuzz 

std::string fizzBuzz(int num1, int num2){
    for(int i=1; i <= 100; i++){

        bool multipleOfNum1 = i % num1 == 0;
        bool multipleOfNum2 = i % num2 == 0;

        if(multipleOfNum1 && multipleOfNum2) { std::cout << "FizzBuzz\n"; }
        else if (multipleOfNum1) { std::cout << "Fizz\n"; }
        else if (multipleOfNum2) { std::cout << "Buzz\n"; } 
        else  { std::cout << i << "\n"; }  
    } 
    return ""; 
};

int main(){

    int num1, num2; 
    std::cout << std::endl;
    std::cout << "Enter a number for FizzBuzz: "; 
    std::cin >> num1;
    std::cout << "Enter another number for FizzBuzz: ";
    std::cin >> num2;

    // Solution:
    std::cout << std::endl;
    std::cout << "-----Result---------" << "\n";
     std::cout << std::endl;
    std::cout << "FizzBuzz of " << num1 << " and " << num2 << "\n";
     std::cout << std::endl;
    std::cout << "--------------------" << "\n";

    std::cout << std::endl;
    std::string retVal = fizzBuzz(num1,num2); 
    std::cout << retVal; 

}