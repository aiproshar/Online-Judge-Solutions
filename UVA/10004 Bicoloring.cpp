//Easy BFS, insted of adding cost, change state
//If state matches with ancestor, it confirms bicolor not possible

#include <bits/stdc++.h>
using namespace std;
#define IO                  ios_base::sync_with_stdio(0);cin.tie(0);
#define READ                freopen("in.txt","r",stdin)
#define WRITE               freopen("out.txt","w",stdout)
//-------------------------------------------------------------------------

#define V_max 210 

class Graph
{
public:
    int v;
    vector<int> E[V_max];
    Graph(int v)
    {
        vector<int> E[V_max];
        Graph::v = v;
    }
    inline void insert_edge(int x, int y)
    {
        E[x].push_back(y);
        E[y].push_back(x);
    }
};

bool bicolor(Graph &G, int source)
{
    vector<int> color;
    for (int i = 0; i < G.v; i++)
    {
        color.push_back(-1);
    }

    queue<int> Q;
    Q.push(source);
    color[source] = 0;
    while (Q.size())
    {
        int Current_Node = Q.front();
        Q.pop();
        for (int i = 0; i < G.E[Current_Node].size(); i++)
        {
            if (color[G.E[Current_Node][i]] == color[Current_Node])
            {
                return false;
            }
            if (color[G.E[Current_Node][i]] == -1)
            {
                color[G.E[Current_Node][i]] = !(color[Current_Node]);
                Q.push(G.E[Current_Node][i]);
            }
        }
    }
    return true;
}
int main()
{
    //READ
    //WRITE
    IO
    while (1)
    {
        int n;
        cin >> n;
        if (!n) return 0;

        Graph G(n);
        int e;
        cin >> e;
        int u, v;
        while (e--)
        {
            cin >> u >> v;
            G.insert_edge(u, v);
        }
        int total_true = 0;
        for (int i = 0; i < n; i++)
        {
            auto ans = bicolor(G, i);
            if (ans) total_true++;
        }
        if (total_true == n)
            cout << "BICOLORABLE." << endl;
        else
            cout << "NOT BICOLORABLE." << endl;
    }
}
