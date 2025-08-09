
// We

class Solution {
public:
    int trap(vector<int>& height) {

        vector<int> lt(height.size(), 0);
        vector<int> rt(height.size(), 0);

        for (int i = 0; i + 1 < height.size(); i++) {
            lt[i + 1] = max(lt[i], height[i]);
        }

        for (int i = height.size() - 1; i > 0; i--) {
            rt[i - 1] = max(rt[i], height[i]);
        }

        int tap_total = 0;

        for (int i = 1; i + 1 < height.size(); i++) {
            tap_total += (min(lt[i], rt[i]) - height[i]) > 0
                             ? (min(lt[i], rt[i]) - height[i])
                             : 0;
        }

        return tap_total;
    }
};