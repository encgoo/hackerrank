#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

// Complete the organizingContainers function below.
string organizingContainers(vector<vector<int>> container) {
    //
    int num_containers = container.size();
    int num_types = container[0].size();
    // Two accumulators
    int *balls_per_container = new int[num_containers];
    int *balls_per_type = new int[num_types];
    // Initialize accumulators
    for (int i = 0; i < num_containers; ++i){
        balls_per_container[i] = 0;
    }
    for (int i = 0; i < num_types; ++i){
        balls_per_type[i] = 0;
    }

    for (int i = 0; i < num_containers; ++i){
        vector<int> balls_in_container = container[i];
        for (int j = 0; j < num_types; ++j){
            balls_per_container[i] += balls_in_container[j];
            balls_per_type[j] += balls_in_container[j];
        }
    }
    // Sort them before comparison
    sort(balls_per_container, balls_per_container + num_containers);
    sort(balls_per_type, balls_per_type + num_types);

    // now compare
    string ret = "Impossible";
    if (num_containers == num_types){
        ret = "Possible";
        for (int i = 0; i < num_containers; ++i){
            if (balls_per_container[i] != balls_per_type[i]){
                ret = "Impossible";
                break;
            }
        }
    }
    return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        vector<vector<int>> container(n);
        for (int i = 0; i < n; i++) {
            container[i].resize(n);

            for (int j = 0; j < n; j++) {
                cin >> container[i][j];
            }

            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        string result = organizingContainers(container);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
