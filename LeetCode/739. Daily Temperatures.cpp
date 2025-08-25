// Crazy logic, no idea !
// I kept track of all the temparatures seen in the future (that was iterating
// backwards)
//  So at day==i, mp[temp] gives you future temp for that day or 0
// so at day i if its 42, we search for 43,44,45.....100 in the future days
//  The closest day we get with a large tem, that our guy

// time: O(n) + O(100) -> O(n), space: O(100) -> O(1)

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {

        vector<int> mp(101, 0);

        vector<int> ans(temperatures.size(), 0);

        for (int i = temperatures.size() - 1; i >= 0; i--) {

            mp[temperatures[i]] = i;
            for (int check_tmp = temperatures[i] + 1; check_tmp <= 100;
                 check_tmp++) {

                if (mp[check_tmp] != 0) {
                    if (ans[i] == 0) {
                        ans[i] = mp[check_tmp] - i;
                    } else {
                        ans[i] = min(ans[i], mp[check_tmp] - i);
                    }
                }
            }
        }

        return ans;
    }
};

// Using decreasing monotonic stack
//  When we see a bigger value that the stack.top(), we start pooping
//  That also means we can keep poping all the values until bigger value
// All the values we poped got a bigger value later, so that our day
//  Pair in stack, <temp, day_no>

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {

        vector<int> ans(temperatures.size(), 0);

        stack<pair<int, int>> st;

        st.push(make_pair(temperatures[0], 0));

        for (int i = 1; i < temperatures.size(); i++) {

            // Restoring decresing monotonic stack property
            while (!st.empty() && temperatures[i] > st.top().first) {
                auto day = st.top();
                st.pop();

                // We saw a day with higher temp infuture

                // The value we poped, which day minus our current day (with
                // higher temp)
                ans[day.second] = i - day.second;
            }

            st.push(make_pair(temperatures[i], i));
        }

        return ans;
    }
};
