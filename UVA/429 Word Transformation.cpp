//Good BFS problem but stupid IO issue, Presentation Error 3/4 times
//map for mapping string to node id
//helper function to validate relationship between nodes
//Construct Graph, Run BFS
//I hate UVA, why dragoon why ! (again couple of hours waste in I/O handling)
#include <bits/stdc++.h>
using namespace std;
#define IO  ios_base::sync_with_stdio(0);cin.tie(0);
#define READ freopen("in.txt", "r", stdin)
#define WRITE freopen("out.txt", "w", stdout)

//-------------------------------------------------------------------------
class Helper
{
public:
    inline static bool check_match(string inp, string match)
    {
        int char_diff = 0;
        if (inp.size() == match.size() && inp != match)
        {
            for (int i = 0; i < inp.size(); i++)
            {
                if (inp[i] != match[i])
                    char_diff++;
            }
        }
        if (char_diff == 1)
            return true;
        return false;
    }
};
class Graph
{
public:
    map<string, vector<string>> E;
    vector<string> wordlist;
    void add_word(string s)
    {
        wordlist.push_back(s);
    }

    void initialize()
    {

        for (auto word_1 = wordlist.begin(); word_1 != wordlist.end(); word_1++)
        {
            for (auto word_2 = wordlist.begin(); word_2 != wordlist.end(); word_2++)
            {
                if (Helper::check_match(*word_1, *word_2))
                {
                    E[*word_1].push_back(*word_1);
                    E[*word_2].push_back(*word_1);
                }
            }
        }
    }
};

int transform_count(Graph &G, string source, string destination)
{
    map<string, int> level;
    for (auto it = G.E.begin(); it != G.E.end(); it++)
    {
        level[it->first] = -1;
    }
    queue<string> Q;
    Q.push(source);
    level[source] = 0;
    while (Q.size())
    {
        string Current_Node = Q.front();
        Q.pop();
        for (auto it = G.E[Current_Node].begin(); it != G.E[Current_Node].end(); it++)
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
    int test;
    cin >> test;
    bool new_line = false;
    while (test--)
    {
        Graph G;
        string node;
        if(new_line) cout << endl;
        if(!new_line) new_line = true;
        while (cin >> node, node != "*")
        {
            G.add_word(node);
        }
        cin.ignore();
        G.initialize();
        string src, dst;
        string line;
        while (getline(cin, line) && line != "")
        {
            stringstream ss(line);
            ss >> src >> dst;
            int ans = transform_count(G, src, dst);
            cout << src << " " << dst << " " << ans << endl;
        }

    }
}