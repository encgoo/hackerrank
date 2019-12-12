#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'shop' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. STRING_ARRAY centers
 *  4. 2D_INTEGER_ARRAY roads
 */

int shop(int n, int k, vector<string> centers, vector<vector<int>> roads) {
    // n <= 1000, k <= 10. This keep track of the min distance to each
    // shop for different fish type combination
    int record[1000][1024];
    // initialize
    for (int i = 0; i < 1000; ++i){
        for (int j = 0; j < 1024; ++j){
            record[i][j] = INT_MAX;
        }
    }
    struct DEST {
        int dest;
        int weight;
    };
    vector<vector<DEST> > roads_(n+1);
    for (int i = 0; i < roads.size(); ++i){
        DEST dest;
        dest.dest  = roads[i][1];
        dest.weight = roads[i][2];
        roads_[roads[i][0] - 1].push_back(dest);
        dest.dest = roads[i][0];
        roads_[roads[i][1] - 1].push_back(dest);
    }
    vector<int> center_fish_types;

    for (int i = 0; i < centers.size(); ++i){
        string c_str = centers[i];
        stringstream ss(c_str);
        string buf;
        vector<int> fish_types;
        while (ss >> buf){
            fish_types.push_back(stoi(buf));
        }

        int fish_type_mask = 0;
        // Skip the first one. It is a count
        for (int j = 1; j < fish_types.size(); ++j){
            fish_type_mask |= 1 << (fish_types[j] - 1);
        }
        center_fish_types.push_back(fish_type_mask);
    }
    // Start from 0
    record[0][center_fish_types[0]] = 0;
    struct STATE {
        int center;
        int fish_mask;
        int dist;
        STATE(int c, int f, int d)
        :center(c), fish_mask(f), dist(d){}
    };
    deque<STATE> q;
    STATE start(0, center_fish_types[0], 0);
    q.push_back(start);
    while (q.size() > 0){
        STATE center = q.front();
        q.pop_front();
        vector<DEST> rds = roads_[center.center];
        for (int i = 0; i < rds.size(); ++i){
            int a_node = rds[i].dest;
            int cur_center_mask = center_fish_types[a_node - 1];
            int next_mask = center.fish_mask | cur_center_mask;
            // Check if we shall add a_node to the q
            int old_dist = record[a_node - 1][next_mask];
            if (old_dist > center.dist + rds[i].weight){
                record[a_node - 1][next_mask] = center.dist + rds[i].weight;
                q.push_back(STATE(a_node - 1, next_mask, center.dist + rds[i].weight));
            }
        }
    }
    int best_time = INT_MAX;
    for (int i = 0; i < 1024; ++i){
        for (int j = i; j < 1024; ++j){
            if ((i | j) == pow(2, k) - 1){
                best_time = min(best_time, max(record[n - 1][i], record[n - 1][j]));
            }
        }
    }
    return best_time;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int m = stoi(first_multiple_input[1]);

    int k = stoi(first_multiple_input[2]);

    vector<string> centers(n);

    for (int i = 0; i < n; i++) {
        string centers_item;
        getline(cin, centers_item);

        centers[i] = centers_item;
    }

    vector<vector<int>> roads(m);

    for (int i = 0; i < m; i++) {
        roads[i].resize(3);

        string roads_row_temp_temp;
        getline(cin, roads_row_temp_temp);

        vector<string> roads_row_temp = split(rtrim(roads_row_temp_temp));

        for (int j = 0; j < 3; j++) {
            int roads_row_item = stoi(roads_row_temp[j]);

            roads[i][j] = roads_row_item;
        }
    }

    int res = shop(n, k, centers, roads);

    fout << res << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
