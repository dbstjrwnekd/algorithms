#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K)
{
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < scoville.size(); i++)
    {
        pq.push(scoville[i]);
    }

    while (pq.size() > 0 && pq.top() < K)
    {
        int mini = pq.top();
        pq.pop();
        if (pq.size() == 0)
            return -1;
        int mini2 = pq.top();
        pq.pop();
        int new_mini = mini + 2 * mini2;
        pq.push(new_mini);
        answer++;
    }

    return answer;
}
