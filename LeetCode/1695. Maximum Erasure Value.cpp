class Solution {
private:


    //Separate modular function
    //One to check if our subarray is valid or not
    //O(n)
    static bool checkValidity(const unordered_map<int, int>&isPresent) {
        for (const auto &pair: isPresent) {
            if (pair.second > 1) {
                return false;
            }
        }
        return true;
    }

    //calculate substring sum
    //O(n)
    static int calculateSubstrSum(const vector<int>&nums, int startPos, int endPos) {
        int _sum = 0;
        for (int it = startPos; it <= endPos; it++) {
            _sum += nums.at(it);
        }
        return _sum;
    }
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_map<int, int> _isPresent;
        if (size(nums) == 1) {
            return nums[0];
        }
        int _maxSum = nums.at(0);
        int startPos = 0;
        int endPos = 0;
        _isPresent[nums[0]]++;
        while (endPos < size(nums)) {
            //O(n)
            if (endPos + 1 == size(nums)) {
                break;
            }
            //Assuming we are stable state
            endPos++;
            _isPresent[nums[endPos]]++;;
            if (checkValidity(_isPresent)) {
                 _maxSum =  max(_maxSum, calculateSubstrSum(nums, startPos, endPos));
            } else {
                // We are in unStable state
                //Lets get to stable state
                while (startPos < endPos) {
                    _isPresent[nums[startPos]]--;
                    startPos++;
                    if (checkValidity(_isPresent) || startPos == endPos) {
                        //We are in stable state, lets break
                        break;
                    }
                }
            }
        }
        return _maxSum;
    }
    //O(n) * (O(n+n))
    //O(n^2) -> This is not optimized
};



class Solution {
    private:

        //We dont need to store All the frequency
        //Upon finding one duplicate we start shrinking upon that duplicate is removed, O(1)
        //Lets use precomputed sum, when we modify subArray we modify the sum in O(1)
        public: int maximumUniqueSubarray(vector < int > & nums) {
            unordered_map < int, int > _isPresent;
            if (size(nums) == 1) {
                return nums[0];
            }
            int _maxSum = nums[0];
            int _sum = nums[0];
            int startPos = 0;
            int endPos = 0;
            _isPresent[nums[0]]++;
            while (endPos < size(nums)) {
                if (endPos + 1 == size(nums)) {
                    break;
                }
                //O(n)
                while (true) {
                    if (endPos + 1 == size(nums)) {
                        break;
                    }
                    endPos++;
                    _isPresent[nums[endPos]]++;
                    //You may figure why we updating the sum, we already moved our pointer, although the subarr is now invalid
                    //It will become valid by shrinking in the next while loop, and we will miss the value in the sum if we dont add now
                    // Ohh debugger thanks a lot,
                    // As long as we are not updating the max, we should calculate sum as necessary
                    _sum += nums[endPos];
                    if (_isPresent[nums[endPos]] == 2) {
                        break;

                    } else {
                        _maxSum = max(_maxSum, _sum);
                    }
                }
                while (startPos < endPos) {
                    _isPresent[nums[startPos]]--;
                    _sum -= nums[startPos];
                    startPos++;
                    if (_isPresent[nums[startPos - 1]] == 1) {
                        break;
                    }
                }
            }
            return _maxSum;
        }
};