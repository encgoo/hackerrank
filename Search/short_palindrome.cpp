#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;

// Complete the shortPalindrome function below.
const unsigned long int mod = 1000000000+7;

unsigned long int shortPalindrome(string s) {
    unsigned long int count = 0;
    unsigned long int  sz = s.size();
    unsigned long int  single_char[26] = {0};
    unsigned long int  two_chars[26][26];
    unsigned long int  three_chars[26] = {0};

    for (int i = 0; i < 26; ++i){
        single_char[i] = 0;
        three_chars[i] = 0;
    }
    for (int i = 0; i < 26; ++i){
        for (int j = 0; j < 26; ++j){
            two_chars[i][j] = 0;
        }
    }

    for (unsigned long int  i = 0; i < sz; ++i){
        char c = s[i];
        count = (count + three_chars[c - 'a'])%mod;
        for (int j = 0; j < 26; ++j){
            three_chars[j] = (three_chars[j] + two_chars[j][c - 'a'])%mod;
        }
        for (int j = 0; j < 26; ++j){
            two_chars[j][c - 'a'] = (two_chars[j][c - 'a'] + single_char[j])%mod;
        }
        single_char[c - 'a'] = (single_char[c-'a'] + 1)%mod;
    }

    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    unsigned long result = shortPalindrome(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
