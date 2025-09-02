// Solution bruteforce
// Lest start with speed to eat biggest pile in an hour
// Then we can start decrease the speed until out total_time > hour
// O(n*max_pile_size)

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int max_banana = 0;
        for(const auto& it: piles){
            max_banana = max(max_banana, it);
        }

        for(int current_speed = max_banana; current_speed > 0; current_speed--){
            int total_time = 0;
            for(const auto& pile:piles){
                total_time += ceil((double)pile/(double)current_speed);
            }
            if(total_time > h){
                return current_speed + 1;
            }
        }

        return -1;
    }
};



// Solution Binary Search
//Why we check from speed 1, 2, 3, ... max_pile, cause the hours_taken is linear relation with speed
//We can find our speed faster, lest start with medium speed
//If medium speed takes time less then h, its good, we have an answer, but we might have better one (closer to h)
//If not, lest get rid of first half (those are more slower speed anyways)


class Solution {

private:
    long long unsigned calculateHours(const vector<int>& piles, int speed){
        long long unsigned int total_time = 0;
        for(const auto& pile:piles){
            total_time += ceil((double)pile/(double)speed);
        }

        return total_time;
    }
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int max_banana = 0;
        for(const auto& it: piles){
            max_banana = max(max_banana, it);
        }

        int ans = 0;
        for(int lo = 1, hi = max_banana; lo <= hi; ){
            int mid = lo + (hi - lo)/2;

            auto mid_time = calculateHours(piles, mid);

            if(mid_time <= h){
                ans = mid;
                hi = mid-1;
            }else{
                lo = mid+1;
            }
        }
        return ans;
    }
};