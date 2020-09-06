//Took ~3 Hours to solve, and another 6 hours to debug (TLE)
//It was stupid MAX heap, i used negative values to make a MAX-HEAP behave like a min-heap but got TLE because of this
//6 Hours -> changed to cstdio, global allocation, dynamic reallocation, register int, removed bits, all short of nonsense and TLE (10+ TLE FML)
//Overloaded Default Constructor (Stupid 700ms runtime, additional cycle for negation and negative compare added cycles and got TLE)
//The Problem is pretty Hard, Dynamic Exploration
//We have the choice to explore selected candidate with/without new proposed edges
//This is kinda difficult to explain in text, every state can go to d states (selected from proposed total)
//A proposed Edge can contribute to reduce distance, but what if we dont select that
//Thats why distance matrix is 2d (caching all the possibilities)
//If we find better path later, we update cache
//An Edge might remain undiscovered in distance array for [0],[1],... but might get discovered later
//If the distance array for destination using any number of allowed array is INF, there is no path
//Its all about state, we can have one candidate node more than once in queue with different states :) 

#define READ                freopen("in.txt","r",stdin)
#define WRITE               freopen("out.txt","w",stdout)
#define IO                  ios_base::sync_with_stdio(false);cin.tie(null);
#define pii                 pair<int, int>
#define piii                pair< int, pii >

#define V_MAX   10001
#define INF     1e9

#include<bits/stdc++.h>
using namespace std;

class Graph
{
public:
    vector<pair<int,int> > cost[V_MAX];
    int V;
public:
    Graph(int V)
        :V(V)
    {
    }
    void insert_edge(int u, int v, int weight)
    {
        cost[u].push_back(make_pair(weight*-1, v));
    }
};
 
int Dijkstra(Graph &G, Graph &P, int source, int p_max)
{
    vector< vector<int> > distance{V_MAX, vector<int>(p_max+1, INF)};
 
    priority_queue< piii, vector<piii>, greater<piii> > PQ;        //Stupid 6 hours eaten by this line
    PQ.push(make_pair(0, make_pair(source, 0)));
    distance[source][0] = 0;
 
    while(PQ.size())
    {
        auto node = PQ.top();
        PQ.pop();
        int u = node.second.first;
        int p_cost = node.second.second;
        for(auto it = G.cost[u].begin(); it != G.cost[u].end(); it++)
        {
            if( (distance[u][p_cost] + it->first * -1) < distance[it->second][p_cost])
            {
                distance[it->second][p_cost] = distance[u][p_cost] + it->first * -1;
                PQ.push(make_pair(distance[it->second][p_cost], make_pair(it->second, p_cost)));
            }
        }
 
        for(auto it = P.cost[u].begin(); it != P.cost[u].end(); it++)
        {
            if( ((distance[u][p_cost] + it->first * -1) < distance[it->second][p_cost+1]) && p_cost + 1 <= p_max)    //Magic Happens Here, Dynamic State :) 
            {
                distance[it->second][p_cost+1] = distance[u][p_cost] + it->first * -1;
                PQ.push(make_pair(distance[it->second][p_cost+1], make_pair(it->second, p_cost+1)));
            }
        }
    }
    int dest_distance = INF;
    for(int i = 0; i <= p_max; i++)
    {
        if(distance[G.V - 1][i] < dest_distance)
            dest_distance = distance[G.V - 1][i];
    }
    if(dest_distance == INF)
        return -1;
    else
        return dest_distance;  
}
 
int main()
{
    //READ;
    //WRITE;
    IO;
    int test;
    cin >> test;
    for(int i = 1; i <= test; i++)
    {
        int v, e, k, d;
        cin >> v >> e >> k >>d;
        Graph G(v);
        while(e--)
        {
            int u, v, weight;
            cin >> u >> v >> weight;
            G.insert_edge(u, v, weight);
        }
        Graph P(v);
        while(k--)
        {
            int u, v, weight;
            cin >> u >> v >> weight;
            P.insert_edge(u, v, weight);
        }
        int distance = Dijkstra(G, P, 0, d);
        if(distance == -1)
            cout << "Case " << i << ": " << "Impossible" << endl;
        else
            cout << "Case " << i << ": " << distance << endl;
    }
}