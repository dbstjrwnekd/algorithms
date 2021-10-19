#include <string>
#include <vector>
#include <queue>

using namespace std;

void bfs(int n, int num, vector<vector<int>> computers, bool *visited);

int solution(int n, vector<vector<int>> computers)
{
    if (n == 1)
        return 1;
    int answer = 0;
    bool visited[n];
    fill(&visited[0], &visited[n], false);

    for (int i = 0; i < n; i++)
    {
        if (visited[i] == false)
        {
            bfs(n, i, computers, visited);
            answer++;
        }
    }

    return answer;
}

void bfs(int n, int num, vector<vector<int>> computers, bool *visited)
{
    queue<int> q;
    q.push(num);
    visited[num] = true;
    while (q.size())
    {
        int cur = q.front();
        q.pop();
        for (int next_node = 0; next_node < n; next_node++)
        {
            if (next_node != cur && !visited[next_node] && computers[cur][next_node] == 1)
            {
                q.push(next_node);
                visited[next_node] = true;
            }
        }
    }
}
