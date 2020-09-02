//Problem is just a simple MST, but i felt the implementation HARD
//Kruskal's because constrain are small, although complete graph
//Main problem is ID_tagging a node from 2d to 1d. And its 2D float, not integer
//+ The Graph is complete. So after ID tagging new inserted vertex we have to iterate through previous all vetices and create edges ( complete Graph)
//Pre_Hash to map 2D float into 1D integer (I felt this one Hardest, implemented string hashing which failed, then learned 2D key of STL:map)
//Unordered map doesn't work, you have to overload hash function based on custom key data type
//If you are not familiar with OOP best of luck scrolling down!

#include <bits/stdc++.h>
using namespace std;
#define READ freopen("in.txt", "r", stdin)
#define WRITE freopen("out.txt", "w", stdout)
//-------------------------------------------------------------------------
class Pre_Hash                     //Helper Pre_Hash method, 2D(float)->1D integer ID
{
    int obj_id = 0;
public:
    map<pair<double, double>, int> mp;
    void insert(double x, double y)
    {
        mp.insert(make_pair(make_pair(x,y), obj_id));
        obj_id++;
    }
    int retrive(double x, double y)
    {
        return mp[make_pair(x,y)];
    }
};

class Graph: public Pre_Hash        
{
public:
    priority_queue<pair<double, pair<int, int>>> PQ;    //Stores all edges in a heap, with source(pre_hashed) and destination(pre_hashed)
    vector<pair<double, double> > co_ordinates;         //We also need to save the original 2D co-ordinated to calculate weight while traversing
    void insert_edge(double x, double y)
    {
        Pre_Hash::insert(x,y);
        co_ordinates.push_back(make_pair(x,y));
        for(auto it = co_ordinates.begin(); it != co_ordinates.end(); it++)
        {
            double weight = sqrt(pow((x - it->first), 2) + pow((y - it->second), 2));
            if(weight == 0.0) continue;
            PQ.push(make_pair(weight * -1, make_pair(Pre_Hash::retrive(x,y), Pre_Hash::retrive(it->first, it->second))));
        }
    }
};

class Disjoint: public Pre_Hash         //Inherited pre_hash class as we wanted to work DSU independently as helper to MST
{
public:
    unordered_map<int, int> parent;     //sketchy buzzwordy people will say, hey whats unordered map ? Its just a map
                                        //How funny people uses std::map<> never knowing what RBT and HT is, and why HT is amortized O(1)
    void initialize_vertex(double x, double y)
    {
        Pre_Hash::insert(x, y);
        parent[Pre_Hash::retrive(x,y)] = Pre_Hash::retrive(x,y);
    }
    int find_representative(int x)
    {
        if (x == parent[x])
            return x;
        parent[x] = find_representative(parent[x]);
        return parent[x];
    }
    void Union(int a, int b)
    {
        parent[find_representative(a)] = parent[find_representative(b)];
    }
};

float MST(Graph &G, Disjoint &D, int n_V)
{
    int mst_size = 0;
    double cost = 0;
    while (mst_size < (n_V - 1))
    {
        auto top_edge = G.PQ.top();
        G.PQ.pop();
        int representative_u =  D.find_representative(top_edge.second.first);
        int representative_v = D.find_representative(top_edge.second.second);
        if(representative_u == representative_v)continue;
        D.Union(representative_u, representative_v);                           
        cost += top_edge.first * -1;
        mst_size++;
    }
    return cost;
}

int main()
{
    //READ;
    //WRITE;
    int test;
    cin >> test;
    bool print_nl = false;
    while (test--)
    {
        if(print_nl)
            cout << endl;
        else
            print_nl = true; 
        int n_V;
        cin >> n_V;
        double x, y;
        Graph G;
        Disjoint D;
        for(int i = 0; i < n_V; i++)
        {
            cin >> x >> y;
            G.insert_edge(x, y);
            D.initialize_vertex(x,y);
        }
        cout << fixed << setprecision(2) << MST(G, D, n_V) << endl;
    }
    return 0;
}
