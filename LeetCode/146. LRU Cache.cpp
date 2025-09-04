
// Super Hard, first time i was forced to use iterator to store Address of
// linked list nodes
//  1. We need to data structures to serve two purpose, one is too help us do
//  the constant get lookups, push / update keys. A unordered_map aka HashTable
//  2. we also need to invalidate cache, need a FIFO structure, so we can get
//  oldest key and remove it from map. Corner case-> on update/get operation, we
//  need to modify the fifo queue, need to find the old entry and refresh it (push at end)
//   refreshKey -> we update FIFO so our recently accessed key's lifespan is increased
// If currentSize of map > allowed size, delete the key of the FIFO front, both from map and list
class HashNode {
public:
    int value;
    list<int>::iterator lst_it;
    HashNode(int value, list<int>::iterator lst_it) {
        this->value = value;
        this->lst_it = lst_it;
    }
    HashNode() {}
};

class LRUCache {

private:
    list<int> lst;
    unordered_map<int, HashNode> mp;
    int capacity;
    void refreshKey(int key) {

        //Push into FIFO stack
        lst.push_back(key);
        //Find the old entry in the list, delete it in O(1) time, this is the most important thing
        lst.erase(mp[key].lst_it);

        //update the list iterator reference in the map
        mp[key].lst_it = prev(lst.end());
    }

public:
    LRUCache(int capacity) {
        mp = unordered_map<int, HashNode>();
        mp.reserve(100);
        lst = list<int>();
        this->capacity = capacity;
    }

    int get(int key) {
        if (!mp.contains(key)) {
            return -1;
        } else {

            refreshKey(key);
            return mp[key].value;
        }
    }

    void put(int key, int value) {
        if (mp.contains(key)) {

            refreshKey(key);
            mp[key].value = value;

        } else {
            lst.push_back(key);
            auto node = HashNode(value, prev(lst.end()));
            mp[key] = node;

            if (mp.size() > capacity) {
                mp.erase(lst.front());
                lst.pop_front();
            }
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */