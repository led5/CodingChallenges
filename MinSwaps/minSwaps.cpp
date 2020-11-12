#include <vector> 

int minimumSwaps(std::vector<int> v) {
    int minSwaps = 0;
    for (int i = 0 ; i < v.size(); i++){
        // Check if current value is where it should be
        if(v[i] == i+1){ 
            continue; 
        }

        // Move current to correct location 
        int tmp = v[i];
        v[i] = v[v[i]-1];
        v[tmp - 1] = tmp;
        i--; 
        minSwaps++;
    }   
    return minSwaps;
}
