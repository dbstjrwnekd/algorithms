#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;
struct compare
{
    bool operator()(pair<int, int> p1, pair<int, int> p2)
    {
        if (p1.first != p2.first)
            return p1.first > p2.first;
        return p1.second > p2.second;
    }
};

int solution(vector<vector<int>> jobs)
{
    int count = 0;
    int cur_time = 0;
    int sum = 0;
    pair<int, int> cur(-1, -1);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    sort(jobs.begin(), jobs.end());
    int time = 0;
    int step = 0;
    while (count < jobs.size())
    {
        while (step < jobs.size() && jobs[step][0] <= time)
        {
            pq.push(make_pair(jobs[step][1], jobs[step][0]));
            step++;
        }
        if (cur.first == -1)
        {
            if (!pq.empty() && pq.top().second <= time)
            {
                cur = pq.top();
                pq.pop();
                cur_time = 0;
            }
        }
        else
        {
            if (cur_time == cur.first)
            {
                sum += time - cur.second;
                cur.first = -1;
                cur_time = 0;
                time--;
                count++;
            }
        }
        time++;
        if (cur.first != -1)
            cur_time++;
    }

    return sum / jobs.size();
}
