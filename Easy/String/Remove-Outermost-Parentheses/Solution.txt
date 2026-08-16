class Solution {
public:
    string removeOuterParentheses(string s) {
        int dep =0;
        string result= "";
        for (char c :s){
            if (c=='('){
                if (dep>0){
                    result += c;
                }
                dep++;
            }
            else {
                dep--;
                if (dep>0){
                    result += c;
                }
            }
        }
        return result;
    }
};