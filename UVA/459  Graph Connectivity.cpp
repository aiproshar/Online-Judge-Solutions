//Sub Graph Compression using DSU (Disjoint Set Union)
//Meesed up some implementation details, was stuck debugging idk how many hours
//Implementation Details : https://codeforces.com/blog/entry/19525 http://www.shafaetsplanet.com/?p=763 
//Problem not that hard or interesting, but sub-graph compression maybe a key component with other algorithms (SCC compression)
#include <bits/stdc++.h>
using namespace std;
#define IO      ios_base::sync_with_stdio(0); cin.tie(0);
#define READ    freopen("in.txt", "r", stdin)
#define WRITE   freopen("out.txt", "w", stdout)
//-------------------------------------------------------------------------

class Disjoint
{
    public:
    map<char, char> representative;

    Disjoint(char v)
    {
        for(char c = 'A'; c <= v; c++)
        {
            representative[c] = c;
        }
    }
    char find_representative(char c)
    {
        if(representative[c] == c) return c;
        representative[c] = find_representative(representative[c]);
        return representative[c];
    }
    void Union(char a, char b)
    {
        representative[find_representative(a)] = find_representative(b);
    }
    int count_distinct_representative()
    {
        set<char> total_count;
        for(auto it = representative.begin(); it != representative.end(); it++)
        {
            total_count.insert(find_representative(it->second));
        }
        return total_count.size();
    }

};


int main()
{
    //READ;
    //WRITE;
    int test;
    cin >> test;
    bool print_nl = false;
    while(test--)
    {
        if(! print_nl) print_nl = true;
        else cout << endl;
        char max;
        cin >> max;
        Disjoint D(max);
        string inp;
        cin.ignore();
        while(getline(cin, inp) && inp != "")
        {
            D.Union(inp[0], inp[1]);
        }
        cout << D.count_distinct_representative() << endl;
    }
    
}