#include <bits/stdc++.h>
#include <algorithm>
#include <iterator>

using namespace std;

// Complete the commonChild function below.
int commonChild(string s1, string s2) {
    // max_len is 5000 according to the description
    enum {
        max_len = 5001
    };
    int s2_pre_rec[max_len] = {0};
    int s2_cur_rec[max_len] = {0};
    // Initialize the edges
    for (int i = 1; i <= s1.size(); ++i){
        copy(begin(s2_cur_rec), end(s2_cur_rec), begin(s2_pre_rec));

        for (int j = 1; j <= s2.size(); ++j){
            if (s1[i - 1] == s2[j - 1]){
                s2_cur_rec[j] = s2_pre_rec[j - 1] + 1;
            }
            else {
                s2_cur_rec[j] = max(s2_cur_rec[j], s2_cur_rec[j - 1]);
            }
        }
    }

    return s2_cur_rec[s2.size()];
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s1;
    getline(cin, s1);

    string s2;
    getline(cin, s2);

    int result = commonChild(s1, s2);

    fout << result << "\n";

    fout.close();

    return 0;
}
