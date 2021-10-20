#include <string>
#include <vector>
#include <queue>

using namespace std;

int bfs(int start, int arr[], vector<int> graph[]);

int solution(int n, vector<vector<int>> edge)
{
    int answer = 0;
    int lengths[n];
    fill(&lengths[0], &lengths[n], 0);

    vector<int> graph[n];

    for (vector<int> dot : edge)
    {
        graph[dot[0] - 1].push_back(dot[1] - 1);
        graph[dot[1] - 1].push_back(dot[0] - 1);
    }

    int max_length = bfs(0, lengths, graph);
    for (int length : lengths)
    {
        if (length == max_length)
            answer++;
    }

    return answer;
}

int bfs(int start, int arr[], vector<int> graph[])
{
    queue<pair<int, int>> q;
    int max_length = 0;
    q.push(make_pair(start, 1));
    while (q.size())
    {
        pair<int, int> cur = q.front();
        q.pop();
        int cur_dot = cur.first;
        int length = cur.second;
        arr[cur_dot] = length;
        max_length = max_length < length ? length : max_length;
        for (int next_dot : graph[cur_dot])
        {
            if (arr[next_dot] == 0)
            {
                q.push(make_pair(next_dot, length + 1));
                arr[next_dot] = length + 1;
            }
        }
    }
    return max_length;
}
