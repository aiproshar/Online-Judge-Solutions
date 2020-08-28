//The stupidest Problem i have seen and wasted time
//Just a simple BFS, but i got 4 times presentation error
//Teaches you how to format output more rather than algorithm
//Ow yeah no its not about not adding new line in end, its about right format (%2d)
//Taking Input, thats another drama with EOF
//Yeah now we know why CF/LC community hates UVA

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

int BFS(Graph &G, int source, int destination)
{
    map<int, int> level;
    for (auto it = G.E.begin(); it != G.E.end(); it++)
    {
        level[it->first] = -1;
    }

    queue<int> Q;
    Q.push(source);
    level[source] = 0;
    while (Q.size())
    {
        int Current_Node = Q.front();
        Q.pop();
        for (auto it = G.E[Current_Node].begin(); it !=  G.E[Current_Node].end(); it++)
        {
            if (level[*it] == -1)
            {
                level[*it] = level[Current_Node] + 1;
                Q.push(*it);
            }
        }
    }
    
    return level[destination];
}
int main()
{
    //READ;
    //WRITE;
    IO
    int test = 1;   
    while(1)
    {
        Graph G;
        for(int i = 1; i < 20; i++)
        {
            int u, v;
            int exit = scanf("%d", &u);
            if (exit == EOF) return 0;
            
            while(u--)
            {
                scanf("%d", &v);
                G.insert_edge(i,v);
            }
            
        }
        int explore_total;
        scanf("%d", &explore_total);
        printf("Test Set #%d\n",test++); 
        while(explore_total--)
        {
            int source, destination;
            scanf("%d %d", &source, &destination);
            int country_to_conquer = BFS(G, source, destination);
            printf("%2d to %2d: %d\n",source, destination, country_to_conquer);
        }
        printf("\n");
    }
    return 0;
}