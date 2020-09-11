//Basic Bellman Ford
//Negative cycle Detection
//Directed Graph
//In undirected graph, any single negative edge will make a negative cycle (hopping -ve edge)
//If there is no cycle, all nodes relaxation saturates in n-1 runs
//proof in MIT 6006 OCW : https://www.youtube.com/watch?v=ozsuci5pIso
//All edges(E) try to relax every vertex(V), O(VE), for complete graph O(V^3)
//Bellman ford is essentially a non-greedy version of dijkstra, if dijkstra finds a -ve cycle
//it might remain busy with that the whole time, so we cant be sure when relaxation saturates
//Bellman being non-greedy, it saturates. If saturation doesn't stops, then there's a -ve cycle
//Bellman does same thing like dijkstra (worst complexity), but it can detect when something is wrong (-ve cycle)
#define READ    freopen("in.txt", "r", stdin)
#define WRITE   freopen("out.txt", "w", stdout)
#define IO      ios_base::sync_with_stdio(false);cin.tie(nullptr);
#define V_MAX   1001
#define INF     1e9
#include <bits/stdc++.h>
using namespace std;

class Graph
{
public:
    vector<pair<int, int>> cost[V_MAX];
    int V;

public:
    Graph(int V)
        : V(V)
    {
    }
    void insert_edge(int u, int v, int weight)
    {
        cost[u].push_back(make_pair(weight, v));
    }
};

bool Bellman_Ford(const Graph &G, int source = 0)
{
    vector<int> distance(G.V, -1);

    distance[source] = 0;
    int n = G.V - 1;

    while (n--)            //Path Relaxation
    {
        for (int i = 0; i < G.V; i++)
        {
            for (int j = 0; j < G.cost[i].size(); j++)
            {
                int u = i;
                int v = G.cost[i][j].second;
                int w = G.cost[i][j].first;
                if (distance[u] + w < distance[v])
                {
                    distance[v] = distance[u] + w;
                }
            }
        }
    }
    for (int i = 0; i < G.V; i++)           //If we can relax further, there at least a -ve cycle exist
    {
        for (int j = 0; j < G.cost[i].size(); j++)
        {
            int u = i;
            int v = G.cost[i][j].second;
            int w = G.cost[i][j].first;
            if (distance[u] + w < distance[v])
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    //READ;
    //WRITE;
    IO;
    int test;
    cin >> test;
    while(test--)
    {
        int v, e;
        cin >> v >> e;
        int x, y, weight;
        Graph G(v);
        while(e--)
        {
            cin >> x >> y >> weight;
            G.insert_edge(x, y, weight);
        }
        bool neg_cycle = Bellman_Ford(G);
        if(neg_cycle)
            cout << "possible"<<endl;
        else
            cout << "not possible"<<endl;        
    }
}
