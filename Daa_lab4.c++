#include <iostream>
#include <vector>
using namespace std;

// Check if placing a queen at (row, col) is safe
bool isSafe(int row, int col, vector<string>& board, int n)
{
    // Check upper diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 'Q') return false;
    
    // Check left side
    for (int j = col; j >= 0; j--)
        if (board[row][j] == 'Q') return false;
    
    // Check lower diagonal
    for (int i = row, j = col; i < n && j >= 0; i++, j--)
        if (board[i][j] == 'Q') return false;

    return true;
}

// Recursive function to solve the N-Queens problem
void solve(int col, vector<string>& board, vector<vector<string>>& solutions, int n, int& count)
{
    if (col == n)
    {
        solutions.push_back(board);    // Store the current board configuration
        count++;
        return;
    }
    
    for (int row = 0; row < n; row++)
    {
        if (isSafe(row, col, board, n))
        {
            board[row][col] = 'Q';                        // Place the queen
            solve(col + 1, board, solutions, n, count);  // Recur for the next column
            board[row][col] = '.';                       // Backtrack by removing the queen
        }
    }
}

// Main function to start solving the N-Queens problem
vector<vector<string>> solveNQueens(int n, int& count)
{
    vector<string> board(n, string(n, '.'));  // Initialize the board
    vector<vector<string>> solutions;         // Store all solutions
    solve(0, board, solutions, n, count);     // Start solving from the first column
    return solutions;
}

int main() {
    int n, count = 0;
    cout << "\nEnter the number of rows and columns for the chess board: ";
    cin >> n;

    vector<vector<string>> queensSolutions = solveNQueens(n, count);

    // Display all possible solutions
    for (const auto& solution : queensSolutions) {
        for (const auto& row : solution) {
            cout << "[" << row << "]" << endl;
        }
        cout << endl;
    }

    cout << "Total number of ways to place the queens: " << count << endl;
    return 0;
}
 