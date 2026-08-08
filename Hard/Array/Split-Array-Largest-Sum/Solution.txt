class Solution {
public:
    int minfunc(vector<int>& nums, int limit){
        int a1=1;
        long long value = 0;
        for (int i = 0; i< nums.size(); i++){
            if (value + nums[i] <= limit){
                value += nums[i];
            }
            else {
                a1++;
                value = nums[i];
            }
        }
        return a1;
    }
    int splitArray(vector<int>& nums, int k) {
        int low = *max_element (nums.begin(), nums.end());
        int high = accumulate(nums.begin(), nums.end(), 0);
        while (low<= high){
            int mid = (low + high)/2;
            int aa  = minfunc(nums,mid);
            if (aa>k){
                low = mid +1;
            }
            else high = mid -1;
        }
        return low;  
    }
};