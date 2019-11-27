#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the highestValuePalindrome function below.
string highestValuePalindrome(string s, int n, int k) {
    // Make a copy of it
    string ret(s);
    int changes_left = k;

    // Make ret palindrome
    int l_ptr = 0;
    int r_ptr = n - 1;

    while (r_ptr > l_ptr){
        if (s[l_ptr] != s[r_ptr]){
            char max_char = max(s[l_ptr], s[r_ptr]);
            ret[l_ptr] = max_char;
            ret[r_ptr] = max_char;
            changes_left --;
        }
        l_ptr ++;
        r_ptr --;
    }
    if (changes_left < 0){
        // Not enough changes to make it palindrome
        return "-1";
    }
    // Restart
    l_ptr = 0;
    r_ptr = n - 1;

    while (l_ptr < r_ptr && changes_left > 0){
        // Only need to handle char not being '9'
        if (ret[l_ptr] != '9'){
            if (changes_left >= 2 && ret[l_ptr]== s[l_ptr] && ret[r_ptr] == s[r_ptr]){
                // These pair has not been changed last time, and we have
                // more than two changes left
                ret[l_ptr] = '9';
                ret[r_ptr] = '9';
                changes_left -= 2;
            }
            else if (changes_left >=1 && (ret[l_ptr] != s[l_ptr] || ret[r_ptr] != s[r_ptr])){
                // We changed one of this pair last time.
                ret[l_ptr] = '9';
                ret[r_ptr] = '9';
                changes_left -= 1;
            }
        }
        l_ptr ++;
        r_ptr --;
    }
    if (l_ptr == r_ptr){
        if (changes_left > 0){
            ret[l_ptr] = '9';
        }
    }
    return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nk_temp;
    getline(cin, nk_temp);

    vector<string> nk = split_string(nk_temp);

    int n = stoi(nk[0]);

    int k = stoi(nk[1]);

    string s;
    getline(cin, s);

    string result = highestValuePalindrome(s, n, k);

    fout << result << "\n";

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
