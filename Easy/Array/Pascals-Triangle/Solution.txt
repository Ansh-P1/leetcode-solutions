class Solution {
public:
    vector<int> generateRow(int row){
        int ans = 1;
        vector<int> ansRow;
        ansRow.push_back(ans);
        for (int i=1; i<row; i++){
            ans = ans * (row-i);
            ans = ans/i;
            ansRow.push_back(ans);
        }
        return ansRow;
    }
    
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> Pans;
        for (int i =1; i<=numRows; i++){
            Pans.push_back(generateRow(i));
        }
        return Pans;   
    }
};