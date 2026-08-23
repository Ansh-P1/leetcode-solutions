class Solution {
public:
    pair<int,int> a(string& s, int left, int right){
        while (left>=0 && right<= s.size() && s[left] == s[right]){
            left--;
            right++;
        }
        return {left+1, right-1};
    }
    string longestPalindrome(string s) {
        int start =0;
        int maxlen =0;
        for (int i=0; i<s.size(); i++){
            auto odd= a(s,i,i);
            int oddlen = odd.second - odd.first +1;
            if (oddlen>maxlen){
                maxlen = oddlen;
                start =odd.first;
            }
            auto even= a(s,i,i+1);
            int evenlen = even.second - even.first +1;
            if (evenlen>maxlen){
                maxlen = evenlen;
                start =even.first;
            }

        }
        return s.substr(start,maxlen);
        
    }
};