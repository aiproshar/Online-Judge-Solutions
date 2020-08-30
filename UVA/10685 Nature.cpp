//Basic DSU
//Find largest Subgraph and its size
//Ref : UVA - 459 : Graph Connectivity
#include <bits/stdc++.h>
using namespace std;
#define IO      ios_base::sync_with_stdio(0); cin.tie(0);
#define READ freopen("in.txt", "r", stdin)
#define WRITE freopen("out.txt", "w", stdout)
//-------------------------------------------------------------------------

class Disjoint
{
    public:
    map<string, string> representative;                 //track of representative nodes
    map<string, int> component_n;                       //Helper Map to count maximum sub-graph size

    void insert(string name)
    {
        representative[name] = name;
        component_n[name] = 0;                          //Initializing all probable rep nodes as 0
    }
    string find_representative(string s)
    {
        if(representative[s] == s) return s;
        representative[s] = find_representative(representative[s]);
        return representative[s];
    }
    void Union(string a, string b)
    {
        representative[find_representative(a)] = find_representative(b);
    }
    int max_subgroup_count()
    {
        int max_count = 0;
        for(auto it = representative.begin(); it != representative.end(); it++)
        {
            string current_representative = find_representative(it->second); //Removing previous bias, a->b->c and then c->a but rep(b) and rep(a) still remains c, but rep(c) is updated
            component_n[current_representative]++;
            if(component_n[current_representative] > max_count) max_count = component_n[current_representative];   //Counting and updating the max as we build up actual final rep info
        }
        return max_count;
    }

};


int main()
{
    READ;
    WRITE;
    IO;
    while(1)
    {
        int c, r;
        cin >> c >>r;
        if (!c && !r) return 0;
        Disjoint D;
        while(c--)
        {
            string name;
            cin >> name;
            D.insert(name);
        }
        while(r--)
        {
            string c1, c2;
            cin >> c1 >> c2;
            D.Union(c1,c2);
        }
        cout << D.max_subgroup_count() << endl;
    }
    
}