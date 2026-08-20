class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int el1= INT_MIN;
        int c1=0;
        int c2 =0;
        int el2 =INT_MIN;
        for (int i=0; i<nums.size(); i++){
            if (c1 ==0 &&  el2 != nums[i] ){
                el1 = nums[i];
                c1=1;;
            }
            else if (c2 ==0 && el1 != nums[i]){
                el2 = nums[i];
                c2=1;
            }
            else if (el1 == nums[i]) c1++;
            else if (el2 == nums[i]) c2++;
            else {
                c1--;
                c2--;
            }
        }
        vector<int> ans;
        c1 = 0;
        c2 = 0;
        for (int i=0; i<nums.size(); i++){
            if (nums[i] == el1) c1++;
            if (nums[i] == el2) c2++;
        }
        int mini = (nums.size()/3)+1;
        if (c1>=mini) ans.push_back(el1);
        if (c2>=mini) ans.push_back(el2);
        sort(ans.begin(), ans.end());

        return ans;
        
    }
};