#include <iostream>
#include <vector>
#include <queue>
#include <set>

#define INF 500001

using namespace std;

int solution(int N, vector<vector<int>> road, int K)
{
    if (N == 1)
        return 1;
    const int SIZE = N;
    int answer = 0;
    int graph[SIZE][SIZE];
    fill(&graph[0][0], &graph[SIZE - 1][SIZE - 1], INF);
    for (vector<int> r : road)
    {
        graph[r[0] - 1][r[1] - 1] = min(graph[r[0] - 1][r[1] - 1], r[2]);
        graph[r[1] - 1][r[0] - 1] = min(graph[r[1] - 1][r[0] - 1], r[2]);
    }

    set<int> possible;
    possible.insert(0);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, 0));

    while (pq.size())
    {
        int cur = pq.top().second;
        int length = pq.top().first;
        pq.pop();
        if (possible.find(cur) == possible.end())
        {
            possible.insert(cur);
        }

        for (int next_node = 0; next_node < N; next_node++)
        {
            if (graph[cur][next_node] != INF && length + graph[cur][next_node] <= K)
            {
                if (possible.find(next_node) == possible.end())
                {
                    pq.push(make_pair(length + graph[cur][next_node], next_node));
                }
            }
        }
    }

    answer = possible.size();

    return answer;
}
