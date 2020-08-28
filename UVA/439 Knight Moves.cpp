//BFS in 2D grid
//Easy problem, but outcome is kinda research topic
//Converted 2D grid into 1D representation (1,2,3,..9,10,..64)
//2 helper methods
//Max value 6 so we can go from any position in board to any other in max 6 moves
//We can run statistical analysis to find the percent of distance, wr to 2D distance bla bla bla (data science)
//64 * 64 * 64 -> total problem + solution Space
//BFS really shines finding global optimum states in linear complexity

#include <bits/stdc++.h>
using namespace std;
#define IO  ios_base::sync_with_stdio(0);cin.tie(0);
#define READ freopen("in.txt", "r", stdin)
#define WRITE freopen("out.txt", "w", stdout)

//-------------------------------------------------------------------------
inline bool move_validity(int x, int y)
{
    if( (x < 9 && x > 0) && (y < 9 && y > 0)) return true;
    return false;
}
inline int one_D(int row, int column)
{
    return row * 8 + column - 8;
}
int Case = 1;
class Graph
{
public:
    vector<int>E[65]; //2D Grid, Row_Column Co-ordinate to identify a node
    Graph() //Initializing and connecting all nodes based on Knight's move
    {
        for (int i = 1; i <= 8; i++)
        {
            for(int j = 1; j <= 8; j++)
            {
                if(move_validity(i+2, j-1))
                {
                    E[one_D(i,j)].push_back(one_D(i+2,j-1));
                    E[one_D(i+2,j-1)].push_back(one_D(i,j));
                }
                if(move_validity(i+2, j+1))
                {
                    E[one_D(i,j)].push_back(one_D(i+2,j+1));
                    E[one_D(i+2,j+1)].push_back(one_D(i,j));
                }
                if(move_validity(i-2, j-1))
                {
                    E[one_D(i,j)].push_back(one_D(i-2,j-1));
                    E[one_D(i-2,j-1)].push_back(one_D(i,j));
                }
                if(move_validity(i-2, j+1))
                {
                    E[one_D(i,j)].push_back(one_D(i-2,j+1));
                    E[one_D(i-2,j+1)].push_back(one_D(i,j));
                }
                if(move_validity(i+1, j-2))
                {
                    E[one_D(i,j)].push_back(one_D(i+1,j-2));
                    E[one_D(i+1,j-2)].push_back(one_D(i,j));
                }
                if(move_validity(i-1, j-2))
                {
                    E[one_D(i,j)].push_back(one_D(i-1,j-2));
                    E[one_D(i-1,j-2)].push_back(one_D(i,j));
                }
                if(move_validity(i+1, j+2))
                {
                    E[one_D(i,j)].push_back(one_D(i+1,j+2));
                    E[one_D(i+1,j+2)].push_back(one_D(i,j));
                }
                if(move_validity(i-1, j+2))
                {
                    E[one_D(i,j)].push_back(one_D(i-1,j+2));
                    E[one_D(i-1,j+2)].push_back(one_D(i,j));
                }
                //Please dont vomit, i love ctrl+v idk why! 
            }
        }
    }
};


int BFS(Graph &G, int source, int destination)
{
    vector<int>level;
    for(int i = 0; i < 65; i++)
    {
        level.push_back(-1);
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
    READ;
    WRITE;
    IO 
    Graph G; //All Graph Structure Same, initialing one single graph for all test case (difference between src and dst) 
    string src, dst;
    while(cin >> src >> dst)
    {
        int r1, r2, c1,c2;
        c1 = src[0] - 'a' + 1;
        r1 = src[1] - '1' + 1;
        c2 = dst[0] - 'a' + 1;
        r2 = dst[1] - '1' + 1;
        int steps = BFS(G, one_D(r1, c1), one_D(r2, c2));
        printf("To get from %c%d to %c%d takes %d knight moves.\n", src[0], r1, dst[0], r2, steps);
    }
    return 0;
}

//To get from f6 to f6 takes 0 knight moves.