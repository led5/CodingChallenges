#include <vector>

int pairDiff(int k, std::vector<int>v){

    // Return count of pairs with difference k
    int count = 0, i = 0, j = 1, n = v.size();
    std::sort(v.begin(), v.end());
    
    while(j < n){
        int diff = v[j] - v[i];
        
        if (diff == k){ count++; j++; i++; }
        else if (diff > k){ i++; }
        else { j++; }
    }
    return count;
}
