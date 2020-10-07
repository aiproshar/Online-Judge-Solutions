//DSU variation, Advanced with tight TL constrain
//REF : UVA 459
//Update number_of_followers in the fly (while doing union)
//Memoization Technique to update follower (of a representative) in constant time


#include <bits/stdc++.h>
using namespace std;
#define IO      ios_base::sync_with_stdio(0); cin.tie(0);
#define READ    freopen("in.txt", "r", stdin)
#define WRITE   freopen("out.txt", "w", stdout)
//-------------------------------------------------------------------------

class Disjoint
{
    public:
    map<string, string> representative;   //track of representative nodes
    map<string, int> follower;            //track of follower
    void check_insert(string name)        
    {
        if (representative.find(name) == representative.end()) //Checking if node exist or not
        {
            representative[name] = name;
            follower[name] = 1;           // Initially every node has 1 follower, himself
        }
    }
    string find_representative(string s)
    {
        if(representative[s] == s) return s;
        representative[s] = find_representative(representative[s]);
        return representative[s];
    }
    void Union(string a, string b)
    {
        if(find_representative(a) == find_representative(b)) return;
        
        follower[find_representative(b)] = follower[find_representative(b)] + follower[find_representative(a)]; //Deep Understanding, Main Runtime Optimization
        //Its necessary to update followers before we change representative. Cause if we update the representtatives first, we double count added elements; n(b) = n(b) + n(b) //as rep(a is now b)
        //preety-printers saved at least couple of hours of Debugging (+ rep) 
        //If we transfer b->rep  from representative node to follower of a->rep [union(a,b)], we increase the followers of a->rep by the follower count of b->rep :) 
        //On the Fly O(1) update; with 2 helper memoization, one for path compression, other for follower update                                                                                                 
        representative[find_representative(a)] = find_representative(b);
    }                                                                                                           

    int subgroup_size(string s)
    {
        return follower[find_representative(s)];
    }

};
int main()
{
    READ;
    WRITE;
    IO;
    int test;
    cin >> test;
    while(test--)
    {
        int f;
        cin >> f;
        Disjoint D;
        string a , b;
        while(f--)
        {
            cin >> a >> b;
            D.check_insert(a);
            D.check_insert(b);
            D.Union(a, b);
            cout << D.subgroup_size(a) << endl;
        }
    }
}