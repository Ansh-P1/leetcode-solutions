class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (n ==0) {
            return;
        }
        int k1 = (k%n);
        if (k1 == 0){
            return;
        }
        vector<int> temp(k1);
        for (int i =0; i<k1; i++){
            temp[i] = nums[i+n-k1];
        }
        for(int i = n-k1-1; i>=0; i--){
            nums[i+k1] = nums[i];
        }
        for(int i =0; i<k1; i++){
            nums[i] = temp[i];
        }   
    }
};