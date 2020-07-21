# include <iostream>

// Build string 

int main(){
    
    for(int i=1; i <= 100; i++){
        std::string output = ""; 
        if (i % 3 == 0) output = "Fizz \n";
        if (i % 5 == 0) output = "Buzz \n";
        if (output == "") output = i;
        std::cout << output << "\n";
    } 
     
    return 0; 
}