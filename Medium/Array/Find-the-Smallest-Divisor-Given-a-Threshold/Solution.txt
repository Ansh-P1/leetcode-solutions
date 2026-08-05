class Solution {
public:
    bool possi(vector<int>& nums, int threshold, int mid){
        int n = nums.size();
        int sum = 0;
        for (int i =0; i<n ; i++){
            sum += ceil((double)nums[i]/mid);
        }
        if (sum<=threshold){
            return true;
        }
        else return false;
    }
    int smallestDivisor(vector<int>& nums, int threshold) {
        int n = nums.size();
        int maxi = INT_MIN;
        int mini = INT_MAX;
        for(int i =0; i<n; i++){
            maxi = max(maxi,nums[i]);
            mini = min(mini,nums[i]);
        }
        int low = 1;
        int high = maxi;
        while (high>low){
            int mid =(low+high)/2;
            if (possi(nums,threshold,mid)){
                high = mid;
            }
            else low = mid +1;

        }
        return low;
        
    }
};