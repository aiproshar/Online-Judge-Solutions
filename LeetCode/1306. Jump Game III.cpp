//Basic BFS
//Memoization to mark if a node is visited or not (yeah saves us from infinite loop too)
//First check if our jumps positions are valid or not, push the valid jump positions if they are not visited
//Oww - Check first for objective, our value in that index is 0 or not
//If we encounter any 0, break and return true, else false
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        vector<bool> visited(arr.size(), false);
        visited[start] = true;
        queue<int>Q;
        Q.push(start);
        while(!Q.empty())
        {
            int top = Q.front();
            Q.pop();
            if(arr[top] == 0)
                return true;
            if(top + arr[top] < arr.size() && !visited[top + arr[top]])
            {
                visited[top + arr[top]] = true;
                Q.push(top + arr[top]);
            }
            if(top - arr[top] >= 0 && !visited[top - arr[top]])
            {
                visited[top - arr[top]] = true;
                Q.push(top - arr[top]);
            }
        }
        return false;
    }
};