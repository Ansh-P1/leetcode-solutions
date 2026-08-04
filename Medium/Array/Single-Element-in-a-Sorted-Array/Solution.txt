class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();
        int low = 0;
        int high = n-2;
        ///int ans = -1;
        while (low <= high){
            int mid = (low + high)/2;
            if (mid % 2 ==1){
                mid --;
            }
            if (nums[mid+1] == nums[mid]){
                ///if ((n - mid+1) % 2 == 0){
                low = mid +2;
            }    
            else high = mid -1 ;
            ///else if (nums[mid-1] == nums[mid])  {///mid -1 == mid 
                ///if (mid % 2==0){
                    ///high = mid -2;
               /// }
                ///else low = mid +1;
            ///}
            ///else {
                ///ans = nums[mid];
                ///return ans;
            ///}

        }
        return nums[low];
        
    }
};