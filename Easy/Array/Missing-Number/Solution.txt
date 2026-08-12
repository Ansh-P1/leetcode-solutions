class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        for (int i =0; i<n; i++){
            sum += nums[i];
        }
        int sum2=0;
        while (n>0){
            sum2 += n;
            n--;
        }
        return sum2-sum;
        
    }
};