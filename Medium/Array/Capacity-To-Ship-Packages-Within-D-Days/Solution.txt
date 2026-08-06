class Solution {
public:
    int loaded (vector<int>& weights, int mid){
        int n = weights.size();
        int day = 1;
        int load = 0; 
        for (int i =0; i<n; i++){
            if (load + weights[i]>mid){
                day ++;
                load = weights[i];
            }
            else load+= weights[i];
        }
        return day;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int n = weights.size();
        int maxi= INT_MIN;
        int sum = 0;
        for (int i =0;i<n; i++){
            maxi = max(maxi,weights[i]);
            sum += weights[i];
        }
        int low = maxi;
        int high = sum;
        while (low <= high){
            int mid = (low+high)/2;
            int load = loaded(weights,mid);
            if (load <= days){
                high = mid -1;
            }
            else low = mid +1;
        }
        return low;  
    }
};