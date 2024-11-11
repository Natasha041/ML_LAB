#include<iostream>
#include<vector>
using namespace std;

// Function to solve the 0/1 Knapsack problem
int knapsack(int W, int weights[], int values[], int n, vector<int>& selectedItems) 
{
    // Create a 2D array to store the maximum value that can be obtained
    int dp[n + 1][W + 1];

    // Initialization of the dp array
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= W; j++)
        {
            if (i == 0 || j == 0) 
            {
                dp[i][j] = 0; // Base case: no items or no capacity
            }
        }
    }

    // Filling the rest of the dp array
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= W; j++) 
        {
            if (weights[i - 1] <= j) 
            {
                // Max value of including or excluding the item
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j]);
            }
            else
            {
                // Item cannot be included
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    // Backtrack to find which items were included
    int res = dp[n][W];
    int w = W;
    for (int i = n; i > 0 && res > 0; i--) 
    {
        // Check if the item was included
        if (res != dp[i - 1][w]) 
        {
            // This item was included
            selectedItems.push_back(i - 1); // Store the index of the included item
            res -= values[i - 1];
            w -= weights[i - 1];
        }
    }

    // Return the maximum value that can be obtained
    return dp[n][W];
}

int main() {
    int n, W;

    // Input number of objects
    cout << "Enter the number of objects: ";
    cin >> n;

    // Input capacity of the knapsack
    cout << "Enter the capacity of the knapsack: ";
    cin >> W;

    // Arrays to store weights and values of the objects
    int weights[n], values[n];

    // Input weights and values
    cout << "Enter the weights and corresponding values of the objects:" << endl;
    for (int i = 0; i < n; i++) 
    {
        cout << "Object " << i + 1 << " - Weight & Value : ";
        cin >> weights[i] >> values[i];
    }

    // Vector to store the indices of selected items
    vector<int> selectedItems;

    // Call the knapsack function and display the result
    int max_value = knapsack(W, weights, values, n, selectedItems);
    cout << "The maximum value that can be obtained is: " << max_value << endl;

    // Display the selected items
    cout << "The selected objects are: ";
    for (int i : selectedItems) 
    {
        cout << "Object " << i + 1 << " (Weight: " << weights[i] << ", Value: " << values[i] << "), ";
    }
    cout << endl;

    return 0;
}