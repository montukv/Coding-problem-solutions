/*121. Best Time to Buy and Sell Stock
Easy

7816

348

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
*/

#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
    vector<int> v;
    while(cin >> n){
        v.push_back(n);

    }
    /*
    //Brute force aproach o(n^2)
    int max_profit = 0,profit =0;

    for (int i = 0; i < v.size(); ++i)
    {
        for (int j = i; j < v.size(); ++j)
        {
            if(v[i] < v[j])
            {
                profit = v[j] - v[i];
                max_profit = max(profit,max_profit);
            }
        }
    }
    cout << max_profit;
    */

    //optimal solution with linear time complexity

    int min_left = INT_MAX,sum=0, max_profit = 0;
    for (int i = 0; i < v.size(); ++i)
    {
        if (v[i] < min_left)
            min_left = v[i];
        sum = v[i] - min_left;
        max_profit = max(sum,max_profit);

    }
    cout << max_profit;

    return 0;
}