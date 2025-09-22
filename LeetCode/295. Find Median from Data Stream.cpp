
//Two heap solution, came up with this on first try. YaY
// We can split the array into two, we only need the two middle elements
// 1,2,3,4,5,6,7,8,9,10
//---------^^-----------
//If we put first half in a max heap, so we get to have 5 in top and a min heap, so we get 6 in top
//If new elememnt is Greater than max heap top, put it to min heap
//We also need to do heap resizing, that means, we add 11,12,13,14. Now 5,6 is not mid anymore
//When size of minHeap and maHEap differs more than one, we need to do resizing
//SO pop the top from max heap and insert it to minHeap and vice versa. Until size diff is 1
//For total odd numbers, maxHeap will be larger size split, so the medium is always max_heap top.

class MedianFinder {
    priority_queue<int> max_heap;
    priority_queue<int, vector<int>, greater<int>> min_heap;

public:
    MedianFinder() {
    }

    void addNum(int num) {
        if (max_heap.empty() || num <= max_heap.top()) {
            max_heap.emplace(num);
        } else {
            min_heap.emplace(num);
        }

        while ( max_heap.size() > 1 + min_heap.size()) {
            auto top = max_heap.top();
            max_heap.pop();
            min_heap.emplace(top);
        }
        while (min_heap.size() > max_heap.size()) {
            auto top = min_heap.top();
            min_heap.pop();
            max_heap.emplace(top);
        }
    }

    double findMedian() {
        if (min_heap.size() == max_heap.size()) {
            return (min_heap.top() + max_heap.top()) / 2.00;
        } else {
            return max_heap.top();
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */