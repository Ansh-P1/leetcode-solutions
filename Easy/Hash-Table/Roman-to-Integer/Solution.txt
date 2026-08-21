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
            if (i==s.size()-1){
                ans += list[s[i]-'A'];
            }
            else if (list[s[i]- 'A'] < list[s[i+1]-'A']){
                ans -= list[s[i]-'A'];   
            }
            else ans += list[s[i]-'A'];
        }
        return ans;
    }
};