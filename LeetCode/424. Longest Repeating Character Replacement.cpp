class Solution {

    // We are using array instead of HashMap, because of data localaization
    // Data stays warm in cache, O although its 26 iteration, its superfast
private:
    int searchMax(const vector<uint32_t>& cnt) {
        int mx = 0;

        for (size_t i = 0; i < 26; i++) {
            if (cnt[i] > mx) {
                mx = cnt[i];
            }
        }

        return mx;
    }

public:
    int characterReplacement(string s, int k) {
        vector<uint32_t> cnt(26, 0);

        int global_max = 0;

        // Below is the general template for sliding window
        /*
                for (int right = 0; right < n; right++) {
                    // Add element at right to window
                    //Change necessary state (ie. sum of sliding window update)
                    // Or char occurance count++
                    //We do the operation and then check if its invalid because of growing

                    while (window_invalid) {
                        //Time to shrink until valid again

                        //Remove element from window, do other state change we did before entering the while loop
                        //Example sum -= nums[left]
                        //Decrease Frequency
                        left++;
                    }

                    // Update result
                }
        */
        for (int left = 0, right = 0; right < s.size(); right++) {
            cnt[s[right] - 'A']++;

            while ((right - left + 1) > searchMax(cnt) + k) {
                cnt[s[left] - 'A']--;
                left++;
            }

            global_max = max(global_max, right - left + 1);
        }

        return global_max;
    }
};