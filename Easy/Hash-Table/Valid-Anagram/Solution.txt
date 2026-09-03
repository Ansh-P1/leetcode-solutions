class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }
        vector<int> arr(26,0);
        for (int i=0; i<s.size(); i++){
            int c = s[i] -'a';
            arr[c]++;
            int ch = t[i] -'a';
            arr[ch]--;
        }

        for (int i=0; i<26; i++){
            if (arr[i] != 0){
                return false;
            }
        }
        return true;
        
    }
};