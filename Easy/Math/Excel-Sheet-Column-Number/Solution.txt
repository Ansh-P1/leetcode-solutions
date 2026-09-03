class Solution {
public:
    int titleToNumber(string columnTitle) {
        int  n = columnTitle.size();
        int cn =0;
        for (int i =0; i<n; i++){
            cn = cn*26 + (columnTitle[i] - 'A'+1);

        }
        return cn;
         
        
    }
};