//It might look like just a shortest path problem, but its more
//Yeah you can solve it with Dijkstra/ Floyd Warshall but i tried to solve using MST as Shafaet Bro's blog suggested
//MST prims because we need to start exploring from specific node (the final spanning tree might be same but we need to calculate stuff)
//Correctin : Maximum Spanning Tree so that our bottleneck weight is lowest
//Every edge in Priority Queue has three property, the source vertex of that edge(explored already), candidate vertex(will be explored if its top in heap)
//and the weight (max weight allowed). The priority Queue is sorted w.r to the weight
//Actual Bottleneck calculation is done while building MST (!Hey you, its Maximum Spanning Tree)
//After poping edge from candidate list, we update maximum_allowed cost for the destination_node of selected candidate edge
//If weight to get to destination vertex of selected edge is lower that bottleneck value to visit previous vertex, we set weight as bollleneck value as dest_vertex 
//If not then just set the bollteneck value from previous edge. Return bottleneck value of destination
//Memorization to calculate bottleneck of newly selected vertex in O(1)
//O(Vlg(E)) : We need to find (V-1) edged from E edges, Heap Access time : lg(E)
//http://www.shafaetsplanet.com/planetcoding/?p=692
#include <bits/stdc++.h>
using namespace std;
#define IO      ios_base::sync_with_stdio(0);cin.tie(0);
#define READ    freopen("in.txt", "r", stdin)
#define WRITE   freopen("out.txt", "w", stdout)
#define INF     20000
//-------------------------------------------------------------------------
class Graph
{
public:
    map<string, vector<pair<int, string>>> E;
    void insert_edge(string source, string destination, int weight)
    {
        E[source].push_back(make_pair(weight, destination));
        E[destination].push_back(make_pair(weight, source));
    }
};

int MST(Graph &G, string source, string destination) 
{
    map<string, bool> visited;                               //Visited_Vertex List
    map<string, int> maximum_allowed_weight;                //Bottleneck
    for (auto it = G.E.begin(); it != G.E.end(); it++)      //Initializing visited_Vertex List
    {
        visited[it->first] = false;
    }
    priority_queue<pair<int, pair<string, string>>> PQ;     //Priority Queue for pushing candidate edges
    PQ.push(make_pair(INF, make_pair(source, source)));
    maximum_allowed_weight[source] = INF;               
    //As we push the source in Priority Queue, we assume there is an imaginary node from source to source 
    //With a Wight of INF (we dont want this imaginary node to add bottleneck, do we ?)
    //More optimization is possible like haulting MST building when we select destination from candidate edged, i'm lazy to optimize that much :P 
    while (PQ.size())
    {
        auto current_node = PQ.top();
        PQ.pop();
        int weight = current_node.first;
        string edge_source = current_node.second.first;
        string edge_destination = current_node.second.second;
        
        if (visited[edge_destination])
        {
            continue;
        }
        visited[edge_destination] = true;
        maximum_allowed_weight[edge_destination] = min(weight, maximum_allowed_weight[edge_source]);
        for (auto it = G.E[edge_destination].begin(); it != G.E[edge_destination].end(); it++)
        {
            if (!visited[it->second])
            {
                PQ.push(make_pair(it->first, make_pair(edge_destination, it->second)));        //Pushing Candidated edges with source_edge, dest_edge and weight
            }                                                                                  //Source, Destination as info to calculate further edge bottlenecks
        }
    }
    return maximum_allowed_weight[destination];
}
int main()
{
    READ;
    WRITE;
    bool newline = false;
    int scenario = 1;
    while(1)
    {
        if(newline) cout << endl;
        else newline = true; 
        int V, E;
        cin >> V >> E;
        if(!V && !E) return 0;
        Graph G;
        string src, dst;
        int weight;
        while(E--)
        {
            cin >> src >> dst >> weight;
            G.insert_edge(src, dst, weight);
        }
        cin >> src >> dst;
        int max_allowed = MST(G, src, dst);
        cout << "Scenario #" << scenario <<endl;
        cout << max_allowed << " tons" << endl;
        scenario++;
    }
}