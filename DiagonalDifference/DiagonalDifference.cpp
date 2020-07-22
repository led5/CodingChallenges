# include <iostream> 
# include <math.h>
# include "vector"
# include "random"

void diagonalDifference(std::vector<std::vector<int> > arr) {
    int principal = 0, secondary = 0, diff = 0; 
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if (i == j)
                principal += arr[i][j];
            if ((i+j) == (arr.size()-1))
                secondary += arr[i][j];
        }
    }
    diff = abs(principal - secondary); 

    std::cout << std::endl; 
    std::cout << "Principal Diagonal: " << principal << std::endl; 
    std::cout << "Secondary Diagonal: " << secondary << std::endl;  
    std::cout << "Diagonal Difference: " << diff << std::endl; 
    std::cout << std::endl; 
}; 

int main(){

    std::vector<std::vector<int> > mat;
    int difference = 0, h = 0, w = 0;
    srand((unsigned int)time(NULL));

    mat.resize(3); 
    for(int i = 0; i < 3; i++){
        mat[i].resize(3); 
        for(int j = 0; j < 3; j++){
            mat[i][j] = rand() % 100;
        } 
    }
    diagonalDifference(mat); 
}