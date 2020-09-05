//2nd Best Shortest Path in Undirected Graph
//May take alternate route/ loop through nodes with lowest cost
//Just keep separate second best distance
//If path relaxion fails, it might be second best
//Check for path relaxation in second_best route
//So compare it with previously stored second best (and also check it is not equal to best distance to that node (i was stuck debugging here, again pretty-printers saved:) )
//In undirected graph, it always takes a loop (hopping) around shortest edge (u,v, 1 -> hopes u and v , making second best only 1 unit larger than best path)
//To find real alternate best path, we need to use directed graph (no hopping)
//5000 nodes, 10^5 max weight, so we set INF more than 5000*10^5 (Codeforces Problem: https://codeforces.com/problemset/problem/20/C Test Case 31 error INF small)
#define READ                freopen("in.txt","r",stdin)
#define WRITE               freopen("out.txt","w",stdout)
#define IO                  ios_base::sync_with_stdio(0);cin.tie(0);
#define V_MAX   5010
#define INF     2e9

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
        cost[v].push_back(make_pair(weight*-1, u));
    }
};

int Dijkstra(Graph &G, int source)
{
    vector<int> parent(G.V, -1);
    vector<int> distance(G.V, INF);
    vector<int>  second_best(G.V, INF);
    priority_queue<pair<int,int> > PQ;
    PQ.push(make_pair(0, source));
    distance[source] = 0;
    while(PQ.size())
    {
        auto u = PQ.top().second;
        PQ.pop(); 
        for(auto it = G.cost[u].begin(); it != G.cost[u].end(); it++)
        {
            if( (distance[u] + it->first * -1) < distance[it->second] )
            {
                distance[it->second] = distance[u] + it->first * -1;
                parent[it->second] = u;
                PQ.push(*it);
            }
            //Probably the most important line of code is the line below
            //Path relaxation condition for second best Path
            else if(((distance[u] + it->first * -1) < second_best[it->second]) && ((distance[u] + it->first * -1) > distance[it->second]))
            {
                second_best[it->second] = distance[u] + it->first * -1;
                PQ.push(*it);
            }
        }
    }
    int back_track = G.V - 1;
    int second_best_penalty = INF;
    //Traverse from destination to source, check for shortest vs second_shortest  per node and pick the smallest difference (penalty)
    while(1)
    {
        if( (second_best[back_track] - distance[back_track]) < second_best_penalty)
        {
            second_best_penalty = second_best[back_track] - distance[back_track];
        }
        back_track = parent[back_track];
        if(back_track == -1)
            break;
    }
    return distance[G.V - 1] + second_best_penalty;
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
        int v, e;
        cin >> v >> e;
        Graph G(v);
        while(e--)
        {
            int u, v, weight;
            cin >> u >> v >> weight;
            G.insert_edge(u-1, v-1, weight);
        }
        int second_best_cost = Dijkstra(G, 0);
        cout << "Case " << i << ": " << second_best_cost << endl; 
    }
}