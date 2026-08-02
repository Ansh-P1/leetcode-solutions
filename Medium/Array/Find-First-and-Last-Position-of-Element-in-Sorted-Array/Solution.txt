class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> ans; 
        int low = 0;
        int high = n-1;
        int a = -1;
        while (low <=high){
            int mid = (high +low)/2;
            if (nums[mid]<= target){
                a = mid;
                low = mid + 1;
            }
            else high = mid -1;
        }
        int b = lower_bound(nums.begin(), nums.end(), target) - nums.begin();

        if (b == n || nums[b]!=target){
            return {-1,-1};
        }
        ans.push_back(b);
        ans.push_back(a);
        return ans;
    }
};