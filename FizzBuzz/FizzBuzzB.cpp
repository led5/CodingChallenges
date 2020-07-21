# include <iostream>

// Build string 

std::string fizzBuzz(int num1, int num2){

    std::string output = "";

    for(int i=1; i <= 100; i++){
        if (i % 3 == 0) output = "Fizz \n";
        if (i % 5 == 0) output = "Buzz \n";
        if (output == "") output = i;
        std::cout << output << "\n";   
    } 
    return output; 
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
    std::cout << "-----Example 1------" << "\n";
     std::cout << std::endl;
    std::cout << "Factors of " << num1 << " and " << num2 << "\n";
     std::cout << std::endl;
    std::cout << "--------------------" << "\n";

    std::cout << std::endl;
    std::string retVal = fizzBuzz(num1,num2); 
    std::cout << retVal << " "; 
    std::cout << std::endl;
}