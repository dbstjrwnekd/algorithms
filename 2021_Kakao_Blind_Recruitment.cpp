#include <string>
#include <vector>
#include <limits>
#include <iostream>

#define INF numeric_limits<int>::max()

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares)
{
    int answer = 0;
    int graph[n][n];
    fill(&graph[0][0], &graph[n - 1][n - 1], INF);

    for (vector<int> fare : fares)
    {
        graph[fare[0] - 1][fare[1] - 1] = fare[2];
        graph[fare[1] - 1][fare[0] - 1] = fare[2];
    }

    for (int i = 0; i < n; i++)
    {
        graph[i][i] = 0;
    }

    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (graph[i][k] != INF && graph[k][j] != INF)
                {
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }
    }

    answer = INF;
    for (int k = 0; k < n; k++)
    {
        if (graph[s - 1][k] != INF && graph[k][a - 1] != INF && graph[k][b - 1] != INF)
        {
            answer = min(answer, graph[s - 1][k] + graph[k][a - 1] + graph[k][b - 1]);
        }
    }

    return answer;
}
