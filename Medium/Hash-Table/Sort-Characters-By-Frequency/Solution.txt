class Solution {
public:
    string frequencySort(string s) {
        int n = s.size();
        int freq[128] ={0}; ///create an array
        for (char c : s){
            freq[c]++; /// recorded the occurance of the char c in string in the indx of its ascii value
        }

        vector<string> buckets(n+1);
        for (int i=0; i<128; i++){
            if (freq[i]>0){
                buckets[freq[i]] += (char)i;
            }
        }

        string result ="";
        for (int fv =n ; fv>=1; fv--){
            for (char c: buckets[fv]){
                for (int k=0; k<fv; k++){
                    result += c;
                }
            }
        }

        return result;
        
    }
};