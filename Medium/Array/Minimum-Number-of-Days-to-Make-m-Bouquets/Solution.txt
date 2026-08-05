class Solution {
public:
    bool possible(vector<int>& bloomDay, int m, int k, int days){
        int n = bloomDay.size();
        int count =0;
        int b = 0;
        for (int i =0; i<n; i++){
            if (days>= bloomDay[i]){
                count ++;
            }
            else {
                b += (count)/k;
                count = 0;
            }
        }
        b += (count)/k;
        return b>=m;
        
    }
    int minDays(vector<int>& bloomDay, int m, int k) {
        long long val = m *1LL*k*1LL;
        int n = bloomDay.size();
        if (val > n) return -1;
        int maxi = INT_MIN;
        int mini = INT_MAX;
        for (int i =0; i<n; i++){
            maxi = max(maxi, bloomDay[i]);
            mini = min(mini, bloomDay[i]);
        }
        int low = mini;
        int high = maxi;
        
        while (low <= high){
            int mid = (low +high)/2;
            if (possible(bloomDay,m,k,mid)){
                high = mid-1;
            }
            else low = mid+1;
        }
        return low;
        
    }
};