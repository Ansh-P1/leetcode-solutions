class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> list(26,0);
        for (int i=0; i<magazine.size(); i++){
            list[magazine[i]-'a']++;
        }
        for (int i=0; i<ransomNote.size(); i++){
            list[ransomNote[i]-'a']--;
            if (list[ransomNote[i]-'a']<0){
                return false;
                break;
            }
        }
        return true;

         
    }
};