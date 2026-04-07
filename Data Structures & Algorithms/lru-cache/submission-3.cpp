class ListNode {
public:
    int key;
    int val;
    ListNode* left;
    ListNode* right;

    ListNode(int k, int v) : key(k), val(v), left(nullptr), right(nullptr) {}
};

class LRUCache {
private:
    int cap;
    unordered_map<int, ListNode*> nodes;
    ListNode* head;
    ListNode* tail;

    void insert(ListNode* node) {
        ListNode* curr_head = head->right;
        head->right = node;
        node->left = head;
        node->right = curr_head;
        curr_head->left = node;
    }

    void remove(ListNode* node) {
        ListNode* lft = node->left;
        ListNode* rgt = node->right;
        lft->right = rgt;
        rgt->left = lft;
    }

public:
    LRUCache(int capacity) {
        cap = capacity;
        nodes.clear();
        head = new ListNode(-1, -1);
        tail = new ListNode(-1, -1);
        head->right = tail;
        tail->left = head;
    }
    
    int get(int key) {
        if (!nodes.contains(key)) return -1;
        ListNode* node = nodes[key];
        remove(node);
        insert(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (nodes.contains(key)) remove(nodes[key]);
        ListNode* node = new ListNode(key, value);
        nodes[key] = node;
        insert(node);

        if (cap < nodes.size()) {
            ListNode* lru = tail->left;
            remove(lru);
            nodes.erase(lru->key);
            delete lru;
        }
    }
};
