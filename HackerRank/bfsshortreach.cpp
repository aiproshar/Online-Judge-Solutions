#include<bits/stdc++.h>
using namespace std;
//Just A BFS, Input Type : Edge Pair to Adjacency List 
//Sigle Source Shortest path Undirected uniform weight(or 1 as default)
int V; //No of vertex. Must be defined in main function and smaller than V_max
vector<int> Adj[1100]; //Adjacency list, [Vertex ID][Iteration over Adjacent nodes]
vector<bool> visited;
vector<int> parent;
vector<int> level;

void BFS(int source)
{
    visited.clear();
    parent.clear();
    level.clear();
    for(int i=0; i<V; i++) //initializing parent, depth (level) and visited list
    {
        visited.push_back(false);
        parent.push_back(-1);
        level.push_back(-1);
    }


    queue<int> Q;    //Pushing Source Node , 3 operation after pushing, update depth,parent and visited array
    Q.push(source);
    visited[source] = true;
    level[source] = 0;
    while(Q.size())
    {
        int Current_Node = Q.front();
        Q.pop();
        for(int i = 0; i < Adj[Current_Node].size(); i++)
        {
            if(!visited[Adj[Current_Node][i]])
            {
                visited[Adj[Current_Node][i]] = true;
                level[Adj[Current_Node][i]] = level[Current_Node]+6;
                parent[Adj[Current_Node][i]] = Current_Node;
                Q.push(Adj[Current_Node][i]);
            }
        }
    }
    for(int i = 0; i < V; i++)
        Adj[i].clear();
}

int main()
{
    int test;
    cin >> test;
    while(test--)
    {
        int E;
        cin >> V >> E;
        while(E--)
        {
            int u,v;
            cin >> u >> v;
            Adj[u-1].push_back(v-1);
            Adj[v-1].push_back(u-1);
        }
        int source;
        cin >> source;
        BFS(source-1);
        for(int i=0; i < V; i++)
        {
            if(i == source-1)
                continue;
            cout<<level[i]<<" ";
        }
        cout << endl;
    }
}