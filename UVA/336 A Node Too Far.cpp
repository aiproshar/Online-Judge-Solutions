//Simple BFS but wait there's more !
//Vertex ID not predefined, it can be 2,78,56 (usning array in inefficient + Out of bound issue may arise)
//STL::Map instead of vector array, iterate map values through iterator
//We dont even need to pre allocate max size because of map ! (Yeah HASH TABLE !!)
//Iterate->first to get the count of total elemets for Initialization of intermediate maps in BFS
//BFS but good STL practice


#include <bits/stdc++.h>
using namespace std;
#define IO  ios_base::sync_with_stdio(0);cin.tie(0);
#define READ freopen("in.txt", "r", stdin)
#define WRITE freopen("out.txt", "w", stdout)

//-------------------------------------------------------------------------
int Case = 1;
class Graph
{
public:
    map<int, vector<int>> E;
    inline void insert_edge(int x, int y)
    {
        E[x].push_back(y);
        E[y].push_back(x);
    }
};

int network_traverse(Graph &G, int source, int TTL)
{
    map<int, int> travel_cost;
    map<int, bool> visited;
    for (auto it = G.E.begin(); it != G.E.end(); it++)
    {
        travel_cost[it->first] = -1;
        visited[it->first] = false;
    }

    queue<int> Q;
    Q.push(source);
    visited[source] = true;
    travel_cost[source] = TTL;
    while (Q.size())
    {
        int Current_Node = Q.front();
        Q.pop();
        for (auto it = G.E[Current_Node].begin(); it !=  G.E[Current_Node].end(); it++)
        {
            if (!visited[*it])
            {
                travel_cost[*it] = travel_cost[Current_Node] - 1;
                visited[*it] = true;
                Q.push(*it);
            }
        }
    }
    int unreachable = 0;
    for(auto it = travel_cost.begin(); it != travel_cost.end(); it++)
    {
        if (it->second < 0) unreachable ++;
    }
    return unreachable;
}
int main()
{
    READ;
    WRITE;
    //IO
    while (1)
    {
        int e;
        cin >> e;
        if (!e) break;
        Graph G;
        while (e--)
        {
            int u, v;
            cin >> u >> v;
            G.insert_edge(u, v);
        }
        while (1)
        {
            int source, TTL;
            cin >> source >> TTL;
            if (!source && !TTL) break;
            int unreachable = network_traverse(G, source, TTL);
            cout << "Case " << Case++ << ": " << unreachable << " nodes not reachable from node " << source << " with TTL = " << TTL << "." << endl;
        }
    }
    return 0;
}