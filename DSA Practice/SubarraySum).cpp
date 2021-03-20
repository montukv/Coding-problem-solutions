/*
Subarray with 0 sum 
Easy Accuracy: 49.91% Submissions: 25431 Points: 2
Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

Example 1:

Input:
5
4 2 -3 1 6

Output: 
Yes

Explanation: 
2, -3, 1 is the subarray 
with sum 0.
Example 2:

Input:
5
4 2 0 1 6

Output: 
Yes

Explanation: 
0 is one of the element 
in the array so there exist a 
subarray with sum 0.
Your Task:
You only need to complete the function subArrayExists() that takes array and n as parameters and returns true or false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the drivers code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= N <= 104
-105 <= a[i] <= 105

*/


#include<its/stdc++.h>
using namespace std;

int main(){

	int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }
    int min_sum = INT_MAX, cur_sum = 0;
    unordered_map<int,int> m;
    int flag = 0,sum = 0;
    for (int i = 0; i < n; ++i)
    {
        sum += a[i];
        if(sum == 0 or m[sum] or m[i] == 0) {
            flag = 1;
            break;
        }

    }
    if(flag == 1) cout << "Yes";
    else cout << "No";

	return 0;
}
