class Solution {
public:
    int lengthOfLastWord(string s) {
        stringstream ss(s);
        string word;
        vector<string> words;
        while (ss>>word){
            words.push_back(word);
        }
        string ans = words[(words.size())-1];
        return ans.size();
        
    }
};