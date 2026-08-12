class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_set<int> st,dup;
        for (int i: nums){
            if (st.count(i)){
                dup.insert(i);
            }
            else st.insert(i);
        }
        vector<int> ans;
        for (int i : dup){
            ans.push_back(i);
        }
        return ans; 
    }
};