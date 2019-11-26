
#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// This is just for showing off.
// Use Visitor design pattern
class Visitor{
public:
    virtual int handle(char pre_state, char g[200][200], int i = 0, int j = 0)=0;
};
class FillVisitor : public Visitor{
public:
    virtual int handle(char pre_state, char g[200][200], int i = 0, int j = 0){
        char ret_state = 0;
        if (pre_state == -1){
            // Replace it with a bomb
            ret_state = 1;
        }
        return ret_state;
    }
};
class DetonateVisitor: public Visitor{
public:
    DetonateVisitor(int h, int w):w(w),h(h){};
    virtual int handle(char pre_state, char g[200][200], int i = 0, int j = 0){
        char ret_state = pre_state;
        if (pre_state == 0){
            ret_state = -1;
            update(g, i + 1, j, -1);
            update(g, i, j + 1, -1);
            update(g, i, j - 1, -1);
            update(g, i - 1, j, -1);
        }
        else if (g[i][j] == -1){
            // Don't override
            ret_state = -1;
        }
        return ret_state;
    }
private:
    void update(char g[200][200], int i, int j, int state){
        if (i >= 0 && j >= 0 && i < h && j < w){
            g[i][j] = state;
        }
    }
    int w;
    int h;
};
class InitVisitor: public Visitor{
public:
    InitVisitor(vector<string> *pgrid):pGrid(pgrid){
    }
    virtual int handle(char pre_state, char g[200][200], int i = 0, int j = 0){
        char ret_state;
        if ((*pGrid)[i][j] == 'O'){
            ret_state = 1;
        }
        else {
            ret_state = -1;
        }
        return ret_state;
    }
private:
    vector<string>* pGrid;
};

class BombGrid{
public:
    enum {num_state = 6};
    BombGrid(int h, int w)
        :h(h),w(w){}
    void traverse(Visitor* pVisitor, int cur_state){
        for (int i = 0; i < h; ++i){
            for (int j = 0; j < w; ++j){
                char state = 0;
                if (cur_state > 0){
                    state = grid_state[cur_state - 1][i][j];
                }
                grid_state[cur_state][i][j] = pVisitor->handle(state, grid_state[cur_state], i, j);
            }
        }
    }
    vector<string> generate_output(int state){
        vector<string> output;
        for (int i = 0; i < h; ++i){
            string row = "";
            for (int j = 0; j < w; ++j){
                if (grid_state[state][i][j] == -1){
                    row += ".";
                }
                else {
                    row += "O";
                }
            }
            output.push_back(row);
        }
        return output;
    }
private:
    // Note the size has limit 1<=r,c<=200
    char grid_state[num_state][200][200];
    int h;
    int w;
};


// Complete the bomberMan function below.
vector<string> bomberMan(int n, vector<string> grid) {
    // The gird repeats itself periodically along the time as
    // 1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6
    // As a result, we just need to compute what it looks like
    // for the first 6 seconds. The first second is the same as
    // the second second, so we just need to store 5 states
    int h = grid.size();
    int w = grid[0].size();
    BombGrid bomb_grid = BombGrid(h, w);
    InitVisitor initVisitor = InitVisitor(&grid);
    FillVisitor fillVisitor = FillVisitor();
    DetonateVisitor detonateVisitor = DetonateVisitor(h, w);

    bomb_grid.traverse(&initVisitor, 0);
    bomb_grid.traverse(&fillVisitor, 1);
    bomb_grid.traverse(&detonateVisitor, 2);
    bomb_grid.traverse(&fillVisitor, 3);
    bomb_grid.traverse(&detonateVisitor, 4);
    bomb_grid.traverse(&fillVisitor, 5);

    int state = (n < 3)? n - 1 : (n - 3)%4 + 2;
    vector<string> ret = bomb_grid.generate_output(state);
    return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string rcn_temp;
    getline(cin, rcn_temp);

    vector<string> rcn = split_string(rcn_temp);

    int r = stoi(rcn[0]);

    int c = stoi(rcn[1]);

    int n = stoi(rcn[2]);

    vector<string> grid(r);

    for (int i = 0; i < r; i++) {
        string grid_item;
        getline(cin, grid_item);

        grid[i] = grid_item;
    }

    vector<string> result = bomberMan(n, grid);

    for (int i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

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
