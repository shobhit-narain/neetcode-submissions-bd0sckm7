class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (beginWord == endWord) return 0;
        unordered_set<string> words{wordList.begin(), wordList.end()};
        if (!words.contains(endWord)) return 0;

        unordered_map<string, vector<string>> patterns;
        int sl = beginWord.size();
        for (const string& word: wordList) {
            for (int i = 0; i < sl; i++) {
                const string pattern = word.substr(0, i) + "." + word.substr(i+1);
                patterns[pattern].push_back(word);
            }
        }

        queue<string> q; q.push(beginWord);
        unordered_set<string> visited;
        int steps = 1;
        while (!q.empty()) {
            for (int i = 0; i < q.size(); i++) {
                string top = q.front(); q.pop();
                visited.insert(top);
                if (top == endWord) return steps;
                for (int idx = 0; idx < sl; idx++) {
                    const string pattern = top.substr(0, i) + "." + top.substr(i+1);
                    for (const string match : patterns[pattern]) {
                        if (!visited.contains(match)) q.push(match);
                    }
                }
            }
            steps++;
        }
        return steps;
    }
};
