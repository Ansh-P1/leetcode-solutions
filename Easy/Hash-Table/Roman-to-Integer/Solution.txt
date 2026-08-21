class Solution {
public:
    int romanToInt(string s) {
        vector<int> list(26);
        list['I'-'A'] = 1;
        list['V'-'A'] = 5;
        list['X'-'A'] = 10;
        list['L' - 'A'] = 50;
        list['C' - 'A'] = 100;
        list['D' - 'A'] = 500;
        list['M' - 'A'] = 1000;
        int ans=0;
        for (int i=0; i<s.size(); i++){
            int curr = list[s[i]-'A'];
            if (i+1<s.size() && curr< list[s[i+1]-'A'] ){
                ans -= curr;
            }
            else ans += curr;
        }
        return ans;
    }
};