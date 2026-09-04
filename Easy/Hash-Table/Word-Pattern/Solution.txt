class Solution {
public:
    bool wordPattern(string pattern, string s) {
        stringstream ss(s);
        string word;
        vector<string> words;
        while (ss>>word){
            words.push_back(word);
        }

        if (pattern.size() != words.size()){
            return false;
        }

        unordered_map<char, string> mapc;
        unordered_map<string, char> maps;

        for (int i=0; i<pattern.size(); i++){
            char c = pattern[i];
            string w = words[i];

            if (mapc.count(c)){
                if(mapc[c] != w){
                    return false;
                }
            }
            else{
                mapc[c] = w;
            }

            if (maps.count(w)){
                if(maps[w] != c){
                    return false;
                }
            }
            else{
                maps[w] = c;
            }
        }
        return true;

        
        
    }
};