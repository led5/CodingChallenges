# include <iostream> 
# include <math.h>
# include "vector"
# include "random"



void diagonalDifference(std::vector<std::vector<int> > arr) {
    int principal = 0, secondary = 0, diff = 0; 
    for(int i = 0; i < arr.size(); i++){
        for(int j = 0; j < arr.size(); j++){
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

    std::cout << std::endl;
    std::cout << "Enter matrix height: " << std::endl;
    std::cin >> h;
    std::cout << "Enter matrix width: " << std::endl; 
    std::cin >> w;
    std::cout << std::endl;

    mat.resize(h); 
    for(int i = 0; i < h; i++){
        mat[i].resize(w); 
        for(int j = 0; j < w; j++){
            mat[i][j] = rand() % 100;
        }
    }
    diagonalDifference(mat); 
}