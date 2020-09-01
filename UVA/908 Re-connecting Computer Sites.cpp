//We just need to find the MST buildup cost
//Adjacency Matrix, Adjacency List Information is Redundant, So just use a Heap to store weight, (src, dst)
//We just need to find (V-1) edges for the MST (A MST with V vertex has V-1 edges, any more than that will introduce a cycle)
//When our Spanning Tree reaches size of (V-1) edges, we stop searching for edges
//Complexity :  O(Elg(E)) 
//Simpler Data Structure and Operation than prims, but slightly worse complexity
//Sparse Graph : Kruskals        Densly Connected Graph : Prims
#include <bits/stdc++.h>
using namespace std;
#define IO      ios_base::sync_with_stdio(0); cin.tie(0);
#define READ    freopen("in.txt", "r", stdin)
#define WRITE   freopen("out.txt", "w", stdout)
//-------------------------------------------------------------------------

class Graph_modified
{
public:
    priority_queue<pair<int, pair<int, int>>> PQ;
    void insert_edge(int source, int destination, int weight)
    {
        PQ.push(make_pair(weight * -1, make_pair(source, destination)));
    }
};
class Disjoint
{
public:
    vector<int> parent;
    Disjoint(int total_vertex)
    {
        for (int i = 0; i <= total_vertex; i++)
        {
            parent.push_back(i);
        }
    }
    int find_representative(int x)
    {
        if (x == parent[x]) return x;
        parent[x] = find_representative(parent[x]);
        return parent[x];
    }
    void Union(int a, int b)
    {
        parent[find_representative(a)] = parent[find_representative(b)];
    }
};
int MST(Graph_modified &G, Disjoint &D, int vertex_no)
{
    int mst_size = 0;
    int cost = 0;
    while (mst_size < (vertex_no - 1))
    {
        auto top_edge = G.PQ.top();
        G.PQ.pop();
        int r1 = D.find_representative(top_edge.second.first);
        int r2 = D.find_representative(top_edge.second.second);
        if (r1 == r2) continue;
        D.Union(r1, r2);
        cost += top_edge.first * -1;
        mst_size++;
    }
    return cost;
}
int main()
{
    READ;
    WRITE;
    IO;
    int total_vertex;
    bool print_nl = false;
    while (cin >> total_vertex)
    {
        if(print_nl) cout << endl;
        else print_nl = true;
        int current_mst_weight = 0;
        int u, v, w;
        for (int i = 1; i < total_vertex; i++)
        {
            cin >> u >> v >> w;
            current_mst_weight += w;
        }
        cout << current_mst_weight << endl;
        int new_lines;
        cin >> new_lines;
        Graph_modified G;
        Disjoint D(total_vertex);
        while (new_lines--)
        {
            cin >> u >> v >> w;
            G.insert_edge(u, v, w);
        }
        int all_lines;
        cin >> all_lines;
        while (all_lines--)
        {
            cin >> u >> v >> w;
            G.insert_edge(u, v, w);
        }
        int cost = MST(G, D, total_vertex);
        cout << cost << endl;
    }
    return 0;
}