class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (beginWord == endWord || endWord.empty()) return 0;
        unordered_set<string> words{wordList.begin(), wordList.end()};
        if (!words.contains(endWord)) return 0;

        unordered_map<string, vector<string>> patterns;
        int sl = beginWord.size();
        wordList.push_back(beginWord);
        for (const string& word: wordList) {
            for (int i = 0; i < sl; i++) {
                string pattern = word.substr(0, i) + "." + word.substr(i+1);
                patterns[pattern].push_back(word);
            }
        }

        queue<string> q;
        q.push(beginWord);
        unordered_set<string> visited{beginWord};
        int steps = 1;
        while (!q.empty()) {
            const int size = q.size();
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                visited.insert(word);
                if (word == endWord) return steps;
                for (int idx = 0; idx < sl; idx++) {
                    // cout << "idx: " << idx << " | word: " << word << "\n";
                    const string pattern = word.substr(0, idx) + "." + word.substr(idx+1);
                    for (const string& match : patterns[pattern]) {
                        if (!visited.contains(match)) {
                            q.push(match);
                            visited.insert(match);
                        }
                    }
                }
            }
            steps++;
        }
        return 0;
    }
};
