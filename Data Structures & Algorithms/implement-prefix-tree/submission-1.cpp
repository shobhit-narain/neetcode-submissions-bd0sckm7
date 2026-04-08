class TrieNode {
    public:
        unordered_map<char, TrieNode*> chars;
        bool isEnd;
};

class PrefixTree {
public:
    TrieNode* root;

    PrefixTree() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* curr = root;
        for (char& c : word) {
            if (!curr->chars.contains(c)) curr->chars[c] = new TrieNode();
            curr = curr->chars[c];
        }
        curr->isEnd = true;
        return;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        for (char& c : word) {
            if (!curr->chars.contains(c)) return false;
            curr = curr->chars[c];
        }
        return curr->isEnd;
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char& c : prefix) {
            if (!curr->chars.contains(c)) return false;
            curr = curr->chars[c];
        }
        return true;
    }
};
