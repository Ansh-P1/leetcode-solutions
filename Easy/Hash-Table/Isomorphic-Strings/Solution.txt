class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int arrs[256] = {0};
        int arrt[256] = {0};

        for (int i=0; i<s.size(); i++){
            char c1 = s[i];
            char c2 = t[i];

            if (arrs[c1] == 0 && arrt[c2] == 0){
                arrs[c1] = c2;
                arrt[c2] = c1;
            }
            else{
                if (arrs[c1] != c2 || arrt[c2] != c1){
                    return false;
                }
            }
        }
        return true;
        
    }
};