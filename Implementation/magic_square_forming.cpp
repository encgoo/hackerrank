/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: yongjian Febg
 *
 * Created on November 18, 2019, 6:11 PM
 */

#include <cstdlib>
#include <algorithm>
#include <stdio.h>
using namespace std;

/*
 * 
 */
int main(){
    int s[3][3];
	
    s[0][0] = 2; s[0][1] = 9; s[0][2] = 8;   
    s[1][0] = 4; s[1][1] = 2; s[1][2] = 7;
    s[2][0] = 5; s[2][1] = 6; s[2][2] = 7;
    

    int change = 0;

    // First the center must be 5
    change += abs(5 - s[1][1]);

    
    int min_center = abs(s[0][1] - 1) + abs(s[2][1] - 9) + abs(s[1][0] - 3) + abs(s[1][2] - 7);
    int min_diag = abs(s[0][0] - 8) + abs(s[2][2] - 2) + abs(s[0][2] - 6) + abs(s[2][0] - 4);
    int min_sum = min_center + min_diag;
    
    
    min_center = abs(s[0][1] - 1) + abs(s[2][1] - 9) + abs(s[1][0] - 7) + abs(s[1][2] - 3);
    min_diag = abs(s[0][0] - 6) + abs(s[2][2] - 4) + abs(s[0][2] - 8) + abs(s[2][0] - 2);
    min_sum = min(min_sum, min_center + min_diag);
    
    min_center = abs(s[0][1] - 9) + abs(s[2][1] - 1) + abs(s[1][0] - 7) + abs(s[1][2] - 3);
    min_diag = abs(s[0][0] - 2) + abs(s[2][2] - 8) + abs(s[0][2] - 4) + abs(s[2][0] - 6);
    min_sum = min(min_sum, min_center + min_diag);
    
    min_center = abs(s[0][1] - 9) + abs(s[2][1] - 1) + abs(s[1][0] - 3) + abs(s[1][2] - 7);
    min_diag = abs(s[0][0] - 4) + abs(s[2][2] - 6) + abs(s[0][2] - 2) + abs(s[2][0] - 8);
    min_sum = min(min_sum, min_center + min_diag);
    
    min_center = abs(s[0][1] - 3) + abs(s[2][1] - 7) + abs(s[1][0] - 1) + abs(s[1][2] - 9);
    min_diag = abs(s[0][0] - 8) + abs(s[2][2] - 2) + abs(s[0][2] - 4) + abs(s[2][0] - 6);
    min_sum = min(min_sum, min_center + min_diag);
    
    min_center = abs(s[0][1] - 3) + abs(s[2][1] - 7) + abs(s[1][0] - 9) + abs(s[1][2] - 1);
    min_diag = abs(s[0][0] - 4) + abs(s[2][2] - 6) + abs(s[0][2] - 8) + abs(s[2][0] - 2);
    min_sum = min(min_sum, min_center + min_diag);

    min_center = abs(s[0][1] - 7) + abs(s[2][1] - 3) + abs(s[1][0] - 1) + abs(s[1][2] - 9);
    min_diag = abs(s[0][0] - 6) + abs(s[2][2] - 4) + abs(s[0][2] - 2) + abs(s[2][0] - 8);
    min_sum = min(min_sum, min_center + min_diag);
    
    min_center = abs(s[0][1] - 7) + abs(s[2][1] - 3) + abs(s[1][0] - 9) + abs(s[1][2] - 1);

    min_diag = abs(s[0][0] - 2) + abs(s[2][2] - 8) + abs(s[0][2] - 6) + abs(s[2][0] - 4);
    min_sum = min(min_sum, min_center + min_diag);
    
    printf("%d", change + min_sum);
    return 0;
}

