class Point{
    int x;
    int y;
    double distance;
public:
    Point(int x, int y){
        this->x = x;
        this->y = y;
        this->distance = sqrt(x*x + y*y);
    }
    vector<int> coordinates() const{
        return {x,y};
    }
    //MaxHeap, for minK elemenets, we need max heap
    //For K max elements, we need minHeap
    friend bool operator < (const Point& p1, const Point& p2) {
        return p1.distance < p2.distance;
    }
};

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        priority_queue<Point>pq;

        for(const auto& point: points){
            pq.emplace(point[0], point[1]);
            if(pq.size() > k)pq.pop();
        }
        
        vector<vector<int>> ans;

        while(!pq.empty()){
            ans.emplace_back(pq.top().coordinates());
            pq.pop();
        }
        return ans;
    }
};