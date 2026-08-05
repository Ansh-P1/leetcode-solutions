class Solution {
public:
    int maximum(vector<int>& piles){
        int n = piles.size();
        int maxi = INT_MIN;
        for (int i =0; i<n; i++){
            maxi = max (maxi, piles[i]);
        }
        return maxi;
    }
    int totalhrs(vector<int>& piles, int thr){
        int n = piles.size();
        int totalhrs = 0;
        for (int i=0; i<n ; i++){
            totalhrs += ceil((double)piles[i]/thr);///mistake = istead of += and use double to make the use of ceila nd have . values 
        }
        return totalhrs;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = maximum(piles);
        while (low < high ){
            long long mid = (low + high)/2;
            int totalhours = totalhrs(piles,mid);
            if (totalhours <= h){
                high = mid;///mistake mid could also be the min that i didnt account to
            }
            else low = mid +1; 
        }
        return low;
        
    }
};