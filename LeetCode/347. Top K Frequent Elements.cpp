

class elements {
public:
    int key;
    int value;
    elements(const int &key, const int &value) {
        this->key = key;
        this->value = value;
    }
    friend bool operator <(const elements& a, const elements& b) {
        return a.value < b.value;
    }
};



class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //compress the stream, so we have unique values and their counts
        //Standard unordered map to increment all the calues

        unordered_map<int, int> mp;
        priority_queue<elements> pq;
        mp.reserve(100000);

        //O(n)
        //Lets build the frequency count map, so key is element and value is freq
        for(const auto& it: nums){
            mp[it]++ ;
        }

        //nlgn
        //Lets build the heap, key is number, value is frequency of that number
        //The main magic is less than operator overload, which is doing everything
        //Max Heap so in top we get key with most freq

        for(const auto& it: mp){
            pq.push(elements{it.first, it.second});
        }


        //nlgn
        //When we pop, as key we get the number with most frequency
        vector<int> ans;
        while(k--){
            ans.emplace_back(pq.top().key);
            pq.pop();
        }

        return ans;
    }
}; // O(n + nlogn) => O(n)




//------------------------ FollowUP--------

//More optimized solution
//For K max elements in a heap, we need to initialize a min_heap with size k, then push one elem and pop immedieatly.
//By doing this, we can gurantee removal of smallest item in K+1 heap, we always end up getting a heap with K size, top
// K max elemems in the stream


class elements {
public:
    int key;
    int value;
    elements(const int &key, const int &value) {
        this->key = key;
        this->value = value;
    }
    friend bool operator <(const elements& a, const elements& b) {

        // Overloading the operator, now we gat min heap
        return a.value > b.value;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //compress the stream, so we have unique values and their counts
        //Standard unordered map to increment all the calues

        unordered_map<int, int> mp;
        priority_queue<elements> pq;
        mp.reserve(100000);

        //O(n)
        //Lets build the frequency count map, so key is element and value is freq
        for(const auto& it: nums){
            mp[it]++ ;
        }

        //
        //Lets build the heap, key is number, value is frequency of that number
        //The main magic is less than operator overload, which is doing everything
        //Min heap, gurantess that smaller values kicked out

        for(const auto& it: mp){
            pq.push(elements{it.first, it.second});
            if (pq.size() > k) pq.pop();
        }


        //nlgn
        //When we pop, as key we get the number with most frequency
        vector<int> ans;
        while(k--){
            ans.emplace_back(pq.top().key);
            pq.pop();
        }

        return ans;
    }
};