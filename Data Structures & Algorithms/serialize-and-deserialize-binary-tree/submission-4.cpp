/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == nullptr) return (string)"N";
        string ret = "";
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            for (int i = 0; i < q.size(); i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node == nullptr) ret += (string)(ret.empty() ? "" : ",") + "N";
                else {
                     ret += (string)(ret.empty() ? "" : ",") + to_string(node->val);
                     q.push(node->left);
                     q.push(node->right);
                }
            }
        }
        return ret;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "N") return nullptr;
        stringstream ss(data);
        string val;
        getline(ss, val, ',');
        TreeNode* root = new TreeNode(stoi(val));
        queue<TreeNode*> q;
        q.push(root);
        while (getline(ss, val, ',')) {
            TreeNode* node = q.front();
            q.pop();
            if (val != "N") {
                node->left = new TreeNode(stoi(val));
                q.push(node->left);
            }
            getline(ss, val, ',');
            if (val != "N") {
                node->right = new TreeNode(stoi(val));
                q.push(node->right);
            }
        }
        return root;
    }
};
