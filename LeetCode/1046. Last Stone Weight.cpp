
//Just a max Heap
//Calculate the new weight after collision and push that on the Heap
//Handle corner case, if stones is 1, there cannot be any collision
//Time complexity: O(nlogn)
//space complexity: O(n)
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {

        if (stones.size() == 1)
            return stones[0];
        priority_queue<int> pq;

        for (const auto& stone : stones) {
            pq.emplace(stone);
        }

        while (pq.size() > 1) {
            auto first = pq.top();
            pq.pop();
            auto second = pq.top();
            pq.pop();

            pq.push(first - second);
        }

        return pq.top();
    }
};