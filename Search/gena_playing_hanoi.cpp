#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

vector<int> make_one_move(vector<int>& lst, int i, int j){
    vector<int> ret;
    int index = 0;
    int top_i = -1;
    int top_j = -1;
    bool found_i = false;
    bool found_j = false;
    while (index < lst.size() && !(found_i && found_j)){
        if (lst[index] == i + 1 && !found_i){
            top_i = index;
            found_i = true;
        }
        if (lst[index] == j + 1 && !found_j){
            top_j = index;
            found_j = true;
        }
        index += 1;
    }
    if (top_i == -1){
        // Nothing on rod i. Can't move from i to j
        // return the empty vector
        return ret;
    }
    if (top_i > top_j && top_j != -1){
        // Top one from i is bigger than top one of j. Can't move
        return ret;
    }

    // copy over
    ret = lst;
    // Move from i to j
    ret[top_i] = j   + 1;
    return ret;
}

int vec_to_index(vector<int> lst){
    int ret = 0;
    for (int i = 0; i < lst.size(); ++i){
        ret = ret << 2 | (lst[i] - 1);
    }
    return ret;
}
bool is_done(vector<int> lst){
    bool done = true;
    for (int i = 0; i < lst.size(); ++i){
        if (lst[i] != 1){
            done = false;
            break;
        }
    }
    return done;
}
int count_steps(int N, vector<int> a){
    // Use BFS
    bool visited[1<<20] = {false};
    queue<vector<int> > q;
    q.push(a);
    visited[vec_to_index(a)] = true;
    bool done = is_done(a);
    int min_count = 0;
    while(q.size() > 0 and !done){
        min_count ++;
        int sz = q.size();
        for (int ii = 0; ii < sz; ++ii){
            vector<int> lst = q.front();
            q.pop();
            for (int i = 0; i < 4; ++i){
                for (int j = 0; j < 4; ++j){
                    if (i != j){
                        // Try to move the top one from i to j
                        vector<int> ret = make_one_move(lst, i, j);
                        if (ret.size() > 0){
                            done = is_done(ret);
                            if (done){
                                break;
                            }
                            int index = vec_to_index(ret);
                            if (!visited[index]){
                                visited[index] = true;
                                q.push(ret);
                            }
                        }
                    }
                }
                if (done){
                    break;
                }
            }
            if (done){
                break;
            }
        }
    }

    return min_count;
}

int main()
{
    int N;
    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split_string(a_temp_temp);

    vector<int> a(N);

    for (int i = 0; i < N; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }
    int count = count_steps(N, a);
    printf("%d", count);
    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
